from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home' ),

    path("user/<str:username>", UserPostListView.as_view(), name='user-posts' ),
    
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    
    path('about/', views.about, name='blog-about' ),

    path("post/new/", PostCreateView.as_view(), name="post-create"),
   
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),

    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
