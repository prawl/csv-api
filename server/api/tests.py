# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ImportFile, ImportRow
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone

class ImportRowModelTest(TestCase):
  def validation_row_creation_positive_float(self):
    row = ImportRow(acv_dist=-1)
    self.assertRaises(ValidationError, row.full_clean)

  def row_creation(self):
    row = ImportRow.objects.create(
      # TODO: Add file attribute test
      # file = ImportFile.objects.create(),
      date = timezone.now().date(),
      retail_sales_volume = 1.3,
      acv_dist = 1.3,
      competition = 1.3,
      edlp = 1.3,
      trade_any_promo =1.3,
      tv = 1.3,
      print_value = 1.3,
      online_display = 1.3,
      preroll_video = 1.3,
      paid_search = 1.3,
      public_relations = 1.3,
      fsi = 1.3,
      digital_coupon = 1.3,
      shopper_marketing = 1.3,
    )
    # TODO: Make these test more intuitive
    self.assertEqual(row.retail_sales_volume, 1.3)
    self.assertEqual(row.acv_dist, 1.3)
    self.assertEqual(row.competition, 1.3)
    self.assertEqual(row.edlp, 1.3)
    self.assertEqual(row.trade_any_promo, 1.3)
    self.assertEqual(row.tv, 1.3)
    self.assertEqual(row.print_value, 1.3)
    self.assertEqual(row.online_display, 1.3)
    self.assertEqual(row.preroll_video, 1.3)
    self.assertEqual(row.paid_search, 1.3)
    self.assertEqual(row.fsi, 1.3)
    self.assertEqual(row.digital_coupon, 1.3)
    self.assertEqual(row.shopper_marketing, 1.3)

# TODO: Write this unit test
# class ImportFileModelTest(TestCase):
#   def test_row_creation(self):
#     csv = SimpleUploadedFile("test.csv", )
