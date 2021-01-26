from django.urls import path
from accounts.views import ProfileUserView, SignInUserView, CreateUserView

app_name = "accounts"

urlpatterns = [
    path('profile/', ProfileUserView.as_view(), name="profile"),
    path('signin/', SignInUserView.as_view(), name="signin"),
    path('create/', CreateUserView.as_view(), name="create"),
    
]
