from django.urls import path, include

app_name = 'api_module'
urlpatterns = [
    path('doll/', include('doll.urls')),
]
