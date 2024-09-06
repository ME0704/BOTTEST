# app.py
from flask import Flask
from app1 import app1
from app2 import app2
from app3 import app3

app = Flask(__name__)
app.register_blueprint(app1, url_prefix='/initiate-monthly-signals')
app.register_blueprint(app2, url_prefix='/initiate-3months-signals')
app.register_blueprint(app3, url_prefix='/initiate-6months-signals')

if __name__ == '__main__':
    app.run()