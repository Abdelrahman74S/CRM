from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name='index'),
    path("register/",views.register , name="register"),
    path("login/",views.LoginUser,name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.LogoutUser, name='logout'),
    path('Create-Record',views.create_record,name='Create_Record'),
    path("view-record/<int:record_id>",views.view_record,name='view_record'),
    path("update-record/<int:record_id>",views.update_record,name='update_record'),
    path('delete-record/<int:record_id>',views.delete_record,name='delete_record'),
    path('search/',views.search_quary,name='search'),
    # path('404',views.Erorr_page,name='Erorr'),

]
 