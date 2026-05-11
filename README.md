# AI Receipt Scanner

AI-powered receipt-to-form extraction web app built for AI Internship Assessment.

---

## Features

- Upload receipt image
- OCR text extraction using Tesseract
- Local LLM extraction using Ollama + Gemma
- Editable items table
- Export structured JSON

---

# System Flow

```text
+------------------+
| Receipt Image    |
+------------------+
          ↓
+------------------+
| Tesseract OCR    |
| Text Extraction  |
+------------------+
          ↓
+------------------+
| Ollama + Gemma   |
| AI Processing    |
+------------------+
          ↓
+------------------+
| Structured JSON  |
+------------------+
          ↓
+------------------+
| Editable UI      |
| Table + Form     |
+------------------+
```
---

## Tech Stack

- Python
- Streamlit
- Tesseract OCR
- Ollama
- Gemma 3B
- Pandas

---

## How To Run

Install dependencies:

```bash
pip install streamlit pillow pytesseract pandas ollama
```

Run the app:

```bash
streamlit run app.py
```

---

## Model Used

- Gemma 3B via Ollama

---

## Prompt Engineering

The LLM is instructed to:

- Extract structured receipt information
- Return ONLY valid JSON
- Avoid markdown and explanations

---

## Assessment Purpose

This repository was built for an AI Internship Assessment involving:

- Receipt OCR
- Generative AI extraction
- Form auto-fill
- Editable structured outputs

---

Why JSON Response Is Important

JSON was used because:

- Structured and machine-readable
- Easy integration with databases and APIs
- Easy conversion into tables and dashboards
- Standard format for AI systems and backend applications
- Easier data validation and processing

Instead of returning plain text, JSON makes the receipt data reusable and scalable for future systems.

---
Why Gemma Model Was Chosen

Gemma was selected because:

Lightweight and efficient
Can run locally using Ollama
Fast inference performance
Suitable for structured information extraction
Lower hardware requirements compared to larger models

This makes it practical for local AI deployment and internship assessment environments.

---

Demo Flow

- Upload receipt image
- OCR extracts text
- LLM processes receipt text
- Structured JSON is generated
- Receipt information is displayed in table format

---

The intervention OCR in this flow is to maintain the cost as efficient as possible. This process will cost less then using vision model to do the Text Extraction itself since the input are text. 

Pros:
Effective for well written printed documents

Cons:
Bad for handwritten and blurry images
