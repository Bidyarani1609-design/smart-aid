import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from pathlib import Path  


# Load trained model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "smart_aid_model.h5"

model = tf.keras.models.load_model(MODEL_PATH)

# Class labels (IMPORTANT - same order as training)
class_names = ['moderate', 'normal', 'severe']

# Function to calculate BMI
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m * height_m)
    return bmi

# BMI based risk
def bmi_risk(bmi):
    if bmi < 14:
        return "Severe"
    elif bmi < 18:
        return "Moderate"
    else:
        return "Normal"

# Prediction function
def predict_image(img_path, height, weight):
    
    # Load image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Model prediction
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # BMI calculation
    bmi = calculate_bmi(height, weight)
    bmi_result = bmi_risk(bmi)

    # Final result
    print("\n--- RESULT ---")
    print("Image Prediction:", predicted_class)
    print("Confidence: {:.2f}%".format(confidence))
    print("BMI:", round(bmi, 2), "-", bmi_result)

# Test run
TEST_IMAGE = Path(__file__).resolve().parent / "test.jpg"
predict_image(TEST_IMAGE, 120, 20)