App Url: http://csv-importer-fe.ngrok.io.ngrok.io/

API Url: http://csv-importer-be.ngrok.io.ngrok.io/api/rows

Admin Panel URL: http://csv-importer-be.ngrok.io.ngrok.io/admin/login/?next=/admin/
  - Admin Panel Credentials
  - Username: prawl
  - Password: securepassword

## How to Use
- Importing rows demo
![Import](https://media.giphy.com/media/i3XE5hJTYT1YwHdg5G/giphy.gif)

- Deleting imported rows
![Delete](https://media.giphy.com/media/3JX8cGbQtXjPQl5Sw8/giphy.gif)

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