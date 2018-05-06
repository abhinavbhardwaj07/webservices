# webservices


This web service project is developed in python using django(It provides a default apache server). 
This service takes in url information to decide weather the provided resource(url) is malicious or not.
Third party can call this service to find out malicious urls.

Please go through the "pre-requirement.txt" to know what all is needed to run this web service. Mostly user need to install some python library apart from mongdb community edition.

How to Deploy and run the server?

Deployment:

User shall take linux system(I used CentOS), Copy the entire folder "webservices-master" in some location.
User shall navigate to the location of the folder under "webservices-master"


Some setting changes:
This project uses:
1) mongodb to fetch the details of urls. so, User need to update the mongodb connection string under "webservices-master/webservices/settings.py"

mongoengine.connect(db='intelligence',
                    host='<some_host>',
                    port=27017,
                    username='<some_user>',
                    password='<some_password>')
					
2) sqlite to store the information of the users
In order to migrate the tables in sqlite, python manage.py migrate

3) create the superuser for the django admin
 python manage.py createsuperuser
 Username (leave blank to use 'aztec'): s_user
Email address: s_user@mail.com
Password:
Password (again):
Superuser created successfully.
(When User calls /users API, this user shall be shown in JSON format)


Running Server:

Under "webservices-master"
User need to run "python manage.py runserver 0.0.0.0:8000"

Databases:
	mongodb has a collection(similar like db in RDBMS) named "malicious_urls_details" that cotains the details of url
	As mongo is schemaless, I am storing these field in a document(row in RDBMS) ===> host, port, original_path, is_malicious, first_seen
	I have created the index on host, port, original_path so that If still billions of data is there in the db, mongo client can fetch the data efficiently.
	// mongo shell
	ex: db.malicious_urls_details.ensureIndex({original_path: 1,host: 1, port: 1}, {background: true,name: 'urllookup_index_by_original_path_host_and_port'});
	As indexes are created on host, port, original_path, duplicate entry is not possible.
	Authentication is enabled on the mongodb.User can add users from mongo shell
	//mongo shell
	ex: db.createUser({user: "intelligence_user",pwd: "s3cretpassw0rd",roles: [ { role: "readWrite", db: "intelligence" }]})
	This ame user shall be used in above mentioned settings.py

What all urls is being supported?
All are REST APIs(response will be returned in JSON format)
1) http://<host>:8000/users
	method: GET
	It will list down all the users in a json format
	response:
	[
		{
			"id": 1,
			"username": "s_user"
		},
		{
			"id": 2,
			"username": "m_user"
		}
	]
2) http://<host>:8000
	method: GET
	As this one is on the "/". Response will only say "server is up"
	response:
	{
		"ping": true,
		"success": true
	}
3) http://<host>:8000/urlinfo/1/<host1>/<port1>/<original_path>
	method: GET
	eg: http://<host>:8000/urlinfo/1/127.0.0.1/8000/home/alone1 (here host = 127.0.0.1, port = 8000, original_path = 'home/alone1")
	response:
	{
		"original_path": "home/alone1",
		"host": "127.0.0.1",
		"is_malicious": true,
		"port": 8000,
		"success": true
	}
	Here, "is_malicious" value will reflect weather url is malicious or not(third party can use "is_malicious")


TestCase:

Test case to check If url is malicious or not is present under location "url_lookup_service/test.py"
Command to run test: under "webservices-master", python manage.py test
Above command will run the tests present in "url_lookup_service/test.py"
