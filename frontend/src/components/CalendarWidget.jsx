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
  additionalData
}) {
  const handleInputChange = (field, value) => {
    const numValue = parseInt(value) || 0;
    onDateChange({
      ...date,
      [field]: numValue
    });
  };

  const canInput = isSource && widget.fields.length > 0 && widget.id !== 'julian_day' && widget.id !== 'lunar_phase';

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
              Как источник
            </button>
          )}
          {!isTarget && widget.supported_directions.includes('to') && (
            <button
              onClick={onSetTarget}
              className="text-xs bg-green-100 hover:bg-green-200 text-green-800 px-2 py-1 rounded"
            >
              Как цель
            </button>
          )}
        </div>
      </div>

      {widget.id === 'lunar_phase' && additionalData ? (
        <div className="space-y-2">
          <div className="text-sm">
            <span className="text-gray-600">JD: </span>
            <span className="font-mono">{additionalData.jd?.toFixed(5) || '--'}</span>
          </div>
          <div className="text-sm">
            <span className="text-gray-600">Лунный день: </span>
            <span className="font-semibold">{additionalData.lunar_day || '--'}</span>
          </div>
          <div className="text-sm">
            <span className="text-gray-600">Фаза: </span>
            <span className="font-semibold">{additionalData.phase || '--'}</span>
          </div>
          <div className="text-sm">
            <span className="text-gray-600">Освещённость: </span>
            <span>{additionalData.illumination?.toFixed(1) || '--'}%</span>
          </div>
          {additionalData.next_phase && (
            <div className="text-sm mt-2 pt-2 border-t">
              <span className="text-gray-600">Следующая фаза: </span>
              <div className="font-semibold">{additionalData.next_phase.type}</div>
              <div className="text-xs text-gray-500">
                {additionalData.next_phase.time_utc || '--'}
              </div>
            </div>
          )}
        </div>
      ) : widget.id === 'julian_day' && additionalData ? (
        <div className="space-y-2">
          <div className="text-2xl font-mono text-center">{additionalData.jd?.toFixed(5) || '--'}</div>
        </div>
      ) : (
        <>
          {canInput && (
            <div className="flex gap-2 mb-4">
              <input
                type="number"
                min="1"
                max="31"
                value={date?.day || ''}
                onChange={(e) => handleInputChange('day', e.target.value)}
                placeholder="День"
                className="w-20 p-2 border border-gray-300 rounded text-center"
              />
              <input
                type="number"
                min="1"
                max="12"
                value={date?.month || ''}
                onChange={(e) => handleInputChange('month', e.target.value)}
                placeholder="Месяц"
                className="w-20 p-2 border border-gray-300 rounded text-center"
              />
              <input
                type="number"
                min="1"
                value={date?.year || ''}
                onChange={(e) => handleInputChange('year', e.target.value)}
                placeholder="Год"
                className="flex-1 p-2 border border-gray-300 rounded text-center"
              />
            </div>
          )}
          
          <div className={`text-lg font-semibold text-center ${!canInput ? 'mt-4' : ''}`}>
            {displayDate}
          </div>
        </>
      )}

      {isSource && (
        <div className="mt-2 text-xs text-blue-600 text-center">
          Источник
        </div>
      )}
      {isTarget && (
        <div className="mt-2 text-xs text-green-600 text-center">
          Цель
        </div>
      )}
    </div>
  );
}

export default CalendarWidget;
