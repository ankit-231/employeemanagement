# Generated by Django 4.2.1 on 2023-05-16 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainuser", "0007_designation_designationhead_role_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="role",
            old_name="role_user",
            new_name="user_role",
        ),
    ]
