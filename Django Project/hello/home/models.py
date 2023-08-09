from django.db import models
#Enter this command in terminal
# python manage.py makemigrations -> makemigrations(create changes and store in file)
# python manage.py migrate        -> migrate(apply the pending chanfes created by makemigrations )

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    

    def __str__(self):
        return self.name
    
