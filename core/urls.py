"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hrms.admin import hr_site
from pm.admin import pm_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr/', hr_site.urls),
    path('pm/', pm_site.urls),
]

admin.site.index_title = 'Admin Dashboard'
admin.site.site_header = 'Build It Bros Administration'
admin.site.site_title = 'Build It Bros | core'
