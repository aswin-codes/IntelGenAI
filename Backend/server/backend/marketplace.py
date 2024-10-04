from .models import Market_prod
from .serializers import Market_ProdSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def product(request, format=None):
    if request.method == 'GET':
        product = Market_prod.objects.all()
        serializer = Market_ProdSerializer(product, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Market_ProdSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            product_data = serializer.data
            response_data={
                'success': True,
                'details': product_data
            }
            return JsonResponse(response_data, status = 201)
        else:
            return JsonResponse({'error':'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error':'Invalid request method'}, status = 400)