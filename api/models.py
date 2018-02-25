# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from compress_storage import ZipFileField
from django.core.validators import MinValueValidator
from django.db import models


class ImportFile(models.Model):
  docfile = ZipFileField(upload_to="uploads/")
  filename = models.CharField(max_length=255,null=True)

  def __str__(self):
    return self.filename

class ImportRow(models.Model):
  file = models.ForeignKey(ImportFile,null=True, on_delete=models.CASCADE)
  date = models.DateField('Date', null=True, blank=True)
  retail_sales_volume = models.FloatField(default=0,validators=[MinValueValidator(0)])
  retail_price = models.FloatField(default=0,validators=[MinValueValidator(0)])
  acv_dist = models.FloatField(default=0,validators=[MinValueValidator(0)])
  competition = models.FloatField(default=0,validators=[MinValueValidator(0)])
  edlp = models.FloatField(default=0,validators=[MinValueValidator(0)])
  trade_any_promo = models.FloatField(default=0,validators=[MinValueValidator(0)])
  tv = models.FloatField(default=0,validators=[MinValueValidator(0)])
  print_value = models.FloatField(default=0,validators=[MinValueValidator(0)])
  online_display = models.FloatField(default=0,validators=[MinValueValidator(0)])
  preroll_video = models.FloatField(default=0,validators=[MinValueValidator(0)])
  paid_search = models.FloatField(default=0,validators=[MinValueValidator(0)])
  public_relations = models.FloatField(default=0,validators=[MinValueValidator(0)])
  fsi = models.FloatField(default=0,validators=[MinValueValidator(0)])
  digital_coupon = models.FloatField(default=0,validators=[MinValueValidator(0)])
  shopper_marketing = models.FloatField(default=0,validators=[MinValueValidator(0)])

