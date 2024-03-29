from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',v.s.loginPage,name='login'),
    path('home/',v.s.homePage,name='home'),
    path('signUp/',v.s.signUpPage,name='signUp'),
    path('signOut/',v.s.signOut,name='signOut'),
    path('signIn/',v.s.signIn,name='signIn'),
    path('addProduct/',v.s.addProduct,name='addProduct'),
    path('addToCart/<int:id>',v.s.addToCart,name='addToCart'),
    path('cart/',v.s.cart,name='cart'),
    path('remove/<int:id>',v.s.remove,name='remove'),
    path('checkOut/',v.s.checkOut,name='checkOut'),
    path('history/',v.s.history,name='history'),
    path('update/<int:id>',v.s.update,name='update'),
    path('delete/<int:id>',v.s.delete,name='delete'),
    path('customers/',v.s.customers,name='customers'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)