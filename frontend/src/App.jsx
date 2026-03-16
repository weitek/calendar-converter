import { useState, useEffect } from 'react';
import Header from './components/Header';
import CalendarWidget from './components/CalendarWidget';
import SummaryModal from './components/SummaryModal';
import { fetchWidgets, convertDate } from './services/api';
import { formatDate, parseDate } from './utils/dateFormats';

function App() {
  const [widgets, setWidgets] = useState([]);
  const [activeSource, setActiveSource] = useState('gregorian');
  const [activeTarget, setActiveTarget] = useState('julian');
  const [dates, setDates] = useState({});
  const [settings, setSettings] = useState(() => {
    const saved = localStorage.getItem('calendarSettings');
    return saved ? JSON.parse(saved) : {
      dateFormat: 'dd.mm.yyyy',
      coordinates: { lat: 51.4769, lng: 0.0005 },
      language: 'ru'
    };
  });
  const [showSummary, setShowSummary] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadWidgets();
  }, []);

  useEffect(() => {
    localStorage.setItem('calendarSettings', JSON.stringify(settings));
  }, [settings]);

  useEffect(() => {
    if (widgets.length > 0 && dates[activeSource]) {
      convertAll();
    }
  }, [activeSource, activeTarget]);

  useEffect(() => {
    loadWidgets();
  }, [settings.language]);

  const loadWidgets = async () => {
    try {
      const data = await fetchWidgets(settings.language);
      setWidgets(data);
      
      // Initialize dates
      const initialDates = {};
      data.forEach(w => {
        if (w.id === 'gregorian') {
          const today = new Date();
          initialDates[w.id] = {
            day: today.getDate(),
            month: today.getMonth() + 1,
            year: today.getFullYear()
          };
        } else {
          initialDates[w.id] = null;
        }
      });
      setDates(initialDates);
      setLoading(false);
    } catch (error) {
      console.error('Error loading widgets:', error);
      setLoading(false);
    }
  };

  const convertAll = async () => {
    const sourceDate = dates[activeSource];
    if (!sourceDate) return;

    const newDates = { ...dates };

    for (const widget of widgets) {
      if (widget.id === activeSource) continue;
      if (widget.id === 'gregorian') {
        newDates[widget.id] = { ...sourceDate };
        continue;
      }

      try {
        const result = await convertDate(activeSource, widget.id, sourceDate, settings.coordinates, settings.language);
        newDates[widget.id] = result;
      } catch (error) {
        console.error(`Error converting to ${widget.id}:`, error);
        newDates[widget.id] = null;
      }
    }

    setDates(newDates);
  };

  const handleDateChange = (calendarId, newDate) => {
    setDates(prev => ({
      ...prev,
      [calendarId]: newDate
    }));
  };

  const handleRecalculate = () => {
    convertAll();
  };

  const getDisplayDate = (calendarId) => {
    const date = dates[calendarId];
    if (!date) return '--';

    if (calendarId === 'julian_day') {
      return date.jd ? date.jd.toFixed(5) : '--';
    }

    if (calendarId === 'lunar_phase') {
      if (!date.phase) return '--';
      return `${date.lunar_day} ${date.phase}`;
    }

    return formatDate(date.day, date.month, date.year, settings.dateFormat);
  };

  const labels = {
    ru: { loading: 'Загрузка...', recalculate: 'Пересчитать' },
    en: { loading: 'Loading...', recalculate: 'Recalculate' }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 flex items-center justify-center">
        <div className="text-xl">{labels[settings.language]?.loading || labels.ru.loading}</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Header 
        settings={settings}
        onSettingsChange={setSettings}
        onShowSummary={() => setShowSummary(true)}
      />

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {widgets.map(widget => (
            <CalendarWidget
              key={widget.id}
              widget={widget}
              date={dates[widget.id]}
              onDateChange={(date) => handleDateChange(widget.id, date)}
              isSource={activeSource === widget.id}
              isTarget={activeTarget === widget.id}
              dateFormat={settings.dateFormat}
              onSetSource={() => setActiveSource(widget.id)}
              onSetTarget={() => setActiveTarget(widget.id)}
              displayDate={getDisplayDate(widget.id)}
              additionalData={dates[widget.id]}
              language={settings.language}
            />
          ))}
        </div>

        <div className="mt-8 flex justify-center">
          <button
            onClick={handleRecalculate}
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg shadow transition-colors"
          >
            {labels[settings.language]?.recalculate || labels.ru.recalculate}
          </button>
        </div>
      </main>

      {showSummary && (
        <SummaryModal
          dates={dates}
          widgets={widgets}
          settings={settings}
          onClose={() => setShowSummary(false)}
        />
      )}
    </div>
  );
}

export default App;
