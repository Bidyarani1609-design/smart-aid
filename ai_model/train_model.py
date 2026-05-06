# Import required libraries
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model

# Step 1: Define dataset path
train_path = r"D:\Ai workspace\smart-aid\dataset\train"

# Step 2: Image preprocessing (rescale + augmentation)
image_gen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2,
    rotation_range=15,
    zoom_range=0.1,
    horizontal_flip=True
)

# Training data
train_data = image_gen.flow_from_directory(
    train_path,
    target_size=(224, 224),
    batch_size=8,
    class_mode='categorical',
    subset='training'
)

# Validation data
val_data = image_gen.flow_from_directory(
    train_path,
    target_size=(224, 224),
    batch_size=8,
    class_mode='categorical',
    subset='validation'
)

# Step 3: Load pre-trained ResNet50 model
base_model = ResNet50(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base layers (so we don't retrain whole model)
for layer in base_model.layers:
    layer.trainable = False

# Step 4: Add custom layers on top
x = base_model.output
x = Flatten()(x)
x = Dense(128, activation='relu')(x)

# Final output layer (3 classes)
predictions = Dense(3, activation='softmax')(x)

# Create final model
model = Model(inputs=base_model.input, outputs=predictions)

# Step 5: Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Step 6: Train model
print("Training started...\n")

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

print("\nTraining completed!")

# Step 7: Save trained model
model.save("smart_aid_model.h5")

print("Model saved as smart_aid_model.h5")