# Generated by Django 4.0.2 on 2022-10-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_projects_options_remove_projects_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
