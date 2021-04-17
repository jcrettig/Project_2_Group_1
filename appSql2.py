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
from flask_cors import CORS

from flask import Flask, jsonify
import json
#################################################
# Database Setup
#################################################

class imdb(Base):
    __tablename__ = 'imdb'
    title = Column(String, primary_key=True)
    user_score = Column(Float)
    year = Column(Integer)
    duration = Column(Integer)
    country = Column(String)
    usa_gross = Column(Integer)
    world_gross = Column(Integer)

class tomato(Base):
    __tablename__ = 'tomato'
    rank = Column(Integer)
    title = Column(String, primary_key=True)
    year = Column(Integer)
    rating = Column(Integer)
    genres = Column(String)

database_path = "project2.db"
engine = create_engine(f"sqlite:///{database_path}", echo = True)
conn = engine.connect()

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session
session = Session(bind=engine)

app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"                                       
        f"/api/v1.0/imdb<br/>"
        f"/api/v1.0/imdb2<br/>"
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
def imdb_route():   
    session = Session(engine)
    imdb_q = session.query(imdb.title, imdb.user_score, imdb.year, imdb.duration, imdb.country, imdb.usa_gross, imdb.world_gross).all()

    session.close()

    # imdb_results = []
    # for title, user_score, year, duration, country, usa_gross, world_gross in imdb_q:
    #     imdb_dict = {}
    #     imdb_dict["title"] = title
    #     imdb_dict["user_score"] = user_score
    #     imdb_dict["year"] = year
    #     imdb_dict["duration"] = duration
    #     imdb_dict["country"] = country
    #     imdb_dict["usa_gross"] = usa_gross
    #     imdb_dict["world_gross"] = world_gross       

    #     imdb_results.append(imdb_dict) 

    rows = [(title, user_score, year, duration, country, usa_gross, world_gross) for title, user_score, year, duration, country, usa_gross, world_gross in imdb_q]
    cols = list(zip(*rows))
    imdb_results = {'title':cols[0], 'user_score':cols[1], 'year':cols[2], 'duration':cols[3], 'country':cols[4], 'usa_gross':cols[5], 'world_gross':cols[6]}


    return jsonify(imdb_results)

@app.route("/api/v1.0/imdb2")
def imdb_route2():   
    session = Session(engine)
    imdb_q = session.query(imdb.title, imdb.user_score, imdb.year, imdb.duration, imdb.country, imdb.usa_gross, imdb.world_gross).all()
    session.close()
    imdb_results = []
    for title, user_score, year, duration, country, usa_gross, world_gross in imdb_q:
        imdb_dict = {}
        imdb_dict["title"] = title
        imdb_dict["user_score"] = user_score
        imdb_dict["year"] = year
        imdb_dict["duration"] = duration
        imdb_dict["country"] = country
        imdb_dict["usa_gross"] = usa_gross
        imdb_dict["world_gross"] = world_gross       
        imdb_results.append(imdb_dict) 
    # rows = [(title, user_score, year, duration, country, usa_gross, world_gross) for title, user_score, year, duration, country, usa_gross, world_gross in imdb_q]
    # cols = list(zip(*rows))
    # imdb_results = {'title':cols[0], 'user_score':cols[1], 'year':cols[2], 'duration':cols[3], 'country':cols[4], 'usa_gross':cols[5], 'world_gross':cols[6]}
    return jsonify(imdb_results)

@app.route("/api/v1.0/imdb_country")
def imdb_country():
    session = Session(engine)
    results = session.query(imdb.country).all()
    session.close()
    all_countries = list(results)
    all_countries = list(zip(*all_countries))[0]    
    return jsonify(all_countries)

@app.route("/api/v1.0/imdb_duration")
def imdb_duration():
    session = Session(engine)
    results = session.query(imdb.duration).all()
    session.close()
    all_duration = list(results)
    all_duration = list(zip(*all_duration))[0]
    return jsonify(all_duration)

