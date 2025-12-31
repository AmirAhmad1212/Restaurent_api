from django.contrib.auth.models import User
from rating.models import Restaurent, Rating, Sales, Staff, StaffSalary
from django.utils import timezone
from pprint import pprint
from django.db import connection
from django.core.management.base import BaseCommand
import random

def run():




    pass







































    #through through_defaults we add additional felds vilauses salary
    # staff = Staff.objects.first()
    # rest = Restaurent.objects.get(name='SHK')
    # staff.restaurents.add(rest,through_defaults = {'salary':23333})




#for creating a staff
    # staff, created = Staff.objects.get_or_create(
    #     name='jhon wick'
    # )


#FOR ADDINF A STAFF TO A RESTAURENT MAKE SURE TO ADDIG RELATED NAME TO M2M KEY AND USE IT HERE
# rest = Restaurent.objects.get(name = 'SAMOSA')
# rest.staff.add(staff)


# for associating a restaurent to a staff use .add function to do it and ensure that use created while useing get or create or itll through error
    # staff.restaurents.add(Restaurent.objects.get(name='ROST'))
    # print(staff)



#script for creating some data into tables
# restaurents = [
#     {'name' : 'KFC', 'letitude': '21.0', 'longitude':'32.5', 'restaurent_type':Restaurent.ChoiceType.KOREAN,'date_opened':timezone.now() - timezone.timedelta(days=12)},
#     {'name' : 'SHANGAI', 'letitude': '21.0', 'longitude':'32.5', 'restaurent_type':Restaurent.ChoiceType.KOREAN,'date_opened':timezone.now() - timezone.timedelta(days=45)},
#     {'name' : 'SHK', 'letitude': '-23.5', 'longitude':'-24.32', 'restaurent_type':Restaurent.ChoiceType.INDIAN,'date_opened':timezone.now() - timezone.timedelta(days=64)},
#     {'name' : 'SWATI', 'letitude': '-23.5', 'longitude':'-24.32', 'restaurent_type':Restaurent.ChoiceType.INDIAN,'date_opened':timezone.now() - timezone.timedelta(days=2)},
#     {'name' : 'PIZZIRIA', 'letitude': '23.4', 'longitude':'17.2', 'restaurent_type':Restaurent.ChoiceType.PAKISTANI,'date_opened':timezone.now() - timezone.timedelta(days=876)},
#     {'name' : 'PATISA', 'letitude': '43.4', 'longitude':'76.9', 'restaurent_type':Restaurent.ChoiceType.ITALIAN,'date_opened':timezone.now() - timezone.timedelta(days=2345)},
#     {'name' : 'PAKORA', 'letitude': '43.4', 'longitude':'76.9', 'restaurent_type':Restaurent.ChoiceType.ITALIAN,'date_opened':timezone.now() - timezone.timedelta(days=322)},
#     {'name' : 'SHAI WALA', 'letitude': '7.8', 'longitude':'16.8', 'restaurent_type':Restaurent.ChoiceType.JAPANESE,'date_opened':timezone.now() - timezone.timedelta(days=263)},
#     {'name' : 'SAMOSA', 'letitude': '7.8', 'longitude':'16.8', 'restaurent_type':Restaurent.ChoiceType.JAPANESE,'date_opened':timezone.now() - timezone.timedelta(days=23)},
#     {'name' : 'BURGER', 'letitude': '26.3', 'longitude':'91.5', 'restaurent_type':Restaurent.ChoiceType.INDIAN,'date_opened':timezone.now() - timezone.timedelta(days=98)},
#     {'name' : 'SANDWISH', 'letitude': '56.9', 'longitude':'23.4', 'restaurent_type':Restaurent.ChoiceType.PAKISTANI,'date_opened':timezone.now() - timezone.timedelta(days=6554)},
#     {'name' : 'ROST', 'letitude': '56.9', 'longitude':'23.4', 'restaurent_type':Restaurent.ChoiceType.PAKISTANI,'date_opened':timezone.now() - timezone.timedelta(days=243)},
# ]

# user = User.objects.first()
# Restaurent.objects.all().delete()
# for restaurent in restaurents:
#     Restaurent.objects.create(**restaurent)

# restaurent = Restaurent.objects.all()
# Rating.objects.all().delete()
# for _ in range(40):
#     Rating.objects.create(
#         user=user,
#         restaurent=random.choice(restaurent),
#         rating=random.randint(1,5)  
#     )        
# Sales.objects.all().delete()
# for _ in range(136):
#     Sales.objects.create(
#         restaurent = random.choice(restaurent),
#         income = random.uniform(5000,50000),
#         date_time = timezone.now() - timezone.timedelta(days=random.randint(20,100)))



# for deleting records REMEMBER the .UPDATE and .DELETE method does not work on indivisual fileds but you can use .FILTER to filter the records to a single field you desire
# rest = Restaurent.objects.filter(name__startswith='LFC')
# rest.delete()



#.update method
# rest = Restaurent.objects.filter(name__startswith = 'TKR')
# rest.update(
#     date_opened = '2024-12-12')


#for updating a single field
#restaurent = Restaurent.objects.get(name='KFC')
# user = User.objects.first()


# restaurent.name = 'LFC'
# restaurent.save(update_fields=['name'])




#the get or create function retreive data of create ift if it doesnt exist
# restaurent, created = Restaurent.objects.get_or_create(
#     name="Shangla",
#     date_opened = '2025-12-29',
#     letitude=232.4235,
#     longitude=343.32,
#     restaurent_type='KR',
# )

# if created:     #in actual if created means if created == True: since create returns bool
#     print("This object is created for and stored into data base")
# print(restaurent)



#for storing data into db
# restaurent = Restaurent.objects.get(name="TKR")
# Sales.objects.create(
#     restaurent = restaurent,
#     income = 9000,
#     date_time = timezone.now(),
# ) 


#accessng data of forignkey relation
# rating = Rating.objects.last()
# print(rating.restaurent)

#through below code we save data of those models which has forignkey
# restaurent = Restaurent.objects.last()
# user = User.objects.first()
# Rating.objects.create(restaurent=restaurent, user=user, rating=Rating.RatingChoice.ONE)



#the following program is used to to save data into DB we used .Create method and it take keyword arguments
# restaurent = Restaurent.objects.create(
#     name= "PizzaHut",
#     date_opened = timezone.now(),
#     letitude = 234343.4,
#     longitude = 2323.234,
#     restaurent_type = Restaurent.ChoiceType.JAPANESE
# )



#the below program is used to Query Pullout Data from DB we use .object Manager for it
#restaurents = Restaurent.objects.all()[:1]
# print(restaurents)


#the below Programm is used to define data for each instance in the model 
#and then save it into DB through .save() function
# restaurent = Restaurent()
# restaurent.name = 'KFC'
# restaurent.date_opened = timezone.now()
# restaurent.letitude = 343554.543
# restaurent.longitude = 435554.543
# restaurent.restaurent_type = Restaurent.ChoiceType.KOREAN
# restaurent.save()