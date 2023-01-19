from django.db import models


STATE_CHOICE = (
    ("Uttora", "Uttora"),
    ("Gulshan", "Gulshan"),
    ("Dhanmondi", "Dhanmondi"),
)
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)
