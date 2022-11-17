#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import re
import random
import os
from flask import Flask, request, jsonify

import base64
import speech_recognition as sr
import wave
from ast import literal_eval


def speechRecognition(data, params):
    r = sr.Recognizer()

    audioFileName = 'test.wav'

    data = base64.b64decode(data)
    params = base64.b64decode(params)
    params = literal_eval(params.decode("utf-8"))

    wave_write = wave.open(audioFileName, "w")
    wave_write.setparams(params)
    wave_write.writeframes(data)
    wave_write.close()


    audioFile = None
    with sr.AudioFile(audioFileName) as source:
        audioFile = r.record(source)

    try:
        text = r.recognize_google(audioFile, language="fr-FR")
        print(text)
        return text
    except Exception as e:
        print (e)

def speechRecognition_local(data, params):
    r = sr.Recognizer()

    audioFileName = 'test.wav'

    #params = literal_eval(params.decode("utf-8"))

    wave_write = wave.open(audioFileName, "w")
    wave_write.setparams(params)
    wave_write.writeframes(data)
    wave_write.close()


    audioFile = None
    with sr.AudioFile(audioFileName) as source:
        audioFile = r.record(source)

    try:
        text = r.recognize_google(audioFile, language="en-EN")
        print(text)
        return text
    except Exception as e:
        print (e)

app = Flask(__name__)


@app.route("/google", methods=["POST"])
def transcribe():
    req_data = request.get_json(force=True)

    # collect the transcription
    result_from_google = speechRecognition(req_data['data'], req_data['params'])

    print("result_from_google", result_from_google)
    # send back the predicted keyword in json format
    reply = {"sentence": result_from_google}

    return jsonify(reply)


@app.route("/test", methods=["POST"])
def test_with_local_Wav():
    path = "test.wav"
    with wave.open(path, 'rb') as file:
        params = str(file.getparams())
        print(params)
        data = file.readframes(file.getnframes())
        #print(data)

        result_from_google = speechRecognition_local(data, params)

        print("result_from_google", result_from_google)

if __name__ == "__main__":
    #test_with_local_Wav()
    app.run(host='0.0.0.0', debug=False, port=5001)
