from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator,MinLengthValidator, MaxLengthValidator,EmailValidator,FileExtensionValidator, MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _
import datetime
import os

# Create your models here.

#Tipos de Usuarios 

def user_directory_path(instance, filename):
    # subcarpeta="img"
    return f"usuario/img/{instance.id}_{filename}"

def validar_telefono(value):
    if len(value)!=10:
        raise ValidationError(_("%(value)s no es un número telefónico válido"),
            params={"value": value},
        )
def validar_nombre(value):
    value=RegexValidator
    value(
    regex=r'^[A-Za-z\s]+$',
    message="El nombre solo debe contener letras y espacios"
    )
    
validar_documento=RegexValidator(
    regex=r'^\d{6,10}',
    message="El número de documento no es válido"
)

validar_password=RegexValidator(
    regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{4,}$',
    message="La contraseña debe tener mínimo 4 caracteres, una mayúscula, un número y un carácter especial"
)
mesan="Hola"
    
class Usuario(AbstractUser):
    TIPO_DOC=[('CC','Cedula de Ciudadania'),
              ('CE','Cedula de Extranjeria'),
              ('TI','Tarjeta de Identidad'),
              ('RC','Registro Civil')]
    GENERO=[('M','Masculino'),
            ('F','Femenino'),
            ('I','Indefinido')]
    TIPO_SANGRE=[('A+','A+'),
                 ('A-','A-'),
                 ('B+','B+'),
                 ('B-','B-'),
                 ('AB+','AB+'),
                 ('AB-','AB-'),
                 ('O+','O+'),
                 ('O-','O-')]
    TIPO_POBLACION=[('N/A','Ninguna'),
                    ('PIV','Poblacion Infantil vulnerable'),
                    ('AMV','Adulto mayor vulnerable'),
                    ('M','Migrante'),
                    ('PD','Población desmovilizada'),
                    ('CI','Comunidad indigena'),
                    ('VFP','Veterano fuerza pública')]
    ESTADO_CIVIL=[('S','Soltero/a'),
                  ('C','Casado/a'),
                  ('V','Viudo/a'),
                  ('UL','Union libre'),
                  ('D','Divorciado/a')]
    TIPO_REGIMEN=[('C','Cotizante'),
                  ('B','Beneficiario'),
                  ('A','Adicional'),
                  ('N/A','No aplica')]
    ESTRATO_SOCIAL=[('E1','Estrato 1'),
                    ('E2','Estrato 2'),
                    ('E3','Estrato 3'),
                    ('E4','Estrato 4'),
                    ('E5','Estrato 5'),
                    ('E6','Estrato 6')]
    first_name=models.CharField(max_length=100,null=False, verbose_name='Nombres',validators=[validar_nombre,MinLengthValidator(3, message="El campo debe contener minimo 3 caracteres")])
    last_name=models.CharField(max_length=100,null=False, verbose_name='Apellidos',validators=[validar_nombre,MinLengthValidator(5, message="El campo debe contener minimo 5 caracteres")])
    email=models.EmailField(max_length=100,null=False,unique=True,verbose_name='Correo electrónico',validators=[EmailValidator(message="Correo electrónico inválido")])
    documento=models.IntegerField(unique=True, null=False,verbose_name='Número de documento',validators=[validar_documento])
    tipo_doc=models.CharField(choices=TIPO_DOC,max_length=2, verbose_name='Tipo de documento')
    genero=models.CharField(max_length=1,null=False,choices=GENERO, verbose_name='Genero')
    tipo_sangre=models.CharField(max_length=3,null=False,choices=TIPO_SANGRE, verbose_name='Tipo de sangre')
    fecha_nacimiento=models.DateField(null=False, verbose_name='Fecha de nacimiento',validators=[MaxValueValidator(datetime.date.today)])
    telefono=models.CharField(max_length=10,null=False, verbose_name='Número de telefono', validators=[validar_telefono],unique=True)
    ciudad=models.CharField(max_length=100, null=False,verbose_name='Ciudad de residencia',validators=[validar_nombre])
    direccion=models.CharField(max_length=100,null=False, verbose_name='Dirección de residencia')
    eps=models.CharField(max_length=100,blank=True, verbose_name='EPS')
    tipo_poblacion=models.CharField(max_length=100,null=False,choices=TIPO_POBLACION, verbose_name='Tipo de población')
    estado_civil=models.CharField(max_length=20,null=False,choices=ESTADO_CIVIL, verbose_name='Estado civil       ')
    tipo_regimen=models.CharField(max_length=20,null=False,choices=TIPO_REGIMEN, verbose_name='Tipo de regimen')
    estrato_social=models.CharField(max_length=20,null=False, choices=ESTRATO_SOCIAL, verbose_name='Estrato social')
    imagen=models.ImageField(upload_to=user_directory_path,blank=True, null=True, verbose_name='Imagen de Usuario',validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])]) #IMAGEEEEEEEEEEEEN
    password=models.CharField(max_length=100, null=False, verbose_name='Contraseña', validators=[validar_password])
    #arl 
    
    @property 
    def medico(self):
        return isinstance(self,Medico)

    @property
    def aux_admin(self):
        return isinstance(self,AuxAdmin)
    
    @property
    def paciente(self):
        return isinstance(self,Paciente)
    
    def delete(self,*args,**kwards): # Numero indefinido de argumentos **
        if self.imagen:
            imagen_path=self.imagen.path
            if os.path.exists(imagen_path):
                os.remove(imagen_path)
        super().delete(*args,**kwards)
    
    def save(self,*args,**kwards):
        if not self.username: 
            self.username=self.documento
        if self.id:
            usuario_antiguo=Usuario.objects.filter(id=self.id).get()
            if usuario_antiguo and usuario_antiguo.imagen:
                imagen_anterior=usuario_antiguo.imagen.path
                if self.imagen!=usuario_antiguo.imagen:
                    if os.path.exists(imagen_anterior):
                        os.remove(imagen_anterior)
        super().save(*args,**kwards)
        
