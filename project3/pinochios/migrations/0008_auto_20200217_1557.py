# Generated by Django 3.0.3 on 2020-02-17 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0007_auto_20200217_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitemoption',
            name='price',
        ),
        migrations.RemoveField(
            model_name='menuoptionaddon',
            name='price',
        ),
    ]
