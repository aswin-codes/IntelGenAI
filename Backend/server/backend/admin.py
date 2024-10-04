from django.contrib import admin
from .models import User
from .models import UserPost
from .models import Comments
from .models import Market_prod


admin.site.register(User)
admin.site.register(UserPost)
admin.site.register(Comments)
admin.site.register(Market_prod)
