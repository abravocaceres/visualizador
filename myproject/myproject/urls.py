from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('display_time.urls')),
    path('random_word/', include ('random_word.urls'))
]
