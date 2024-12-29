from django.urls import path

from . import views

urlpatterns=[
    path('<page>/',views.action),
    path('',views.index),
    path('auth/<page>/',views.auth),
    path('<page>/<operation>/<int:id>', views.actionId)
]