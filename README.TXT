Installation
Backend
# python3 and node should be installed
# mkdir backend mkdir frontend    		- create folders backend frontend
# cd backend
# python3 -m venv venv 	 				- create virtual environment in backend folder
# source venv/bin/activate 				- activate source
# pip install django djangorestframework django-cors-headers - install django
# django-admin startproject backendapi 	- create django project
# cd backendapi 						- cd to backendapi
# django-admin startapp api 			- start app
# python3 manage.py migrate 			- migrate
# python3 manage.py  createsuperuser 	- create django superuser
# add in backendapi->settings.py installed apps -> 'rest_framework','corsheaders','api'
# python3 manage.py migrate 			- migrate
# python3 manage.py runserver
# write view classes in views.py of api folder
# create new file in api folder for serializer
# in backendapi/backendapi folder edit urls.py file and add route for api.
# create file urls.py in api folder.
# add blank path and import urls from backend folder


Frontend
# npx create-react-app frontendapp 	- create react application
# cd frontendapp 
# npm start
# remove logo.svg, app.test.js
# create folder components 


# npm install react-router-dom
# npm i react-bootstrap
# npm install --save bootstrap@latest
# import '../node_modules/bootstrap/dist/css/bootstrap.min.css'; in index.js