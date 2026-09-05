from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# In-memory data for the "what happened" step choices.
# In a real app this might come from a database or config file.
CHOICES = [
    "Unwanted comments or messages",
    "Unwanted touching or advances",
    "Threats or unfair treatment",
    "Something else",
]

LANGUAGES = ["English", "हिन्दी", "தமிழ்", "বাংলা", "తెలుగు", "मराठी", "ગુજરાતી", "ਪੰਜਾਬੀ", "اردو", "ಕನ್ನಡ", "മലയാളം"]


@app.route("/")
def index():
    """Render the main landing page with the navigator section."""
    return render_template(
        "index.html",
        choices=CHOICES,
        languages=LANGUAGES,
    )


@app.route("/api/rights", methods=["POST"])
def get_rights():
    """
    Prototype endpoint: given the selected concern, return guidance text.
    Replace this with real POSH Act guidance logic / lookups later.
    """
    data = request.get_json(silent=True) or {}
    selection = data.get("selection", "")

    # Placeholder logic — swap in real rights-mapping content here.
    guidance = {
        "message": (
            "Based on your answer, we can explain which POSH Act "
            "protections may apply and show internal, external, and "
            "support options."
        ),
        "selection": selection,
    }
    return jsonify(guidance)


if __name__ == "__main__":
    app.run(debug=True)
