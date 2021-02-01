from django.urls import path
from accounts.views import CreateUserView, SignInUserView, SignOutView, UserEditView

app_name = "accounts"

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup"),
    path('signin/', SignInUserView.as_view(), name="signin"),
    path('signout/', SignOutView.as_view(), name="signout" ),
    path('profile/update', UserEditView.as_view(), name="update" ),
    
]