class Paciente(Usuario):
    ocupacion=models.CharField(max_length=100,blank=True, verbose_name='Ocupación')
    TIPO_PACIENTE = [
        ('ESTANDAR', 'Estandar'),
        ('PREMIUM', 'Premium')
        ]
    tipo_paciente = models.CharField(max_length=10, choices=TIPO_PACIENTE, default='ESTANDAR',verbose_name='Tipo de paciente')
    
    def __str__(self):
        return self.first_name, self.last_name

    
class Empleado(Usuario):
    TURNO=[('6am-2pm','6:00 AM - 2:00 PM'),
           ('2pm-10pm', '2:00 PM - 10:00 PM'),
           ('10pm-6am','10:00 PM - 6:00 AM')]
    turno=models.CharField(max_length=50,blank=True, verbose_name='Turno', choices=TURNO)
    cargo=models.CharField(max_length=100, null=False, verbose_name='Cargo')
    
    def __str__(self):
        return self.first_name

class Medico(Empleado):
    tarjeta_prof=models.CharField(max_length=50, null=False, unique=True, db_index=True, verbose_name='Número de tarjeta profesional')
    especializacion=models.CharField(max_length=100, blank=True, verbose_name='Especialización(Si la posee)')

    def __str__(self):
        return self.first_name

class AuxAdmin(Empleado):
    departamento_trabajo=models.CharField(max_length=100, blank=True,verbose_name='Departamento de trabajo')
    
    def __str__(self):
        return self.first_name


#Cita Medica 

class Diagnostico(models.Model):
    codigo_enfermedad=models.TextField(blank=True, verbose_name='Codigo del diagnóstico')
    nombre_enfermedad=models.TextField(blank=True, verbose_name='Nombre de la enfermedad')
    descr_enfermedad=models.TextField(blank=True, verbose_name='Descripción de la enfermedad')
    
