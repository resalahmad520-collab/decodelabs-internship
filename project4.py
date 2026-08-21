import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

model = MobileNetV2(weights="imagenet")

img_path = "sample.jpg"

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)

img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

predictions = model.predict(img_array)

results = decode_predictions(predictions, top=3)[0]

print("Image Recognition Results:")
print("--------------------------")

for _, label, confidence in results:
    print(f"{label}: {confidence * 100:.2f}%")