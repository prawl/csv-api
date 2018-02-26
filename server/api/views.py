# -*- coding: utf-8 -*-
from .forms import DocumentForm
from .models import ImportFile
from .models import ImportRow
from .serializers import ImportRowSerialzier
from datetime import datetime 
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from rest_framework.response import Response
from rest_framework.views import APIView
import csv # Import the CSV libaray to making parsing CSV easier https://docs.python.org/3.4/library/csv.html
import ipdb # Allow the execution to be halted for better debugging
import json

class ImportRowIndex(APIView):
    def get(self, request):
        import_rows = ImportRow.objects.all()
        serializer = ImportRowSerialzier(import_rows, many=True)
        return Response(serializer.data)

class ImportFileUpload(APIView):
    def post(self, request):
        uploaded_file = request.FILES['file']
        sniffer = csv.Sniffer()
        if not sniffer.has_header(uploaded_file.read(2048)):
           response = HttpResponse(json.dumps({'message': "The file is missing header data. Please ensure it's in the proper format and try again."}), content_type="application/json") 
           response.status_code = 400
           return response

        newdoc = ImportFile(docfile=uploaded_file,filename=uploaded_file.name)
        newdoc.save() # validate here
        newdoc.docfile.compress() # After saving the file compress it

        # Read the contents of the uploaded file
        file_reader = csv.DictReader(uploaded_file, delimiter=',')
        next(file_reader, None) # skip the headers row
        for row in file_reader:
            self.parse_row(row, newdoc) # Create an Import Row Object for each CSV row
        return Response({'status': 200 })

    def parse_row(self, row, uploaded_file):
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