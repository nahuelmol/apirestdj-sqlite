from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .views import UserViewSet, Pet_VS, CustomerViewSet
from .views import FriendsViewSet, LanguagesViewSet, CountriesViewSet  

app_name = 'apirest'

router = routers.DefaultRouter()

router.register(r'user_data', 		UserViewSet)
router.register(r'friends_data', 	FriendsViewSet)
router.register(r'languages', 		LanguagesViewSet)
router.register(r'countries', 		CountriesViewSet)
router.register(r'customer',		CustomerViewSet,basename='costumer')

urlpatterns = router.urls
