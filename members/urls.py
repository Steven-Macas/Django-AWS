from django.urls import path
from . import views

app_name = 'en_face'

urlpatterns = [
    path('', views.index, name='index'),
    path('prueba/', views.prueba, name='prueba'),
    path('upload/', views.upload, name='upload'),
    path('manage_upload/', views.manage_upload, name='manage_upload'),
    path('show_image/<int:id>', views.show_image, name='show_image'),
    path('proccess_image/<int:id>', views.proccess_image, name='proccess_image'),
    path('<int:iddetalle>/', views.detalle, name='detalle'),
    path('detalle/<int:iddetalle>/', views.detalle, name='detalle'),
    path('ajax/', views.ajax, name='ajax'),
    path('usaajax/', views.uajax, name='usaajax'),
    #path('ruta1/', views.ruta1, name = 'ruta1'),
    #path('ruta2/', views.ruta2, name = 'ruta2'),
    
]