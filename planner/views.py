from django.shortcuts import redirect, render
from .forms import EventSettingsForm

EVENTS = [
    {
        'title': 'Подготовка к экзамену по Django',
        'date': '2026-04-01',
        'time': '18:00',
        'category': 'Учёба',
        'notification_type': 'Email',
        'reminder': 'За 1 час',
    },
    {
        'title': 'Командная встреча по проекту',
        'date': '2026-04-03',
        'time': '10:30',
        'category': 'Работа',
        'notification_type': 'Telegram',
        'reminder': 'За 30 минут',
    },
    {
        'title': 'Личная тренировка',
        'date': '2026-04-05',
        'time': '08:00',
        'category': 'Личное',
        'notification_type': 'SMS',
        'reminder': 'За 10 минут',
    },
]

FEATURES = [
    'Планирование учебных, рабочих и личных событий',
    'Персональные уведомления по Email, Telegram и SMS',
    'Сохранение темы и языка интерфейса через cookies',
    'Отслеживание последней посещённой страницы',
]

STATS = {
    'active_events': 12,
    'today_reminders': 5,
    'favorite_channel': 'Telegram',
}


def _read_preferences(request):
    return {
        'theme': request.COOKIES.get('theme', 'light'),
        'language': request.COOKIES.get('language', 'ru'),
        'last_page': request.COOKIES.get('last_page', 'Главная'),
    }


def home(request):
    preferences = _read_preferences(request)
    response = render(
        request,
        'planner/home.html',
        {
            'features': FEATURES,
            'stats': STATS,
            'preferences': preferences,
        },
    )
    response.set_cookie('last_page', 'Главная', max_age=60 * 60 * 24 * 30)
    return response


def create_event(request):
    preferences = _read_preferences(request)
    initial_data = {
        'theme': preferences['theme'],
        'interface_language': preferences['language'],
    }

    if request.method == 'POST':
        form = EventSettingsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            event = {
                'title': data['title'],
                'date': data['date'].strftime('%Y-%m-%d'),
                'time': data['time'].strftime('%H:%M'),
                'category': dict(form.fields['category'].choices).get(data['category']),
                'notification_type': dict(form.fields['notification_type'].choices).get(data['notification_type']),
                'reminder': dict(form.fields['reminder_minutes'].choices).get(data['reminder_minutes']),
            }
            EVENTS.append(event)

            response = redirect('events_list')
            response.set_cookie('theme', data['theme'], max_age=60 * 60 * 24 * 30)
            response.set_cookie('language', data['interface_language'], max_age=60 * 60 * 24 * 30)
            response.set_cookie('last_page', 'Создание события', max_age=60 * 60 * 24 * 30)
            return response
    else:
        form = EventSettingsForm(initial=initial_data)

    response = render(
        request,
        'planner/create_event.html',
        {'form': form, 'preferences': preferences},
    )
    response.set_cookie('last_page', 'Создание события', max_age=60 * 60 * 24 * 30)
    return response


def events_list(request):
    preferences = _read_preferences(request)
    response = render(
        request,
        'planner/events_list.html',
        {
            'events': EVENTS,
            'preferences': preferences,
        },
    )
    response.set_cookie('last_page', 'Список событий', max_age=60 * 60 * 24 * 30)
    return response
