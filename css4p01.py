# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:32:58 2024

@author: HadrianBezuidenhout
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")
df = pd.DataFrame(file)

df.drop_duplicates(inplace = True)
df = df.reset_index(drop=True)

# Question 1
print("Question 1:")
top_rated = pd.Series(df["Rating"]).idxmax() # Extracts the index of the top rated movie
print(df["Title"][top_rated]) # Prints the title in the index

# Question 2
print("Question 2:")
revenue = (pd.Series(df["Revenue (Millions)"])).dropna() # Extracts revenue and removes NaN values
average_revenue = revenue.mean() # Finds average
print(average_revenue)

# Question 3
print("Question 3:")
filtered = df[(2015 <= df['Year']) & (df['Year'] <= 2017)] # Filters data to be between specific years
revenue = pd.Series(filtered["Revenue (Millions)"]).dropna() # Extracts revenue from those years and removes NaN's
average_revenue = revenue.mean() # Calculate average for those years
print(average_revenue)

# Question 4
print("Question 4:")
filtered = df[df["Year"]==2016] # Exrtacts movies made in 2016
no_of_movies = len(filtered) # Counts the number of movies
print(no_of_movies)

# Question 5
print("Question 5:")
filtered = df[df["Director"].str.contains("Christopher Nolan")] # Filters dataframe for Christopher Nolan Movies
no_of_movies = len(filtered) # Counts number of movies
print(no_of_movies)

# Question 6
print("Question 6:")
filtered = df[df["Rating"]>=8] # Filters data set for ratings of at least 8
no_of_movies = len(filtered) # Counts number of movies
print(no_of_movies)

# Question 7
import numpy as np
print("Question 7:")
filtered = df[df["Director"].str.contains("Christopher Nolan")] # Filters dataframe for Chrisopher Nolan movies
print(np.percentile(filtered["Rating"], 50)) # 50th percentile resprents the Median (middle)

# Question 8
print("Question 8:")
grouped = df.groupby(['Year']) # Groups data for processing
mean_values = grouped['Rating'].mean() # Calculates the average of the ratings in each year
mean_values = mean_values[mean_values>=max(mean_values)] # Finds the year with the highest average rating
print(mean_values)

# Question 9
print("Question 9:")
num_2006 = len(df[df["Year"]==2006]) # Finds the number of movies made in 2006
num_2016 = len(df[df["Year"]==2016]) # Finds the number of movies made in 2016
per_increase = abs((num_2016-num_2006)/num_2006)*100 # Finds the percentage increase in the number of movies made
print(per_increase)

# Question 10
print("Question 10:")
from collections import Counter
actors = (pd.Series(df["Actors"])) # Extracts the names of all the actors for each movie
actors = actors.str.split(', ', expand=True) # Seperates the names of the individual actors
actors = actors.to_numpy().flatten() # Lists all actors in a single row

dict = {'name': Counter(actors).keys(), 'frequency': Counter(actors).values()} # Lists unique actors and there frequency of appearance
actor_freq = pd.DataFrame(dict).dropna() # Removes any NaN values
actor_freq = actor_freq.reset_index(drop=True) # Resets indices
print(actor_freq["name"][actor_freq["frequency"].idxmax()]) # Prints the name of the most frequent actor

# Question 11
print("Question 11:")
genre = (pd.Series(df["Genre"])) # Extracts all genres in all movies
genre = genre.str.split(',', expand=True).dropna() # Seperates the genres and removes NaN values
genre = genre.to_numpy().flatten() # Lists all genres in one row
unique_genres = len(Counter(genre).keys()) # Counts the number of unique genres
print(unique_genres)

# Question 12
print("Question 12:")
corr = df.dropna().corr(numeric_only = True)
#print("Votes correlate more strongly with revenue than ratings and metascore do with revenue. Showing that it is the opinion of the audience and note critics that determine a movies financial success.")
#print("Runtime is positively correlated with revenue and ratings, as well as negatively correlated with the ranking. Showing that movies with longer runtime are more successful and generate more income.")
#print("A negative correlation between ratings and the year seems to suggest that on average people are liking the movies that are being released less each year")
#print("It is clear that each category in the numerical data correlates one-to-one with itself.")
#print("The correlation between votes and ratings/metascore is positive but not strong. Showing that the general audience and critics don't entirely agree.")






















