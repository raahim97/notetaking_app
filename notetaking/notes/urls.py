from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('note_detail/<id>/', note_detail, name='note_detail'),
    path('edit_note/<id>/', edit_note, name='edit_note'),
    path('delete_note/<id>/', delete_note, name='delete_note'),
    path('login/', login_attempt, name='login_attempt'),
    path('register/', register_attempt, name='register_attempt'),
    path('logout/', logout_attempt, name='logout_attempt'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
