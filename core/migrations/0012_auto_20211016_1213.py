# Generated by Django 3.2.8 on 2021-10-16 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211016_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprovacao',
            name='dca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dca', verbose_name='DCA'),
        ),
        migrations.AlterField(
            model_name='catfornecedor',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor'),
        ),
        migrations.AlterField(
            model_name='compras_locacao',
            name='locacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.locacao_acao', verbose_name='ação'),
        ),
        migrations.AlterField(
            model_name='compras_locacao',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='compras_locacao',
            name='trp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trp', verbose_name='tRP'),
        ),
        migrations.AlterField(
            model_name='contfornecedor',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor'),
        ),
        migrations.AlterField(
            model_name='contrato_locacao',
            name='locacao_acao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.locacao_acao', verbose_name='Solicitação'),
        ),
        migrations.AlterField(
            model_name='contrato_locacao',
            name='pagto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pagamento', verbose_name='Pagamento'),
        ),
        migrations.AlterField(
            model_name='contrato_locacao',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='cronograma',
            name='locacao_acao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.locacao_acao', verbose_name='Solicitação'),
        ),
        migrations.AlterField(
            model_name='cronograma',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='dca',
            name='licitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.licitacao', verbose_name='Licitação'),
        ),
        migrations.AlterField(
            model_name='dca',
            name='locacao_acao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.locacao_acao', verbose_name='Solicitação'),
        ),
        migrations.AlterField(
            model_name='dca',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='endfornecedor',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='compras_loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compras_locacao'),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='tipo_pagto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipopagto', verbose_name='Tipo de Pagamento'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='locacao_acao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.locacao_acao'),
        ),
        migrations.AlterField(
            model_name='status',
            name='tipo_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_status', verbose_name='tipo de Status'),
        ),
    ]
