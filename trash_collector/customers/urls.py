from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('change_day/', views.change_day, name="change_day"),
    path('delete/<int:customers_id>', views.delete, name='delete'),
    path('<int:customers_id>', views.detail, name="detail"),
    path('edit/<int:customers_id>', views.edit, name='edit'),
    path('customers/<customer>', views.CustomersListView.as_view(), name="customers")
]
