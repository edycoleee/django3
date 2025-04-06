#customer/urls.py
from django.urls import path
from .views import test1_customer,test2_customer

urlpatterns = [
    path('test1', test1_customer, name='rev_test1_customer'),  # Mengembalikan respons sederhana “Hello Django”.
    path('test2', test2_customer, name='rev_test2_customer'),  # Mengirim JSON dan mengembalikan kembali data yang sama
]