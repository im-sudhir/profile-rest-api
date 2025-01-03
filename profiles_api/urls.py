from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router =DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profile', views.UserProfileViewSet)
router.register(f'feed', views.UserProfileFeedViewset)

urlpatterns=[
    # path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]