class CitaMedica(models.Model):
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='citas', verbose_name='Paciente')
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='citas', verbose_name='Medico')
    codigo_remision=models.CharField(max_length=50, unique=True, null=False, verbose_name='Codigo de remisión')
    fecha_consulta=models.DateTimeField(null=False, default=datetime.date.today, verbose_name='Fecha de consulta')
    hora_consulta=models.TimeField(null=False, verbose_name='Hora de la consulta')
    motivo_consulta=models.TextField(null=False, verbose_name='Motivo de consulta')
    nombre_acompañante=models.CharField(max_length=100, blank=True, verbose_name='Nombre del acompañante')
    parentesco_acompañante=models.CharField(max_length=50, blank=True, verbose_name='Parentesco del acompañante')
    diagnostico=models.CharField(max_length=50, null=False)
    cabeza_cuello_otros=models.TextField(blank=True, verbose_name='Cabeza, cuello, otras consideraciones')
    cardiorespiratorio=models.TextField(blank=True, verbose_name='Cardiorespiratorio')
    gastrointestinal=models.TextField(blank=True)
    genito_urinario=models.TextField(blank=True)
    osteomuscular=models.TextField(blank=True)
    extremidad_inferior=models.TextField(blank=True, verbose_name='Extremidades inferiores')
    neurologico=models.TextField(blank=True, verbose_name='Consideraciones neurológicas')
    hematopoyetico=models.TextField(blank=True)
    piel_farenas=models.TextField(blank=True, verbose_name='Piel, farenas')
    otros=models.TextField(blank=True, verbose_name='Otras consideraciones')
    descripcion=models.TextField(blank=True, verbose_name='')
    peso=models.CharField(max_length=5, null=False, verbose_name='Peso(kg)')
    talla=models.CharField(max_length=5, null=False, verbose_name='Talla(cm)')
    respiracion=models.CharField(max_length=5, null=False, verbose_name='Respiración')
    pulso=models.CharField(max_length=5, null=False, verbose_name='Pulso')
    temperatura=models.CharField(max_length=5, null=False, verbose_name='Temperatura(°C)')
    medicamento=models.CharField(max_length=100, null=False, verbose_name='Medicamento remitido')
    dosificacion=models.CharField(max_length=100, null=False, verbose_name='Dosificación del medicamento')
    via_admon=models.CharField(max_length=50,null=False, verbose_name='Via de Administración')
    cantidad=models.CharField(max_length=50,null=False, verbose_name='Cantidad')
    recomendacion=models.TextField(blank=True, verbose_name='Recomendaciones')
    punto_entrega=models.CharField(max_length=200, null=False, verbose_name='Punto de entrega')
    tipo_convenio=models.CharField(max_length=10, blank=True, verbose_name='Tipo de convenio')
    dato_contacto=models.CharField(max_length=10, null=False, verbose_name='Datos de contacto')
    fecha_exp=models.DateTimeField(null=False, default=datetime.date.today, verbose_name='Fecha de expedición de la orden médica')
#Historia Clinica
    
    
class Vacunas(models.Model):
    cod_vacuna=models.CharField(max_length=50, unique=True)
    descripcion=models.TextField()
    dosis=models.CharField(max_length=100)
    fecha_vac=models.DateField()
    nro_dosis=models.CharField(max_length=50)
    refuerzos=models.CharField(max_length=100)
    via_aplicacion=models.CharField(max_length=100)
    eventos_adversos=models.TextField()
    intervalo=models.CharField(max_length=100)

class Antecedentes(models.Model):
    cod_antecedentes=models.CharField(max_length=50, unique=True, verbose_name='Código de antecedentes')
    patologicos=models.TextField(verbose_name='Antecedentes patológicos')
    quirurgicos=models.TextField(verbose_name='Antecedentes quirurgicos')
    alergicos=models.TextField(verbose_name='Antecedentes alergicos')
    ginecologicos=models.TextField(verbose_name='Antecedentes ginecológicos')
    obstetricos=models.TextField(verbose_name='Antecedentes obstetricos')
    farmacologicos=models.TextField(verbose_name='Antecedentes farmacológicos')
    familiares=models.TextField(verbose_name='Antecedentes familiares')

