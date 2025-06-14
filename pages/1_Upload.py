import time
import streamlit as st
from image_processing.file_conversion import convert_pdf_to_image, open_image

def upload_receipt_page() -> None:
    """
    This function deals with the uploading and processing of the receipt file.

    Allows users to upload an image (png, jpg, jpeg) or pdf (converts only the first
    page to an image) and saves the processed receipt image in the "processed_receipts"
    directory.

    It displays the uploaded receipt image and provides options for users to select
    which fields they want extracted and in what output format (json or excel).
    """
    st.title("Upload receipt")
    # Upload receipt
    uploaded_receipt = st.file_uploader(
        "Upload the image of the receipt", type=["png", "jpg", "jpeg", "pdf"]
    )

    if uploaded_receipt is not None:
        # PDF formaat convert to image and return only first page
        if uploaded_receipt.type == "application/pdf":
            receipt = convert_pdf_to_image(uploaded_receipt)
        # Image files
        else:
            receipt = open_image(uploaded_receipt)

        # # Display image
        # st.image(receipt, caption="Uploaded receipt")

        # Selection of data to be extracted
        output_options = [
            "Date of purchase",
            "Location",
            "Prices",
            "Items bought",
            "Merchant",
        ]
        selected_data = st.multiselect(
            "What data would you like to extract", output_options
        )

        # Selection of output format
        output_format = st.radio("Choose output format:", ["JSON", "Excel"])

        
        if st.button("Extract data"):
            st.write("Upload successful, reading receipt!!")
            st.write(f"Extracting {', '.join(selected_data)} in {output_format} format")

            # Temporarily display the image
            placeholder = st.empty()
            placeholder.image(receipt, caption="Uploaded receipt")
            time.sleep(10)  # Show image for 5 seconds
            placeholder.empty()  # Clear the image display


upload_receipt_page()