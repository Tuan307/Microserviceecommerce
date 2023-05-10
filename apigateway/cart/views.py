from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartSerializer
from rest_framework.decorators import api_view
import requests
# Create your views here.

@api_view(['POST'])
def post( request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        userId = request.data.get("userId")
        user = getOneUser(userId)
        if user.status_code != 200:
            return Response(status=404)
        #userId = user.data.id
        productId = request.data.get("productId")
        product = getOneProduct(productId)
        if product.status_code != 200:
            return Response(status=404)
        url = "http://127.0.0.1:8001/cart/"
        data = {}
        data["productId"] = productId
        data["userId"] = userId
        response = requests.post(url, data)
        return Response(data,status=200)

@api_view(['GET'])
def get( request, userId):
    url = "http://127.0.0.1:8001/cartuser/"+str(userId)
    response = requests.get(url)
    return Response(data=response.json(), status=200)


def getOneUser(userId):
    url = "http://127.0.0.1:8003/user/"+str(userId)
    response = requests.get(url)
    return response

def getOneProduct(productId):
    url = "http://127.0.0.1:8002/product/"+str(productId)
    response = requests.get(url)
    return response
