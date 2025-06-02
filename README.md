# Real-Time Translation of Road Signs
Victoria Chan's final year project

## About
Real-time translation of road signs project to take in an input image of a full road scene and return a translated description of all detected road signs to the user.

**Notice**: System was coded in the Anaconda environment on a Macbook Pro M1, with 8gb RAM, on MacOS Sequoia (15.4.1). iPhone 16 Pro running iOS 18.3 was the primary mobile application simulator. No Windows testing has been done.

## Setup
`git clone` this repository, it is recommended the folder this is cloned into has the same name

Unless specified, do not rename folders otherwise loading issues may occur when executing the full pipeline.

**Datasets:**
No dataset is included in this git repository due to large folder sizes. They should be installed and renamed accordingly:
- [GTSRB](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) - download folders: "Meta", "Train", "Test", files: "Meta.csv", "Train.csv", "Test.csv", place into one folder and rename to "gtsrb-data"
- [GTSDB](https://sid.erda.dk/public/archives/ff17dc924eba88d5d01a807357d6614c/published-archive.html) - download zip file "FullIJCNN2013.zip" and rename the folder to "gtsdb-data". Before running anything else, run the "gtsdb_yolo.py" file to convert GTSDB to YOLO format. These can be used to test the system due to YOLO not taking images in PPM format.

As well as renaming the folder, both folders should be placed into one folder called "datasets".
Example: "fyp-victoria-chan/datasets/gtsrb-data/" should contain all the data downloaded from the Kaggle GTSRB dataset

**Dependencies:**
`pip install requirements.txt`

## Running the program
**On MacOS:**
- Open terminal
- Go to the directory "fyp-victoria-chan" if the folder name isn't different
- Enter `./startup.sh`
- Do not click anything until the app is running

**On any other OS:**
- As I do not have access to another device, I have not tested running the program on another device. It is recommended to run the program on a MacOS device that has XCode installed as all coding and testing has been done on MacOS.

## Understanding the directory
**Key files/folders:**
- datasets/ - all datasets
- py-files/ - all python scripts and backend related files
    - detection-results/ - all results from running "detection.py" are stored here
    - models/ - contains both the CNN and YOLOv8 models
    - cropping.py - crops road signs from full scenes
    - descriptions.py - dictionary mapping each class to a description
    - full_pipeline.py - when executed, runs the full backend pipeline (input, detection, cropping, classification, translation, output)
    - gtsdb_yolo.py - converts raw GTSDB data to YOLO format
    - gtsdb.yaml - used to train YOLOv8 model
    - lang_codes.md - full list of languages, and their associated language code, that are supported by LibreTranslate
    - load_data.py - load data from GTSRB to train or test CNN model
    - main.py - used to connect backend to frontend with Flask API
    - model.py - define the CNN architecture and compile parameters
    - testing.py - used to test the CNN model only
    - training.py - used to train the CNN model
    - translate.py - translates text into another language
- road-sign-translator/ - React + Expo mobile application
