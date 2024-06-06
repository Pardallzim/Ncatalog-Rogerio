# Generated by Django 5.0.6 on 2024-06-05 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('descript', models.TextField()),
                ('path', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Curtida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('curtida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.curtida')),
                ('roupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.roupa')),
            ],
        ),
        migrations.AddField(
            model_name='curtida',
            name='members',
            field=models.ManyToManyField(through='myapp.Comentario', to='myapp.roupa'),
        ),
    ]
