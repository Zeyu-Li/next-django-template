from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from common.logging.logging_service import Logger

# Create your tests here.
class AppTest(TestCase):
    def setUp(self):
        pass

    def testLogging(self):
        Logger().info("Log Working")

    def testAnonymousUserCannotTriggerTestEmail(self):
        response = self.client.get('/')
        self.assertResponse403(response)
        self.assertEqual(len(mail.outbox), 0)

    def testAdminCanTriggerTestEmail(self):
        admin = get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')
        self.client.force_login(admin)
        response = self.client.get('/')
        self.assertResponse200(response)
        self.assertEqual(len(mail.outbox), 1)

    def assertResponse200(self, response):
        """ Given response has status_code 200 OK"""
        self.assertEqual(response.status_code, 200)

    def assertResponse201(self, response):
        """ Given response has status_code 201 CREATED"""
        self.assertEqual(response.status_code, 201)

    def assertResponse301(self, response):
        """ Given response has status_code 301 MOVED PERMANENTLY"""
        self.assertEqual(response.status_code, 301)

    def assertResponse302(self, response):
        """ Given response has status_code 302 FOUND"""
        self.assertEqual(response.status_code, 302)

    def assertResponse400(self, response):
        """ Given response has status_code 400 BAD REQUEST"""
        self.assertEqual(response.status_code, 400)

    def assertResponse401(self, response):
        """ Given response has status_code 401 UNAUTHORIZED"""
        self.assertEqual(response.status_code, 401)

    def assertResponse403(self, response):
        """ Given response has status_code 403 FORBIDDEN"""
        self.assertEqual(response.status_code, 403)

    def assertResponse404(self, response):
        """ Given response has status_code 404 NOT FOUND"""
        self.assertEqual(response.status_code, 404)
