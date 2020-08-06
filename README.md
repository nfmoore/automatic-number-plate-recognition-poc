# Automatic Number Plate Recognition Proof of Concept with Azure Cognitive Services

Automatic number-plate recognition is a technology that uses optical character recognition on images to read vehicle registration plates. This repository will illistrate how [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/#overview) can be used to develop such a solution.

[Custom Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/home) will be used to develop object detection model will be used to identify the coordinates of a vehicle's number plate in an image. This will be used to crop the image to focus on the number plate. The [Read API](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/concept-recognizing-text) will than use this cropped image to perform optical character recognition (OCR) to extract the number plate from the image.

## Getting Started

### Setup the Environment

Create a new conda environment from the [`environment.yml`](environment/environment.yml) file:

```bash
conda env create -f environment/environment.yml
```

Note: you must have installed [Anaconda](https://docs.anaconda.com/anaconda/install/).

### Download Images

Sample images have been sourced from [this](http://www.zemris.fer.hr/projects/LicensePlates/english/results.shtml) site from a database that contains over 500 images of the rear views of various vehicles (cars, trucks, busses), taken under various lighting conditions (sunny, cloudy, rainy, twilight, night light). This data will be used to train a custom vision object detection model and perform OCR.

To download these images execute [`download_images.py`](src/download_images.py) in your conda environment:

```bash
conda activate opencv
python src/download_images.py
```

Note: this will create a directory called `images`.

### Develop Custom Vision Model

To develop a custom vision model head over to [Custom Vision](https://www.customvision.ai) and use a subset of the images that have been downlaoded in the prior step. This can be done by:

1. Signing in and create a new project. Choose your own Name, Description and Resource (using your Azure subscription). Select `Object Detection` as the Project Type and leave the Domain as `General`.

2. Upload at least 15 images, select the number plate using the editor (give the number plate objects the same same e.g. `number-plate`).

3. Train a model once all images have been loaded. Once training is complete a set of performance metrics will be displayed. The `Quick Training` option should be sufficient for this step.

4. Published the trained model as a REST API. Publishing generates the URL and authentication key for this service. This will be used in the next step.

## Create Configuration File

Include the endpoints and access keys for the Custom Vision service and Computer Vision service in a file called `cognitive-services.ini` in a directory called `configuration`.

This file should be as follows:

```ini
[custom_vision]
key = <custom vision api key>
imgurl = <custom vision url (should end with /image)>

[computer_vision]
key = <computer vision api key>
url = <computer vision url>
```

### Run the Notebook

Open the jupyter notebook [`automatic-number-plate-recognition.ipynb`](src/automatic-number-plate-recognition.ipynb), choose and image and run the notebook. Ensure you run this notebook in the conda environment you created earlier.
