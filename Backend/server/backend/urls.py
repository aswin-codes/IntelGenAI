from django.contrib import admin
from django.urls import path
from backend import signup_views
from backend import login_views
from backend import marketplace
from backend import comments
from backend import community

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", signup_views.sign_up),
    path("login/",login_views.login, name = 'login'),
    path("marketplace/", marketplace.product),
    path("comments/", comments.comment),
    path("community/",community.post),

]
