from flask import Flask, render_template
from auth import *

app = Flask(__name__)

app.secret_key = 'Dem gains'

@app.route('/')
def home():
  return render_template('index.html')
