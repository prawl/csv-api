from rest_framework import serializers
from .models import ImportRow

class ImportRowSerialzier(serializers.ModelSerializer):
  class Meta:
    model = ImportRow
    # Send all of the attributes about the Import Row as Json, except the file association
    exclude = ('file',)
