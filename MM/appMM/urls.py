from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path("",views.landing_page, name="landing_page"),
    path("logout", views.landing_page, name="landing_page"),
    path("our_story",views.our_story,name="our_story"),
    path("home", views.home, name="home"),
    path("signup", views.sign_up, name="sign_up"),
    path("sig_http",views.signup_http,name="signup_http"),
    path("l1", views.log_in, name="log_in"),
    path("menu", views.menu_view, name="menu_view"),
    path("books", views.books, name="books"),
    path("barista", views.barista_view, name="barista_view"),
    path("gallery", views.gallery_view, name="gallery_view"),
    path("workshop", views.workshop_view, name="workshop_view"),
    path("log_http", views.log_http, name="log_http"),
    path("path2", views.productregistration, name="productregistration"),
    path("path7/<int:id3>", views.productprofileupdate, name="productprofileupdate"),
    path("path10/<int:id2>", views.productdelete, name="productdelete"),
    path("path12", views.allproductprofiledata, name="allproductprofiledata"),
    path("path13", views.userproductdata, name="userproductdata"),
    path("path15/<int:id4>/<str:id5>/<int:id>", views.usercart, name="usercart"),
    path("path16", views.usercartdata, name="usercartdata"),
    path("path17", views.userproductsearch, name="userproductsearch"),
    path("path20", views.userbilldata, name="userbilldata"),
    path("path18", views.userbill, name="userbill"),
    path("path19/<int:id10>", views.usercartdelete, name="usercartdelete"),
    path("path22", views.userpayment, name="userpayment"),
    path("path23", views.userpaymentsuccess, name="userpaymentsuccess"),
    path("path24/<str:id>", views.data, name="data"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)