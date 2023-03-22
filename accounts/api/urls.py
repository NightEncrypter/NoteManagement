from django.urls import path
from . import views
urlpatterns=[
    
    path('',views.getComments,name="get-comment"),
    path('comment',views.comment,name="comment"),
]