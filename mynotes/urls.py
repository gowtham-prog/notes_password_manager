from django.urls import path
from . import apps
from . import views
urlpatterns =[
      path("",views.active,name="index"),
      path("index", views.index, name="index"),
      path("login",views.login_view,name="login"),
      path("register",views.register,name="register"),
      path("logout",views.logout_view,name="logout"),
      path("home",views.homepage,name="homepage"),
      path("notes",views.fnotes,name="notes"),
      path("about",views.about,name="about"),
      path("contact",views.contact,name="contact"),
      path(r'^create/',views.create,name="create"),
      path("create_pwd", views.create_pwd, name= "create_pwd"),
      path("retrieve", views.retrieve, name="retrieve"),
      path("decrypter/<int:id>", views.decrypter, name="decrypter"),
      path("delete/<int:id>",views.delete,name= "delete"),
      path("nlogin",views.nlogin,name="nlogin"),
      path("blogin",views.blogin,name="blogin"),
      path("dlogin/<int:id>", views.dlogin,name="dlogin"),
      path("deletion/<int:id>", views.deletion, name = "deletion"),
]