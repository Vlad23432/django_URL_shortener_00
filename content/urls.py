from django.urls import path
from . import views


urlpatterns = [
    path('<slug:url>', views.page_view, name='page_detail')
]