# Generated by Django 2.2.2 on 2019-11-27 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20191126_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='aluno',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistema.Aluno'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='ano_letivo',
            field=models.IntegerField(default='2019'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='titulacao',
            field=models.CharField(default='Titular', max_length=50),
        ),
    ]