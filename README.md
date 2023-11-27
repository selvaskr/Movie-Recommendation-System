# Movie-Recommendation-System
## Introduction:

I have developed a web application for a movie recommendation system using Django. I utilized the TMDB API for fetching movie posters and employed web scraping techniques with Beautiful Soup. 

The system showcases the latest upcoming and top-rated movies on the home page, creating an engaging and dynamic user interface.

## Dataset

For the dataset, I collected three datasets from Kaggle:

* The first dataset contains data from 1916 to 2016.(Upload in the Dataset Foider)
* The second dataset spans from 1816 to 2017.(Cannot upload to Dataset Folder due to Large size.)
  
  Dataset Link:
  
      https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv , 
      https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=credits.csv   
* The third dataset covers the years 2008 to 2021.(Upload in the Dataset Foider)
* Additionally, for the year 2022, movie data was scraped from Wikipedia using web scraping techniques, while genre information was obtained through the TMDB API.

## Pre-processing

Pre-processing was implemented in three different files for each dataset:

* In the pre-processing file for 1816 to 2017, the first two datasets were imported, and various pre-processing techniques were applied. These included removing duplicates based on movie names, extracting directors and the first three actor names from the cast and crew column, and eliminating records with null values.

* In the pre-processing file for 2008 to 2021, the third dataset was imported, and similar pre-processing techniques were applied. Additionally, an API was used to fetch movie genres, as a majority of records had genre information represented as null values.

* In the pre-processing file for 2022, web scraping techniques were employed to fetch movie details for the year 2022. Similar pre-processing techniques, as mentioned above, were applied, and the API was used to retrieve movie genres.


## Recommendation file:

I have imported the combined dataset and computed the cosine similarity matrix for the dataset. Due to the large size (10 GB) of the similarity matrix, it takes a considerable amount of time to run. Therefore, I have saved it as a pickle file. This way, every time the program runs, it can use the saved file instead of recomputing the cosine similarity.

❌❌ I have didnot upload the similarity matrix file due to its large size. ❌❌


# Installation:
* Clone this repository.
* Create a virtual environment.
* Activate the environment.
* Install the required dependencies with pip install -r requirements.txt.
* Run file the from the folder recommendsystem.[py manage.py runserver]

# Website Screenshots:

## Home Page
![image](https://github.com/selvaskr/Movie-Recommendation-System/assets/94179992/59f52fe0-1a81-4335-b7a7-397709cd190b)

## Recommendation Page 1
![image](https://github.com/selvaskr/Movie-Recommendation-System/assets/94179992/8a19ff71-91db-4368-8bc3-34be3f5e26d3)

## Recommendation Page 2
![image](https://github.com/selvaskr/Movie-Recommendation-System/assets/94179992/66fd386b-88b8-4b43-a89f-704172cdc065)


