# ScamGuard for Students

ScamGuard is a student-first tool that helps detect fake job listings, internships, and training scams shared via WhatsApp, Telegram, LinkedIn, emails, and random websites.

It focuses on **prevention before damage** by explaining risks clearly instead of just labeling something as a scam.

---

## 🚨 Problem

Students and freshers are frequently targeted by:
- Fake internships and job offers
- Scam training programs demanding registration fees
- Messages misusing reputed institution names
- Urgency-based pressure tactics

These scams cause:
- Financial loss
- Misuse of personal data
- Career confusion and stress

There is no simple, real-time verification tool focused specifically on students.

---

## 💡 Solution

ScamGuard analyzes the content of a message or link and provides:
- **Risk Level** (Low / Medium / High)
- **Detected Red Flags**
- **Clear explanation in simple language**
- **Safe guidance** (no legal advice)

The system combines:
- Rule-based scam detection (reliable & explainable)
- Google Gemini for human-friendly explanations

---

## ✨ Key Features

- Student-focused scam detection
- Explainable results (not a black box)
- Works for messages, links, and email content
- No login required
- No user data stored
- Fast and demo-friendly

---

## 🧠 Tech Stack

- Python
- Flask
- HTML / CSS / JavaScript
- Google Gemini API (for explanation enhancement)

---

## ▶️ How to Run Locally

### Prerequisites
- Python 3.9+
- Gemini API key

### Steps

```bash
pip install flask google-generativeai
python app.py
