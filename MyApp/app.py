import os
# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, and_
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "postgresql+psycopg2://postgres:changeme@localhost:5432/test"
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://fnuobabcdkhzxk:8b6a8c76d850a1c4972372e8e087dbbf1fbec76ca5b2ff1e31e3a3f39fe86cf1@ec2-174-129-254-235.compute-1.amazonaws.com:5432/d2plbk9leajbu9"
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

from .models import My_data

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
print("print keys")
print(Base.classes.keys())
# Save references to each table
TempTableData = Base.classes.my_test_table


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/getnames")
def getnames():
    print("in getnames")
    results = db.session.query(TempTableData.myname, TempTableData.myname1).all()
    print(results)
    myDataResults = []
    for result in results:
        myDataResult = {}
        myDataResult["myname"] = result[0]
        myDataResult["myname1"] = result[1]
        myDataResults.append(myDataResult)
    return jsonify(myDataResults)

if __name__ == "__main__":
    app.run(debug=True)





