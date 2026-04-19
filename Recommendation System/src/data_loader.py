import os
import pandas as pd
import kagglehub

def load_movie_data():
    """
    Downloads the TMDB 5000 dataset via Kaggle API and loads it into a Pandas DataFrame.
    """
    print("Fetching TMDB movie dataset...")
    # Downloads to a local cache automatically
    path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
    csv_path = os.path.join(path, "tmdb_5000_movies.csv")
    
    print("Loading data into Pandas...")
    df = pd.read_csv(csv_path)
    
    # We only need the title and the plot description (overview)
    df = df[['title', 'overview']]
    
    # Drop any movies that don't have a plot description
    df['overview'] = df['overview'].fillna('')
    
    print(f"Successfully loaded {len(df)} movies.")
    return df
