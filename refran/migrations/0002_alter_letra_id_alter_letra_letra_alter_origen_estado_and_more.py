# Generated by Django 4.2.7 on 2024-04-04 07:28

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('refran', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letra',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='letra',
            name='letra',
            field=models.CharField(max_length=1, unique=True, verbose_name='Letra'),
        ),
        migrations.AlterField(
            model_name='origen',
            name='estado',
            field=models.CharField(blank=True, choices=[('r', 'Revisión'), ('a', 'Aprobado')], default='r', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='origen',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='origen',
            name='nombre',
            field=models.CharField(max_length=120, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='palabra',
            name='estado',
            field=models.CharField(blank=True, choices=[('r', 'Revisión'), ('a', 'Aprobada')], default='r', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='palabra',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Registrada'),
        ),
        migrations.AlterField(
            model_name='palabra',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='palabra',
            name='palabra',
            field=models.CharField(max_length=31, verbose_name='Palabra'),
        ),
        migrations.AlterField(
            model_name='palabra',
            name='significado',
            field=models.TextField(default='', max_length=352, verbose_name='Significado'),
        ),
        migrations.AlterField(
            model_name='refran',
            name='dicho',
            field=models.TextField(max_length=191, verbose_name='Refrán'),
        ),
        migrations.AlterField(
            model_name='refran',
            name='estado',
            field=models.CharField(blank=True, choices=[('r', 'Revisión'), ('a', 'Aprobado'), ('p', 'Publicado')], default='r', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='refran',
            name='explicacion',
            field=models.TextField(max_length=251, verbose_name='Explicación'),
        ),
        migrations.AlterField(
            model_name='refran',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
