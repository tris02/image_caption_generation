import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# URL of the page to scrape
url = "https://en.wikipedia.org/wiki/School"

# Define a user-agent header to avoid 403 errors
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Download the page with headers
response = requests.get(url, headers=headers)
# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all img elements
img_elements = soup.find_all('img')

# Open a file to write the captions
with open("captions.txt", "w") as caption_file:
    # Iterate over each img element
    for img_element in img_elements:
        img_url = img_element.get('src')

        # Skip if the image is an SVG, GIF, or too small (likely an icon)
        if img_url.endswith(('.svg', '.gif')) or '1x1' in img_url:
            continue

        # Correct the URL if it's malformed
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http://') and not img_url.startswith('https://'):
            continue  # Skip URLs that don't start with http:// or https://

        try:
            # Download the image with headers
            response = requests.get(img_url, headers=headers, timeout=5)  # Add headers and timeout
            response.raise_for_status()  # Raise an exception for bad responses

            # Check if the content is an image
            if 'image' not in response.headers.get('content-type', ''):
                print(f"Skipping non-image content: {img_url}")
                continue

            # Convert the image data to a PIL Image
            raw_image = Image.open(BytesIO(response.content))

            # Skip very small images
            if raw_image.size[0] * raw_image.size[1] < 400:
                continue

            raw_image = raw_image.convert('RGB')

            # Process the image
            inputs = processor(raw_image, return_tensors="pt")
            # Generate a caption for the image
            out = model.generate(**inputs, max_new_tokens=50)
            # Decode the generated tokens to text
            caption = processor.decode(out[0], skip_special_tokens=True)

            # Write the caption to the file, prepended by the image URL
            caption_file.write(f"{img_url}: {caption}\n")

        except UnidentifiedImageError:
            print(f"Skipping unsupported or corrupted image: {img_url}")
        except Exception as e:
            print(f"Error processing image {img_url}: {e}")
            continue
