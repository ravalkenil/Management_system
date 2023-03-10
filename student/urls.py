from re import template
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    # path('',include('student.urls')),
    path('',views.register_request,name="register"),
    path('login/',views.loginform,name="loginform"),
    path('Sdashbord/',views.Sdashbord,name="dashbord"),
    path('Fdashbord/',views.Facultydashbord,name="facultydashbord"),
    path('logout/',views.user_logout,name="user_logout"),
    path('trackapplication/',views.track_appliction,name="trackapplication_student"),
    path('studentdashbord/',views.student_dashbord,name="studentdashbord"),
    path('changepassword/',views.user_changepassword,name="changepassword"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complate/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    path('save/',views.savedata,name="savedata"),
    path('save1/',views.savedata1,name="savedata1"),
    path('api/',include('student.api.urls'))
]