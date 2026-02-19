import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"
class_labels = model.classes_.tolist()

def predict_output(input_df: pd.DataFrame):

    # predict the class
    predict_class = model.predict(input_df)[0]

    # Get the probability of all the classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predict_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }