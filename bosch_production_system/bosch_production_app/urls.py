from django.urls import path
from . import views
urlpatterns = [
path('',views.show_login_page),
    path('select/',views.show_select_page),
    path('register/',views.show_register_page),
    path('admin_dashboard/',views.show_admin_dashboard, name='admin_dashboard'),
    path('users/',views.show_users, name='users'),
    path('components/',views.show_components, name='components'),
    path('inbox/',views.show_inbox, name='inbox'),
    path('profile/',views.show_profile, name='profile'),
    # manager
    # path('manager_dashboard/',views.show_manager_dashboard, name='profile'),
    # path('mcomponents/',views.show_m_components, name='components'),
    # path('minbox/',views.show_m_inbox, name='inbox'),
    # path('mprofile/',views.show_m_profile, name='profile')
]