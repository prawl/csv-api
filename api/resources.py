from tastypie.resources import ModelResource
from api.models import ImportRow

class ImportRowResource(ModelResource):
  class Meta:
    queryset = ImportRow.objects.all()
    resource_name = 'rows'