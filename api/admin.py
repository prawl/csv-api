# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ImportRow, ImportFile
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"

class ImportRowResource(resources.ModelResource):
  # TODO: Figure out how to transform date into appropriate format
  # date = fields.Field(attribute="date", column_name="Observation Date")
  retail_sales_volume = fields.Field(attribute="retail_sales_volume", column_name="Retail Sales Volume")
  retail_price = fields.Field(attribute="retail_price", column_name="Retail Price")
  acv_dist = fields.Field(attribute="acv_dist", column_name="ACV Distribution")
  competition = fields.Field(attribute="competition", column_name="Competiton")
  edlp = fields.Field(attribute="edlp", column_name="EDLP")
  trade_any_promo = fields.Field(attribute="trade_any_promo", column_name="Trade Any Promo")
  tv = fields.Field(attribute="tv", column_name="TV")
  print_value = fields.Field(attribute="print_value", column_name="Print")
  online_display = fields.Field(attribute="online_display", column_name="Online Display")
  preroll_video = fields.Field(attribute="preroll_video", column_name="Pre-roll Video")
  paid_search = fields.Field(attribute="paid_search", column_name="Paid Search")
  public_relations = fields.Field(attribute="public_relations", column_name="Public Relations")
  fsi = fields.Field(attribute="fsi", column_name="FSI")
  digital_coupon = fields.Field(attribute="digital_coupon", column_name="Digital Coupon")
  shopper_marketing = fields.Field(attribute="shopper_marketing", column_name="Shopper Marketing")


  class Meta:
    model = ImportRow
    skip_unchanged = True
    fields = ('id', 'date', 'retails_sales_volumn', 'acv_dist', 'competition', 'edlp', 'trade_any_promo', 'tv', 'print_value', 'online_display', 'preroll_video', 'paid_search', 'public_relations', 'fsi', 'digital_coupon', 'shopper_marketing')
    widgets = {
              'date':  {'format': '%d-%m-%Y'},
              }

class ImportRowAdmin(ImportExportModelAdmin):
  resource_class = ImportRowResource

admin.site.register(ImportRow, ImportRowAdmin) 
