from django.db import models
from datetime import date, datetime




class User(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print('Засейвил')

    def __str__(self):
        return self.email

class Client(models.Model):
    name = models.CharField(max_length=20)
    card_number = models.IntegerField(16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name
class Worker(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    extra_price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    start_price = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredient, related_name="foods", through="Order")
    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(ingredient.name for ingredient in self.ingredients.all()),

        )

class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(null=True)

    def __str__(self):
        return f'Клиент: {self.client}, обслуживает: {self.worker}, еда и ингредиенты:{self.food}, ' \
               f'время заказа:{self.order_date_time}'



