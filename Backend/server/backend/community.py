from .models import UserPost
from .serializers import UserPostSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def post(request, format=None):
    if request.method == 'GET':
        post = UserPost.objects.all()
        serializer = UserPostSerializer(post, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserPostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            post_data = serializer.data
            response_data={
                'success': True,
                'details': post_data
            }
            return JsonResponse(response_data, status = 201)
        else:
            return JsonResponse({'error':'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error':'Invalid request method'}, status = 400)