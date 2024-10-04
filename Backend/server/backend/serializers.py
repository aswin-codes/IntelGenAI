from rest_framework import serializers
from .models import User
from .models import UserPost
from .models import Comments
from .models import Market_prod
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','username','password','email','language']

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['img','title','description',]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['username','description','likes']

class Market_ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market_prod
        fields = ['title','img','price','description','duration','type']