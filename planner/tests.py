from django.test import TestCase
from django.urls import reverse


class PlannerViewsTest(TestCase):
    def test_home_page_opens(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'EventPlanner')

    def test_create_event_sets_cookies_and_redirects(self):
        response = self.client.post(
            reverse('create_event'),
            {
                'title': 'Тестовое событие',
                'date': '2026-04-10',
                'time': '12:30',
                'category': 'study',
                'notification_type': 'email',
                'reminder_minutes': '30',
                'interface_language': 'ru',
                'theme': 'dark',
                'notes': 'Проверка формы',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.cookies['theme'].value, 'dark')
        self.assertEqual(response.cookies['language'].value, 'ru')
