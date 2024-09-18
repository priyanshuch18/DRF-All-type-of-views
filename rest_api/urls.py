
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register('post',views.PostViewSet,basename = 'post')

urlpatterns = [
    # path('post',views.Posts,name = 'post'),
    # path('post',views.PostAPIView.as_view(),name = 'post'),
    # path('post',views.genericApiView.as_view(),name = 'post'),



    # path('post/<int:id>',views.posts_detail,name = 'posts_detail'),
    # path('post/<int:id>',views.postDetailAPIViews.as_view(),name = 'posts_detail'),
    # path('post/<int:id>/',views.genericApiView.as_view(),name = 'post'),
    path('',include(router.urls))


]

