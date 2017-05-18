from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/check_user/repositories/so-exam2/A00212740/test.db'
db = SQLAlchemy(app)


class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpu = db.Column(db.String(80), nullable=False)
    ram = db.Column(db.String(120), nullable=False)
    hdd = db.Column(db.String(120), nullable=False)
    service = db.Column(db.String(120), nullable=False)


    def __init__(self, cpu, ram, hdd, service):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.service = service

    def __repr__(self):
	stats = self.cpu +" " + self.ram + " " + self.hdd+ " " + self.service

        return '<stats %r>' % stats
