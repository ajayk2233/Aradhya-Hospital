# Generated by Django 3.0 on 2020-02-27 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_data', '0011_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='Name',
            new_name='name',
        ),
    ]