# Generated by Django 5.0.4 on 2024-04-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не более 15 символов', max_length=15, verbose_name='Введите имя')),
                ('surname', models.CharField(help_text='Не более 15 символов', max_length=15, verbose_name='Введите фамилию')),
            ],
            options={
                'ordering': ['surname', 'name'],
            },
        ),
    ]
