from flask import Flask
from flask_odoo import Odoo

app = Flask(__name__)
app.config["ODOO_URL"] = "http://localhost:8069"
app.config["ODOO_DB"] = "odoo"
app.config["ODOO_USERNAME"] = "admin"
app.config["ODOO_PASSWORD"] = "admin"
odoo = Odoo(app)
