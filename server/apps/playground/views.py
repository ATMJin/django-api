from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"message": "Hello, GET world!"})
    elif request.method == "POST":
        return Response({"message": "Hello, POST world!"})


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, world! GET"})

    def post(self, request):
        return Response({"message": "Hello, world! POST"})
