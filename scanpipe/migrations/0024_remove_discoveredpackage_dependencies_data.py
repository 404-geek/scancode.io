# Generated by Django 4.1 on 2022-08-31 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("scanpipe", "0023_migrate_dependencies"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discoveredpackage",
            name="dependencies_data",
        ),
    ]
