# Generated by Django 4.1 on 2022-08-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_application_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_model',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]