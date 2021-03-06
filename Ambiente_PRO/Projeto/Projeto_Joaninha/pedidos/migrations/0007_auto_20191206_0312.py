# Generated by Django 2.1.2 on 2019-12-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_auto_20191206_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='acompanhamentos',
            field=models.CharField(choices=[('', 'Selecione'), ('Sem Acompanhamento', 'Sem Acompanhamento'), ('Banana Frita', 'Banana Frita'), ('Linguça', 'Linguiça'), ('Ovo', 'Ovo'), ('Couve(virado)', 'Couve(virado)'), ('Legumes refogados', 'Legumes refogados'), ('Escarola', 'Escarola'), ('Fritas', 'Fritas')], default='Selecione', max_length=100),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='horario',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='saladas',
            field=models.CharField(choices=[('', 'Selecione'), ('Sem Salada', 'Sem Salada'), ('Alface e pepino', 'Alface e pepino'), ('Repolho e cenoura', 'Repolho e cenoura')], default='Selecione', max_length=50),
        ),
    ]
