"""capstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from capstagram.views import home
from users.views import *
from posts.views import *

urlpatterns = [
    url(r'^signin/$', UserSignIn.as_view(), name="signin"),
    url(r'^signout/$', UserSignOut.as_view(), name="signout"),
    url(r'^signup/$', UserSignUp.as_view(), name="signup"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^posts/$', PostListView.as_view(), name="list"),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name="detail"),

] + static(settings.MEDIA_URL, document_ROOT=settings.MEDIA_ROOT)
