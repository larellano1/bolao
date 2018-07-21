# Generated by Django 2.0.7 on 2018-07-21 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0011_time_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolao',
            name='administrador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bolao_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bolao',
            name='encerrado',
            field=models.BooleanField(default=False),
        ),
    ]
