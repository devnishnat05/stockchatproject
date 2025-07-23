from django.urls import path,include
from rest_framework.routers import DefaultRouter
from chatbot.views import BookViewSet

router= DefaultRouter()
router.register (r'test',BookViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
