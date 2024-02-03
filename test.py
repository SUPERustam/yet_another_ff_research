# Imports
import requests
import os
import mimetypes
import httpx
import asyncio


# Absolute path
absolute_path = os.path.dirname(__file__)

api_key = "pipeline_sk_f6cLHs3LUKObckk7z9bEzM4Jbu0aDIGY"

# Headers
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {api_key}"
}


async def upload_img(path: str) -> tuple:
    upload_url = "https://www.mystic.ai/v4/files"
    img_name = os.path.basename(path)
    mime = mimetypes.guess_type(path)[0]
    if img_name[-4:] == "webp":
        mime = "image/webp"

    if not os.path.exists(path):
        raise FileNotFoundError(f"No file found at {path}")

    if not mime:
        raise ValueError(f"Could not determine MIME type for file {path}")

    async with open(path, "rb") as img_file:
        files = {"pfile": (img_name, img_file, mime)}
        headers = {
            "accept": "application/json",
            "authorization": "Bearer pipeline_sk_iIGN0tU7Jifjdmycp-gOVoqJyYjLAVQA"
        }
        response = httpx.post(upload_url, files=files, headers=headers)
        return response.json()["id"], response.json()["path"]

# define with lang as optional argument


async def run_inference(img_path: str, lang: str) -> str:
    try:
        m_id, m_path = await upload_img(img_path)
    except Exception as e:
        print("An error occurred while uploading the image:")
        print(str(e))

    # Debug print
    # print(f"File ID: {m_id}, File path: {m_path}")

    # URL for the API endpoint
    url = 'https://www.mystic.ai/v4/runs'

    m_path = "https://storage.mystic.ai/" + m_path
    # Data payload for the POST request
    data = {
        "pipeline": "uriel/easyocr-r:v31",
        "inputs": [
            {
                "type": "file",
                "file_path": m_path
            },
            {
                "type": "string",
                "value": lang
            }
        ]
    }

    # Sending the POST request
    print("Running inference...")
    print(data)

    response = httpx.post(url, json=data, headers=headers)
    # Checking the response

    if response.status_code == 200:
        print("Request successful")
    else:
        print("Request failed")
        print("Status code:", response.status_code)
        print("Response:", response.text)

    return response.json()


path = absolute_path + "/images/test_images/rus1.png"
print(asyncio.run(run_inference(path, "ru")))
