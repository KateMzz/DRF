from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# @api_view(['GET', 'POST'])
# def api_home(request, *args, **kwargs):
#     # body = request.body
#     # data ={}
#     # try:
#     #     data = json.loads(body)
#     # except:
#     #     pass
#     # print(data.keys())
#     # print(request.headers)
#     # data['headers'] = dict(request.headers)
#     # data['params'] = dict(request.GET)
#     # data['content_type'] = dict.content_type
#
#     instance = Product.objects.all().order_by("?").last()
#     data = {}
#     if instance:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return JsonResponse(data)



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

# Create your views here.
