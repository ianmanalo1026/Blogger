from django.urls import path
from core.views import (HomeListView, 
                        CreatePostView, 
                        DetailPostView, 
                        UpdatePostView, 
                        DeletePostView,
                        MyProfileView,
                        OtherUserProfileView)
app_name = "core"

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('create', CreatePostView.as_view(), name='create'),
    path('myprofile', MyProfileView.as_view(), name='myprofile'),
    path('user', OtherUserProfileView.as_view(), name='user'),
    path('detail/<int:pk>', DetailPostView.as_view(), name='detail'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
]
