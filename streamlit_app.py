import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ScamGuard for Students", page_icon="🛡️")

st.title("🛡️ ScamGuard for Students")
st.write("Paste a job, internship, course link, or email message")

# --- API KEY ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

content = st.text_area("Message content", height=180)

if st.button("Check Authenticity"):
    if not content.strip():
        st.warning("Please paste some content.")
    else:
        text = content.lower()
        indicators = []

        # Rule-based detection
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

        # Risk scoring
        if len(indicators) >= 3:
            risk = "High"
        elif len(indicators) == 2:
            risk = "Medium"
        else:
            risk = "Low"

        # Explanation
        if len(indicators) == 0:
            explanation = "No common scam indicators were detected in this message."
        else:
            explanation = "This message shows patterns commonly used in scams targeting students."

            try:
                prompt = f"""
Explain in simple language why these indicators suggest risk for students:
{indicators}
"""
                explanation = model.generate_content(prompt).text.strip()
            except:
                pass

        # Output
        st.subheader(f"Risk Level: {risk}")
        st.write("**Why?**", explanation)

        st.write("**Red Flags:**")
        if indicators:
            for i in indicators:
                st.write("•", i)
        else:
            st.write("None detected")

        st.write("**Safe Guidance:**")
        st.info(
            "Do not pay any fees or share personal information. "
            "Verify opportunities through official websites."
        )
