from flask import Flask
from rank import app

app.run(host="0.0.0.0", debug=True, port=5550)