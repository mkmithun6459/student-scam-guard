from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# 🔑 USE A VALID GEMINI API KEY (NEW ONE)
genai.configure(api_key="GEMINI API KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    content = request.json.get("content", "")
    text = content.lower()

    indicators = []

    # -------- RULE-BASED SCAM DETECTION --------
    if "₹" in text or "fee" in text or "pay" in text:
        indicators.append("Requests upfront payment")

    if "guaranteed" in text:
        indicators.append("Claims guaranteed placement")

    if "final call" in text or "apply now" in text or "limited" in text:
        indicators.append("Uses urgency or pressure tactics")

    if "forms.gle" in text or "google form" in text:
        indicators.append("Uses Google Form instead of official website")

    if "certificate" in text:
        indicators.append("Overemphasis on certificates")

    if "whatsapp" in text:
        indicators.append("Uses personal contact instead of official email")

    # -------- RISK SCORING --------
    if len(indicators) >= 3:
        risk_level = "High"
    elif len(indicators) == 2:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # -------- CONSISTENT EXPLANATION --------
    if len(indicators) == 0:
        explanation = (
            "No common scam indicators were detected in this message based on known patterns."
        )
    else:
        explanation = (
            "This message shows patterns commonly used in scams that target students, "
            "such as payment requests, urgency, or vague benefits."
        )

    safe_guidance = (
        "Do not pay any fees or share personal information. "
        "Verify opportunities through official company or institute websites."
    )

    # -------- GEMINI (OPTIONAL EXPLANATION ENHANCER) --------
    if len(indicators) > 0:
        try:
            prompt = f"""
Explain in simple, student-friendly language why the following indicators suggest risk:

{indicators}

Keep it short and clear.
"""
            response = model.generate_content(prompt)
            explanation = response.text.strip()
        except:
            pass  # fallback explanation already set

    return jsonify({
        "risk_level": risk_level,
        "indicators": indicators,
        "explanation": explanation,
        "safe_guidance": safe_guidance
    })


if __name__ == "__main__":
    app.run(debug=True)
