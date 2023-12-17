# Import the dependencies.
import numpy as np
import datetime as dt
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)
#################################################

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

Base.classes.keys()


# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/vi.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/between_temp/start/end<br/>"

    )

################################################
# Flask Routes
################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from today
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)


    # Query for the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
        

    session.close()
    # Dict with date as the key and prcp as the value
    precip = []
    for date, prcp in precipitation:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip.append(precip_dict)
        
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """Return a list of stations."""
    results = session.query(Station.station).all()
    
    session.close()

    # Unravel results into a 1D array and convert to a list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/vi.0/tobs")
def temp_monthly():
    session = Session(engine)
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from today
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)


    # Query the primary station for all tobs from the last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    session.close()

    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    
    # Return the results
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
def stats_start(start=None):
    session = Session(engine)
    """Return TMIN, TAVG, TMAX."""
    
    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]


    # calculate TMIN, TAVG, TMAX for dates greater than start
    results = session.query(*sel).\
        filter(Measurement.date >= start).all()

    session.close()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/between_temp/<start>/<end>")
def stats(start=None, end=None):
    session = Session(engine)
    """Return TMIN, TAVG, TMAX."""


    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]


    if not end:
        # calculate TMIN, TAVG, TMAX for dates greater than start
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()


        # Unravel results into a 1D array and convert to a list
        temps = list(np.ravel(results))
        return jsonify(temps)


    # calculate TMIN, TAVG, TMAX with start and stop
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    session.close()


    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


if __name__ == '__main__':
    app.run(debug=True)