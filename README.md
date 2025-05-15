# Real-Time Translation of Road Signs
Victoria Chan's final year project (31012194)

## About
Real-time translation of road signs project to take in an input image of a full road scene and return a translated description of all detected road signs to the user.

**Notice**: System was coded in the Anaconda environment on a Macbook Pro M1, with 8gb RAM, on MacOS Sequoia (15.4.1). No Windows testing has been done.

## Setup
`git clone` this repository, it is recommended the folder this is cloned into has the same name

Unless specified, do not rename folders otherwise loading issues may occur when executing the full pipeline.

**Datasets:**
No dataset is included in this git repository due to large folder sizes. They should be installed and renamed accordingly:
- [GTSRB](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) - download folders: "Meta", "Train", "Test", files: "Meta.csv", "Train.csv", "Test.csv", place into one folder and rename to "gtsrb-data"
- [GTSDB](https://sid.erda.dk/public/archives/ff17dc924eba88d5d01a807357d6614c/published-archive.html) - download zip file "FullIJCNN2013.zip" and rename the folder to "gtsdb-data". Before running anything else, run the "gtsdb_yolo.py" file to convert GTSDB to YOLO format. These can be used to test the system due to YOLO not taking images in PPM format.

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