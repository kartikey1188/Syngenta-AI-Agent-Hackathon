import os
import pdfplumber
from pathlib import Path

def convert_pdf_to_txt():
    """
    Convert all PDF files in the pdf_documents folder to text files
    and save them in the txt_documents folder with the same name.
    """
    # Define paths
    current_dir = Path(__file__).parent
    pdf_folder = current_dir.parent / "pdf_documents"
    txt_folder = current_dir
    
    # Ensure the txt_documents folder exists
    txt_folder.mkdir(exist_ok=True)
    
    # Check if pdf_documents folder exists
    if not pdf_folder.exists():
        print(f"Error: PDF folder not found at {pdf_folder}")
        return
    
    # Get all PDF files
    pdf_files = list(pdf_folder.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in the pdf_documents folder.")
        return
    
    print(f"Found {len(pdf_files)} PDF files to convert...")
    
    # Convert each PDF file
    for pdf_file in pdf_files:
        try:
            print(f"Converting: {pdf_file.name}")
            
            # Extract text from PDF
            text_content = ""
            with pdfplumber.open(pdf_file) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    page_text = page.extract_text()
                    if page_text:
                        text_content += f"--- Page {page_num + 1} ---\n"
                        text_content += page_text + "\n\n"
            
            # Create output filename (same name but with .txt extension)
            output_filename = pdf_file.stem + ".txt"
            output_path = txt_folder / output_filename
            
            # Write text to file
            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(text_content)
            
            print(f"✓ Successfully converted {pdf_file.name} to {output_filename}")
            
        except Exception as e:
            print(f"✗ Error converting {pdf_file.name}: {str(e)}")
    
    print("\nConversion process completed!")

def main():
    """Main function to run the converter"""
    print("Starting PDF to Text conversion...")
    convert_pdf_to_txt()

if __name__ == "__main__":
    main()
