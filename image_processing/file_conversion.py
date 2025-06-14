import pdf2image
from PIL import Image
from streamlit.runtime.uploaded_file_manager import UploadedFile

def convert_pdf_to_image(uploaded_receipt: UploadedFile) -> Image.Image:
    """
    Converts the first page of an uploaded PDF file to a PIL Image.

    Args:
        uploaded_receipt (UploadedFile): A PDF file uploaded via Streamlit's file uploader.

    Returns:
        Image.Image: A PIL Image object representing the first page of the PDF.
    """
    receipt = pdf2image.convert_from_bytes(uploaded_receipt.read())[0]
    return receipt

def open_image(uploaded_receipt: UploadedFile) -> Image.Image:
    """
    Opens an uploaded image file and returns it as a PIL Image object.

    Args:
        uploaded_receipt (UploadedFile): An image file uploaded via Streamlit's file uploader.

    Returns:
        Image.Image: A PIL Image object representing the uploaded image.
    """
    receipt = Image.open(uploaded_receipt)
    return receipt
