# Generated by Django 4.1.3 on 2023-03-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0017_centerproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='products',
            field=models.ManyToManyField(to='ERP.centerproduct'),
        ),
    ]
