## Image Alignment using pytesseract and WandImage


**Requirements**

You need to install [tesseract-ocr](https://github.com/tesseract-ocr/tesseract)

For Debian and Ubuntu based distros

`sudo apt install tesseract-ocr`

2. Create a virtualenv and install the required modules

`python3 -m pip install --user virtualenv`

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`


## Server

`python3 app/app.py`

Runs flask server in debug mode


## Usage

1. You can go to `localhost:5000` and upload the image

2. Use Curl

`curl -F "image=@/path/to/img" localhost:5000/alignment`

3. Download image with wget

```
 wget $(curl -F "image=@/path/to/image" localhost:5000/alignment | jq -r '.data')

```

The images are saved in `server/output/` folder.

