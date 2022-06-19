from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.logging.logging_service import Logger

# Create your views here.
@api_view(['GET'])
def test(request):
    Logger().info("test")
    return Response("+1")
