from rest_framework.response import Response
from rest_framework.decorators import api_view
from common.logging.logging_service import Logger
from common.email.email_service import send_email

# Create your views here.
@api_view(['GET'])
def test(request):
    Logger().info("test")
    send_email('Test', 'This is a test email', 'hello@antarcticsolutions.ca')
    return Response("+1")
