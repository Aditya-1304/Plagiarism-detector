# titles/utils.py
import string

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util
from fuzzywuzzy import fuzz

# Initialize transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def preprocess_title(title):
    # Implement your preprocessing logic here
    return title.lower()

def compute_similarity(new_title, existing_titles):
    # Implement your similarity computation logic here
    # For demonstration, return dummy values
    cosine_sim = [0.5] * len(existing_titles)
    fuzzy_sim = [0.7] * len(existing_titles)
    return cosine_sim, fuzzy_sim