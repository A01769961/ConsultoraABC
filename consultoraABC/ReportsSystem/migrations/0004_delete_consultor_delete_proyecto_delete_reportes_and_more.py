# Generated by Django 4.1.7 on 2023-03-17 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReportsSystem', '0003_alter_consultor_status_alter_usuario_mlastname_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='consultor',
        ),
        migrations.DeleteModel(
            name='proyecto',
        ),
        migrations.DeleteModel(
            name='reportes',
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
