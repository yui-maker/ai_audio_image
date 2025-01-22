import os
import base64
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    print("OpenAI API Key not set")
    
MODEL = "gpt-4o-mini"
openai = OpenAI()

def image_generator(style = "Pop Art"):
    image_response = openai.images.generate(
            model="dall-e-3",
            prompt=f"Finnish winter. In {style} style.",
            size="1024x1024",
            n=1,
            response_format="b64_json",
        )
    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))

image = image_generator("Street Art/Graffiti")
image.show()