# Generated by Django 4.1.3 on 2023-02-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0004_alter_payslip_slip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='slip',
            field=models.FileField(blank=True, null=True, upload_to='media/updateimg'),
        ),
    ]
