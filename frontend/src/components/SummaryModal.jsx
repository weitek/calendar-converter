function SummaryModal({ dates, widgets, settings, onClose }) {
  const getWidgetName = (id) => {
    const widget = widgets.find(w => w.id === id);
    return widget ? widget.name : id;
  };

  const formatDisplayDate = (date, widgetId) => {
    if (!date) return '--';

    if (widgetId === 'julian_day') {
      return date.jd ? date.jd.toFixed(5) : '--';
    }

    if (widgetId === 'lunar_phase') {
      if (!date.phase) return '--';
      return `JD: ${date.jd?.toFixed(2) || '--'}, День: ${date.lunar_day}, Фаза: ${date.phase}`;
    }

    if (!date.day) return '--';
    
    const { day, month, year } = date;
    
    if (widgetId === 'chinese') {
      return `${year}-${month}-${day}${date.is_leap ? ' (високосный)' : ''}`;
    }
    
    if (widgetId === 'hebrew') {
      return `${date.hebrew_month_name || ''} ${day}, ${year}`;
    }

    return formatDate(day, month, year, settings.dateFormat);
  };

  const formatDate = (day, month, year, format) => {
    const d = String(day).padStart(2, '0');
    const m = String(month).padStart(2, '0');
    const y = String(year);
    
    if (format === 'yyyy-mm-dd') {
      return `${y}-${m}-${d}`;
    }
    return `${d}.${m}.${y}`;
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-lg shadow-xl max-w-2xl w-full max-h-[80vh] overflow-auto">
        <div className="p-4 border-b flex justify-between items-center">
          <h2 className="text-xl font-bold">Сводка</h2>
          <button
            onClick={onClose}
            className="text-gray-500 hover:text-gray-700 text-2xl"
          >
            ×
          </button>
        </div>

        <div className="p-4">
          <table className="w-full">
            <thead>
              <tr className="bg-gray-100">
                <th className="p-3 text-left">Календарь</th>
                <th className="p-3 text-left">Дата</th>
              </tr>
            </thead>
            <tbody>
              {widgets.map(widget => (
                <tr key={widget.id} className="border-b hover:bg-gray-50">
                  <td className="p-3 font-medium">{widget.name}</td>
                  <td className="p-3">
                    {formatDisplayDate(dates[widget.id], widget.id)}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="p-4 border-t bg-gray-50">
          <p className="text-sm text-gray-600">
            Время пользователя: {Intl.DateTimeFormat().resolvedOptions().timeZone}
          </p>
        </div>
      </div>
    </div>
  );
}

export default SummaryModal;
