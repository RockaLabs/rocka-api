from django.conf.urls import url, include

from rest_framework import routers

from api.views.user import UserViewSet
from api.views.profile import rocker_list

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
	url(r'',(include(router.urls))),
	url(r'profiles',rocker_list),

]