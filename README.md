# image_caption_generation

A Python package for generating captions for images from both webpages and local images using Gradio and the Salesforce Bootstrapping Language-Image Pre-training (BLIP) model.

## Features

- **Webpage Image Scraping and Captioning**: Scrapes images from a given webpage URL, generates captions using the Salesforce BLIP model, and stores the results in a text file (`captions.txt`).
- **Local Image Captioning with Gradio**: Allows users to upload local images and generates captions for those images using the Gradio interface.
  
## Installation

### Prerequisites

- Python 3.8 or higher

### Clone the Repository

```bash
git clone https://github.com/tris02/image_caption_generation.git
cd image_caption_generation
```

### Install Dependencies
1. Set up a virtual environment (optional but recommended):

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

2. Install the package and its dependencies:

```bash
pip install -r requirements.txt
```

### Usage
The package provides two main functionalities: URL image scraping and local image captioning using Gradio.

1. Functionality 1: Scraping Images from a Webpage and Generating Captions. To scrape images from a webpage and generate captions, run the following command: 

```bash
python automate_url_captioner.py
```

This will scrape all the images from a given webpage URL and generate captions for each image. The results (image URLs and their corresponding captions) will be saved in `captions.txt`.

2. Functionality 2: Local Image Captioning Using Gradio. To caption local images through a web interface using Gradio, run the following command:

```bash
python image_captioning_app.py
```

This will launch a Gradio web interface in your browser where you can upload local images, and the model will generate captions for each uploaded image.

### Requirements

The package requires the following dependencies:

```
requests==2.31.0
beautifulsoup4==4.12.3
Pillow==10.4.0
torch==2.2.1
transformers==4.38.2
huggingface-hub==0.24.6
tokenizers==0.15.2
gradio==4.44.0
pytest==8.3.3
pydantic==2.9.1
langchain==0.1.11
```

### Testing
The package includes basic tests for the core functionality. You can run the tests using pytest:

```bash
pytest tests/
```
