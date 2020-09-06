
from django.urls import path

from pwn import views



urlpatterns = [

    path('',views.showIndex,name='pwn_main'),
    path('pwn_login_check/',views.pwn_login_check,name='pwn_login_check'),
    path('welcome/',views.welcome,name='welcome'),

    path('state/',views.openState,name='state'),
    path('savestateform',views.savestateform,name='savestateform'),
    path('savestateformredirect/',views.savestateformredirect,name='savestateformredirect'),
    path('updatestate/<int:id>',views.updatestateform,name='updatestate'),
    path('deletestate/',views.deletestate,name='deletestate'),
    path('statedeleteconfirmYes/',views.statedeleteconfirmYes,name='statedeleteconfirmYes'),
    path('statedeleteconfirmNo/',views.statedeleteconfirmNo,name='statedeleteconfirmNo'),


    path('city/',views.openCity,name='city'),
    path('savecityform/',views.savecityform,name='savecityform'),
    path('savecityformredirect/',views.savecityformredirect,name='savecityformredirect'),
    path('updatecity/<int:id>',views.updatecityform,name='updatecity'),
    path('deletecity/',views.deletecity,name='deletecity'),
    path('citydeleteconfirmYes/',views.citydeleteconfirmYes,name='citydeleteconfirmYes'),
    path('citydeleteconfirmNo/',views.citydeleteconfirmNo,name='citydeleteconfirmNo'),



    path('cuisine/',views.openCusine,name='cuisine'),
    path('vendor/',views.openVendor,name='vendor'),
    path('resports/',views.openReporsts,name='reports'),
    path('logout/',views.pwn_login_check,name='logout'),
]
