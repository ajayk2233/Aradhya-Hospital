# Generated by Django 3.0 on 2020-03-01 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AradhyaGallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='g_desc',
        ),
    ]