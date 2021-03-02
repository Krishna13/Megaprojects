from django.shortcuts import render

# Create your views here.
def show_login_page(request):
    return render(request,'login.html')

def show_select_page(request):
    return render(request,'select.html')

def show_register_page(request):
    return render(request,'register.html')

# ADMIN

def show_admin_dashboard(request):
    return render(request,'admin_templates/dashboard.html')

def show_users(request):
    return render(request, "admin_templates/user.html")

def show_components(request):
    return render(request, "admin_templates/component.html")


def show_inbox(request):
    return render(request, "admin_templates/inbox.html")

def show_profile(request):
    return render(request, "admin_templates/profile.html")


# Manager


def show_manager_dashboard(request):
    return render(request,'manager_templates/dashboard.html')

def show_m_users(request):
    return render(request, "manager_templates/user.html")

def show_m_components(request):
    return render(request, "manager_templates/component.html")


def show_m_inbox(request):
    return render(request, "manager_templates/inbox.html")

def show_m_profile(request):
    return render(request, "manager_templates/profile.html")