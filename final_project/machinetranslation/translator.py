import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-03-14',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    frenchtext = language_translator.translate(
        text= english_text,
        model_id='en-fr').get_result()

    return frenchtext.get("translations")[0].get("translation")

def french_to_english(french_text):
    englishtext = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return englishtext.get("translations")[0].get("translation")