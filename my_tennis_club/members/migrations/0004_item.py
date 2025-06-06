# Generated by Django 5.2.1 on 2025-06-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_member_joined_data_member_joined_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
