# Generated by Django 5.0.6 on 2024-07-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('suscriber', 'Suscriber'), ('author', 'Author')], default='suscriber', max_length=10),
        ),
    ]
