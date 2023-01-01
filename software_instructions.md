# Sevak

## **Prerequisites:**

-	Python should be installed in the computer. (Preferably, Python 3.10) 
-	Make sure that inside path is within the Sevak directory. If not, the command is [cd Seva].
-	Also, use command [pip install virtualenv] in order to install virtual environments.
-	Now, make a virtual environment named hi using command [virtualenv hi].	

## **Activation of Virtual Environments:**

For Windows devices- [.hi/Scripts/activate] </br>
For Mac or Linux devices- [source hi/bin/activate]

## **Setting-up Instructions:**

-	Install all the dependencies using [pip install -r requirements.txt] command.
-	Verify all the dependencies are installed using [pip freeze] command and compare it with requirements.txt.
-	Now run [python manage.py makemigrations] followed by [python manage.py migrate]
-	After all migrations are applied, we are ready to use the web-app now. </br>
To get it running on the localhost- [python manage.py runserver] and then {Ctrl + Click} on http://127.0.0.1:8000/ to visit the website.
-	Also, if you want to set an admin to the website go to http://127.0.0.1:8000/admin.
Then, run the [python manage.py createsuperuser] command to enter the credentials and start working.
-	You should now able to utilize the fully-functional web application, Sevak.

## Deployment link- 
-- [Azure](https://sevak.azurewebsites.net/) :link: </br>
