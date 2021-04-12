#################################################
# Imports
#################################################
import numpy as np
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

imdb_file = "imdb_clean.csv"
tomato_file = "tomato_clean.csv"

imdb_df = pd.read_csv(imdb_file)
tomato_df = pd.read_csv(tomato_file)

################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"                                       
        f"/api/v1.0/imdb<br/>"
        f"/api/v1.0/imdb_country<br/>"
        f"/api/v1.0/imdb_duration<br/>"
        f"/api/v1.0/imdb_title<br/>"
        f"/api/v1.0/imdb_usgross<br/>"
        f"/api/v1.0/imdb_userscore<br/>"
        f"/api/v1.0/imdb_worldgross<br/>"
        f"/api/v1.0/imdb_year<br/><br/>"
        f"/api/v1.0/tomato<br/>"   
        f"/api/v1.0/tomato_genres<br/>"        
        f"/api/v1.0/tomato_rank<br/>"
        f"/api/v1.0/tomato_rating<br/>"
        f"/api/v1.0/tomato_title<br/>"
        f"/api/v1.0/tomato_year<br/>"
    )

@app.route("/api/v1.0/imdb")
def imdb():
    return jsonify(json.JSONDecoder().decode(imdb_df.to_json()))  

@app.route("/api/v1.0/imdb_country")
def imdb_country():
    return jsonify(json.JSONDecoder().decode(imdb_df["country"].to_json()))

@app.route("/api/v1.0/imdb_duration")
def imdb_duration(): 
    return jsonify(json.JSONDecoder().decode(imdb_df["duration"].to_json()))   

@app.route("/api/v1.0/imdb_title")
def imdb_title():
    return jsonify(json.JSONDecoder().decode(imdb_df["title"].to_json()))  

@app.route("/api/v1.0/imdb_usgross")
def imdb_usgross():
    return jsonify(json.JSONDecoder().decode(imdb_df["usa_gross"].to_json())) 

@app.route("/api/v1.0/imdb_userscore")
def imdb_userscore():
    return jsonify(json.JSONDecoder().decode(imdb_df["user_score"].to_json())) 

@app.route("/api/v1.0/imdb_worldgross")
def imdb_worldgross():
    return jsonify(json.JSONDecoder().decode(imdb_df["world_gross"].to_json())) 

@app.route("/api/v1.0/imdb_year")
def imdb_year():
    return jsonify(json.JSONDecoder().decode(imdb_df["year"].to_json()))      

@app.route("/api/v1.0/tomato")
def tomato():
    return jsonify(json.JSONDecoder().decode(tomato_df.to_json()))

@app.route("/api/v1.0/tomato_genres")
def tomato_genres():
    return jsonify(json.JSONDecoder().decode(tomato_df["genres"].to_json()))

@app.route("/api/v1.0/tomato_rank")
def tomato_rank():
    return jsonify(json.JSONDecoder().decode(tomato_df["rank"].to_json()))

@app.route("/api/v1.0/tomato_rating")
def tomato_rating():
    return jsonify(json.JSONDecoder().decode(tomato_df["rating"].to_json()))

@app.route("/api/v1.0/tomato_title")
def tomato_title():
    return jsonify(json.JSONDecoder().decode(tomato_df["title"].to_json()))

@app.route("/api/v1.0/tomato_year")
def tomato_year():
    return jsonify(json.JSONDecoder().decode(tomato_df["year"].to_json()))
    
if __name__ == '__main__':
    app.run(debug=True)
