# =========================
# llm_logic.py
# =========================

from ollama_client import ask_ollama
import json
import re


class ReceiptExtractor:

    def extract_receipt_info(self, receipt_text):

        prompt = f"""
You are a receipt extraction AI.

Extract receipt information and return ONLY valid JSON.

NO explanation.
NO markdown.
NO extra text.

IMPORTANT RULES:

- "amount" = original item/service amount
- "discount" = discount value if available
- "total_paid" = actual paid amount after discount/payment
- Detect currency automatically
- Return clean numeric values only
- Remove OCR noise symbols like | or weird commas

JSON format:

{{
    "store_name": "",
    "date": "",
    "currency": "",
    "amount": "",
    "discount": "",
    "total_paid": "",
    "items": [
        {{
            "name": "",
            "price": ""
        }}
    ]
}}

Receipt Text:
{receipt_text}
"""

        response = ask_ollama(prompt)

        try:

            json_match = re.search(r'\{.*\}', response, re.DOTALL)

            if json_match:

                cleaned_json = json_match.group()

                data = json.loads(cleaned_json)

                return data

            return {
                "error": "No JSON found",
                "raw_response": response
            }

        except Exception as e:

            return {
                "error": str(e),
                "raw_response": response
            }