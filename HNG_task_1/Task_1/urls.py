from django.urls import re_path # type: ignore
from .views import ClassifyNumberView

urlpatterns = [
            re_path(r'^api/classify-number/?$', ClassifyNumberView.as_view(), name='classify_number'),

            ]
