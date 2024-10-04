from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def login(request, format=None):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username = username, password = password)
        except User.DoesNotExist:
            return JsonResponse({'error':'Invalid username or password'}, status = 400)

        user_data = UserSerializer(user).data
        response_data = {
            'success': True,
            'details': user_data
        }
        return JsonResponse(response_data, status=200)

    return JsonResponse({'error':'Invalid request method'}, status=400)