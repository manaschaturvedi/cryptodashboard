"""bitcoin_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from homepage.views import homepage
from accounts.views import user_signup,user_login,user_logout
from dashboard.views import dashboard,populate_database_with_data,get_coin_table

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='homepage'),
    url(r'^signup/', user_signup, name='user_signup'),
    url(r'^login/', user_login, name='user_login'),
    url(r'^logout/', user_logout, name='user_logout'),
    url(r'^dashboard/(?P<user_id>\d+)/$', dashboard, name='dashboard'),
    url(r'^data-seeding/', populate_database_with_data, name='populate_database_with_data'),
    url(r'^get-coin-table/', get_coin_table, name='get_coin_table'),
]
