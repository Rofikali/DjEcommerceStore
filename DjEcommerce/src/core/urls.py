from django.urls import path
from core.views import home, detail_view

app_name = 'cores'

urlpatterns = [
    path('', home, name='home'),
    path("detail/<slug:slug>/", detail_view,  name="detail")
]
