# Generated by Django 5.0 on 2023-12-12 03:52

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikidatamodel',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]