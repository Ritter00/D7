# Generated by Django 3.2.6 on 2021-09-08 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_comment_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]