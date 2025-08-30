from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from server.apps.playground.models import Item
from server.apps.playground.serializer import ItemSerializer


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


class GetAllItemsView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class GetItemDetailView(APIView):
    def get(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
        serializer = ItemSerializer(item)
        return Response(serializer.data)


class GetNameItemsView(APIView):
    def get(self, request, name):
        items = Item.objects.filter(name=name)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class CreateItemView(APIView):
    def post(self, request):
        try:
            if not request.data.get("name"):
                return Response({"error": "Name field is required."}, status=400)

            serializer = ItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
