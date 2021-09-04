from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('delete/<int:employees_id>', views.delete, name='delete'),
    path('<int:employees_id>', views.detail, name="detail"),
    path('edit/<int:employees_id>', views.edit, name='edit'),
    path('employees/<employee>', views.EmployeesListView.as_view(), name="employees")

]