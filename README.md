# yuja-dl

yuja-dl is a Python script that downloads videos from [YUJA](https://www.yuja.com/) to an mp4 file. 

## Dependencies

- Python 3
- ChromeDriver
- ffmpeg
- selenium-wire
- requests

## Installation

1. Clone this repository using `git clone https://github.com/eric-minassian/yuja-dl.git` .
2. Install the dependencies using `pip install -r requirements.txt` .
3. If using Mac OS, or Debian-based Linux, you are done. If using Windows, you will need to download the [ChromeDriver](https://chromedriver.chromium.org/downloads) and add it to your PATH. For Windows, you will also need to install [ffmpeg](https://ffmpeg.org/download.html) and add it to your PATH. Instructions for adding to PATH can be found [here](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)) .

## Usage

1. Run `python yuja-dl.py` .
2. Enter the URL of the video you want to download.
3. Once the video is downloaded, it will be saved in the ouput folder.