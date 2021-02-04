# Generated by Django 3.0.3 on 2020-02-17 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinochios', '0009_remove_menuitemoption_meal_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuAddOnPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('add_on', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pinochios.MenuOptionAddOn')),
                ('meal_size', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pinochios.MealSize')),
            ],
        ),
        migrations.CreateModel(
            name='MenuOptionPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('itemOption', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pinochios.MenuItemOption')),
                ('meal_size', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pinochios.MealSize')),
            ],
        ),
        migrations.RemoveField(
            model_name='optionprice',
            name='itemOption',
        ),
        migrations.RemoveField(
            model_name='optionprice',
            name='meal_size',
        ),
        migrations.DeleteModel(
            name='AddOnPrice',
        ),
        migrations.DeleteModel(
            name='OptionPrice',
        ),
    ]
