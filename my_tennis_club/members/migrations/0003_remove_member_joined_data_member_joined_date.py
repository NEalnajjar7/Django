# Generated by Django 5.2.1 on 2025-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_data_member_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='joined_data',
        ),
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
    ]
