App Url: http://csv-importer-fe.ngrok.io.ngrok.io/

API Url: http://csv-importer-be.ngrok.io.ngrok.io/api/rows

Admin Panel URL: http://csv-importer-be.ngrok.io.ngrok.io/admin/login/?next=/admin/
  - Admin Panel Credentials
  - Username: prawl
  - Password: securepassword

# TODOs:

# API
- [X] Create Models
- [X] Create Routes
- [X] Create Serializers
- [X] Write tests
- [X] Validate the header row exists
- [] Refactor tests
- [] Update DB with postgres instead of mysql
# FE
- [X] Allow the user to upload the CSV
- [X] Allow the user to view all of the import rows
- [] Display negative number validation on the FE
- [] Write tests
- [] Setup the grunt watch task