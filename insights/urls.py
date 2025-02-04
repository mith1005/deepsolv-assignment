from django.urls import path
from .views import get_facebook_page, get_recent_posts

urlpatterns = [
    path("page/<str:username>/", get_facebook_page, name="get_facebook_page"),
    path("posts/<str:username>/", get_recent_posts, name="get_recent_posts"),
]
