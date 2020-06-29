from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('users', views.create_users),
    path('dashboard', views.dashboard),
    path('feels', views.create_feels), 
    path('like/<int:feels_id>', views.create_like)
]