# MT-for-TeBaQA
This repository contains an api that can be used as an intermediary to ask NL quetion in spanish by using MT
To install the tool  run:

```
pip install -r requirements.txt
```

You can modify the information of the TeBaQA API (ip and port) in the translation_service/Config/Config.ini file.

We work with the Opus MT translator available in Higging Face by Helsinki-NLP.

To run the API use the command:
```
uvicorn translation_service.translation_api:app  --reload --log-config translation_service/Logs/log_config.ini --port 8091
```