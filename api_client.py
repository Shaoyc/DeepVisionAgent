# api_client.py

import base64
from zhipuai import ZhipuAI
from config import API_KEY

client = ZhipuAI(api_key=API_KEY)

def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def infer_glm4v_flash(image_path, prompt):
    image_b64 = image_to_base64(image_path)
    response = client.chat.completions.create(
        model="glm-4v-flash",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}}
            ]
        }],
        temperature=0.1,
        max_tokens=512
    )
    return response.choices[0].message.content.strip()