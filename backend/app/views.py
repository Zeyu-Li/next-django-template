from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from common.logging.logging_service import Logger
from common.email.email_service import send_email

# Create your views here.
# Sends a real email on every call, so only staff may trigger it; otherwise anyone could
# use it to spam the recipient and burn the SMTP/SendGrid quota.
@api_view(['GET'])
@permission_classes([IsAdminUser])
def test(request):
    Logger().info("test")
    send_email('Test', 'This is a test email', 'hello@antarcticsolutions.ca')
    return Response("+1")
