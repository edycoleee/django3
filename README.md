## DJANGO API 2 RABEL YANG TIDAK BERHUBUNGAN

tabel pelanggan: tbl_customer (id, nameCustomer, email, nohp).
tabel produk: tbl_product (id, nameProduct, spesifikasi, price)

## 1. GITHUB

```js
echo "# django3" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/edycoleee/django3.git
git push -u origin main
```

## 2. BUAT VENV
```py
#buat folder dj-api2 >> buka dengan vscode
#create venv
python3 -m venv .venv
#activate venv
source .venv/bin/activate
#check python venv
which python
#deactivate venv
#deactivate
```

```py
#melanjutkan 
python3 -m pip install --upgrade pip
python3 -m pip --version
```

```py
pip install django djangorestframework

django-admin --version

django-admin startproject restapi .

python manage.py runserver

#Starting development server at http://127.0.0.1:8000/

```

## 3 API 1 >> Customer API Specification

tabel customer: tbl_customer (id, nameCustomer, email, nohp).

BASE URL : `http://127.0.0.1:8000/api`

### 1. Create Customer
### 2. Get All Customer
### Endpoint
**GET** `/cust`

### Response (200 OK)
```json
{
  "message": "Data Customer Semua",
  "total": 1,
  "data": [
    {
      "id": 1,
      "nameCustomer": "Edy Cole",
      "email": "edy@gmail.com",
      "nohp": "08122850264"
    }
  ],
  "url": "/cust"
}
```

### 3. Get Customer by ID
### Endpoint
**GET** `/cust/{id}`

### Response (200 OK)
```json
{
  "message": "Data Customer ditemukan",
  "data": {
    "id": 1,
      "nameCustomer": "Edy Cole",
      "email": "edy@gmail.com",
      "nohp": "08122850264"
  },
  "url": "/cust/1"
}
```

### Response (404 Not Found)
```json
{
  "message": "Data Customer tidak ditemukan"
}
```

### 5. Delete Customer
### Endpoint
**DELETE** `/cust/{id}`

### Response (200 OK)
```json
{
  "message": "Data Customer berhasil dihapus",
  "data": {
    "id": 1
  },
  "url": "/cust/1"
}
```

### Response (404 Not Found)
```json
{
  "message": "Data Customer tidak ditemukan"
}
```
=============================

## 4. DATABASE ORM 

>> jika menggunakan ORM pakailah langkah dibawah

Secara default, Django akan membuat nama tabel di database berdasarkan nama aplikasi dan nama model dengan format:
`<nama_aplikasi>_<nama_model>`

```py
#/siswa/model.py
from django.db import models

class Customer(models.Model):
    nameCustomer = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    nohp = models.CharField(max_length=15)

    class Meta:
        db_table = "tbl_customer"  # Menentukan nama tabel di SQLite

```

```py
python3 manage.py makemigrations
python3 manage.py migrate
```

CEK DATA

```py
python manage.py dbshell

.tables
```

## 5. DATABASE NO ORM

>> jika tidak menggunakan ORM pakailah langkah dibawah

```py
python3 manage.py dbshell
```

```sql
-- create tabel
CREATE TABLE tbl_customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nameCustomer TEXT NOT NULL,
    email TEXT NOT NULL,
    nohp TEXT NOT NULL
);


-- mengetahui semua tabel yang ada
.tables 

-- melihat struktur tabel
PRAGMA table_info(tbl_customer); 
```

## 6. URL

### 1. /restapi/settings.py 

>> INSTALLED_APPS	>> Mendaftarkan aplikasi agar Django bisa mengelola model, admin, dsb.

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customer' # Tambahkan aplikasi customer di sini
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware', # sementara utk mempermudah pengetesan
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


```

### 2. /restapi/urls.py 

>> include('customer.urls')	>> Memberi tahu Django untuk mencari URL patterns di customer/urls.py.

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customer.urls'))
]
```
### 3. /customer/urls.py

Sebelum membuat api customer mari membuat simulasi dulu untuk latihan

#### 1. API - SEDERHANA

1. GET /test1

Deskripsi: Mengembalikan respons sederhana “Hello Django”.

Endpoint: /test1

Method: GET

✅ Contoh Response

Status: 200 OK

```json
{
  "response": "Hello Django"
}
```

2. POST /test2

Deskripsi: Mengirim JSON dan mengembalikan kembali data yang sama.

Endpoint: /test2

Method: POST

Request Headers:

Content-Type: application/json

Request Body:

```json
{
  "key1": "Value1",
  "key2": "Value2"
}
```
✅ Contoh Response

Status: 200 OK

```json
{
  "response": {
    "key1": "Value1",
    "key2": "Value2"
  }
}
```

#### 3. URLS - SEDERHANA
```py
#customer/urls.py
from django.urls import path
from .views import test1_customer,test2_customer

urlpatterns = [
    path('test1', test1_customer, name='rev_test1_customer'),  # Mengembalikan respons sederhana “Hello Django”.
    path('test2', test2_customer, name='rev_test2_customer'),  # Mengirim JSON dan mengembalikan kembali data yang sama
]
```

#### 4. VIEWS - SEDERHANA
```py
#customer/views.py
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from rest_framework.parsers import JSONParser

@csrf_exempt
def test1_customer(request):
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        return JsonResponse({"response" : "Hello Django"})

@csrf_exempt
def test2_customer(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        return JsonResponse({"response" : data})
```

#### 5. UNIT TEST - SEDERHANA

```py
# customer/tests.py
from django.test import TestCase
from django.urls import reverse
import json

class CustomerAPITestCase(TestCase):
    
    def test_test1_customer(self):
        """Test GET /test1 returns Hello Django"""
        #Mengambil URL berdasarkan nama route (rev_test1_customer) yang sudah didefinisikan di urls.py.
        url = reverse('rev_test1_customer')
        #Simulasi request GET ke URL tersebut.
        response = self.client.get(url)
        #Memastikan response memiliki status HTTP 200 (OK).
        self.assertEqual(response.status_code, 200)
        #Key "response" ada dalam JSON.
        response_data = response.json()
        self.assertIn('response', response_data)
        #Value dari "response" adalah string "Hello Django".
        self.assertEqual(response_data["response"], "Hello Django")

    def test_test2_customer(self):
        """Test POST /test2 returns the same data"""
        url = reverse('rev_test2_customer')
        data = {"key1": "Value1", "key2": "Value2"}
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        
        response_data = response.json()
        self.assertIn('response', response_data)
        self.assertEqual(response_data["response"], data)
```

```py
#menjalankan test sederhana
python manage.py test customer
#menjalankan test detail
python manage.py test customer --verbosity=2
```

#### 6. REQUEST REST - SEDERHANA
```json
### 1. GET TEST
 GET http://localhost:8000/api/test1 HTTP/1.1

### 2. POST TEST 
POST http://localhost:8000/api/test2
content-type: application/json

{
"key1": "Value1", "key2": "Value2"
}
```


### 7. VIEWS

## 8. UNIT TEST

## 9. RESUEST REST

## 10. API 1 >> Customer API Specification

tabel produk: tbl_product (id, nameProduct, spesifikasi, price)

