from django.db import models

class FacebookPage(models.Model):
    username = models.CharField(max_length=255, unique=True)
    page_name = models.CharField(max_length=255, null=True, blank=True)
    page_url = models.URLField(null=True, blank=True)
    fb_id = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    total_followers = models.IntegerField(null=True, blank=True)
    total_likes = models.IntegerField(null=True, blank=True)
    creation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.page_name or self.username

class Post(models.Model):
    page = models.ForeignKey(FacebookPage, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    post_url = models.URLField()
    likes = models.IntegerField()
    comments_count = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post from {self.page.username}"
