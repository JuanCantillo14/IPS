from django import forms
from proyecto_ips_app.models import *
from django.core.exceptions import ValidationError
import os

class UsuarioFormulario(forms.ModelForm):
    class Meta:
        model= Usuario
        fields=[
            # 'username', 
            'first_name', 
            'last_name', 
            'email' ,
            'documento',
            'tipo_doc',
            'genero',
            'tipo_sangre',
            'fecha_nacimiento',
            'telefono',
            'ciudad',
            'direccion',
            'eps',
            'tipo_poblacion',
            'estado_civil',
            'tipo_regimen',
            'estrato_social',
            'imagen',
            'password', 
        ]
        
        widgets= {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen':forms.FileInput()
        }
        
        def validar_imagen(self):
            imagen = self.cleaned_data.get(imagen)

            if imagen:
                extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
                if extension not in ['jpg', 'png', 'jpeg']:
                    raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
                if imagen.size > 102400:
                    raise ValidationError('El tamaño máximo del archivo es 100 KB')
            return imagen

class PacienteFormulario(forms.ModelForm):
    class Meta:
        model= Paciente
        fields=[
            # 'username', 
            'first_name', 
            'last_name', 
            'email' ,
            'documento',
            'tipo_doc',
            'genero',
            'tipo_sangre',
            'fecha_nacimiento',
            'telefono',
            'ciudad',
            'direccion',
            'eps',
            'tipo_poblacion',
            'estado_civil',
            'tipo_regimen',
            'estrato_social',
            'imagen',
            'ocupacion',
            'tipo_paciente',
            'password', 
        ]
        widgets= {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen':forms.FileInput()
        }
        
        # def validar_imagen(self):
        #     imagen = self.cleaned_data.get(imagen)

        #     if imagen:
        #         extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
        #         if extension not in ['jpg', 'png', 'jpeg']:
        #             raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
        #         if imagen.size > 102400:
        #             raise ValidationError('El tamaño máximo del archivo es 100 KB')
        #     return imagen

class MedicoFormulario(forms.ModelForm):
    class Meta:
        model= Medico
        fields= [
            # 'username', 
            'first_name', 
            'last_name', 
            'email' ,
            'documento',
            'tipo_doc',
            'genero',
            'tipo_sangre',
            'fecha_nacimiento',
            'telefono',
            'ciudad',
            'direccion',
            'eps',
            'tipo_poblacion',
            'estado_civil',
            'tipo_regimen',
            'estrato_social', 
            'imagen',
            'turno',
            'cargo',
            'tarjeta_prof',
            'especializacion',
            'password', 
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen':forms.FileInput()
        }
        
        # def validar_imagen(self):
        #     imagen = self.cleaned_data.get(imagen)

        #     if imagen:
        #         extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
        #         if extension not in ['jpg', 'png', 'jpeg']:
        #             raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
        #         if imagen.size > 102400:
        #             raise ValidationError('El tamaño máximo del archivo es 100 KB')
        #     return imagen

class AuxAdminFormulario(forms.ModelForm):
    class Meta:
        model= AuxAdmin
        fields=[
            # 'username', 
            'first_name', 
            'last_name', 
            'email' ,
            'documento',
            'tipo_doc',
            'genero',
            'tipo_sangre',
            'fecha_nacimiento',
            'telefono',
            'ciudad',
            'direccion',
            'eps',
            'tipo_poblacion',
            'estado_civil',
            'tipo_regimen',
            'estrato_social', 
            'imagen',
            'turno',
            'cargo',
            'departamento_trabajo',
            'password', 
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen':forms.FileInput()
        }
        
        # def validar_imagen(self):
        #     imagen = self.cleaned_data.get(imagen)

        #     if imagen:
        #         extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
        #         if extension not in ['jpg', 'png', 'jpeg']:
        #             raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
        #         if imagen.size > 102400:
        #             raise ValidationError('El tamaño máximo del archivo es 100 KB')
        #     return imagen
        
class DiagnosticoFormulario(forms.ModelForm):
    class Meta:
        model= Diagnostico
        fields= [
            'codigo_enfermedad',
            'nombre_enfermedad',
            'descr_enfermedad'
        ]

class CitaMedicaFormulario(forms.ModelForm):
    class Meta:
        model=CitaMedica
        
        fields=[
            'paciente',
            'medico',
            'codigo_remision',
            'fecha_consulta',
            'hora_consulta',
            'motivo_consulta',
            'nombre_acompañante',
            'parentesco_acompañante',
            'diagnostico',
            'cabeza_cuello_otros',
            'cardiorespiratorio',
            'gastrointestinal',
            'genito_urinario',
            'osteomuscular',
            'extremidad_inferior',
            'neurologico',
            'hematopoyetico',
            'piel_farenas',
            'otros',
            'descripcion',
            'peso',
            'talla',
            'respiracion',
            'pulso',
            'temperatura',
            'medicamento',
            'dosificacion',
            'via_admon',
            'cantidad',
            'recomendacion',
            'punto_entrega',
            'tipo_convenio',
            'dato_contacto',
            'fecha_exp'
        ]
        widgets = {
            'fecha_consulta': forms.DateInput(attrs={'type': 'date'}),
            'fecha_exp': forms.DateInput(attrs={'type': 'date'}),
            'hora_consulta': forms.TimeInput(attrs={'type':'time'}),
        }


class VacunasFormulario(forms.ModelForm):
    class Meta:
        model = Vacunas
        exclude = ['cita']
        fields=[
            'cod_vacuna',
            'descripcion',
            'dosis',
            'fecha_vac',
            'nro_dosis',
            'refuerzos',
            'via_aplicacion',
            'eventos_adversos',
            'intervalo'
        ]
        widgets={
            'fecha_vac': forms.DateInput(attrs={'type': 'date'})
        }
        
class AntecedentesFormulario(forms.ModelForm):
    class Meta: 
        model= Antecedentes
        fields= [
            'cod_antecedentes',
            'patologicos',
            'quirurgicos',
            'alergicos',
            'ginecologicos',
            'obstetricos',
            'farmacologicos',
            'familiares'
        ]        
