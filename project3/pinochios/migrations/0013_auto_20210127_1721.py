# Generated by Django 3.0.3 on 2021-01-27 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0012_auto_20210127_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='add_on_options',
            field=models.ManyToManyField(null=True, to='pinochios.MenuItemAddOn'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='menu_item_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pinochios.MenuItemOption'),
        ),
    ]
