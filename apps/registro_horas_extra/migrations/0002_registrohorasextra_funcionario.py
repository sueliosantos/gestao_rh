# Generated by Django 4.0.2 on 2022-02-07 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_funcionario_departamentos_funcionario_empresa_and_more'),
        ('registro_horas_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohorasextra',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]