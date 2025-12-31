from django.db import models
from django.contrib.auth.models import User
#Restaurent
#user
#rating
#sales

class Restaurent(models.Model):
    class ChoiceType(models.TextChoices):
        PAKISTANI = 'PK', 'Pakistani'
        ITALIAN = 'IT', 'Italian'
        INDIAN = 'IN', 'Indian'
        JAPANESE = 'JP', 'Japanese'
        KOREAN = 'KR', 'Korean'

    name = models.CharField("Website Name",max_length=200)
    website = models.URLField("Website Url", default='')
    date_opened = models.DateField(auto_now_add=True)
    letitude = models.FloatField()
    longitude = models.FloatField()
    restaurent_type = models.CharField(max_length=2, choices=ChoiceType.choices,default=ChoiceType.PAKISTANI)

    def __str__(self):
        return self.name


class Rating(models.Model):
    class RatingChoice(models.TextChoices):
        ONE = '1'
        TWO = '2'
        TWO_FIVE = '2.5'
        THREE = '3'
        FOUR = '4'
        FIVE = '5'
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='ratings')
    restaurent = models.ForeignKey(Restaurent, on_delete=models.CASCADE, related_name='rating')
    rating = models.CharField(max_length=3, choices=RatingChoice.choices,default=RatingChoice.TWO_FIVE )

    def __str__(self):
        return f"Rating of {self.restaurent} --> {self.rating}"


class Staff(models.Model):
    name = models.CharField(max_length=200)
    restaurents = models.ManyToManyField(Restaurent, related_name='staff', through='StaffSalary')

    def __str__(self):
        return self.name


class StaffSalary(models.Model):
    staffname = models.ForeignKey(Staff,on_delete=models.CASCADE)
    restaurents = models.ForeignKey(Restaurent,on_delete=models.CASCADE)
    salary = models.IntegerField()


class Sales(models.Model):
    restaurent = models.ForeignKey(Restaurent,on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"sales of {self.restaurent} --> {self.income}"


