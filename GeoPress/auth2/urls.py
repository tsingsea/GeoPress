# https://www.django-rest-framework.org/tutorial/quickstart/#urls
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'auth2' # 解决<form class="form" action="{% url 'auth2:register' %}" method="post">报错
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register, name='register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))#drf编程
]