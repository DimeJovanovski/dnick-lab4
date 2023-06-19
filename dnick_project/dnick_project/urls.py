from django.contrib import admin
from django.urls import path
import blog_app.views as blogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', blogViews.posts, name="posts"),
    path('add/post/', blogViews.addPost, name="add_post"),
    path('profile/', blogViews.profile, name="profile"),
    path('blockedUsers/', blogViews.blockedUsers, name="blocked_users"),
]
