# Generated by Django 2.0.7 on 2018-07-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_regulamento_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regulamento',
            name='regras',
        ),
        migrations.AddField(
            model_name='regulamento',
            name='regras',
            field=models.ManyToManyField(to='show.Regra'),
        ),
    ]
