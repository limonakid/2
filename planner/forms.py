from django import forms


THEME_CHOICES = [
    ('light', 'Светлая'),
    ('dark', 'Тёмная'),
]

LANGUAGE_CHOICES = [
    ('ru', 'Русский'),
    ('en', 'English'),
]

NOTIFICATION_CHOICES = [
    ('email', 'Email'),
    ('telegram', 'Telegram'),
    ('sms', 'SMS'),
]


class EventSettingsForm(forms.Form):
    title = forms.CharField(label='Название события', max_length=100)
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='Время', widget=forms.TimeInput(attrs={'type': 'time'}))
    category = forms.ChoiceField(
        label='Категория',
        choices=[
            ('study', 'Учёба'),
            ('work', 'Работа'),
            ('personal', 'Личное'),
            ('meeting', 'Встреча'),
        ],
    )
    notification_type = forms.ChoiceField(label='Тип уведомлений', choices=NOTIFICATION_CHOICES)
    reminder_minutes = forms.ChoiceField(
        label='Напомнить заранее',
        choices=[
            ('10', 'За 10 минут'),
            ('30', 'За 30 минут'),
            ('60', 'За 1 час'),
            ('1440', 'За 1 день'),
        ],
    )
    interface_language = forms.ChoiceField(label='Язык интерфейса', choices=LANGUAGE_CHOICES)
    theme = forms.ChoiceField(label='Тема', choices=THEME_CHOICES)
    notes = forms.CharField(label='Комментарий', required=False, widget=forms.Textarea(attrs={'rows': 4}))
