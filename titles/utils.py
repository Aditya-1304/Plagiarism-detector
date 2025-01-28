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
    stop_words = set(stopwords.words('english'))
    title = title.lower().translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(title)
    return [word for word in words if word not in stop_words]

def compute_similarity(new_title, existing_titles):
    # Use both fuzzy matching and semantic similarity
    embeddings = model.encode([new_title] + existing_titles, convert_to_tensor=True)
    cosine_sim = util.cos_sim(embeddings[0], embeddings[1:])
    fuzzy_sim = [fuzz.ratio(new_title, t) for t in existing_titles]
    
    return cosine_sim, fuzzy_sim
