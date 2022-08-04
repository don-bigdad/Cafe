from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True,max_length=40,db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("position")


class Event(models.Model):
    name = models.CharField(unique=True,max_length=100,db_index=True)
    description = models.CharField(unique=True,max_length=300)
    event_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("name")


class Dish(models.Model):
    name = models.CharField(unique=True,max_length=30,db_index=True)
    price = models.PositiveIntegerField()
    ingredient = models.CharField(unique=True,max_length=300)
    position = models.SmallIntegerField(unique=True)
    in_category = Category.name

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position')

class Picture(models.Model):
    path = models.ImageField()
    position = models.SmallIntegerField(unique=True,db_index=True)

