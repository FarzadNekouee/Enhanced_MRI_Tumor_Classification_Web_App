# 🧠 Enhanced MRI Brain Tumor Classification Web App
![MRI Brain Tumor Classification](/cover_image/cover_image.png)


## 🔍 Overview
In this project, we have developed a machine learning model focused on accurately classifying MRI brain images into categories such as normal, pituitary tumor, meningioma tumor, and glioma tumor. Recognizing the critical need for precise diagnoses, especially in regions with limited access to high-quality medical imaging, this model is fine-tuned to perform exceptionally well on both high-quality and low-quality images. This approach ensures robust generalization and broad utility in various healthcare environments. Beyond the model development, a significant part of this project involves the implementation of a Web Application. Utilizing Streamlit, we have deployed the trained model into an interactive web app, enabling users to upload MRI images and receive instant classification results. To ensure easy and reliable deployment, the entire application has been containerized using Docker. This approach simplifies the process of setting up the app in different environments, making it accessible and easy to use, regardless of the underlying platform. 


## 🎯 Objectives
Key milestones accomplished in this project include:

- **Dataset Exploration:** Delving into the dataset to understand class distribution and image dimensions, setting the stage for tailored model development.

- **Augmentation with Artificially Degraded Images:** Implementing image degradation techniques to simulate low-quality MRIs, enhancing the model's robustness and its performance in varied medical imaging environments.

- **Transfer Learning with ResNet50V2:** Adopting the ResNet50V2 pre-trained model to leverage its high accuracy and prevent overfitting, despite a modest dataset size.

- **Focused Model Training and Fine-Tuning:** Precisely training and fine-tuning the model to ensure reliable classification of MRI brain images into normal, pituitary tumor, meningioma tumor, and glioma tumor categories.

- **Validation Performance Assessment:** Thoroughly evaluating the model on a validation set with various performance metrics to confirm its reliability and accuracy.

- **Web Application Development and Deployment:** Creating an interactive Streamlit-based web application to demonstrate the model's capabilities in a user-friendly interface, enabling MRI image classification.

- **Containerization with Docker:** Streamlining the app deployment process using Docker, ensuring easy setup and consistent performance across different platforms, enhancing accessibility and usability.


## 📚 Dataset Description
The dataset comprises MRI images classified into four distinct categories, each representing different brain conditions. Here is a summary of the dataset's composition:

- **Normal:** Represents healthy brain images without any tumor, totaling 438 images, accounting for 14.15% of the dataset.
- **Glioma Tumor:** Images showing glioma tumors, with 901 images making up 29.10% of the dataset.
- **Meningioma Tumor:** Images indicating meningioma tumors, consisting of 913 images, which is 29.49% of the dataset.
- **Pituitary Tumor:** Depicts pituitary tumors, with 844 images, constituting 27.26% of the dataset.

The entire dataset consists of 3,096 MRI images, providing a comprehensive view for training and validating the brain tumor classification model. Below is a visual representation of sample images from each class, illustrating the variety and complexity of the MRI scans that the model will be trained on:

![Sample MRI Images](/cover_image/dataset_overview.png)


## 📁 File Descriptions

- **`Enhanced_MRI_Brain_Tumor_Classification.ipynb`**: The Jupyter notebook detailing the methodology, from initial data analysis to final model training.
- **`app.py`**: The Streamlit application script for the interactive web app, which uses the trained model to classify MRI images.
- **`Dockerfile`**: Contains the necessary commands to assemble the Docker image for running the Streamlit web app.
- **`requirements.txt`**: Lists all the Python dependencies required for running the web app.
- **`model/`**: The directory where the [trained model file](https://drive.google.com/file/d/1YAYTEHoAS0xkPjw_IJpvxsngHjyd5ST6/view?usp=sharing) is stored, ready to be used by the web app.
- **`demo.gif`**: A GIF demonstration showcasing the web app in action, providing a visual guide on how users can interact with it.
- **`cover_image/`**: Contains images used throughout the README.md for visual aid and project representation.
- **`test_images/`**: A collection of MRI images from the validation set used to demonstrate the model's predictive capabilities.
- **`LICENSE`**: The MIT License under which this project is released, detailing the terms under which it can be freely used and distributed.
- **`README.md`**: This documentation provides an overview, objectives, and essential information about the project.


## 🚀 Instructions for Local Execution

To run the Enhanced MRI Brain Tumor Classification Web App on your local machine, follow these steps:  

1. **Clone the Repository**: Begin by cloning the project repository to your local machine using the command:
    ```bash
    git clone https://github.com/FarzadNekouee/Enhanced_MRI_Tumor_Classification_Web_App.git
    ```

2. **Navigate to the Project Directory**: Change into the project directory:
    ```bash
    cd Enhanced_MRI_Tumor_Classification_Web_App
    ```

3. **Download the Pre-trained Model**: The pre-trained model is available on Google Drive. Download it by clicking [here](https://drive.google.com/file/d/1YAYTEHoAS0xkPjw_IJpvxsngHjyd5ST6/view?usp=sharing) and place it in the `model` directory within the cloned repository.

4. **Prepare Docker Environment**: Verify that Docker is operational on your machine. To construct the Docker image for the app, execute the following command in your project directory:
    ```bash
    docker build -t mri-tumor-streamlit-app .
    ```
   In case you face any issues with Docker Hub access, such as a '403 Forbidden' error, first pull the base Python image using this command:
    ```bash
    docker pull python:3.9-slim
    ```
   Once the base image is successfully pulled, retry building the app image.
    
5. **Run the Streamlit App**: Start the Streamlit app in a Docker container by executing the following command:
    ```bash
    docker run -p 8080:8080 mri-tumor-streamlit-app
    ```
    Note: Replace `8080` with your preferred port if necessary.

6. **Access the Web App**: Open your web browser and visit `http://localhost:8080` to interact with the MRI Brain Tumor Classification Web App. A demo of the app in action is available below:


![Web App Demo](demo.gif)

Enjoy exploring the app and classifying MRI brain images!


## 🔗 Additional Resources

- 🌐 **Kaggle Notebook**: Interested in a Kaggle environment? Explore the notebook [here](https://www.kaggle.com/code/farzadnekouei/enhanced-mri-brain-tumor-classification).
- 🌐 **Dataset Source**: Available on [Kaggle](https://www.kaggle.com/datasets/susandaneshmand/mri-images).
- 🤝 **Connect on LinkedIn**: Have questions or looking for collaboration? Let's connect on [LinkedIn](https://linkedin.com/in/farzad-nekouei-7535aa53/).