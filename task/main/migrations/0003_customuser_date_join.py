# Generated by Django 4.2.6 on 2023-10-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_join',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
