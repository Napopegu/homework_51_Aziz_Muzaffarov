from django.urls import path
from webapp.views import index_view,cat_index

urlpatterns = [
    path('', index_view),
    path('cats_stats/', cat_index),
]