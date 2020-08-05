from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('users', views.create_users),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('feels', views.create_feels), 
    path('comment', views.create_comment), 
    path('like/<int:feels_id>', views.create_like),
    path('unlike/<int:feels_id>', views.delete_like),
    path('logout', views.logout)
]