# Generated by Django 4.2.4 on 2023-10-06 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_student_address_alter_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='Active', max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=14),
        ),
    ]
