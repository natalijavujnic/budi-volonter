from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.shortcuts import redirect

class YourTestCase(TestCase):
    def setUp(self):
        from ..model_funcs import (insertActivity, insertOrganization,
                                  insertVolunteer)
        self.factory = RequestFactory()
        self.user = insertVolunteer('marko', 'markovic', '1990-01-01', 'marko@gmail.com', 'Pass1234', '')
        self.org = insertOrganization(ime='TestOrg', pib=88888888, telefon='0616357399', email='org@gmail.com', lozinka='Pass1234')
        self.act = insertActivity(org=self.org, name='testAkt', desc='', spots=1, startD='2024-09-09', endD='2025-02-02', deadline='2025-02-01', reqs='', city='', country='Srbija', categories='')

    def apply_middleware(self, request):
        # Function to pass to middleware
        get_response = lambda req: None

        # Apply the SessionMiddleware
        session_middleware = SessionMiddleware(get_response)
        session_middleware.process_request(request)
        request.session.save()

        # Apply the AuthenticationMiddleware
        auth_middleware = AuthenticationMiddleware(get_response)
        auth_middleware.process_request(request)

    def test_NoUser(self):
        request = self.factory.post(reverse('view_applications'), {})
        from ..views import view_applications

        self.apply_middleware(request)

        response = view_applications(request)
        self.assertEqual(response.status_code, 302)  # Check for redirect status
        self.assertEqual(response.url, reverse('login'))  # Check redirect URL

    def test_userVol(self):
        request = self.factory.post(reverse('view_applications'), {})
        from ..views import view_applications

        self.apply_middleware(request)
        request.user = self.user

        response = view_applications(request)
        self.assertEqual(response.status_code, 302)  # Check for redirect status
        self.assertEqual(response.url, reverse('welcome'))  # Check redirect URL

