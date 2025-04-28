print("Welcome to AI-Powered Resume Analyzer!")
import nltk
import spacy

print("Welcome to AI-Powered Resume Analyzer!")

# Load English tokenizer, POS tagger, parser, NER, and word vectors
nlp = spacy.load('en_core_web_sm')

# Example Resume Text
resume_text = """
John Doe
Experienced Data Scientist with 5+ years in machine learning, Python programming, and data analysis.
"""

# Process the text
doc = nlp(resume_text)

# Extract Entities (like skills, names, etc.)
for ent in doc.ents:
    print(ent.text, ent.label_)





