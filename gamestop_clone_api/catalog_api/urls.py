from django.urls import path
from . import views

urlpatterns = [
    path('api/listing', views.ListingSet.as_view(), name='listing_set'),
    path('api/listing/<int:pk>', views.ListingDetail.as_view(), name='listing_detail')
]