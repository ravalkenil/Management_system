# Generated by Django 4.1 on 2022-08-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_custom',
            name='Role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]