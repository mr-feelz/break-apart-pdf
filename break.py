import fitz  # PyMuPDF

def split_pdf_pages(pdf_path, output_folder):
    # Open the source PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        # Assuming the page number is at the bottom, you might need to adjust how you extract this
        lines = text.strip().split('\n')
        footer_page_number = lines[-1].strip()  # Customize based on your PDF's footer format

        # Create a new PDF with just this page
        output_pdf = fitz.open()  # New, empty PDF
        output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)
        
        # Construct the output PDF path with the footer page number
        output_path = f"{output_folder}/Page_{footer_page_number}.pdf"

        # Save the single page PDF
        output_pdf.save(output_path)
        output_pdf.close()  # Close the newly created PDF

        print(f"Saved: {output_path}")
    
    pdf_document.close()  # Close the source PDF

# Specify the path to the source PDF and the output folder
pdf_path = "<INPUT PDF>.pdf" #The input PDF that you would like to break apart into individual pages
output_folder = "<OUTPUT FOLDER>" #folder you'd like to use to output all the pages.

# Call the function with your paths
split_pdf_pages(pdf_path, output_folder)
