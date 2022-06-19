from django.test import TestCase
from app.logging.logging_service import logger

# Create your tests here.
class AppTest(TestCase):
    def setUp(self):
        pass

    def testLogging(self):
        Logger().info("test")
