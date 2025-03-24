from flask import Flask, request, render_template, session, redirect, url_for
from flask import render_template
import numpy as np
import pandas as pd

import os
from pyspark.sql import SparkSession
import sys
from functions import f



sys.path.append("C:/Users/kondo/OneDrive/Documents/GitHub/MovieRecommender-main/MovieGroupProj/movie_app/functions")

import os

os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jdk-21"
os.environ["SPARK_HOME"] = "C:\\spark\\spark-3.5.5-bin-hadoop3"
os.environ["PATH"] += os.pathsep + os.path.join(os.environ["JAVA_HOME"], "bin")

spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext
sc

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/recc", methods=['GET', 'POST'])
def recc():
    import time
    start_time = time.time()
    print("Loading movie table...")

    # Load all movie data
    df = f.movieTable()
    print(f"Columns in DataFrame: {df.columns.tolist()}")  # Log the column names
    
    # Get unique years for the filter dropdown
    years = sorted(df['Year'].unique().tolist())  # Use the correct column name 'Year'
    
    # Handle year filter
    selected_year = request.form.get('year_filter', '') if request.method == 'POST' else ''
    if selected_year:
        df = df[df['Year'] == int(selected_year)]  # Filter by selected year
    
    li = df.values.tolist()
    print(f"Loaded {len(li)} movies in {time.time() - start_time:.2f} seconds")
    return render_template("recc.html", data=li, years=years, selected_year=selected_year)

@app.route('/process', methods=['GET', 'POST']) 
def process(): 
    if request.method == "POST":
        # Get selected movie IDs
        movie_ids = request.form.getlist('movie_ids')
        print(f"Processing selected movie IDs: {movie_ids}")
        
        # Validate the number of selected movies
        if not movie_ids:
            return render_template('recc.html', error="Please select at least one movie.")
        if len(movie_ids) > 5:
            return render_template('recc.html', error="You can select up to 5 movies only.")
        
        try:
            import time
            start_time = time.time()
            
            # Convert movie_ids to a comma-separated string for f.selToList()
            data = ','.join(movie_ids)
            recommendations = f.selToList(data)
            if recommendations is None or len(recommendations) == 0:
                print("No recommendations found")
                return render_template('recc.html', error="No recommendations found for the selected movies.")
            
            # Since f.selToList() returns a pandas DataFrame
            recs = recommendations.values.tolist()
            print(f"Found {len(recs)} recommendations in {time.time() - start_time:.2f} seconds")
            
            session["recMovies"] = recs
            return redirect(url_for('suggestions'))
        except Exception as e:
            print(f"Error in processing: {e}")
            return render_template('recc.html', error=f"Error processing recommendations: {str(e)}")
    
    return render_template('recc.html')


@app.route('/suggestions')
def suggestions():
    movies = session['recMovies']  
  
    # make table with recommended movies
    return render_template("suggestions.html", data=movies)
    
    






