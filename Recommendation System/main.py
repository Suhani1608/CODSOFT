from src.data_loader import load_movie_data
from src.recommender import MovieRecommender

def main():
    print("--- Movie Recommendation System ---")
    
    # 1. Load Data
    df = load_movie_data()
    
    # 2. Initialize and Train the Recommender
    recommender = MovieRecommender(df)
    recommender.train()
    
    # 3. Test it out!
    print("\n--- System Ready ---")
    
    # You can change these titles to test different movies in the dataset
    test_movies = ["The Dark Knight", "Avatar", "The Avengers"]
    
    for movie in test_movies:
        print(f"\nIf you liked '{movie}', you might also like:")
        recommendations = recommender.get_recommendations(movie, top_n=5)
        
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")

if __name__ == "__main__":
    main()
