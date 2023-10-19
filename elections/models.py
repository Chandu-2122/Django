from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    
    def __str__(self):
        return self.username

# lets create a model to store live facial images of the user 
class LiveFacialImage(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='live_facial_images')
    Captured_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return
    
#lets create a model for elections
class Election(models.Model):
    Title = models.CharField(max_length=100)
    Start_time = models.DateTimeField()
    End_time = models.DateTimeField()
    Is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
# let's create a model for candidates
class Candidate(models.Model):
    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    Description = models.TextField()
    
    def __str__(self):
        return self.Name
    
#let's create a model to mark if the user has voted or not
class VotedOrNot(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name='has_voted')
    Has_voted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
#let's create a model to store the votes
class Vote(models.Model):
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    Election = models.ForeignKey(Election, on_delete=models.CASCADE)
    Vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f'Votes for {self.candidate.name} in {self.election.title}'

