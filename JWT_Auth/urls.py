from django.conf.urls import url
from .views import Login, Verify

urlpatterns = [
    url(r"^login", Login.as_view(), name="get_jwt"),
    url(r"^verify", Verify.as_view(), name="verify_jwt"),
]
