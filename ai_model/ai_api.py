# Import required libraries
from fastapi import FastAPI, File, UploadFile, Form
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from pathlib import Path
import shutil

# Create FastAPI app
app = FastAPI()

# Step 1: Load trained model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "smart_aid_model.h5"

print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully!")

# Class labels (same order as training)
class_names = ["moderate", "normal", "severe"]


# Step 2: BMI calculation
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi_value = weight_kg / (height_m * height_m)
    return bmi_value


# Step 3: BMI category
def get_bmi_category(bmi):
    if bmi < 14:
        return "severe"
    elif bmi < 18:
        return "moderate"
    else:
        return "normal"


# Step 4: Prediction API
@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    height: float = Form(...),
    weight: float = Form(...)
):
    try:
        # Save uploaded image temporarily
        temp_file = Path("temp.jpg")
        with open(temp_file, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Load and preprocess image
        img = image.load_img(temp_file, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0

        # Model prediction
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_class = class_names[predicted_index]
        confidence = float(np.max(prediction) * 100)

        # BMI calculation
        bmi_value = calculate_bmi(height, weight)
        bmi_category = get_bmi_category(bmi_value)

        # Final decision logic
        if predicted_class != bmi_category:
            final_result = "Possible Risk - Further Check Needed"
        else:
            final_result = f"Confirmed {predicted_class.capitalize()}"

        # Final response
        return {
            "image_prediction": predicted_class,
            "confidence": round(confidence, 2),
            "bmi": round(bmi_value, 2),
            "bmi_result": bmi_category,
            "final_result": final_result
        }

    except Exception as error:
        return {"error": str(error)}