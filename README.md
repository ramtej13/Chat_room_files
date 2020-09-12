# Chat_room_files

This is a chat room on your local host using django framework 

# Steps to run the code 

Terminal commands to install all the dependenses and to start the project 
- pip install django
- pip install channels_redis
- pip install -U channels
- django-admin startproject hello
- cd hello
- python manage.py startapp chat


File to replace 
- download the chat_room_files on your computer and extract the files
- replace all the files from @hello/hello to your @hello/hello in you project 
- replace all the files from @hello/chat to  @hello/chat in your project
- copy the static dictionary from @hello to @hello in your project


Make the migrations after replacing the files.
- python manage.py migrate
- python manage.py makemigrations


Use this command to create 2 superusers to access the chat room 
- python manage.py createsuperuser

Run the redis server on termenal or command prompt

Start the local host using below command
- python manage.py runserver

loging into user
- open two browser 
- use the below link to login as superuser in each of the browser
    - http://127.0.0.1:8000/admin/    

Finally
- after logging as super user  
- go to the below url to c the chat room 
  - http://127.0.0.1:8000/chat/   
  
 

new commit commands 

- git clone https://github.com/ramtej13/Chat_room_files.git
- pip3 install requirements.txt
- python3 manage.py makemigrations 
- python3 manage.py migrate
- python3 manage.py collectstatic
- python3 manage.py createsuperuser
- python3 manage.py runserver 




