"""
If you are in the same directory as this file (app.py), you can run run the app using gunicorn:

    in general :
    $ gunicorn --bind 0.0.0.0:<PORT> app:app

    here :
    $ gunicorn --bind 0.0.0.0:8080 serving_client:app

gunicorn can be installed via:

    $ pip install gunicorn

"""
import os
import openai

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def predict():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/predict
    """

    # Get POST json data
    json = request.get_json()

    # Replace YOUR_API_KEY with your OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = json["prompt"]

    # Set the maximum number of tokens to generate in the response
    max_tokens = 128

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = completion.choices[0].text
    print(answer)

    response = {"text": answer}
    return jsonify(response)  # response must be json serializable!



if __name__ == '__main__':
    import requests

    class GPT3Client:
        def __init__(self, ip: str = "0.0.0.0", port: int = 8080):
            self.base_url = f"http://{ip}:{port}"


        def test(self, prompt):
            res = requests.post(url=self.base_url + "/generate",
                                json={'prompt': prompt})
            print(res.json()["text"])
            return res.json()["text"]


    sc = GPT3Client()
    sc.test(prompt="Question : Quel est le cours d'Apple en Chine ? Réponse de l'api : {'value': 129,62, 'currency': 'USD', 'gap': 4,60, percent_gap: 3,68}. Génère une phrase pour répondre à la question avec ces informations")
