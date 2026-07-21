""" Deployment of Emotion Detection via Flask """
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector
        function. 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dom_emotion = response['dominant_emotion']
    del response['dominant_emotion']
    if dom_emotion is None:
        return 'Invalid text! Please try again!'
    return f'For the given statement, the system response is {json.dumps(response)[1:-2]}. \
                    The dominant emotion is <b>{dom_emotion}</b>.'

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0",port=5000)
