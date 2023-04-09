from django.contrib import admin
from django.urls import path
from Agriculture import views
from Agriculture.views import new_loan, loan_detail
urlpatterns = [
    path("", views.index, name = "Agriculture"),
    path("login", views.login, name = "Login"),
    path("main", views.main, name = "Main"),
    path("main2", views.main2, name = "Main2"),
    path("main3", views.main3, name = "Main3"),
    path("new_partner", views.new_partner, name = "New_Partner"),
    path("terms_conditions", views.terms_conditions, name = "Terms_Conditions"),
    path("partner_first", views.partner_first, name = "Partner_First"),
    path("dashboard_owner", views.db_owner, name = "Dashboard_Owner"),
    path("dashboard_partner", views.db_partner, name = "Dashboard_Partner"),
    path("partner_seeds", views.partner_seeds, name = "Partner_Seeds"),
    path("partner_crops", views.partner_crops, name = "Partner_Crops"),
    path("dashboard_middleman", views.db_middleman, name = "Dashboard_Middleman"),
    path("middleman_crops", views.middleman_crops, name = "Middleman_crops"),
    path("owner_machinery", views.owner_machinery, name = "Owner_Machinery"),
    path("owner_seeds", views.owner_seeds, name = "Owner_Seeds"),
    path("owner_crops", views.owner_crops, name = "Owner_Crops"),
    path('new_loan/', new_loan, name="new_loan"),
    path('loan/<int:loan_id>/', loan_detail, name="loan_detail")
]
