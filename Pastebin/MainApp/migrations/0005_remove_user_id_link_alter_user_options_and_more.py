# Generated by Django 5.0.4 on 2024-05-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_link_remove_user_active_link_remove_user_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_link',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(help_text='Не более 15 символов', max_length=15, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(help_text='Не более 15 символов', max_length=15, verbose_name='Фамилия'),
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
