from django.urls import path
from .views import joinform, join, loginform, joinsuccess, checkemail, login, logout, update, updateform

app_name = "users"
urlpatterns = [
    path('joinform/', joinform, name="joinform"),
    path('join/', join, name="join"),
    path('joinsuccess', joinsuccess, name="joinsuccess"),

    path('api/checkemail', checkemail, name="checkemail"),

    path('loginform/', loginform, name="loginform"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),

    path('updateform', updateform, name="updateform"),
    path('update', update, name="update"),
]
