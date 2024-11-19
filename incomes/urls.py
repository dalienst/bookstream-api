from django.urls import path

from incomes.views import IncomeListCreateView, IncomeDetailView

urlpatterns = [
    path("", IncomeListCreateView.as_view(), name="income_list"),
    path("<str:slug>/", IncomeDetailView.as_view(), name="income_detail"),
]
