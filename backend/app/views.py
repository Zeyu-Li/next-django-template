from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger('app')

# Create your views here.
@api_view(['GET'])
def test(request):
    logger.info("test")
    return Response("+1")
