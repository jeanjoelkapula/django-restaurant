# Generated by Django 3.0.3 on 2020-02-11 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='order_item_total',
        ),
    ]