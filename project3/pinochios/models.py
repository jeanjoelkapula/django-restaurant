from django.db import models
import datetime

# Create your models here.
class MenuItemAddOn(models.Model):
    add_on_name = models.CharField(max_length=255)
    small_price = models.DecimalField(max_digits=8, decimal_places=2, default = 0)
    large_price = models.DecimalField(max_digits=8, decimal_places=2, default = 0)

    def __str__(self):
        return self.add_on_name

class MenuItemOption(models.Model):
    menu_option_name = models.CharField(max_length=255)
    small_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    large_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.menu_option_name

class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=255)
    menu_description = models.CharField(max_length=255)
    menu_item_image = models.ImageField(upload_to='item_images', null=True)
    menu_options = models.ManyToManyField(MenuItemOption)
    add_on_options = models.ManyToManyField(MenuItemAddOn, blank=True)

    def __str__(self):
        return self.menu_item_name

class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete = models.DO_NOTHING)
    menu_item_option = models.ForeignKey(MenuItemOption, on_delete = models.DO_NOTHING)
    add_on_options = models.ManyToManyField(MenuItemAddOn)
    quantity = models.IntegerField()
    order_item_total  = models.FloatField()
    
class Order(models.Model):
    order_date = models.DateField(default=datetime.date.today)
    order_status = models.CharField(max_length=50)
    order_amount = models.FloatField(null=True)
    order_items = models.ForeignKey(OrderItem, on_delete = models.DO_NOTHING, null=False)



