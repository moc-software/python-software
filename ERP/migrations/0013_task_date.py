# Generated by Django 4.1.3 on 2023-03-05 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0012_service_date_task_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
