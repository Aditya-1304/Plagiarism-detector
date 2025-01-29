# Plagiarism Detector

This project is a plagiarism detector that uses various libraries to analyze and compare text. Follow the instructions below to set up the necessary dependencies.

## Installation

To get started, you need to install the following Python libraries:

1. **torch**
2. **nltk**
3. **sentence-transformers**
4. **fuzzywuzzy**

### Step-by-Step Guide

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/plagiarism-detector.git
   cd plagiarism-detector
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required libraries:**

   ```bash
   pip install torch nltk sentence-transformers fuzzywuzzy
   ```

4. **Download NLTK data:**

   Open a Python shell and run the following commands to download the necessary NLTK data:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

Once you have installed the dependencies, you can run the plagiarism detector script:

```bash
python detect_plagiarism.py
```

Make sure to replace `detect_plagiarism.py` with the actual script name if it's different.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
