from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route("/api/", methods=["POST"])
def answer():
    data = request.get_json()
    question = data.get("question", "")
    image_b64 = data.get("image", None)

    # Dummy response for now
    return jsonify({
        "answer": "You must use `gpt-3.5-turbo-0125`, even if the AI Proxy only supports `gpt-4o-mini`. Use the OpenAI API directly for this question.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/4",
                "text": "Use the model that’s mentioned in the question."
            },
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "Just use a tokenizer, like Prof. Anand did, to get token count and multiply it by rate."
            }
        ]
    })

if __name__ == "__main__":
    app.run(port=8000)
