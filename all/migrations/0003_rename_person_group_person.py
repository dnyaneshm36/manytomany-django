# Generated by Django 4.0.1 on 2022-01-31 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0002_rename_members_group_person_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='person',
            new_name='Person',
        ),
    ]
