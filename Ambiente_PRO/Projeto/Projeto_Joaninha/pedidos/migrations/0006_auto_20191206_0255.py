# Generated by Django 2.1.2 on 2019-12-06 05:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_auto_20191205_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidos',
            options={'ordering': ('horario',)},
        ),
        migrations.AddField(
            model_name='pedidos',
            name='horario',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
