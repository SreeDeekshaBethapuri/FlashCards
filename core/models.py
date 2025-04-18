from django.db import models

# Create your models here.

#defining the shape of the flashcard. We want the keyword and definition to be a charfield with 100, and 1000 characters at max respectively. 
class Flashcard(models.Model):
    keyword = models.CharField(max_length=100)
    definition = models.CharField(max_length=1000)

    def __str__(self):
        return self.keyword