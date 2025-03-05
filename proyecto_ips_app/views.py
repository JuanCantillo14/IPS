from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import update_session_auth_hash
from proyecto_ips_app.models import * 
from django.contrib import messages
from proyecto_ips_app.forms import *

# Create your views here.

#Menu principal
# @login_required
def home(request):
    return render(request, 'home.html')

def inicio(request):
    tipo_usuario = None

    if request.user.is_authenticated:
        usuario_logueado = request.user
        if isinstance(usuario_logueado, Medico):
            tipo_usuario = 'Medico'
        elif isinstance(usuario_logueado, AuxAdmin):
            tipo_usuario = 'AuxAdmin'
        elif isinstance(usuario_logueado, Paciente):
            tipo_usuario = 'Paciente'
        else:
            tipo_usuario = 'Usuario no identificado'

    return render(request, 'inicio.html', {'tipo_usuario': tipo_usuario})

def login_usuario(request):
    if request.method == 'POST':
        username_recibido = request.POST.get('username')
        password_recibido = request.POST.get('password')
        
        if not username_recibido or not password_recibido:
            return render(request, 'usuario/login.html', {'mensaje_error': 'Por favor, complete todos los campos.'})
        
        usuario = authenticate(request, username=username_recibido, password=password_recibido)
        
        if usuario is not None:
            login(request, usuario)
            
            # Verificar el tipo de usuario
            if Medico.objects.filter(id=usuario.id).exists():
                return render(request, 'medico/perfil.html', {'tipo_usuario': 'Medico'})
            elif AuxAdmin.objects.filter(id=usuario.id).exists():
                return render(request, 'aux_admin/perfil.html', {'tipo_usuario': 'AuxAdmin'})
            elif Paciente.objects.filter(id=usuario.id).exists():
                return render(request, 'paciente/perfil.html', {'tipo_usuario': 'Paciente'})
            else:
                messages.error(request, 'El usuario no tiene un rol válido asignado.')
                return redirect('home')
                
        return render(request, 'usuario/login.html', {'mensaje_error': 'Credenciales incorrectas, intente de nuevo.'})

    return render(request, 'usuario/login.html')

# def login_usuario(request):
#     if request.method == 'POST':
#         username_recibido = request.POST.get('username')
#         password_recibido = request.POST.get('password')
        
#         if not username_recibido or not password_recibido:
#             return render(request, 'usuario/login.html', {'mensaje_error': 'Por favor, complete todos los campos.'})
        
#         usuario = authenticate(request, username=username_recibido, password=password_recibido)
        
#         if usuario is not None:
#             login(request, usuario)
            
#             # Verificar el tipo de usuario
#             if hasattr(usuario, 'medico'):
#                 return render(request,'medico/perfil.html',{'tipo_usuario':'Medico'})
#                 # return redirect('detallar_medico')
#             elif hasattr(usuario, 'aux_admin'):
#                 return render(request, 'aux_admin/perfil.html', {'tipo_usuario': 'AuxAdmin'})
#             elif hasattr(usuario, 'paciente'):
#                 return render(request, 'paciente/perfil.html', {'tipo_usuario': 'Paciente'})
#             else:
#                 messages.error(request, 'El usuario no tiene un rol válido asignado.')
#                 return redirect('home')
#         return render(request, 'usuario/login.html', {'mensaje_error': 'Credenciales incorrectas, intente de nuevo.'})
#     return render(request, 'usuario/login.html')
    
def logout_usuario(request):
    logout(request)
    return redirect('home')

# region usuario

def registrar_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = formulario.save(commit=False) # Se crea un objeto usuario en memoria
            # Cifra la contraseña utilizando set_password()
            usuario.set_password(formulario.cleaned_data['password'])
            usuario.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('registrar_usuario')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = UsuarioFormulario()
    return render(request, 'usuario/insertar.html', {'formulario': formulario})

@login_required
def actualizar_usuario(request):
    usuario = request.user  # Usuario logueado

    if request.method == 'POST':
        formulario = UsuarioFormulario(request.POST, request.FILES, instance=usuario)  # Se incluye request.FILES
        
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # Aún no guardar en la BD
            nueva_password = formulario.cleaned_data.get('password')

            if nueva_password:
                usuario.set_password(nueva_password)

            # Si se subió una nueva imagen, actualizarla
            if 'imagen' in request.FILES:
                usuario.imagen = request.FILES['imagen']
            
            # Si el usuario dejó el campo de imagen en blanco, eliminar la imagen
            elif not formulario.cleaned_data.get('imagen'):
                usuario.imagen = None  

            usuario.save()  # Ahora sí guardamos todo en la BD
            update_session_auth_hash(request, usuario)  # Mantiene la sesión activa después de actualizar la contraseña            
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('perfil_usuario')

        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')

    else:
        formulario = UsuarioFormulario(instance=usuario)

    return render(request, 'usuario/actualizar.html', {'formulario': formulario})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar.html', {'usuarios':usuarios})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect(listar_usuarios)

