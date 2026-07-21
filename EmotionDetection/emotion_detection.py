import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobject =  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobject, headers=headers)
    t = json.loads(response.text)
    e = t["emotionPredictions"][0]["emotion"]
    max_emotion = max(e, key=e.get)
    e["dominant_emotion"] = max_emotion
    return e
