# Generated by Django 3.0.3 on 2020-02-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0003_menuitem_menu_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menu_item_image',
            field=models.ImageField(null=True, upload_to='item_images'),
        ),
    ]
