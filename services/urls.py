from django.urls import path
from .views import *




urlpatterns = [
    path('received-error/', CreateServiceFrom.as_view(), name='new_error'),
    path('received-error-list/', ReturnErrorsView.as_view(), name='error_list'),
    path('received-error/edit/&sr=<int:pk>/', EditServiceForm.as_view(), name='edit_service_form'),
    path('error-checking/&value=<int:pk>/', FindingResultView.as_view(), name="finding"),
    path('get_product_info/<str:product_code>/', get_product_info, name='get_product_info'),

]
