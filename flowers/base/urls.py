from django.urls import path
from .import views
from base.form import contactform, Order,BookingForm
from django.contrib.auth.views import LogoutView



urlpatterns=[
    path('',views.home,name='home'),
    path('flowers/',views.flowers,name='flowers'),
    path('contact/',views.contact,name='contact'),
    path('order/',views.order,name='order'),
    path('booking/',views.booking,name='booking'),
    
    path('success/',views.success,name='success'),
    path('flowerlist/', views.flower_list, name='flowerlist'),
    path('flower/<int:id>/',views.flower_detail,name='flowerdetail'),
    
    path('login/',views.login,name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),



]