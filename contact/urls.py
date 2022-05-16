from django.urls import path
from . import views


app_name = 'contact'

urlpatterns = [
        path('', views.index, name='index'),  # 一覧画面
        path('contact_form/', views.contact_form, name='contact_form'),  # フォーム
        path('contact_form/contact/complete/', views.complete, name='complete'),  # 完了画面
]