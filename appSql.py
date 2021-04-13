#################################################
# Imports
#################################################
import numpy as np
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

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
engine = create_engine("sqlite:///project2.db")             
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table

imdb_df = pd.read_sql_table('imdb', engine)               
print (imdb_df)       

tomato_df = pd.read_sql_table('tomato', engine)               
print (tomato_df)  

# imdb_result = engine.execute('SELECT * FROM "imdb";')     
# # print(result.fetchall())                                

imdb = Base.classes.imdb                                 
tomato = Base.classes.tomato

#################################################
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

#imdb Data
@app.route("/api/v1.0/imdb")
def imdb():   
    session = Session(engine)
    imdb_q = session.query(imdb.title, imdb.user_score, imdb.year, imdb.duration, imdb.country, imdb.usa_gross, imdb.world_gross).all()

    session.close()

    imdb = []
    for title, user_score, year, duration, country, usa_gross, world_gross in imdb_q:
        imdb_dict = {}
        imdb_dict["title"] = title
        imdb_dict["user_score"] = user_score
        imdb_dict["year"] = year
        imdb_dict["duration"] = duration
        imdb_dict["country"] = country
        imdb_dict["usa_gross"] = usa_gross
        imdb_dict["world_gross"] = world_gross       

        imdb.append(imdb_dict) 

    return jsonify(imdb)

@app.route("/api/v1.0/imdb_country")
def imdb_country():
    session = Session(engine)
    results = session.query(imdb.country).all()
    session.close()
    all_countries = list(np.ravel(results))
    return jsonify(all_countries)

@app.route("/api/v1.0/imdb_duration")
def imdb_duration():
    session = Session(engine)
    results = session.query(imdb.duration).all()
    session.close()
    all_duration = list(np.ravel(results))
    return jsonify(all_duration)

@app.route("/api/v1.0/imdb_title")
def imdb_title():
    session = Session(engine)
    results = session.query(imdb.title).all()
    session.close()
    all_titles = list(np.ravel(results))
    return jsonify(all_titles)

@app.route("/api/v1.0/imdb_usgross")
def imdb_usgross():
    session = Session(engine)
    results = session.query(imdb.usa_gross).all()
    session.close()
    all_usa_gross = list(np.ravel(results))
    return jsonify(all_usa_gross)

@app.route("/api/v1.0/imdb_userscore")
def imdb_userscore():
    session = Session(engine)
    results = session.query(imdb.user_score).all()
    session.close()
    all_user_scores = list(np.ravel(results))
    return jsonify(all_user_scores)

@app.route("/api/v1.0/imdb_worldgross")
def imdb_worldgross():
    session = Session(engine)
    results = session.query(imdb.world_gross).all()
    session.close()
    all_world_gross = list(np.ravel(results))
    return jsonify(all_world_gross)

@app.route("/api/v1.0/imdb_year")
def imdb_year():
    session = Session(engine)
    results = session.query(imdb.year).all()
    session.close()
    all_years = list(np.ravel(results))
    return jsonify(all_years)

#Tomato Data
@app.route("/api/v1.0/tomato")
def tomato():
    session = Session(engine)
    tomato_q = session.query(tomato.rank, tomato.title, tomato.year, tomato.rating, tomato.genres).all()

    session.close()

    tomato = []
    for rank, title, year, rating, genres in tomato_q:
        tomato_dict = {}
        tomato_dict["rank"] = rank
        tomato_dict["title"] = title
        tomato_dict["year"] = year
        tomato_dict["rating"] = rating
        tomato_dict["genres"] = genres             

        tomato.append(tomato_dict) 

    return jsonify(tomato)

@app.route("/api/v1.0/tomato_genres")
def tomato_genres():
    session = Session(engine)
    results = session.query(tomato.genres).all()
    session.close()
    all_genres = list(np.ravel(results))
    return jsonify(all_genres)   

@app.route("/api/v1.0/tomato_rank")
def tomato_rank():
    session = Session(engine)
    results = session.query(tomato["rank"]).all()
    session.close()
    all_ranks = list(np.ravel(results))
    return jsonify(all_ranks)
    
@app.route("/api/v1.0/tomato_rating")
def tomato_rating():
    session = Session(engine)
    results = session.query(tomato.rating).all()
    session.close()
    all_ratings = list(np.ravel(results))
    return jsonify(all_ratings)
    
@app.route("/api/v1.0/tomato_title")
def tomato_title():
    session = Session(engine)
    results = session.query(tomato.title).all()
    session.close()
    all_titles = list(np.ravel(results))
    return jsonify(all_titles)        

@app.route("/api/v1.0/tomato_year")
def tomato_year():
    session = Session(engine)
    results = session.query(tomato.year).all()
    session.close()
    all_years = list(np.ravel(results))
    return jsonify(all_years)

if __name__ == '__main__':
    app.run(debug=True)
