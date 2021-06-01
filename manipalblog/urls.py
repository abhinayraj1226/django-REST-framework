from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="index"),
    path('adduser',views.addUser, name="addUser"),
    path('postblog', views.postBlog, name="postBlog"),
    path('comment', views.post_comment, name="post_comment"),
    path('updateBlog/<int:pk>', views.updateBlog, name="updateBlog"),
    path('deleteComment/<int:pk>', views.deleteComment, name="deleteComment"),
]
