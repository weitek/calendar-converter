function CalendarWidget({
  widget,
  date,
  onDateChange,
  isSource,
  isTarget,
  dateFormat,
  onSetSource,
  onSetTarget,
  displayDate,
  additionalData,
  language = 'ru'
}) {
  const labels = {
    ru: {
      asSource: 'Как источник',
      asTarget: 'Как цель',
      source: 'Источник',
      target: 'Цель',
      jd: 'JD',
      lunarDay: 'Лунный день',
      phase: 'Фаза',
      illumination: 'Освещённость',
      nextPhase: 'Следующая фаза',
      day: 'День',
      month: 'Месяц',
      year: 'Год'
    },
    en: {
      asSource: 'As source',
      asTarget: 'As target',
      source: 'Source',
      target: 'Target',
      jd: 'JD',
      lunarDay: 'Lunar Day',
      phase: 'Phase',
      illumination: 'Illumination',
      nextPhase: 'Next Phase',
      day: 'Day',
      month: 'Month',
      year: 'Year'
    }
  };

  const l = labels[language] || labels.ru;
  const handleInputChange = (field, value) => {
    if (field === 'jd') {
      if (value === '') {
        onDateChange({ jd: 0 });
      } else {
        const numValue = parseFloat(value);
        onDateChange({ jd: isNaN(numValue) ? 0 : numValue });
      }
    } else {
      if (value === '') {
        onDateChange({ ...date, [field]: 0 });
      } else {
        const numValue = parseInt(value, 10);
        onDateChange({
          ...date,
          [field]: isNaN(numValue) ? 0 : numValue
        });
      }
    }
  };

  const canInput = isSource && widget.fields.length > 0;
  const canBeTarget = widget.supported_directions.includes('to');

  return (
    <div className={`bg-white rounded-lg shadow-md p-4 ${isSource ? 'ring-2 ring-blue-500' : ''} ${isTarget ? 'ring-2 ring-green-500' : ''}`}>
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800">{widget.name}</h3>
        
        <div className="flex gap-2">
          {!isSource && (
            <button
              onClick={onSetSource}
              className="text-xs bg-blue-100 hover:bg-blue-200 text-blue-800 px-2 py-1 rounded"
            >
              {l.asSource}
            </button>
          )}
          {!isTarget && canBeTarget && (
            <button
              onClick={onSetTarget}
              className="text-xs bg-green-100 hover:bg-green-200 text-green-800 px-2 py-1 rounded"
            >
              {l.asTarget}
            </button>
          )}
        </div>
      </div>

      {widget.id === 'lunar_phase' && additionalData && !isSource ? (
        <div className="space-y-2">
          <div className="text-sm">
            <span className="text-gray-600">{l.jd}: </span>
            <span className="font-mono">{additionalData.jd?.toFixed(5) || '--'}</span>
          </div>
          <div className="text-sm">
            <span className="text-gray-600">{l.lunarDay}: </span>
            <span className="font-semibold">{additionalData.lunar_day || '--'}</span>
          </div>
          <div className="text-sm">
            <span className="text-gray-600">{l.phase}: </span>
            <span className="font-semibold">{additionalData.phase || '--'}</span>
          </div>
          <div className="text-sm">
            <span className="text-gray-600">{l.illumination}: </span>
            <span>{additionalData.illumination?.toFixed(1) || '--'}%</span>
          </div>
          {additionalData.next_phase && (
            <div className="text-sm mt-2 pt-2 border-t">
              <span className="text-gray-600">{l.nextPhase}: </span>
              <div className="font-semibold">{additionalData.next_phase.type}</div>
              <div className="text-xs text-gray-500">
                {additionalData.next_phase.time_utc || '--'}
              </div>
            </div>
          )}
        </div>
      ) : widget.id === 'julian_day' && additionalData && !isSource ? (
        <div className="space-y-2">
          <div className="text-2xl font-mono text-center">
            {typeof additionalData === 'number' ? additionalData.toFixed(5) : 
             typeof additionalData === 'object' && additionalData !== null ? additionalData.jd?.toFixed(5) : '--'}
          </div>
        </div>
      ) : (
        <>
          {canInput && (
            <div className="flex gap-2 mb-4">
              {widget.id === 'julian_day' ? (
                <input
                  type="number"
                  min="0"
                  value={date?.jd || ''}
                  onChange={(e) => handleInputChange('jd', e.target.value)}
                  placeholder="JD"
                  className="w-full p-2 border border-gray-300 rounded text-center font-mono"
                />
              ) : (
                <>
                  <input
                    type="number"
                    min="1"
                    max="31"
                    value={date?.day || ''}
                    onChange={(e) => handleInputChange('day', e.target.value)}
                    placeholder={l.day}
                    className="w-20 p-2 border border-gray-300 rounded text-center"
                  />
                  <input
                    type="number"
                    min="1"
                    max="12"
                    value={date?.month || ''}
                    onChange={(e) => handleInputChange('month', e.target.value)}
                    placeholder={l.month}
                    className="w-20 p-2 border border-gray-300 rounded text-center"
                  />
                  <input
                    type="number"
                    min="1"
                    value={date?.year || ''}
                    onChange={(e) => handleInputChange('year', e.target.value)}
                    placeholder={l.year}
                    className="flex-1 p-2 border border-gray-300 rounded text-center"
                  />
                </>
              )}
            </div>
          )}
          
          <div className={`text-lg font-semibold text-center ${!canInput ? 'mt-4' : ''}`}>
            {displayDate}
          </div>
        </>
      )}

      {isSource && (
        <div className="mt-2 text-xs text-blue-600 text-center">
          {l.source}
        </div>
      )}
      {isTarget && (
        <div className="mt-2 text-xs text-green-600 text-center">
          {l.target}
        </div>
      )}
    </div>
  );
}

export default CalendarWidget;
