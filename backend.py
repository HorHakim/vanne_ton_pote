import base64
import requests
import os
from mistralai import Mistral
import io
from dotenv import load_dotenv
load_dotenv()


def convert_image(image):


    # Convertir l'image en bytes via un buffer
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")  # Change "JPEG" selon ton format si besoin (ex: "PNG")
    img_bytes = buffered.getvalue()

    # Encoder en base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    # Afficher le résultat
    return img_base64




def vanne_mon_pote(image):

    base64_image = convert_image(image)

    # Retrieve the API key from environment variables
    api_key = os.environ["MISTRAL_KEY"]

    # Specify model
    model = "pixtral-12b-2409"

    # Initialize the Mistral client
    client = Mistral(api_key=api_key)

    # Define the messages for the chat
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Tu es un pote un peu moqueur mais gentil. Tu viens de voir une photo de mon ami. En te basant uniquement sur cette image, fais-lui une vanne marrante mais pas méchante. Sois créatif, style vanne de pote, comme à la récré. Une phrase ou deux max."
                },
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}" 
                }
            ]
        }
    ]

    # Get the chat response
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )

    # Print the content of the response
    return chat_response.choices[0].message.content