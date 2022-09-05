from django.urls import path
from .views import CustomUserCreate, UserDetail

app_name = 'api'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
     path('<int:id>/', UserDetail.as_view(), name='detailuser'),
]
