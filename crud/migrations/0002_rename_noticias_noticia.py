# Generated by Django 4.1 on 2022-08-31 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='noticias',
            new_name='noticia',
        ),
    ]
