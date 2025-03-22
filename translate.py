# translate.py
# Translate descriptions into target language
# Full list of language codes in "lang_codes.txt"
# Run "libretranslate" in terminal before running script

import requests
import json
from descriptions import DESCRIPTIONS

# Translate text
def translate_text(text, target_lang, api_url="http://127.0.0.1:5000/translate"):
    payload = {
        "q": text,  #text to translate
        "source": "en",  #source language
        "target": target_lang,  #target language code
        "format": "text"  #plain text format
    }
    headers = {"Content-Type": "application/json"}  #specify content type is JSON
    
    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)  #POST request to LibreTranslate
        
        # Handle response from API
        if response.status_code == 200:  #successful response
            return response.json().get("translatedText", "Translation failed")  #get translated text
        else:
            return f"Error: {response.status_code}, {response.text}"  #error message
    
    except requests.exceptions.RequestException as e:  #handle network errors
        return f"Request failed: {e}"

# Test
if __name__ == "__main__":
    target_lang = input("Enter target language code: ")
    
    print("\nTranslated Descriptions:")
    for sign, desc in DESCRIPTIONS.items():
        print(f"Sign {sign}: {translate_text(desc, target_lang)}")
