# Generated by Django 2.0.7 on 2018-07-11 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0009_auto_20180710_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palpites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='bolao',
            name='imagem',
            field=models.CharField(default='bolao_padrao.jpg', max_length=100),
        ),
        migrations.AddField(
            model_name='usuariodetalhes',
            name='imagem',
            field=models.CharField(default='avatar.jpg', max_length=100),
        ),
        migrations.AddField(
            model_name='palpites',
            name='bolao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Bolao'),
        ),
        migrations.AddField(
            model_name='palpites',
            name='gols',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.Gol'),
        ),
        migrations.AddField(
            model_name='palpites',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]