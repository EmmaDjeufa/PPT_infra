#dalle.py
from urllib.parse import quote

def generate_image(prompt):
    image_url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    return {
        "error": False,
        "image_url": image_url
    }