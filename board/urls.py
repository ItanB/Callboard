from django.contrib import admin
from django.urls import path, include

from .views import AdList, AdDetail, CreateAd, AdUpdate, AdDelete, ReplyList, ReplyCreate, ReplyUpdate, delete_reply, PostSearch, AccountDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('board', AdList.as_view(), name='list'),
    path('<int:pk>', AdDetail.as_view(), name='fullad'),
    path('create/', CreateAd.as_view(), name='create'),
    path('<int:pk>/update/', AdUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', AdDelete.as_view(), name='delete'),
    path('replies/', ReplyList.as_view(), name='replies'),
    path('reply/create/', ReplyCreate.as_view(), name='reply_create'),
    path('reply/<int:pk>/update/', ReplyUpdate.as_view(), name='reply_update'),
    path('delete/<int:pk>/', delete_reply, name='delete_reply'),
    path('account/<int:pk>/', AccountDetail.as_view(), name='account'),
    path('search/', PostSearch.as_view(), name='search'),

]