@login_required
def ver_perfil_usuario(request):
    usuario = request.user.id  # Ver página el perfil del usuario
    return render(request, 'usuario/detallar.html', {'usuario': usuario})

@login_required
def detallar_usuario(request):
    usuario = request.user.id  # Ver los detalles del usuario
    return render(request, 'usuario/detallar.html', {'usuario': usuario })

# region Paciente
#Metodos de Paciente
# @login_required
def crear_paciente(request):
    if request.method=='POST':
        formulario= PacienteFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            paciente=formulario.save(commit=False)
            #contraseña encriptada :)
            paciente.set_password(formulario.cleaned_data['password'])
            paciente.save()
            messages.success(request, 'Paciente registrado en el sistema éxitosamente')
            return redirect('crear_paciente')
        else:
            messages.error(request, 'Se encontraron errores en el registro. Vuelva a intentarlo')
    else: 
        formulario= PacienteFormulario()
    return render(request, 'paciente/insertar.html',{'formulario':formulario})

def listar_paciente(request): 
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/listar.html', {'pacientes':pacientes})

def detallar_paciente(request,id):
    pacientes=get_object_or_404(Paciente,id=id)
    return render(request,'paciente/detallar.html',{'paciente':pacientes})

def actualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == "POST":
        formulario = PacienteFormulario(request.POST, instance=paciente)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            # Si el usuario cambió la contraseña se la cifra antes de pasarla al objeto medico
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                paciente.set_password(nueva_password)
            paciente.save()
            messages.success(request, 'paciente actualizado exitosamente.')
            return redirect('detallar_paciente', id)
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = PacienteFormulario(instance=paciente)
    return render(request, 'paciente/actualizar.html', {'formulario': formulario})

def eliminar_paciente(request,id):
    paciente=get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('listar_paciente')

# region Aux Administrativo
#Metodos de Aux Administrativo
def crear_aux_admin(request):
    if request.method=='POST':
        formulario= AuxAdminFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            aux_admin=formulario.save(commit=False)
            #contraseña encriptada :)
            aux_admin.set_password(formulario.cleaned_data['password'])
            aux_admin.save()
            messages.success(request, 'Auxiliar Administrativo registrado en el sistema éxitosamente')
            return redirect('crear_aux_admin')
        else:
            messages.error(request, 'Se encontraron errores en el registro. Vuelva a intentarlo')
    else: 
        formulario= AuxAdminFormulario()
    return render(request, 'aux_admin/insertar.html',{'formulario':formulario})

def listar_aux_admin(request):
    aux_admins = AuxAdmin.objects.all()
    return render(request, 'aux_admin/listar.html', {'aux_admins':aux_admins})

def detallar_aux_admin(request,id):
    aux_admins=get_object_or_404(AuxAdmin,id=id)
    return render(request,'aux_admin/detallar.html',{'aux_admin':aux_admins})

# def actualizar_aux_admin(request, id):
#     aux_admin = get_object_or_404(AuxAdmin, id=id)
#     if request.method == "POST":
#         formulario = AuxAdminFormulario(request.POST, instance=aux_admin)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('listar_aux_admin')  
#     else:
#         formulario = AuxAdminFormulario(instance=aux_admin)
#     return render(request, 'aux_admin/actualizar.html', {'formulario': formulario})

@login_required
def actualizar_aux_admin(request):
    try:
        aux_admin = AuxAdmin.objects.get(id=request.user.id)  # Obtiene el médico autenticado
    except AuxAdmin.DoesNotExist:
        messages.error(request, "No tienes un perfil de Auxiliar Administrativo registrado.")
        return redirect('home')

    if request.method == 'POST':
        formulario = AuxAdminFormulario(request.POST, request.FILES, instance=aux_admin)
        if formulario.is_valid():
            aux_admin = formulario.save(commit=False)

            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                aux_admin.set_password(nueva_password)
                aux_admin.save()  # Guardar antes de actualizar la sesión
                update_session_auth_hash(request,aux_admin)  # Mantiene la sesión activa
            else:
                aux_admin.save()  # Guardar normalmente si la contraseña no cambia

            messages.success(request, "Perfil Auxiliar Administrativo actualizado exitosamente.")
            return redirect('perfil_aux_admin')
        else:
            messages.error(request, "Hay errores en el formulario.")
    else:
        formulario = MedicoFormulario(instance=aux_admin)

@login_required
def ver_perfil_aux_admin(request):
    aux_admin = request.user.medico  # Ver el perfil del médico
    return render(request, 'aux_admin/detallar.html', {'aux_admin': aux_admin})

def eliminar_aux_admin(request,id):
    aux_admin=get_object_or_404(Paciente, id=id)
    aux_admin.delete()
    return redirect('listar_aux_admin')
    