@app.route("/api/v1.0/imdb_title")
def imdb_title():
    session = Session(engine)
    results = session.query(imdb.title).all()
    session.close()
    all_titles = list(results)
    all_titles = list(zip(*all_titles))[0]
    return jsonify(all_titles)

@app.route("/api/v1.0/imdb_usgross")
def imdb_usgross():
    session = Session(engine)
    results = session.query(imdb.usa_gross).all()
    session.close()
    all_usa_gross = list(results)
    all_usa_gross = list(zip(*all_usa_gross))[0]
    return jsonify(all_usa_gross)

@app.route("/api/v1.0/imdb_userscore")
def imdb_userscore():
    session = Session(engine)
    results = session.query(imdb.user_score).all()
    session.close()
    all_user_scores = list(results)
    all_user_scores = list(zip(*all_user_scores))[0]
    return jsonify(all_user_scores)

@app.route("/api/v1.0/imdb_worldgross")
def imdb_worldgross():
    session = Session(engine)
    results = session.query(imdb.world_gross).all()
    session.close()
    all_world_gross = list(results)
    all_world_gross = list(zip(*all_world_gross))[0]
    return jsonify(all_world_gross)

@app.route("/api/v1.0/imdb_year")
def imdb_year():
    session = Session(engine)
    results = session.query(imdb.year).all()
    session.close()
    all_years = list(results)
    all_years = list(zip(*all_years))[0]
    return jsonify(all_years)

#Tomato Data
@app.route("/api/v1.0/tomato")
def tomato_route():
    session = Session(engine)
    tomato_q = session.query(tomato.rank, tomato.title, tomato.year, tomato.rating, tomato.genres).all()

    session.close()

    # tomato_results = []
    # for rank, title, year, rating, genres in tomato_q:
    #     tomato_dict = {}
    #     tomato_dict["rank"] = rank
    #     tomato_dict["title"] = title
    #     tomato_dict["year"] = year
    #     tomato_dict["rating"] = rating
    #     tomato_dict["genres"] = genres             

    #     tomato_results.append(tomato_dict) 
 
    rows = [(rank, title, year, rating, genres) for rank, title, year, rating, genres in tomato_q]
    cols = list(zip(*rows))
    tomato_results = {'rank':cols[0], 'title':cols[1], 'year':cols[2], 'rating':cols[3], 'genres':cols[4]}


    return jsonify(tomato_results)

@app.route("/api/v1.0/tomato_genres")
def tomato_genres():
    session = Session(engine)
    results = session.query(tomato.genres).all()
    session.close()
    all_genres = list(results)
    all_genres = list(zip(*all_genres))[0]
    return jsonify(all_genres)   

@app.route("/api/v1.0/tomato_rank")
def tomato_rank():
    session = Session(engine)
    results = session.query(tomato.rank).all()
    session.close()
    all_ranks = list(results)
    all_ranks = list(zip(*all_ranks))[0]
    return jsonify(all_ranks)
    
@app.route("/api/v1.0/tomato_rating")
def tomato_rating():
    session = Session(engine)
    results = session.query(tomato.rating).all()
    session.close()
    all_ratings = list(results)
    all_ratings = list(zip(*all_ratings))[0]
    return jsonify(all_ratings)
    
@app.route("/api/v1.0/tomato_title")
def tomato_title():
    session = Session(engine)
    results = session.query(tomato.title).all()
    session.close()
    all_titles = list(results)
    all_titles = list(zip(*all_titles))[0]
    return jsonify(all_titles)        

@app.route("/api/v1.0/tomato_year")
def tomato_year():
    session = Session(engine)
    results = session.query(tomato.year).all()
    session.close()
    all_years = list(results)
    all_years = list(zip(*all_years))[0]
    return jsonify(all_years)

if __name__ == '__main__':
    app.run(debug=True)
