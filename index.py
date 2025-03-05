from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
GENAI_API_KEY = "AIzaSyAPQMyULAP3iY-tZmWz9G8SwHXm2i8ydro"
genai.configure(api_key=GENAI_API_KEY)

@app.route("/chat", methods=["GET"])
def chat():
    user_input = request.args.get("query")

    if not user_input:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel requires a variable named `app`
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)