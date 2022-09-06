from django.urls import path
from .views import signup, log_in, log_out,products

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('products/',products,name='products'),
]