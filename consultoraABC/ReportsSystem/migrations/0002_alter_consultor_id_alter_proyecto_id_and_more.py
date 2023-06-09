# Generated by Django 4.1.7 on 2023-03-17 04:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ReportsSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
