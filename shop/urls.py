from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path("",views.index,name="shop"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("login/",views.login,name="Log_in"),
     path("signup/",views.signup,name="sign_up"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/",views.checkout,name="Checkout"),
]