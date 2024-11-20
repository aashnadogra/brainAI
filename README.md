# brainAI
**brainAI** is an advanced web application designed to assist in the detection of brain tumors using medical images, specifically MRI scans. The project combines state-of-the-art deep learning techniques, including **Convolutional Neural Networks (CNN)** for tumor classification and **Generative Adversarial Networks (GANs)** for data augmentation, to enhance the accuracy and reliability of predictions. Additionally, the application integrates **Explainable AI (XAI)** methods to provide interpretable and transparent model predictions, making it especially valuable for healthcare professionals.

## Key Features

- **Brain Tumor Detection:**  
  The core functionality of the application is its ability to analyze brain MRI images and classify them as either containing a tumor or not and detect which type of tumor. Using deep learning models like CNNs, the application is trained on a large dataset of brain scans to detect abnormalities indicative of tumors.

- **Data Augmentation with GANs:**  
  To improve the model's generalization and robustness, the application utilizes **Generative Adversarial Networks (GANs)** for data augmentation. This technique helps to artificially generate additional training data, especially in situations where the dataset might be limited, leading to improved model performance.

- **Explainable AI (XAI):**  
  The application includes **XAI** features to explain the reasoning behind the model's predictions. Using techniques such as **Grad-CAM (Gradient-weighted Class Activation Mapping)**, it highlights the regions in the brain MRI images that were most influential in the model's decision, offering transparency and aiding medical professionals in trusting and understanding the predictions.

- **Web Interface:**  
  BrainAI provides a user-friendly web interface built using **Flask**, where users can upload brain MRI images for analysis. The model processes the uploaded image, makes a prediction, and displays both the result and a visual explanation (heatmap) of the decision-making process.

## How It Works

1. **Image Upload and Prediction:**  
   Users can upload MRI scans of the brain, and the model will process the image, output a prediction (e.g., whether a tumor is present), and display the result in a web interface.

2. **Model Explanation:**  
   Alongside the prediction, the application uses **XAI** methods to explain which areas of the image the model focused on while making its decision. This is achieved using visual explanations like heatmaps or Grad-CAM, ensuring that medical professionals can interpret the model's reasoning.

3. **Data Augmentation:**  
   GANs are employed to augment the training dataset. The GAN generates synthetic images that resemble real MRI scans, effectively expanding the dataset without requiring new data collection. This technique helps the model learn more diverse features and generalize better to unseen data.

4. **Model Training and Evaluation:**  
   The model is trained on a dataset of brain MRI images, and its performance is continuously evaluated to ensure high accuracy. The training process also incorporates augmentation to ensure the model can handle various image conditions.

5. **Deploying as a Web Application:**  
   Once the model is trained and ready, it is deployed in a web application using Flask. Users can easily interact with the system by uploading images, receiving predictions, and viewing model explanations in a web browser.


## Technologies Used

- **Flask** for the web framework.
- **TensorFlow / Keras** for implementing the deep learning model (CNN).
- **GAN (Generative Adversarial Networks)** for data augmentation.
- **Grad-CAM** for visual explanation of model predictions.
- **OpenCV** and **PIL** for image processing.
- **HTML/CSS/JS** for the front-end user interface.

