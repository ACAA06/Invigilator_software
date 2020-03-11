from django.urls import path

from . import views

urlpatterns = [path("login", views.login, name="login"),
               path("home", views.mail, name="lala"),
               path("dashboard", views.dashboard, name="dashboard"),
               path("fdashboard", views.fdashboard, name="fdashboard"),
               path("fallotment", views.allotmentlist, name="fallotment"),
               path("", views.session, name="logout"),
               path("addfaculty", views.addfaculty, name="addfaculty"),
               path("alteration", views.alteration, name="alteration"),
               path("accept", views.accept, name="accept"),
               path("decline", views.decline, name="decline"),
               path("addtimetable", views.addtimetable, name="addtimetable"),
               path("addexam", views.addexam, name="addexam"),
               path("allotfaculty", views.allotfaculty, name="allotfaculty"),
               path("allot", views.allot, name="allot"),
               path("rooms", views.addroom, name="room"),
               ]
