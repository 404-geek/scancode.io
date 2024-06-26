# Generated by Django 4.2.6 on 2023-11-30 10:12

from django.db import migrations


def migrate_project_input_sources_data(apps, schema_editor):
    Project = apps.get_model("scanpipe", "Project")
    InputSource = apps.get_model("scanpipe", "InputSource")

    projects = Project.objects.exclude(input_sources={})
    for project in projects:
        for filename, value in project.input_sources.items():
            if value == "uploaded":
                is_uploaded = True
                download_url = ""
            else:
                is_uploaded = False
                download_url = value

            InputSource.objects.create(
                project=project,
                download_url=download_url,
                filename=filename,
                is_uploaded=is_uploaded,
            )


def reverse_migrate_project_input_sources_data(apps, schema_editor):
    Project = apps.get_model("scanpipe", "Project")
    InputSource = apps.get_model("scanpipe", "InputSource")

    projects = Project.objects.filter(inputsources__isnull=False)
    for project in projects:
        project.input_sources = {
            source.filename: "uploaded" if source.is_uploaded else source.download_url
            for source in project.inputsources.all()
        }
        project.save()

    InputSource.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("scanpipe", "0048_inputsource"),
    ]

    operations = [
        migrations.RunPython(
            migrate_project_input_sources_data,
            reverse_code=reverse_migrate_project_input_sources_data,
        ),
    ]
