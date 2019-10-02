
import os

from flask import Flask, render_template, redirect, request, url_for

from flask_pymongo import PyMongo

from bson.objectid import ObjectId 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'update_keys'

app.config["MONGO_URI"] = os.getenv('MONGO_URI')


mongo = PyMongo(app)


@app.route('/')

@app.route('/get_keys')

def get_keys():

    return render_template("keys.html", keys=mongo.db.keys.find())


@app.route('/add_key')

def add_key():

    return render_template('addkey.html',

                           categories=mongo.db.categories.find())

@app.route('/insert_key', methods=['POST'])

def insert_key():

    keys = mongo.db.keys

    keys.insert_one(request.form.to_dict())

    return redirect(url_for('get_keys'))


if __name__ == '__main__':

    app.run(host=os.environ.get('IP'),

            port=(os.environ.get('PORT')),

            debug=True)
