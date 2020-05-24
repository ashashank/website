from django.conf.urls import url
from django.urls import path
from blog import views

urlpatterns = [
      url(r'^list/$',views.PostListView.as_view(),name='post_list'),
      url(r'^about/$',views.AboutView.as_view(),name='about'),
      url(r'^career/$',views.CareerView.as_view(),name='career'),
      url(r'^blogs/$',views.BlogView.as_view(),name='blogs'),
      path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
      url(r'^post/new/$',views.CreatePostView.as_view(),name='post_form'),
]
