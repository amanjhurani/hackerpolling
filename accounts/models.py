from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


EXPERT = (
    ('Data Structures', 'Data Structures'),
    ('C++', 'C++'),
    ('Algorithms', 'Algorithms'),
    ('Java', 'Java'),
    ('Python', 'Python'),
)


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique =True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS
    challenges_solved = models.IntegerField(default=0)
    rating = models.IntegerField(range(1,6),default=1)
    expertise = models.CharField('Gender',max_length=40,choices=EXPERT)
    votes = models.IntegerField(default=0)
    vote_given = models.BooleanField(default=False)
    vote_given_to = models.CharField(max_length=100)



    