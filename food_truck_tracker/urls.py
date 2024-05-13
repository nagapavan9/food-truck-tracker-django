from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='api/foodtrucks/')),
    path('admin/', admin.site.urls),
    path('api/', include('food_truck.urls')),  # Include the trucks app URLs under the /api/ path
]

