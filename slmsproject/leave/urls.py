from django.urls import path
from .import views

urlpatterns=[
    path('apply/',views.apply_leave,name='apply_leave'),
    path('myleave/',views.my_leaves,name='my_leaves'),
    path('view/',views.view_leaves,name='view_leaves'),
    path('approve/<int:id>/',views.approve_leave,name='approve_leave'),
    path('reject/<int:id>/',views.reject_leave,name='reject_leave'),
]
