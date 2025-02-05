# # main.py

# from utils.data_loader import load_titles
# from models.plagiarism_model import PlagiarismModel

# def main():
#     # Load the dataset from the JSON file (adjust the path if necessary)
#     dataset = load_titles('data/titles_with_ids.json')
    
#     # Extract the list of titles from the dataset
#     titles = [record['title'] for record in dataset]
    
#     # Initialize and train the plagiarism detection model
#     model = PlagiarismModel()
#     model.fit(titles)
    
#     # Prompt the user to enter a title to check
#     print("Enter a title to check for plagiarism similarity:")
#     new_title = input().strip()
    
#     # Get the maximum similarity score and the indices of the most similar t
#     titles
#     score, indices = model.predict(new_title)
#     print(f"\nPlagiarism Score (max similarity): {score:.2f}")
    
#     print("\nMost similar title(s) from the dataset:")
#     for idx in indices:
#         print(f" - {titles[idx]}")
    
#     # Optionally, display all titles with similarity above a threshold (e.g., 0.5)
#     threshold = 0.5
#     similar_titles = model.get_similar_titles(new_title, threshold=threshold)
#     print(f"\nTitles with similarity >= {threshold}:")
#     for title, sim in similar_titles:
#         print(f" - {title} (score: {sim:.2f})")

# if __name__ == '__main__':
#     main()

from utils.data_loader import load_titles
from models.plagiarism_model import PlagiarismModel
import os
from joblib import dump, load

MODEL_PATH = 'data/trained_model.joblib'

def main():
    # Check if we have a trained model
    if os.path.exists(MODEL_PATH):
        print("Loading trained model...")
        model_data = load(MODEL_PATH)
        model = PlagiarismModel()
        model.vectorizer = model_data['vectorizer']
        model.titles = model_data['titles']
        model.title_vectors = model_data['vectors']
    else:
        print("Training new model...")
        # Load the dataset from the JSON file
        dataset = load_titles('data/titles_with_ids.json')
        titles = [record['title'] for record in dataset]
        
        # Initialize and train the plagiarism detection model
        model = PlagiarismModel()
        model.fit(titles)
        
        # Save the trained model
        dump({
            'vectorizer': model.vectorizer,
            'titles': model.titles,
            'vectors': model.title_vectors
        }, MODEL_PATH)

    # Rest of your code remains the same
    print("Enter a title to check for plagiarism similarity:")
    new_title = input().strip()
    
    score, indices = model.predict(new_title)
    print(f"\nPlagiarism Score (max similarity): {score:.2f}")
    
    print("\nMost similar title(s) from the dataset:")
    for idx in indices:
        print(f" - {model.titles[idx]}")
    
    threshold = 0.5
    similar_titles = model.get_similar_titles(new_title, threshold=threshold)
    print(f"\nTitles with similarity >= {threshold}:")
    for title, sim in similar_titles:
        print(f" - {title} (score: {sim:.2f})")

if __name__ == '__main__':
    main()