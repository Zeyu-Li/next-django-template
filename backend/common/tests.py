from django.test import TestCase
from common.logging.logging_service import Logger

# Create your tests here.
class CommonsTest(TestCase):
    def setUp(self):
        pass

    def testLogging(self):
        Logger().info("Log Working")