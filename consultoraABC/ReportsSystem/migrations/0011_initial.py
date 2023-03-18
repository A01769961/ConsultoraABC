# Generated by Django 4.1.7 on 2023-03-17 23:18

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ReportsSystem', '0010_delete_consultor_delete_proyecto_delete_reportes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='consultor',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=8, max_length=8, prefix='id_', primary_key=True, serialize=False)),
                ('id_proyecto', models.IntegerField()),
                ('status', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=8, max_length=8, prefix='id_', primary_key=True, serialize=False)),
                ('id_administrador', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='reportes',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=8, max_length=8, prefix='id_', primary_key=True, serialize=False)),
                ('id_consultor', models.IntegerField()),
                ('id_administrador', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('hora', models.IntegerField()),
                ('txt_consultor', models.TextField()),
                ('acredita_admin', models.BooleanField()),
                ('txt_admin', models.TextField()),
                ('acredita_cliente', models.BooleanField()),
                ('txt_cliente', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('PlastName', models.CharField(max_length=40)),
                ('MLastName', models.CharField(max_length=40)),
                ('mail', models.CharField(max_length=20)),
                ('contrasenia', models.CharField(max_length=16)),
                ('rol', models.CharField(max_length=3)),
            ],
        ),
    ]
