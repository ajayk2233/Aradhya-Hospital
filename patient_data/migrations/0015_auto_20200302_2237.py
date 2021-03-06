# Generated by Django 3.0 on 2020-03-03 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient_data', '0014_contactus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient_data.Doctor'),
        ),
        migrations.AlterField(
            model_name='record',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient_data.Patient'),
        ),
    ]
