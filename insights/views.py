from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import FacebookPage, Post
from .serializers import FacebookPageSerializer, PostSerializer
from .scraper import scrape_facebook_page

@api_view(["GET"])
def get_facebook_page(request, username):
    try:
        page = FacebookPage.objects.get(username=username)
    except FacebookPage.DoesNotExist:
        page = scrape_facebook_page(username)
        if not page:
            return Response({"error": "Page not found"}, status=404)

    serializer = FacebookPageSerializer(page)
    return Response(serializer.data)

@api_view(["GET"])
def get_recent_posts(request, username):
    posts = Post.objects.filter(page__username=username).order_by("-created_at")
    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(posts, request)
    
    serializer = PostSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
