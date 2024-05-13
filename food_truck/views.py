from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import F
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework import viewsets
from .models import FoodTruck
from .serializers import FoodTruckSerializer

class FoodTruckViewSet(viewsets.ViewSet):
    serializer_class = FoodTruckSerializer
    def list(self, request):
        latitude = request.query_params.get('latitude', None)
        longitude = request.query_params.get('longitude', None)

        # Define bounds for latitude and longitude
        min_latitude, max_latitude = 37.6395, 37.9298
        min_longitude, max_longitude = 122.2818, 123.1738  # Convert these to negative if West

        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)  # Ensure longitude is negative for West
                user_location = Point(longitude, latitude, srid=4326)

                # Check if the provided coordinates are within the allowed range
                if (min_latitude <= latitude <= max_latitude) and (min_longitude <= longitude <= max_longitude):
                    # trucks = FoodTruck.objects.all()
                    trucks = FoodTruck.objects.all()
                    trucks_within_distance = [
                        truck for truck in trucks
                        if user_location.distance(Point(truck.longitude, truck.latitude, srid=4326)) <= D(m=1000).m
                    ]

                    # Paginate the filtered trucks
                    paginator = Paginator(trucks_within_distance, 10)  # Show 10 trucks per page
                    page = request.query_params.get('page')
                    trucks_page = paginator.get_page(page)

                    return render(request, 'food_truck/food_truck_list.html', {'trucks': trucks_page})
                else:
                    return render(request, 'food_truck/food_truck_list.html', {'error': 'Latitude and/or longitude out of range.'})
            except ValueError:
                return render(request, 'food_truck/food_truck_list.html', {'error': 'Invalid latitude or longitude.'})
        else:
            return render(request, 'food_truck/food_truck_list.html')