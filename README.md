# OrangeHRM Selenium Portfolio Project

Mini proyecto de portfolio QA con Python, Selenium y pytest.

## Incluye
- Page Object Model (POM)
- BasePage reutilizable
- Fixture de pytest para el driver
- Test de login exitoso
- Test de login inválido
- Logging básico
- Screenshots

## Estructura
```text
orangehrm-selenium/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   └── test_login.py
├── screenshots/
├── conftest.py
├── requirements.txt
└── README.md
```

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
pytest -s -v
```

Las capturas se guardan en la carpeta `screenshots/`.
