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
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://hczvmouktniqbp:5f9dfa1f934f3ddb25c3e144b3cf99f072df39ef44892a8f83e871e13e7b664d@ec2-50-19-95-77.compute-1.amazonaws.com:5432/d8th1nc1jcipjo"
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

# from .models import Pet

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





