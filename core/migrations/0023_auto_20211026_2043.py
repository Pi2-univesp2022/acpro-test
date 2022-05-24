# Generated by Django 3.2.8 on 2021-10-26 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_locacao_acao_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras_locacao',
            name='sede',
            field=models.BooleanField(default=False, verbose_name='Sede'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='licitacao',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='descricao',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='observacoes',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='acao',
            name='projeto',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.projeto', verbose_name='projeto'),
        ),
    ]
