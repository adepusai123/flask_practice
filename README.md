# flask_practice

Features:
**Compliant with WSGI (Web services Gateway Interfaces)**
**Fllows Jinja2 Template Engine**
**Has in-built development server and debugger**
**Provides support for integrated unit testing**
**Supports RESTful request dispatching**
**Provides Session management**
**Enhances flexibility and extensibility through various libraries**
**Supports various cloud deployments**

Architecture follows as MVT 
M - Model (Data management)
V - View (business logic and maps request & response)
T - Template (HTML)


Installation create Virtual Python environment

``pip install flask``

create app.py 
add basic code then start the server as below

it execute app.py or wsgi.py default

We need to set file name for Flask Environemnt if file name differs

``set FLASK_APP=filename`` 
Set Environment mode

``set FLASK_ENV=development`` it enables built in debugger

Now run server using cmd ``flask run`` runs on 5000
``http://127.0.0.1:5000/``

