# models/plagiarism_model.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class PlagiarismModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.title_vectors = None
        self.titles = []  # This will store the raw titles

    def fit(self, titles):
        """
        Fit the model on a list of titles.

        Args:
            titles (list of str): The training titles.
        """
        self.titles = titles
        self.title_vectors = self.vectorizer.fit_transform(titles)

    def predict(self, new_title):
        """
        Given a new title, compute its cosine similarity with the dataset titles.
        
        Args:
            new_title (str): The title to check.
        
        Returns:
            tuple: A tuple containing:
                - max_sim (float): The maximum cosine similarity score.
                - similar_indices (ndarray): Indices of titles with the maximum similarity.
        """
        new_vec = self.vectorizer.transform([new_title])
        sims = cosine_similarity(new_vec, self.title_vectors)
        max_sim = np.max(sims)
        similar_indices = np.where(sims[0] == max_sim)[0]
        return max_sim, similar_indices

    def get_similar_titles(self, new_title, threshold=0.5):
        """
        Retrieve all titles from the dataset that have a similarity above the given threshold.

        Args:
            new_title (str): The title to check.
            threshold (float): The similarity threshold.
        
        Returns:
            list of tuple: A list of tuples where each tuple contains a title and its similarity score.
        """
        new_vec = self.vectorizer.transform([new_title])
        sims = cosine_similarity(new_vec, self.title_vectors)
        similar_titles = []
        for idx, sim in enumerate(sims[0]):
            if sim >= threshold:
                similar_titles.append((self.titles[idx], sim))
        return similar_titles
