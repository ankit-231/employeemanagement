# Generated by Django 4.2.1 on 2023-05-15 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("mainuser", "0003_alter_employee_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="date_joined",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
