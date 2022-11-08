from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question_id/<int:question_id>', views.question_page, name='question_page'),
    path('hot/', views.hot, name='hot'),
    path('ask/', views.ask, name='ask'),
    path('settings/', views.settings, name='settings'),
    path('tag/', views.tag, name='tag'),
    path('authorization/', views.authorization, name='authorization'),
    path('registration/', views.registration, name='registration')
]
