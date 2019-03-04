"""Restframe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin


from app01 import views
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^publishes/$', views.PublishView.as_view(),name="publish"), #  View:view(request)=====APIView:dispatch()
    url(r'^publishes/(?P<pk>\d+)/$', views.PublishDetailView.as_view(),name="detailpublish"), #  View:view(request)=====APIView:dispatch()

    url(r'^books/$', views.BookView.as_view(),name="books"),
    url(r'^books/(\d+)/$', views.BookDetailView.as_view(),name="detailbook"),

]