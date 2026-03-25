# EventPlanner — Django-приложение для планирования событий

Учебный проект на Django по теме: **сайт для планирования событий с настройками уведомлений**.

## Что реализовано

- новый Django-проект и приложение `planner`;
- HTML-форма создания события;
- стили через внешний CSS-файл;
- текстовый и графический контент по теме планирования событий;
- сохранение пользовательских настроек через **cookies**:
  - тема интерфейса;
  - язык интерфейса;
  - последняя посещённая страница;
- данные хранятся прямо в коде с использованием списков и словарей.

## Структура проекта

```bash
event_planner_project/
├── event_planner/
├── planner/
│   ├── static/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   └── tests.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <ВАША_ССЫЛКА_НА_GITHUB>
cd event_planner_project
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

### 3. Активация виртуального окружения

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 5. Применение миграций

```bash
python manage.py migrate
```

### 6. Запуск сервера

```bash
python manage.py runserver
```

После запуска откройте в браузере:

```text
http://127.0.0.1:8000/
```

## Проверка тестов

```bash
python manage.py test
```

## Рекомендуемая история коммитов

```bash
git init
git add .
git commit -m "Initial commit: create Django project"

git add .
git commit -m "Add views, templates, static files and cookies"

git add .
git commit -m "Add README and final polish"
```

## Публикация на GitHub

```bash
git remote add origin <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
git branch -M main
git push -u origin main
```

После публикации GitHub выдаст ссылку на репозиторий, её и нужно отправить преподавателю.
