# Generated by Django 2.1.4 on 2019-02-17 17:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo_jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='nome')),
                ('slug', models.SlugField(blank=True, verbose_name='slug')),
                ('descricao', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Conteúdo')),
                ('imagem', models.ImageField(blank=True, default='', null=True, upload_to='foto/post', verbose_name='Foto')),
                ('iframe', models.CharField(blank=True, default='', max_length=350, null=True, verbose_name='iframe url')),
                ('criado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='nome')),
                ('slug', models.SlugField(blank=True, verbose_name='slug')),
                ('descricao', ckeditor.fields.RichTextField(blank=True, default='', null=True, verbose_name='Conteúdo')),
                ('imagem', models.ImageField(blank=True, default='', null=True, upload_to='foto/post', verbose_name='Foto')),
                ('criado', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='capitulo_jogo',
            name='chave_estrangeira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Jogo', verbose_name='jogo'),
        ),
    ]
