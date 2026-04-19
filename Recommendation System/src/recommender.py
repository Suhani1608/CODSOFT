from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class MovieRecommender:
    def __init__(self, df):
        self.df = df.reset_index(drop=True)
        self.cosine_sim = None
        self.indices = pd.Series(self.df.index, index=self.df['title']).drop_duplicates()

    def train(self):
        """
        Converts text plots into TF-IDF vectors and calculates the similarity matrix.
        """
        print("Extracting features and training the recommender...")
        # Remove English stop words (the, a, and, etc.)
        tfidf = TfidfVectorizer(stop_words='english')
        
        # Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(self.df['overview'])
        
        # Compute the cosine similarity matrix
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        print("Training complete!")

    def get_recommendations(self, title, top_n=5):
        """
        Takes a movie title and returns the top_n most similar movies.
        """
        if title not in self.indices:
            return f"Movie '{title}' not found in the dataset."

        # Get the index of the movie that matches the title
        idx = self.indices[title]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top most similar movies (ignoring the movie itself)
        sim_scores = sim_scores[1:top_n+1]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top most similar movies
        return self.df['title'].iloc[movie_indices].tolist()
