# Calendar Converter

Web-приложение для конвертации дат между различными календарными системами.

## Поддерживаемые календари

- **Григорианский** - современный календарь
- **Юлианский** - исторический календарь
- **Китайский** - китайский лунный календарь
- **Еврейский** - иудейский календарь
- **Julian Day** - астрономическая нумерация дней
- **Лунный** - фазы луны

## Технологический стек

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: FastAPI (Python)
- **Node.js**: для JavaScript библиотек (lunar-javascript)
- **Reverse Proxy**: Caddy
- **Container**: Docker Compose

## Запуск

### Требования

- Docker
- Docker Compose

### Команды

```bash
# Сборка и запуск всех сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f

# Остановка
docker-compose down
```

### Доступ

- Приложение доступно по адресу: http://localhost:80
- API: http://localhost:80/api
- Health check: http://localhost:80/health

## Разработка

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Тесты

```bash
cd backend
pip install -r requirements-test.txt
pytest tests/ -v
```

## Структура проекта

```
calendar-converter/
├── backend/           # FastAPI приложение
│   ├── routers/       # API endpoints
│   ├── services/      # Бизнес-логика
│   └── tests/        # Тесты
├── frontend/         # React приложение
│   └── src/
│       ├── components/
│       ├── services/
│       └── utils/
├── nodejs/           # Node.js сервис
├── caddy/           # Конфигурация Caddy
└── docker-compose.yml
```

## Конфигурация

Настройки хранятся в `.env` файле:

- `SERVER_TIMEZONE` - часовой пояс сервера
- `NODE_SERVICE_URL` - URL Node.js сервиса
- `DEFAULT_LATITUDE` / `DEFAULT_LONGITUDE` - координаты для лунных фаз
