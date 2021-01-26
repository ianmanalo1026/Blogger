from django.urls import path
from accounts.views import ProfileUserView, CreateUserView, SignInUserView, SignOutView

app_name = "accounts"

urlpatterns = [
    path('profile/', ProfileUserView.as_view(), name="profile"),
    path('signup/', CreateUserView.as_view(), name="signup"),
    path('signin/', SignInUserView.as_view(), name="signin"),
    path('signout/', SignOutView.as_view(), name="signout" ),
    
]
