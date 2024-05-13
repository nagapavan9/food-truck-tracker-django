from django.apps import AppConfig



class StartupServiceConfig(AppConfig):
    print('Started --------------->')
    name = 'food_truck'
    default_auto_field = 'django.db.models.BigAutoField'


        # Import and run your startup script here
    def ready(self):
        print('Here!')
        # # Import and run your startup script here
        from .startup_service import FoodTruckDataLoad
        FoodTruckDataLoad().handle()




    