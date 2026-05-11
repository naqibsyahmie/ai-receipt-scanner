import streamlit as st
from PIL import Image
import pytesseract
import pandas as pd
import json

from llm_logic import ReceiptExtractor

# ====================================
# Tesseract Path
# ====================================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ====================================
# Initialize Extractor
# ====================================
extractor = ReceiptExtractor()

# ====================================
# Page Config
# ====================================
st.set_page_config(
    page_title="AI Receipt Scanner",
    layout="centered"
)

# ====================================
# Title
# ====================================
st.title("🧾 AI Receipt Scanner")

st.write(
    "Upload a receipt image and automatically extract receipt information using OCR + Local LLM."
)

# ====================================
# Upload File
# ====================================
uploaded_file = st.file_uploader(
    "Upload Receipt",
    type=["png", "jpg", "jpeg"]
)

# ====================================
# If File Uploaded
# ====================================
if uploaded_file is not None:

    # Open Image
    image = Image.open(uploaded_file)

    # Display Image
    st.image(
        image,
        caption="Uploaded Receipt",
        width="stretch"
    )

    # ====================================
    # Analyze Button
    # ====================================
    if st.button("Analyze Receipt"):

        # ====================================
        # OCR Extraction
        # ====================================
        with st.spinner("Reading receipt..."):

            extracted_text = pytesseract.image_to_string(image)

        # ====================================
        # AI Extraction
        # ====================================
        with st.spinner("Analyzing with AI..."):

            result = extractor.extract_receipt_info(extracted_text)

        # ====================================
        # Success
        # ====================================
        if result and "error" not in result:

            st.success("Receipt analyzed successfully!")

            # ====================================
            # Editable Form
            # ====================================
            st.subheader("Receipt Form")

            merchant_name = st.text_input(
                "Merchant Name",
                value=result.get("store_name", "")
            )

            date = st.text_input(
                "Date",
                value=result.get("date", "")
            )

            currency = st.text_input(
                "Currency",
                value=result.get("currency", "")
            )

            total_amount = st.text_input(
                "Total Amount",
                value=result.get("total", "")
            )

            paid_amount = st.text_input(
                "Paid Amount",
                value=result.get("amount", "")
            )

            # ====================================
            # Items Section
            # ====================================
            st.subheader("Items")

            items = result.get("items", [])

            # Clean Prices
            for item in items:

                if "price" in item:

                    price = str(item["price"])

                    price = price.replace("|", "")
                    price = price.replace("MYR", "")
                    price = price.replace("RM", "")
                    price = price.strip()

                    item["price"] = price

            # ====================================
            # Editable Table
            # ====================================
            if items:

                df = pd.DataFrame(items)

                edited_df = st.data_editor(
                    df,
                    width="stretch",
                    num_rows="dynamic"
                )

            else:

                st.warning("No items found.")

                edited_df = pd.DataFrame()

            # ====================================
            # Submit Button
            # ====================================
            if st.button("Submit Receipt"):

                final_data = {
                    "merchant_name": merchant_name,
                    "date": date,
                    "currency": currency,
                    "total_amount": total_amount,
                    "paid_amount": paid_amount,
                    "items": edited_df.to_dict(orient="records")
                }

                st.success("Receipt submitted successfully!")

                # ====================================
                # Final JSON
                # ====================================
                st.subheader("Final Submitted Data")

                st.json(final_data)

                # ====================================
                # Download JSON
                # ====================================
                json_data = json.dumps(final_data, indent=4)

                st.download_button(
                    label="Download Final JSON",
                    data=json_data,
                    file_name="final_receipt.json",
                    mime="application/json"
                )

            # ====================================
            # Raw JSON
            # ====================================
            with st.expander("View Raw JSON"):

                st.json(result)

        else:

            st.error("Failed to extract receipt information.")

            st.json(result)