from django.db import models
import datetime
import os

class Category(models.Model):
    name = models.CharField(unique=True,max_length=40,db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("position",)
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

class Event(models.Model):

    def get_date_name(self, filename: str) -> str:
        file_ext = "." + filename.strip().split(".")[-1]
        date = "Party_picture"+str(datetime.datetime.now()).split(".")[0].replace(" ", "-") + file_ext
        return os.path.join("Events/", date)

    slug = models.SlugField(max_length=100,db_index=True)
    name = models.CharField(unique=True,max_length=100,db_index=True)
    description = models.TextField(unique=True,max_length=2000)
    event_price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to=get_date_name)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ("event_price",)
        verbose_name = "События"
        verbose_name_plural = "События"

class Dish(models.Model):

    def get_date_name(self,filename:str) -> str:
        file_ext="."+filename.strip().split(".")[-1]
        date="Typical_dish"+str(datetime.datetime.now()).split(".")[0].replace(" ","-")+file_ext
        return os.path.join("dishes/",date)

    slug = models.SlugField(max_length=100,db_index=True)
    name = models.CharField(unique=True,max_length=30,db_index=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField(max_length=100,blank=True)
    ingredient = models.CharField(max_length=300,unique=False)
    position = models.SmallIntegerField()
    in_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_date_name)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        index_together = (('id','slug'),)
        verbose_name = "Блюда"
        verbose_name_plural = "Блюда"

class AboutUs(models.Model):
    pozition = models.PositiveIntegerField(unique=True,blank=False)
    title = models.CharField(max_length=100)
    exactly_about_us = models.TextField(max_length = 2000)

    class Meta:
        verbose_name = "Про нас"
        verbose_name_plural = "Про нас"

    def __str__(self):
        return self.title


class Specials(models.Model):

    def get_date_name(self,filename:str) -> str:
        file_ext="."+filename.strip().split(".")[-1]
        date="Special"+str(datetime.datetime.now()).split(".")[0].replace(" ","-")+file_ext
        return os.path.join("Specials/",date)
    title = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100, db_index=True)
    name = models.CharField(unique=True, max_length=30, db_index=True)
    about = models.TextField(max_length=2000)
    picture = models.ImageField(upload_to=get_date_name)
    pozition = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Cпециальные предложения"
        verbose_name_plural = "Cпециальные предложения"

    def __str__(self):
        return self.name