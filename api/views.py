# -*- coding: utf-8 -*-
from .forms import DocumentForm
from .models import ImportFile
from .models import ImportRow
from datetime import datetime 
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
import csv # Import the CSV libaray to making parsing CSV easier https://docs.python.org/3.4/library/csv.html

def list(request):
    # Load documents for the list page
    documents = ImportFile.objects.all()

    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['docfile']
            newdoc = ImportFile(docfile=uploaded_file,filename=uploaded_file.name)
            newdoc.save()
            newdoc.docfile.compress() # After saving the file compress it

            # Read the contents of the uploaded file
            file_reader = csv.DictReader(uploaded_file, delimiter=',')
            next(file_reader, None) # skip the headers row
            for row in file_reader:
                parse_row(row, newdoc) # Create an Import Row Object for CSV row

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

def parse_row(row, uploaded_file):
    ImportRow.objects.create(
        file=uploaded_file,
        date=datetime.strptime(row["Observation Date"], '%m/%d/%Y'),
        retail_sales_volume=row['Retail Sales Volume'],
        retail_price=row['Retail Price'],
        acv_dist=row['ACV Distribution'],
        competition=row['Competition'],
        edlp=row['EDLP'],
        trade_any_promo=row['Trade Any Promo'],
        tv=row['TV'],
        print_value=row['Print'],
        online_display=row['Online Display'],
        preroll_video=row['Pre-roll Video'],
        paid_search=row['Paid Search'],
        public_relations=row['Public Relations'],
        fsi=row['FSI'],
        digital_coupon=row['Digital Coupon'],
        shopper_marketing=row['Shopper Marketing'],
    ) 
