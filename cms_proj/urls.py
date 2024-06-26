"""cms_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user_app import views as user_views
from api_app import views as api_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CMS APIs",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",user_views.home,name='home'),
    path("main/", user_views.main, name = 'main'), 
    path('signin/', user_views.signin, name='signin'),
    path('signout/', user_views.signout, name='signout'),
    path('register/', user_views.register, name='register'),
    path('create_policy/', user_views.create_policy, name='create_policy'),
    path('policy_detail/', user_views.read_policy, name='read_policy'),
    path('read_claim/', user_views.read_claim, name='read_claim'),
    path('create_claim/', user_views.create_claim, name='create_claim'),
    path('', include('django_prometheus.urls')),



    
    path('api/signup/', api_views.signup_api, name='signup_api'),
    path('api/login/', api_views.login_api, name='login_api'),
    path('api/user/claims/', api_views.user_claim_list, name='user_claim_list'),
    path('api/admin/claims/', api_views.admin_claim_list, name='admin_claim_list'),
    path('api/admin/claims/<uuid:claim_id>/', api_views.admin_claim_update, name='admin_claim_update'),
    path('api/admin/claims/<uuid:claim_id>/delete/', api_views.admin_claim_delete, name='admin_claim_delete'),
    path('api/admin/policies/', api_views.admin_policy_list, name='admin_policy_list'),
    path('api/admin/policies/<int:policy_number>/', api_views.admin_policy_update, name='admin_policy_update'),
    path('api/admin/policies/<int:policy_number>/delete/', api_views.admin_policy_delete, name='admin_policy_delete'),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
