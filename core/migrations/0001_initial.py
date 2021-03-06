# Generated by Django 3.2.8 on 2021-10-13 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('observacoes', models.CharField(max_length=100, verbose_name='Observações')),
                ('data_base', models.DateField(verbose_name='Data Base')),
            ],
            options={
                'verbose_name': 'Ação',
                'verbose_name_plural': 'Ações',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cnpj', models.CharField(max_length=50, verbose_name='CNPJ')),
                ('site', models.CharField(max_length=100, verbose_name='Site')),
                ('observacoes', models.CharField(max_length=100, verbose_name='Observaçoes')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Linguagem',
                'verbose_name_plural': 'Linguagens',
            },
        ),
        migrations.CreateModel(
            name='Locacao_Acao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(default='', max_length=50, verbose_name='Descriçao')),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.acao', verbose_name='açao')),
            ],
            options={
                'verbose_name': 'Solicitação de Locação',
                'verbose_name_plural': 'Solicitações de Locação',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locais',
            },
        ),
        migrations.CreateModel(
            name='Memorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('data_memorial', models.DateField(verbose_name='Data do Memorial')),
            ],
            options={
                'verbose_name': 'Memorial',
                'verbose_name_plural': 'Memoriais',
            },
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('valor', models.CharField(max_length=50, verbose_name='Valor')),
                ('observacoes', models.CharField(max_length=100, verbose_name='Observaçoes')),
            ],
            options={
                'verbose_name': 'Parâmetro',
                'verbose_name_plural': 'Parâmetros',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Status',
                'verbose_name_plural': 'Tipos de Status',
            },
        ),
        migrations.CreateModel(
            name='TipoLocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Locação',
                'verbose_name_plural': 'Tipos de Locação',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('tipo_status', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.tipo_status', verbose_name='tipo de Status')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('etapa', models.CharField(max_length=50, verbose_name='Etapa')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_termino', models.DateField(verbose_name='Data de Término')),
                ('locacao_acao', models.ForeignKey(default=99, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.locacao_acao')),
            ],
            options={
                'verbose_name': 'Período',
                'verbose_name_plural': 'Períodos',
            },
        ),
        migrations.AddField(
            model_name='locacao_acao',
            name='memorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.memorial', verbose_name='memorial'),
        ),
        migrations.AddField(
            model_name='locacao_acao',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.status', verbose_name='status'),
        ),
        migrations.AddField(
            model_name='locacao_acao',
            name='tipo_locacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipolocacao', verbose_name='tipo de Locaçao'),
        ),
        migrations.AddField(
            model_name='acao',
            name='linguagem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='core.linguagem', verbose_name='linguagem'),
        ),
        migrations.AddField(
            model_name='acao',
            name='local',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='core.local', verbose_name='local'),
        ),
        migrations.AddField(
            model_name='acao',
            name='projeto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='core.projeto', verbose_name='projeto'),
        ),
        migrations.AlterUniqueTogether(
            name='locacao_acao',
            unique_together={('tipo_locacao', 'acao')},
        ),
    ]
