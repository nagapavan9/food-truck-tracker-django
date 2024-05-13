

# class FoodTruckDataLoad():
#     def __init__(self) -> None:
#         print("startup service ran successfully --------------------->")
#         pass
import csv
from django.core.management.base import BaseCommand
from food_truck.models import FoodTruck

# class FoodTruckDataLoad(BaseCommand):
#     # help = 'Load a list of food trucks from a CSV file'

#     def handle(self, *args, **options):
#         with open('food_truck/data/food-truck-data.csv', newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 FoodTruck.objects.create(
#                     applicant=row['Applicant'],
#                     facility_type=row['FacilityType'],
#                     address=row['Address'],
#                     food_items=row['FoodItems'],
#                     latitude=float(row['Latitude']),
#                     longitude=float(row['Longitude']),
#                     status=row['Status']
#                 )
class FoodTruckDataLoad(BaseCommand):
    # help = 'Load a list of food trucks from a CSV file only if the database is empty'

    def handle(self, *args, **options):
        # Check if any records already exist in the database
        if FoodTruck.objects.exists():
            self.stdout.write(self.style.SUCCESS('Database already populated. No new data loaded.'))
            return
        
        with open('food_truck/data/food-truck-data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                FoodTruck.objects.create(
                    applicant=row['Applicant'],
                    facility_type=row['FacilityType'],
                    address=row['Address'],
                    food_items=row['FoodItems'],
                    latitude=float(row['Latitude']),
                    longitude=float(row['Longitude']),
                    status=row['Status']
                )
            self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database.'))