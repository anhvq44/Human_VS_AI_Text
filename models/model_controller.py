import pickle
import numpy as np
from keras import models
from keras.preprocessing.sequence import pad_sequences

MODEL_PATH = "models/alp.h5"
TOKENIZER_PATH = "models/tokenizer.pickle"
MAX_LEN = 4405

_model = None
_tokenizer = None

def load_model():
    global _model
    
    if _model is None:
        _model = models.load_model(MODEL_PATH)
 
    return _model

def load_tokenizer():
    global _tokenizer
    
    if _tokenizer is None:
        with open('models/tokenizer.pickle', 'rb') as handle:
            _tokenizer = pickle.load(handle)
            
    return _tokenizer

def preprocess(text):
    tokenizer = load_tokenizer()
    text_seq = tokenizer.texts_to_sequences([text])
    text_padded = pad_sequences(text_seq, maxlen=MAX_LEN, padding="post", truncating="post")
    return text_padded

def predict(text):
    if not text or not text.strip():
        raise ValueError("Input text must not be empty.")
 
    model = load_model()
    padded   = preprocess(text)
 
    ai_prob    = float(model.predict(padded, verbose=0)[0][0])
    human_prob = 1.0 - ai_prob
 
    label      = "AI Generated" if ai_prob >= 0.5 else "Human Written"
    confidence = ai_prob if ai_prob >= 0.5 else human_prob
    
    return {
        "label": label,
        "confidence": round(confidence, 4),
        "ai_prob": round(ai_prob, 4),
        "human_prob": round(human_prob, 4),
    }
    
def predict_batch(texts):
    if not texts:
        return []
    
    model = load_model()
    tokenizer = load_tokenizer()
    
    seqs   = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(seqs, maxlen=MAX_LEN, padding="post", truncating="post")
    
    raw_probs = model.predict(padded, verbose=0).flatten()
    
    results = []
    for ai_prob in raw_probs:
        human_prob = 1.0 - ai_prob
        label      = "AI Generated" if ai_prob >= 0.5 else "Human Written"
        confidence = ai_prob if ai_prob >= 0.5 else human_prob
        results.append({
            "label":      label,
            "confidence": round(float(confidence), 4),
            "ai_prob":    round(float(ai_prob), 4),
            "human_prob": round(float(human_prob), 4),
        })
 
    return results

