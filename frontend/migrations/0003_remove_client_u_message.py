# Generated by Django 5.0.6 on 2024-06-09 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_client_u_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='u_message',
        ),
    ]
