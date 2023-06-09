# Generated by Django 4.2.1 on 2023-05-16 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainuser", "0006_alter_employee_is_deleted"),
    ]

    operations = [
        migrations.CreateModel(
            name="Designation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("description", models.CharField(max_length=250)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="DesignationHead",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="role",
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.AddField(
            model_name="role",
            name="role_user",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
