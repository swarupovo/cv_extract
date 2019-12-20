from django.urls import path

from api import views
from api.views import Upload

urlpatterns = [
    path("upload/", Upload.as_view(), name="upload_cv"),

    ]