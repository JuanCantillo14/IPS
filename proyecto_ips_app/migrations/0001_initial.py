# Generated by Django 5.1.2 on 2025-02-28 00:25

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('documento', models.CharField(max_length=20, unique=True, verbose_name='Número de documento')),
                ('tipo_doc', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('CE', 'Cedula de Extranjeria'), ('TI', 'Tarjeta de Identidad'), ('RC', 'Registro Civil')], max_length=2, verbose_name='Tipo de documento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('I', 'Indefinido')], max_length=1, verbose_name='Genero')),
                ('tipo_sangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, verbose_name='Tipo de sangre')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=10, verbose_name='Número de telefono')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad de residencia')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección de residencia')),
                ('eps', models.CharField(blank=True, max_length=100, verbose_name='EPS')),
                ('tipo_poblacion', models.CharField(choices=[('N/A', 'Ninguna'), ('PIV', 'Poblacion Infantil vulnerable'), ('AMV', 'Adulto mayor vulnerable'), ('M', 'Migrante'), ('PD', 'Población desmovilizada'), ('CI', 'Comunidad indigena'), ('VFP', 'Veterano fuerza pública')], max_length=100, verbose_name='Tipo de población')),
                ('estado_civil', models.CharField(choices=[('S', 'Soltero/a'), ('C', 'Casado/a'), ('V', 'Viudo/a'), ('UL', 'Union libre'), ('D', 'Divorciado/a')], max_length=20, verbose_name='Estado civil')),
                ('tipo_regimen', models.CharField(choices=[('C', 'Cotizante'), ('B', 'Beneficiario'), ('A', 'Adicional'), ('N/A', 'No aplica')], max_length=20, verbose_name='Tipo de regimen')),
                ('estrato_social', models.CharField(choices=[('E1', 'Estrato 1'), ('E2', 'Estrato 2'), ('E3', 'Estrato 3'), ('E4', 'Estrato 4'), ('E5', 'Estrato 5'), ('E6', 'Estrato 6')], max_length=20, verbose_name='Estrato social')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='usuario/img', verbose_name='Imagen de Usuario')),
                ('password', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_antecedentes', models.CharField(max_length=50, unique=True, verbose_name='Código de antecedentes')),
                ('patologicos', models.TextField(verbose_name='Antecedentes patológicos')),
                ('quirurgicos', models.TextField(verbose_name='Antecedentes quirurgicos')),
                ('alergicos', models.TextField(verbose_name='Antecedentes alergicos')),
                ('ginecologicos', models.TextField(verbose_name='Antecedentes ginecológicos')),
                ('obstetricos', models.TextField(verbose_name='Antecedentes obstetricos')),
                ('farmacologicos', models.TextField(verbose_name='Antecedentes farmacológicos')),
                ('familiares', models.TextField(verbose_name='Antecedentes familiares')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_enfermedad', models.TextField(blank=True, verbose_name='Codigo del diagnóstico')),
                ('nombre_enfermedad', models.TextField(blank=True, verbose_name='Nombre de la enfermedad')),
                ('descr_enfermedad', models.TextField(blank=True, verbose_name='Descripción de la enfermedad')),
            ],
        ),
        migrations.CreateModel(
            name='Vacunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_vacuna', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField()),
                ('dosis', models.CharField(max_length=100)),
                ('fecha_vac', models.DateField()),
                ('nro_dosis', models.CharField(max_length=50)),
                ('refuerzos', models.CharField(max_length=100)),
                ('via_aplicacion', models.CharField(max_length=100)),
                ('eventos_adversos', models.TextField()),
                ('intervalo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('turno', models.CharField(blank=True, choices=[('6am-2pm', '6:00 AM - 2:00 PM'), ('2pm-10pm', '2:00 PM - 10:00 PM'), ('10pm-6am', '10:00 PM - 6:00 AM')], max_length=50, verbose_name='Turno')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('proyecto_ips_app.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ocupacion', models.CharField(blank=True, max_length=100, verbose_name='Ocupación')),
                ('tipo_paciente', models.CharField(choices=[('ESTANDAR', 'Estandar'), ('PREMIUM', 'Premium')], default='ESTANDAR', max_length=10, verbose_name='Tipo de paciente')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('proyecto_ips_app.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AuxAdmin',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='proyecto_ips_app.empleado')),
                ('departamento_trabajo', models.CharField(blank=True, max_length=100, verbose_name='Departamento de trabajo')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('proyecto_ips_app.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('empleado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='proyecto_ips_app.empleado')),
                ('tarjeta_prof', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Número de tarjeta profesional')),
                ('especializacion', models.CharField(blank=True, max_length=100, verbose_name='Especialización(Si la posee)')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('proyecto_ips_app.empleado',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_remision', models.CharField(max_length=50, unique=True, verbose_name='Codigo de remisión')),
                ('fecha_consulta', models.DateTimeField(default=datetime.date.today, verbose_name='Fecha de consulta')),
                ('hora_consulta', models.TimeField(verbose_name='Hora de la consulta')),
                ('motivo_consulta', models.TextField(verbose_name='Motivo de consulta')),
                ('nombre_acompañante', models.CharField(blank=True, max_length=100, verbose_name='Nombre del acompañante')),
                ('parentesco_acompañante', models.CharField(blank=True, max_length=50, verbose_name='Parentesco del acompañante')),
                ('diagnostico', models.CharField(max_length=50)),
                ('cabeza_cuello_otros', models.TextField(blank=True, verbose_name='Cabeza, cuello, otras consideraciones')),
                ('cardiorespiratorio', models.TextField(blank=True, verbose_name='Cardiorespiratorio')),
                ('gastrointestinal', models.TextField(blank=True)),
                ('genito_urinario', models.TextField(blank=True)),
                ('osteomuscular', models.TextField(blank=True)),
                ('extremidad_inferior', models.TextField(blank=True, verbose_name='Extremidades inferiores')),
                ('neurologico', models.TextField(blank=True, verbose_name='Consideraciones neurológicas')),
                ('hematopoyetico', models.TextField(blank=True)),
                ('piel_farenas', models.TextField(blank=True, verbose_name='Piel, farenas')),
                ('otros', models.TextField(blank=True, verbose_name='Otras consideraciones')),
                ('descripcion', models.TextField(blank=True, verbose_name='')),
                ('peso', models.CharField(max_length=5, verbose_name='Peso(kg)')),
                ('talla', models.CharField(max_length=5, verbose_name='Talla(cm)')),
                ('respiracion', models.CharField(max_length=5, verbose_name='Respiración')),
                ('pulso', models.CharField(max_length=5, verbose_name='Pulso')),
                ('temperatura', models.CharField(max_length=5, verbose_name='Temperatura(°C)')),
                ('medicamento', models.CharField(max_length=100, verbose_name='Medicamento remitido')),
                ('dosificacion', models.CharField(max_length=100, verbose_name='Dosificación del medicamento')),
                ('via_admon', models.CharField(max_length=50, verbose_name='Via de Administración')),
                ('cantidad', models.CharField(max_length=50, verbose_name='Cantidad')),
                ('recomendacion', models.TextField(blank=True, verbose_name='Recomendaciones')),
                ('punto_entrega', models.CharField(max_length=200, verbose_name='Punto de entrega')),
                ('tipo_convenio', models.CharField(blank=True, max_length=10, verbose_name='Tipo de convenio')),
                ('dato_contacto', models.CharField(max_length=10, verbose_name='Datos de contacto')),
                ('fecha_exp', models.DateTimeField(default=datetime.date.today, verbose_name='Fecha de expedición de la orden médica')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='proyecto_ips_app.paciente', verbose_name='Paciente')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='proyecto_ips_app.medico', verbose_name='Medico')),
            ],
        ),
    ]
