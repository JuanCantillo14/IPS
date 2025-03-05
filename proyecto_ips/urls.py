"""
URL configuration for proyecto_ips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from proyecto_ips_app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('accounts/',include('django.contrib.auth.urls')),

    path('usuario/registrar/', registrar_usuario, name='registrar_usuario'),
    path('usuario/eliminar/<int:usuario_id>', eliminar_usuario, name='eliminar_usuario'),
    path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
    path('usuario/actualizar/', actualizar_usuario, name='actualizar_usuario'),
    path('usuario/detallar/', detallar_usuario, name='detallar_usuario'),
    path('usuario/ver-perfil/', ver_perfil_usuario, name='perfil_usuario'),
    path('usuario/login/', login_usuario, name='login_usuario'),
    path('usuario/logout/', logout_usuario, name='logout_usuario'),

    #Urls de Paciente
    path('paciente/insertar/',crear_paciente, name='crear_paciente'),
    path('paciente/listar/',listar_paciente,name='listar_paciente'),
    path('paciente/detallar/<int:id>/',detallar_paciente, name='detallar_paciente'),
    path('paciente/actualizar/<int:id>/', actualizar_paciente, name='actualizar_paciente'),
    path('paciente/eliminar/<int:id>/',eliminar_paciente,name='eliminar_paciente'),

    #Urls de Medico
    path('medico/insertar/',crear_medico, name='crear_medico'),
    path('medico/listar/',listar_medico,name='listar_medico'),
    path('medico/detallar/<int:id>/',detallar_medico, name='detallar_medico'),
    path('medico/actualizar/<int:id>/', actualizar_medico, name='actualizar_medico'),
    path('medico/eliminar/<int:id>/',eliminar_medico,name='eliminar_medico'),
    path('medico/ver-perfil/', ver_perfil_medico, name='perfil_medico'),
    #Urls de Aux Admin
    path('aux_admin/insertar/',crear_aux_admin, name='crear_aux_admin'),
    path('aux_admin/listar/',listar_aux_admin,name='listar_aux_admin'),
    path('aux_admin/detallar/<int:id>/',detallar_aux_admin, name='detallar_aux_admin'),
    path('aux_admin/actualizar/<int:id>/', actualizar_aux_admin, name='actualizar_aux_admin'),
    path('aux_admin/eliminar/<int:id>/',eliminar_aux_admin,name='eliminar_aux_admin'),

    #Urls de Cita Medica
    path('cita/insertar/',crear_cita, name='crear_cita'),
    path('cita/listar/',listar_citas,name='listar_citas'),

    #Urls de Login y Logout
    # path('registration/login/',login_usuario,name='login_usuario'),
    # path('registration/logout/',logout_usuario,name='logout_usuario'),

    path('hc/listar/',listar_hc,name='listar_hc'),
    path('antecedentes/insertar/',crear_antecedentes, name='crear_antecedentes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
