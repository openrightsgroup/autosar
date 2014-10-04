from django.db import models

# Create your models here.

from django import forms

from datetime import date

class NameForm(forms.Form):
  your_name = forms.CharField(label='Your name', max_length=100, initial="your name")
  address = forms.CharField(label='Address', max_length=100, initial="address")
  date = forms.CharField(label='date', max_length=100, initial=date.today() )

  details = [
      forms.BooleanField( label="YOUR PERSONNEL FILE",),
      forms.BooleanField( label="emails between A and B (between 1/6/11 and 1/9/11);",),
      forms.BooleanField( label="your medical records (between 2006 & 2009) held by Dr C at D hospital;",),
      forms.BooleanField( label="CCTV camera situated at (E location) on 23/5/12 between 11am and 5pm;",),
      forms.BooleanField( label="copies of statements (between 2006 & 2009) held in account number xxxxx).",),
      ]
