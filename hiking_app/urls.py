from django.urls import path, include 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('hike.urls')),
    path('', include('form_app.urls'))
]
