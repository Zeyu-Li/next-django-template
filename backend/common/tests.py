import os
import subprocess
import sys

from django.conf import settings
from django.test import TestCase
from common.logging.logging_service import Logger

# Create your tests here.
class CommonsTest(TestCase):
    def setUp(self):
        pass

    def testLogging(self):
        Logger().info("Log Working")


class SettingsTest(TestCase):
    """Loads backend.settings in a fresh interpreter with a controlled environment."""

    BASE_ENV = {
        'SECRET_KEY': 'test-secret-key',
        'SENDGRID_USERNAME': 'user',
        'SENDGRID_PASSWORD': 'password',
    }

    def load_settings(self, **env):
        child_env = {k: v for k, v in os.environ.items() if k not in ('DJANGO_DEBUG', 'SECRET_KEY', 'ALLOWED_HOSTS')}
        child_env.update(self.BASE_ENV)
        child_env.update({k: v for k, v in env.items() if v is not None})
        for key in [k for k, v in env.items() if v is None]:
            child_env.pop(key, None)
        child_env['DJANGO_SETTINGS_MODULE'] = 'backend.settings'
        return subprocess.run(
            [sys.executable, '-c', 'from django.conf import settings; print(settings.DEBUG, settings.ALLOWED_HOSTS)'],
            cwd=settings.BASE_DIR, env=child_env, capture_output=True, text=True,
        )

    def testDebugFalseStringDisablesDebug(self):
        result = self.load_settings(DJANGO_DEBUG='False')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith('False'), result.stdout)

    def testDebugIsOffByDefault(self):
        result = self.load_settings(DJANGO_DEBUG=None)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith('False'), result.stdout)

    def testDebugTrueStringEnablesDebug(self):
        result = self.load_settings(DJANGO_DEBUG='True')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(result.stdout.startswith('True'), result.stdout)

    def testSecretKeyHasNoHardcodedFallback(self):
        result = self.load_settings(SECRET_KEY=None)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('SECRET_KEY', result.stderr)

    def testAllowedHostsComeFromEnvironment(self):
        result = self.load_settings(ALLOWED_HOSTS='api.example.com,localhost')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("['api.example.com', 'localhost']", result.stdout)

    def testUnknownHostIsRejected(self):
        response = self.client.get('/healthcheck/status', HTTP_HOST='evil.example')
        self.assertEqual(response.status_code, 400)

    def testHealthCheck(self):
        response = self.client.get('/healthcheck/status')
        self.assertEqual(response.status_code, 200)
