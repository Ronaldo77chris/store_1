from django.urls import path
from apps.users.views import Username
urlpatterns=[
    path('usernames/<username:username>/count/',Username.as_view()),
]