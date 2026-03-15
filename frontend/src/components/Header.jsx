import { useState } from 'react';

function Header({ settings, onSettingsChange, onShowSummary }) {
  const [showSettings, setShowSettings] = useState(false);

  const handleFormatChange = (e) => {
    onSettingsChange({
      ...settings,
      dateFormat: e.target.value
    });
  };

  const handleCoordsChange = (field, value) => {
    onSettingsChange({
      ...settings,
      coordinates: {
        ...settings.coordinates,
        [field]: parseFloat(value) || 0
      }
    });
  };

  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <h1 className="text-2xl font-bold text-gray-800">
            Конвертер календарей
          </h1>
          
          <div className="flex items-center gap-4">
            <button
              onClick={() => setShowSettings(!showSettings)}
              className="text-gray-600 hover:text-gray-800"
            >
              ⚙️ Настройки
            </button>
            
            <button
              onClick={onShowSummary}
              className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
            >
              Сводка
            </button>
          </div>
        </div>

        {showSettings && (
          <div className="mt-4 p-4 bg-gray-50 rounded-lg">
            <h3 className="font-semibold mb-3">Настройки</h3>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Формат даты
                </label>
                <select
                  value={settings.dateFormat}
                  onChange={handleFormatChange}
                  className="w-full p-2 border border-gray-300 rounded"
                >
                  <option value="dd.mm.yyyy">ДД.ММ.ГГГГ</option>
                  <option value="yyyy-mm-dd">ГГГГ-ММ-ДД</option>
                </select>
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Координаты для лунных фаз
                </label>
                <div className="flex gap-2">
                  <input
                    type="number"
                    step="0.0001"
                    value={settings.coordinates.lat}
                    onChange={(e) => handleCoordsChange('lat', e.target.value)}
                    placeholder="Широта"
                    className="w-1/2 p-2 border border-gray-300 rounded"
                  />
                  <input
                    type="number"
                    step="0.0001"
                    value={settings.coordinates.lng}
                    onChange={(e) => handleCoordsChange('lng', e.target.value)}
                    placeholder="Долгота"
                    className="w-1/2 p-2 border border-gray-300 rounded"
                  />
                </div>
                <p className="text-xs text-gray-500 mt-1">
                  По умолчанию: Гринвич (51.4769, 0.0005)
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  );
}

export default Header;
