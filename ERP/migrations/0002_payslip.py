# Generated by Django 4.1.3 on 2023-02-12 18:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('ERP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaySlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('slip', models.FileField(blank=True, null=True, upload_to='')),
                ('txnid', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.employee')),
            ],
        ),
    ]
