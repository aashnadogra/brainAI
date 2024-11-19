from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from io import BytesIO

app = Flask(__name__)

model = tf.keras.models.load_model('prediction/brain_tumor_classifier.h5')

# Define class labels (ensure 'notumor' is in the last position for easy checking)
class_labels = ['glioma', 'meningioma', 'pituitary', 'notumor']

# Confidence threshold for detecting unknown tumors
CONFIDENCE_THRESHOLD = 0.50

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resnet')
def resnet():
    return render_template('resnet.html')

@app.route('/vgg')
def vgg():
    return render_template('vgg.html')

@app.route('/gans')
def gans():
    return render_template('gans.html')

@app.route('/detection')
def detection():
    return render_template('detection.html')

@app.route('/gan_dataset')
def gan_dataset():
    return render_template('gan_dataset.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded!', 400

    file = request.files['file']

    # Read the image file and convert it to a format suitable for keras
    img = image.load_img(BytesIO(file.read()), target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    predictions = model.predict(img_array)
    predicted_probabilities = predictions[0]
    max_probability = np.max(predicted_probabilities)
    predicted_class_index = np.argmax(predicted_probabilities)
    predicted_class_label = class_labels[predicted_class_index]

    # Check for 'notumor' class or low confidence
    if predicted_class_label == 'notumor':
        result = f'No tumor detected with confidence: {max_probability * 100:.2f}%'
    
    elif max_probability < CONFIDENCE_THRESHOLD:
        result = f'Tumor detected, but type is not in trained classes. Confidence: {max_probability * 100:.2f}%'
    
    else:
        result = f'Tumor detected: {predicted_class_label} with confidence: {max_probability * 100:.2f}%'

    return render_template('detection_output.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
