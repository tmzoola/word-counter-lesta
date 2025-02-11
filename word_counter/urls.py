from django.urls import path
from .views import TFIDFView

urlpatterns = [
    path("", TFIDFView.as_view(), name="tfidf_view"),
]
