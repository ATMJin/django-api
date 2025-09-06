from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from server.apps.playground.models import Item
from server.apps.playground.serializer import ItemSerializer
from server.utils.pagination import PageNumberWithSizePagination


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


# class ItemViewSet(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 item = Item.objects.get(pk=pk)
#                 serializer = ItemSerializer(item)
#                 return Response(serializer.data)
#             except Item.DoesNotExist:
#                 return Response({"error": "Item not found"}, status=404)
#         else:
#             items = Item.objects.all()
#             serializer = ItemSerializer(items, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         try:
#             if not request.data.get("name"):
#                 return Response({"error": "Name field is required."}, status=400)

#             serializer = ItemSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data, status=201)
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)

#     def delete(self, request, pk):
#         try:
#             item = Item.objects.get(pk=pk)
#             item.delete()
#             return Response(status=204)
#         except Item.DoesNotExist:
#             return Response({"error": "Item not found"}, status=404)

#     def put(self, request, pk):
#         try:
#             item = Item.objects.get(pk=pk)
#             serializer = ItemSerializer(item, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
#         except Item.DoesNotExist:
#             return Response({"error": "Item not found"}, status=404)
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)


class ItemViewSet(ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    # pagination_class = PageNumberPagination
    pagination_class = PageNumberWithSizePagination
    queryset = Item.objects.order_by("id")
    page_size = 5

    filter_backends = [OrderingFilter]
    ordering_fields = ["name", "id"]
