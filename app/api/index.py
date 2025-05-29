from flask import Flask
from vercel_wsgi import handle_request  # Enables Flask to run on Vercel

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask app deployed on Vercel!'

# Vercel entry point
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
