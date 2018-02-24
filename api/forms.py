# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
   filename = forms.FileField(
        label='Select a file'
    )