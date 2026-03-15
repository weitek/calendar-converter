# AGENTS.md - Agent Coding Guidelines

This document provides guidelines for agentic coding agents working in this repository.

## Project Overview

Calendar Converter - A web application for converting dates between different calendar systems (Gregorian, Julian, Hebrew, Chinese, Julian Day, Lunar phases). Built with React + Vite (frontend), FastAPI (backend), Node.js service, and Caddy reverse proxy.

## Build/Lint/Test Commands

### Backend (Python/FastAPI)

```bash
# Install dependencies
cd backend
pip install -r requirements.txt
pip install -r requirements-test.txt

# Run development server with hot reload
uvicorn main:app --reload

# Run all tests
pytest tests/ -v

# Run single test file
pytest tests/unit/test_hebrew.py -v

# Run single test
pytest tests/unit/test_hebrew.py::TestHebrew::test_to_hebrew_known_date -v

# Run tests with coverage
pytest tests/ --cov=. --cov-report=html
```

### Frontend (React/Vite)

```bash
cd frontend
npm install
npm run dev      # Development server
npm run build    # Production build
npm test         # Run tests (vitest)
npm test -- --watch  # Watch mode
```

### Docker (Full Stack)

```bash
docker-compose up -d    # Build and start all services
docker-compose logs -f  # View logs
docker-compose down     # Stop all services
```

## Code Style Guidelines

### Python (Backend)

**Imports:** Standard library first, then third-party, then local. Use explicit relative imports: `from services import hebrew`. Sort alphabetically.

**Formatting:** Use Black (line length: 100). 4 spaces for indentation. Use f-strings. Add trailing commas.

**Types:** Use type hints for all function parameters and return types. Use `Optional[X]` over `X | None`.

**Naming:**
- Classes: `PascalCase` (e.g., `DateModel`)
- Functions/variables: `snake_case` (e.g., `to_hebrew`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `HEBREW_EPOCH`)
- Private: prefix with underscore

**Error Handling:** Always wrap conversion logic in try/except. Return error info: `{"source": "...", "value": None, "error": str(e)}`

**API Endpoints:** Use `async def`. Add docstrings (in Russian). Use appropriate HTTP methods. Return Pydantic models.

**Project Structure:**
```
backend/
├── main.py           # FastAPI app entry point
├── config.py         # Settings
├── models.py          # Pydantic models
├── routers/          # API route handlers
│   ├── convert.py
│   └── widgets.py
├── services/         # Business logic
│   ├── gregorian_julian.py
│   ├── hebrew.py
│   ├── chinese.py
│   ├── lunar_phase.py
│   └── jd.py
└── tests/
    ├── unit/
    └── integration/
```

### JavaScript/React (Frontend)

**Imports:** ES6 syntax. Group: React/libraries, components, utilities.

**Formatting:** Prettier. 2 spaces. Use const/let, not var. Prefer arrow functions.

**Naming:**
- Components: `PascalCase` (e.g., `CalendarWidget`)
- Functions: `camelCase` (e.g., `handleDateChange`)
- Files: `kebab-case.js` or `PascalCase.jsx`

**Components:** Functional components with hooks. Keep small. Extract reusable logic into custom hooks.

**State:** useState for local state, useEffect for side effects. Clean up subscriptions.

**Error Handling:** Wrap async in try/catch. Display user-friendly errors.

**Project Structure:**
```
frontend/src/
├── App.jsx
├── main.jsx
├── components/
│   ├── Header.jsx
│   ├── CalendarWidget.jsx
│   └── SummaryModal.jsx
├── services/api.js
└── utils/
    ├── converter.js
    └── dateFormats.js
```

## General Guidelines

1. **Environment:** Never commit secrets. Use `.env.example`.
2. **Config:** All via environment or `.env`, not hardcoded.
3. **Testing:** Write tests for new features. Follow existing patterns.
4. **Comments:** Add for complex logic only.
5. **Docstrings:** Google-style for Python.
6. **Commits:** Meaningful messages describing the "why".

## Single Test Commands

```bash
# Python
pytest tests/unit/test_hebrew.py::TestHebrew::test_to_hebrew_known_date -v

# JavaScript
npm test -- --run src/utils/dateFormats.test.js
```

## Development Workflow

1. Create feature branch
2. Make incremental commits
3. Run tests before submitting
4. Follow style guidelines
5. Update docs if needed

## LSP Configuration

The following LSP/config files are set up for IDE support:

- `.vscode/settings.json` - VS Code settings (Pylsp for Python, Prettier for JS/TS)
- `pyrightconfig.json` - Python type checking configuration
- `frontend/tsconfig.json` - TypeScript configuration for frontend
- `frontend/.eslintrc.json` - ESLint configuration

### Recommended VS Code Extensions

- Python: `ms-python.python`, `ms-python.black-formatter`, `ms-python.isort`
- JavaScript/React: `dbaeumer.vscode-eslint`, `esbenp.prettier-vscode`
- All: `editorconfig.editorconfig`
