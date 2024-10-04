from .models import Comments
from .serializers import CommentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def comment(request, format=None):
    if request.method == 'GET':
        comment = Comments.objects.all()
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            comment_data = serializer.data
            response_data={
                'success': True,
                'details': comment_data
            }
            return JsonResponse(response_data, status = 201)
        else:
            return JsonResponse({'error':'Invalid user data', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'error':'Invalid request method'}, status = 400)