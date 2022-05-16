# project/contact/views.py

from django.shortcuts import render


""" 一覧画面"""
def index(request):
    return render(request, 'contact/index.html')


""" お問い合わせフォーム画面"""
def contact_form(request):
    return render(request, 'contact/contact_form.html')


""" 送信完了画面"""
def complete(request):
    return render(request, 'contact/complete.html')