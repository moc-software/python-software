# Generated by Django 4.1.3 on 2023-03-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0018_service_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='centerproduct',
            name='purchase_price',
            field=models.IntegerField(default=300),
        ),
    ]
