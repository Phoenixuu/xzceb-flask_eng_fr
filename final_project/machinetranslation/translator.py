import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('ldvqtM2bQcB3nbHTsvktfKbDIWfUxnfQLcHyZuWeGSp9')
language_translator = LanguageTranslatorV3(
    version='2022-03-14',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/4467ed22-d25b-47eb-ad78-1bc308d6d0bf')

def english_to_french(english_text):
    frenchtext = language_translator.translate(
        text= english_text,
        model_id='en-es').get_result()

    return frenchtext

def french_to_english(french_text):
    englishtext = language_translator.translate(
        text=french_text,
        model_id='en-es').get_result()
    return englishtext