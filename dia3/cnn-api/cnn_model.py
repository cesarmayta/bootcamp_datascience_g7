import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from pathlib import Path

model_save_path = Path(__file__).resolve().parent / "my_garbage_classifier_model.h5"
loaded_model = tf.keras.models.load_model(model_save_path)

def predict_class(image_path):
    classes = ['trash', 'glass', 'metal', 'plastic', 'cardboard', 'paper']
    img_size = (64, 64)
    img = image.load_img(image_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = loaded_model.predict(img_array, verbose=0)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_name = classes[predicted_class_index]
    return predicted_class_name
