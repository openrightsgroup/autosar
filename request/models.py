from django.db import models
from django import forms
from datetime import date

class NameForm(forms.Form):
  your_name = forms.CharField(label='Your name', max_length=100, initial="your name")
  address = forms.CharField(label='Address', max_length=100, initial="address")
  date = forms.CharField(label='date', max_length=100, initial=date.today() )

  details = [
      forms.BooleanField( label="Do you, or have you ever, processed any personal data about me?",),
      forms.BooleanField( label="Your personnel file",),
      forms.BooleanField( label="emails between A and B (between 1/6/11 and 1/9/11);",),
      forms.BooleanField( label="your medical records (between 2006 & 2009) held by Dr C at D hospital;",),
      forms.BooleanField( label="CCTV camera situated at (E location) on 23/5/12 between 11am and 5pm;",),
      forms.BooleanField( label="copies of statements (between 2006 & 2009) held in account number xxxxx).",),
      forms.BooleanField( label="What information about location (e.g. traffic/ number plate / MAC address or IMEI) do you have about me?",),
      forms.BooleanField( label="What data are you giving to others, and what is the reason?",),
      forms.BooleanField( label="What are the sources of each of the items I've requested so far?",),
      forms.BooleanField( label="What automated decisions have you, are you, or will be making with my data",),
      forms.BooleanField( label="Any transactions, charges or any other data related to my accounts",),
      forms.BooleanField( label="Original executed (signed) agreements at the time of my starting the relationship with you and any modifications (signed or not)",),
      forms.BooleanField( label="Dictionary of all the codes used in all documentations relating to me, with explanation of all the possible values for each code",),
      forms.BooleanField( label="Please inform me, prior to delivering my request, if you require a processing fee. Please note that you requiring a fee does not prolong the 40 day statutory term for fulfilling this request. In addition, what forms of payment do you accept?",),
      forms.BooleanField( label="What commissions or other payments have you made or will you make to any other third party in relation with the provision, packaging, or referrals regarding my relationship with you",),
      forms.BooleanField( label="Correspondance to, from or about me",),
      forms.BooleanField( label="Log of calls and transcripts if available, and recordings, if available of any calls to from or about me",),
      forms.BooleanField( label="What are the data retention policies for archival, backup and destruction of each of the personal information requested below",),
      forms.BooleanField( label="What ID numbers have you associated with me or my account(s) and what other third party ID's about myself do you have, how do you validate them and correlate them?",),
      forms.BooleanField( label="Any information about any criminal records that I may have",),
      forms.BooleanField( label="Any CCTV records, telephone records, or any other audio/visual recording",),
      forms.BooleanField( label="General statement of account",),
      forms.BooleanField( label="Medical records",),
      forms.BooleanField( label="If you exclude anything from the reply to this request, what exemptions are you invoking?",),
      
      ]
