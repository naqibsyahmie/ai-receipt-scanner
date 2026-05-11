# AI Receipt Scanner

AI-powered receipt-to-form extraction web app built for AI Internship Assessment.

---

## Features

- Upload receipt image
- OCR text extraction using Tesseract
- Local LLM extraction using Ollama + Gemma
- Auto-filled editable form
- Editable items table
- Export structured JSON

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