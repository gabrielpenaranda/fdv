# Generated by Django 3.1 on 2021-06-01 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo de persona',
                'verbose_name_plural': 'Tipo de personas',
                'db_table': 'tipopersonas',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='TipoTercero',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tipo de tercero',
                'verbose_name_plural': 'Tipo de terceros',
                'db_table': 'tipoterceros',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=70, unique=True, verbose_name='Nombre')),
                ('nombre_juridico', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Nombre jurídico')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Dirección')),
                ('rif', models.CharField(blank=True, max_length=10, unique=True, verbose_name='RIF')),
                ('nit', models.CharField(blank=True, max_length=10, null=True, verbose_name='NIT')),
                ('telefono', models.CharField(blank=True, max_length=80, verbose_name='Teléfono(s)')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, verbose_name='E-mail')),
                ('web', models.URLField(blank=True, max_length=250, null=True, verbose_name='Sitio web')),
                ('descripcion_actividad', models.TextField(blank=True, null=True, verbose_name='Descripción de la actividad')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.ciudad', verbose_name='Ciudad')),
                ('tamano_empresa', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='base.tamanoempresa', verbose_name='Tamaño de empresa')),
                ('tipo_empresa', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='base.tipoempresa', verbose_name='Tipo de empresa')),
                ('tipo_tercero', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='terceros.tipotercero', verbose_name='Tipo de tercero')),
                ('tipocapital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.tipocapital', verbose_name='Tipo de capital')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.vendedor', verbose_name='Vendedor')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.zona', verbose_name='Zona')),
            ],
            options={
                'verbose_name': 'Tercero',
                'verbose_name_plural': 'Terceros',
                'db_table': 'terceros',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Sucursal')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=50, verbose_name='Teléfono(s)')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.ciudad', verbose_name='Ciudad')),
                ('tercero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='terceros.tercero', verbose_name='Tercero')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'sucursales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('cargo', models.CharField(max_length=70, verbose_name='Cargo')),
                ('telefono_oficina', models.CharField(max_length=70, verbose_name='Teléfono(s) de oficina')),
                ('telefono_celular', models.CharField(max_length=70, verbose_name='Celular')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('tercero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='terceros.tercero', verbose_name='Tercero')),
                ('tipopersona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='terceros.tipopersona', verbose_name='Tipo de persona')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'personas',
                'ordering': ['tercero_id__nombre', 'apellido', 'nombre', 'cargo'],
            },
        ),
    ]
