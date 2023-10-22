"""
URL configuration for callboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from board.views import AdList, AdDetail, CreateAd, AdUpdate, AdDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', AdList.as_view(), name='list'),
    path('<int:pk>', AdDetail.as_view(), name='fullad'),
    path('create/', CreateAd.as_view(), name='create'),
    path('<int:pk>/update/', AdUpdate.as_view(), name='update'),
path('<int:pk>/delete/', AdDelete.as_view(), name='delete'),

]
