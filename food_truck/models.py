from django.db import models


#This is a table named FoodTruck in database.

class FoodTruck(models.Model):
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255)
    food_items = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.applicant
