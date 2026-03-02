from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# OpenAI setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# MongoDB setup
mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client["chatdb"]
collection = db["messages"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        ai_reply = response.choices[0].message.content

        # Save to MongoDB
        collection.insert_one({
            "user_message": user_message,
            "ai_reply": ai_reply,
            "timestamp": datetime.utcnow()
        })

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)