# Generated by Django 3.2.8 on 2021-10-10 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, verbose_name='Login')),
                ('senha', models.CharField(max_length=255, verbose_name='Senha')),
                ('assunto', models.CharField(max_length=255, verbose_name='Assunto')),
                ('mensagem', models.TextField(blank=True, verbose_name='Mensagem')),
            ],
        ),
        migrations.CreateModel(
            name='MensagemParaTodos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(blank=True, verbose_name='Mensagem')),
            ],
        ),
        migrations.CreateModel(
            name='PaginaCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_antigo', models.CharField(max_length=12)),
                ('preco_novo', models.CharField(max_length=12)),
                ('video_apresentacao', models.FileField(blank=True, upload_to='static/videos/videos_depoimentos')),
                ('titulo_video_1', models.CharField(blank=True, max_length=255)),
                ('video_depoimento_1', models.FileField(blank=True, upload_to='static/videos/videos_depoimentos')),
                ('titulo_video_2', models.CharField(blank=True, max_length=255)),
                ('video_depoimento_2', models.FileField(blank=True, upload_to='static/videos/videos_depoimentos')),
                ('titulo_video_3', models.CharField(blank=True, max_length=255)),
                ('video_depoimento_3', models.FileField(blank=True, upload_to='static/videos/videos_depoimentos')),
                ('titulo_video_4', models.CharField(blank=True, max_length=255)),
                ('video_depoimento_4', models.FileField(blank=True, upload_to='static/videos/videos_depoimentos')),
            ],
        ),
    ]
