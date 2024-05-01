# Generated by Django 5.0.4 on 2024-04-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active_link',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
