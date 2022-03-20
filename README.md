radio-corona.ca/wise_project
radio-corona.ca/[username] 

Features:

1. multi-user blog 
2. French language
3. post news
4. Form Ajax UI
5. mysqldb backend

Tech spec

initial requirements:

- Django hotsauce 1.4
- Python 3
- Django 3.1.1
- mysqldb

Views:

Login: /login/ 
-> Support OAuth2 authentication
-> cookies (session) 

Register: /register/

Post: /submit/ -> Create a new post instance
-> tagging/categories 
-> image support/upload


class Post(models.Model):
 "A post sent by a user"
 user 
 category (optional) 
 comments 
 tags (optional)
 image (optional) 
 text = Bonjour le monde, vive les merdias!

class Comment(models.Model):
 "A reply to a post by a registered user"
 post 
 user 
 image (optional)

class LoginController(FormController):
    "Allow people to login/register"

class FormController(WSGIController):
    "Standalone controller to interact with forms using ajax"

  
-> reddit 

