# Generated by Django 3.0.3 on 2020-02-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0002_auto_20200211_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_description',
            field=models.CharField(default='We have a variety of delicious pizza. We have sicilian pizza and regular pizza.Choose your favorite topings for your pizza', max_length=255),
            preserve_default=False,
        ),
    ]