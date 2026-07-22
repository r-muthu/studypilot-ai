import fitz
from pathlib import Path


def extract_text(pdf_path: Path) -> tuple[str, int]:
    """
    Extract all text from a PDF.

    Returns:
        tuple:
            full_text
            number_of_pages
    """

    document = fitz.open(pdf_path)

    pages = []

    for page in document:
        pages.append(page.get_text())

    document.close()

    return "\n".join(pages), len(pages)