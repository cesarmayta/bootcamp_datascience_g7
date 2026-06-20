import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# 1 . defino variables
model_save_path = "my_garbage_classifier_model.h5"
clasess = ['trash', 'glass', 'metal', 'plastic', 'cardboard', 'paper']

# 2. Load the model
loaded_model = tf.keras.models.load_model(model_save_path)
print("Modelo cargado exitosamente.")

# 3. Prepare the image for prediction
image_path = 'plastic_02566.jpg'
img_size = (64, 64) # Ensure this matches the target_size used in ImageDataGenerator

# Load the image
img = image.load_img(image_path, target_size=img_size)

# Convert the image to a numpy array
img_array = image.img_to_array(img)

# Rescale the image (same as train_data.rescale=1./255)
img_array = img_array / 255.0

# Add a batch dimension (model expects a batch of images)
img_array = np.expand_dims(img_array, axis=0)

# 4. Make a prediction
predictions = loaded_model.predict(img_array, verbose=0)

# Get the predicted class index
predicted_class_index = np.argmax(predictions[0])

# Map the index to the class name
predicted_class_name = classes[predicted_class_index]

print(f"\nLa imagen '{os.path.basename(image_path)}' es predicha como: {predicted_class_name}")
print(f"Probabilidades de predicción: {predictions[0]}")

# 5. Display the image and prediction
plt.figure(figsize=(4, 4))
plt.imshow(img) # Display the loaded PIL image
plt.title(f'Predicción: {predicted_class_name}', fontsize=12)
plt.axis('off')
plt.show()