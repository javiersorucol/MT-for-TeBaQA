import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from fastapi import FastAPI, HTTPException

from transformers import pipeline

from utils.Configuration_utils import read_config_file
from utils.Request_utils import query_api_post

from DTOs.translation_DTOs import Question_DTO

# Reading the config file
config_file_path = 'translation_service/Config/Config.ini'
config = read_config_file(config_file_path)

# saving config vars
translations_modes = dict(config.items('TRANSLATION-MODES'))
tebaqa_server = dict(config['TEBAQA-SERVER'])

# Initalizating translators

translators = {}
for key, value in translations_modes.items():
    translators[key] = pipeline('translation', model=value)


app = FastAPI()

@app.post('/ask/')
def ask(question : Question_DTO):
    try:  
        if translators.get(question.mode) is None:
            raise HTTPException(status_code=404, detail='Translation mode not found.')
        
        question.text = translators.get(question.mode)(question.text)[0].get('translation_text')

        url = 'http://' + tebaqa_server.get('ip') + ':' + tebaqa_server.get('port') + tebaqa_server.get('question_path') 
        res = query_api_post(url=url, headers= {'Content-Type' : 'text/plain'}, params={'query': question.text, 'lang' : 'en'}, json_payload={})
        return res.get('json')
        
    except:
        raise HTTPException(status_code=500, detail='Unknown error.')

# # End Points

# @app.post('/translate/')
# def translate(question :  Question_DTO):
    
#     #If translation mode does not exist, return error
#     if translators.get(question.mode) is None:
#         raise HTTPException(status_code=404, detail='Translation mode not found.')
    
#     try:    
#         # translate
#         question.text = translators.get(question.mode)(question.text)[0].get('translation_text')
#         return question
        
#     except:
#         raise HTTPException(status_code=500, detail='Unknown error.')

