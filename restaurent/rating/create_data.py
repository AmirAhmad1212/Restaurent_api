from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from rating.models import Restaurent, Rating, Sales
import random


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        #get or create a user
        user = User.objects.get_or_create(username='amir')
        if not username.exists():
            user = User.objects.create_superuser(username = 'amir',password = 'amir' )
        else:
            user = user.first()

        restaurents = [
            {'name' : 'KFC', 'letitude': '21.0', 'longitude':'32.5', 'restaurent_type':'Restaurent.ChoiceType.KOREAN','date_opened':timezone.now() - timezone.timedelta(days=12)},
            {'name' : 'SHANGAI', 'letitude': '21.0', 'longitude':'32.5', 'restaurent_type':'Restaurent.ChoiceType.KOREAN','date_opened':timezone.now() - timezone.timedelta(days=45)},
            {'name' : 'SHK', 'letitude': '-23.5', 'longitude':'-24.32', 'restaurent_type':'Restaurent.ChoiceType.INDIAN','date_opened':timezone.now() - timezone.timedelta(days=64)},
            {'name' : 'SWATI', 'letitude': '-23.5', 'longitude':'-24.32', 'restaurent_type':'Restaurent.ChoiceType.INDIAN','date_opened':timezone.now() - timezone.timedelta(days=2)},
            {'name' : 'PIZZIRIA', 'letitude': '23.4', 'longitude':'17.2', 'restaurent_type':'Restaurent.ChoiceType.PAKISTANI','date_opened':timezone.now() - timezone.timedelta(days=876)},
            {'name' : 'PATISA', 'letitude': '43.4', 'longitude':'76.9', 'restaurent_type':'Restaurent.ChoiceType.ITALIAN','date_opened':timezone.now() - timezone.timedelta(days=2345)},
            {'name' : 'PAKORA', 'letitude': '43.4', 'longitude':'76.9', 'restaurent_type':'Restaurent.ChoiceType.ITALIAN','date_opened':timezone.now() - timezone.timedelta(days=322)},
            {'name' : 'SHAI WALA', 'letitude': '7.8', 'longitude':'16.8', 'restaurent_type':'Restaurent.ChoiceType.JAPANESE','date_opened':timezone.now() - timezone.timedelta(days=263)},
            {'name' : 'SAMOSA', 'letitude': '7.8', 'longitude':'16.8', 'restaurent_type':'Restaurent.ChoiceType.JAPANESE','date_opened':timezone.now() - timezone.timedelta(days=23)},
            {'name' : 'BURGER', 'letitude': '26.3', 'longitude':'91.5', 'restaurent_type':'Restaurent.ChoiceType.INDIAN','date_opened':timezone.now() - timezone.timedelta(days=98)},
            {'name' : 'SANDWISH', 'letitude': '56.9', 'longitude':'23.4', 'restaurent_type':'Restaurent.ChoiceType.PAKISTANI','date_opened':timezone.now() - timezone.timedelta(days=6554)},
            {'name' : 'ROST', 'letitude': '56.9', 'longitude':'23.4', 'restaurent_type':'Restaurent.ChoiceType.PAKISTANI','date_opened':timezone.now() - timezone.timedelta(days=243)},
        ]


        Restaurent.objects.all().delete()
        for restaurent in restaurents:
            Restaurent.objects.create(**restaurent)

        restaurent = Restaurent.objects.all()

        for _ in range(40):
            Rating.objects.create(
                user=user,
                restaurent=random.choice(restaurent),
                rating=random.choice(Rating.RatingChoice)  
            )        

        for _ in range(136):
            Sales.objects.create(
                restaurent = random.choice(restaurent),
                income = random.uniform(5000,50000),
                date_time = timezone.now() - timezone.timedelta(days=random.randint(20,100))
            )

