import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#setup database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
base = automap_base()
base.prepare(engine, reflect = True)
measurement = base.classes.measurement
station = base.classes.station

#setup flask
app = Flask(__name__)

#routes

@app.route("/")
def welcome():
    """List all available api routes"""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)

    results = session.query(measurement.date, measurement.prcp).all()
    session.close()
    prcp_list = []
    for row in results:
        prcp_dict = {}
        prcp_dict[row.date] = row.prcp
        prcp_list.append(prcp_dict)
    
    return jsonify(prcp_list)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(station.name).all()
    session.close()

    stations = list(np.ravel(results))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    year_temp = session.query(measurement.tobs, measurement.date).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date.between('2016-08-23', '2017-08-23'))
    session.close()

    tobs_list = []
    for row in year_temp:
        tobs_dict = {}
        tobs_dict[row.date] = row.tobs
        tobs_list.append(tobs_dict)
    
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def temps(start):
    session = Session(engine)
    results = session.query(func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= start).all()
    session.close()
    temps_list = list(np.ravel(results))
    return jsonify(temps_list)

@app.route("/api/v1.0/<start>/<end>")
def temps2(start, end):
    session = Session(engine)
    results = session.query(func.max(measurement.tobs), func.min(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date.between(start, end).all()
    session.close()
    temps_list = list(np.ravel(results))
    return jsonify(temps_list)


    