# region Medico
#Metodos de Medico   
def crear_medico(request):
    if request.method == 'POST':
        formulario=MedicoFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            medico = formulario.save(commit=False)
            medico.set_password(formulario.cleaned_data['password'])
            medico.save()
            messages.success(request,'Medico creado exitosamente')
            return redirect('crear_medico')
        else:
            messages.error(request,'Hay errores en el registro. Vuelva e intentelo')
    else:
        formulario = MedicoFormulario()
        
    return render(request,'medico/insertar.html',{'formulario': formulario})

def listar_medico(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/listar.html', {'medicos':medicos})

def detallar_medico(request,id):
    medicos = get_object_or_404(Medico, id=id)
    return render(request,'medico/detallar.html',{'medico':medicos})

# def actualizar_medico(request, id):
#     medico = get_object_or_404(Medico, id=id)
#     if request.method == "POST":
#         formulario = MedicoFormulario(request.POST, instance=medico)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('listar_medico')  # Cambia por la URL adecuada
#     else:
#         formulario = MedicoFormulario(instance=medico)
#     return render(request, 'medico/actualizar.html', {'formulario': formulario})

@login_required
def actualizar_medico(request):
    try:
        medico = Medico.objects.get(id=request.user.id)  # Obtiene el médico autenticado
    except Medico.DoesNotExist:
        messages.error(request, "No tienes un perfil de médico registrado.")
        return redirect('home')

    if request.method == 'POST':
        formulario = MedicoFormulario(request.POST, request.FILES, instance=medico)
        if formulario.is_valid():
            medico = formulario.save(commit=False)

            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                medico.set_password(nueva_password)
                medico.save()  # Guardar antes de actualizar la sesión
                update_session_auth_hash(request, medico)  # Mantiene la sesión activa
            else:
                medico.save()  # Guardar normalmente si la contraseña no cambia

            messages.success(request, "Perfil médico actualizado exitosamente.")
            return redirect('perfil_medico')
        else:
            messages.error(request, "Hay errores en el formulario.")
    else:
        formulario = MedicoFormulario(instance=medico)
        
@login_required
def ver_perfil_medico(request):
    medico = request.user.medico  # Ver el perfil del médico
    return render(request, 'medico/detallar.html', {'medico': medico})

def eliminar_medico(request,id):
    medico=get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('listar_medico')

# region Cita Medica
#Metodos de cita medica

def crear_cita(request):
    if request.method == 'POST':
        formulario = CitaMedicaFormulario(request.POST)
        if formulario.is_valid():
            cita = formulario.save(commit=False)
            cita.save()
            messages.success(request, 'Cita médica creada exitosamente.')
            return redirect('listar_citas')
        else:
            messages.error(request, 'Revise los errores y continue.')
    else:
        formulario = CitaMedicaFormulario()
    return render(request, 'cita/insertar.html', {'formulario': formulario})


def listar_citas(request):
    citas = CitaMedica.objects.all()
    return render(request, 'cita/listar.html', {'citas':citas})

#Metodos de Historia Clinica
def listar_hc(request):
    antecedentes = Antecedentes.objects.all()
    citas = CitaMedica.objects.all()
    
    contexta={
        'citas':citas,
        'antecedentes':antecedentes
    }
    return render(request, 'hc/listar.html', contexta)

#Metodos de Antecedentes
def crear_antecedentes(request):
    if request.method == 'POST':
        formulario = AntecedentesFormulario(request.POST)
        if formulario.is_valid():
            antecedente = formulario.save(commit=False)
            antecedente.save()
            messages.success(request, 'Antecedentes creados exitosamente.')
            return redirect('listar_hc')
        else:
            messages.error(request, 'Revise los errores y continue.')
    else:
        formulario = AntecedentesFormulario()
    return render(request, 'antecedentes/insertar.html', {'formulario': formulario})


def listar_antecedentes(request):
    antecedentes = Antecedentes.objects.all()
    return render(request, 'antecedentes/insertar.html', {'antecedentes':antecedentes})

#Metodos de Login de Usuariososososososososososososos 



# def login_usuario(request):
#     if request.method == 'POST':
#         # Si los input no están vacíos:
#         if ((request.POST.get('username') != None) and (request.POST.get('password')) != None):
#             username_recibido = request.POST.get('username')
#             password_recibido = request.POST.get('password') 
#             autenticar = authenticate(
#                 username = username_recibido, 
#                 password = password_recibido
#                 )
#             if autenticar is not None: # Si variable autenticar no es vacía
#                 login(request, autenticar) # Guarda datos de la sesión en el navegador
#                 return redirect('home')
#             else:
#                 mensaje_error = 'Credenciales incorrectas, intente de nuevo'
#                 return render(request, 'registration/login.html', {'mensaje_error': mensaje_error})
#     else:
#         return render(request, 'registration/login.html')
    