from PyPDF2 import PdfMerger
from flask import Flask, request, render_template,send_file,abort
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def merge_pdfs():
    if request.method == 'POST':
        # Get all the uploaded PDF files
        pdf_files = request.files.getlist('pdf_files[]')
        if not os.path.exists('uploads'):
            os.makedirs('uploads')

        # Save the uploaded files to the uploads directory
        for pdf_file in pdf_files:
            pdf_file.save(os.path.join('uploads', pdf_file.filename))
        # Merge the PDF files
        merger = PdfMerger()
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        merged_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S%f')}_merged.pdf"
        merged_file_path = os.path.join('uploads', merged_filename)
        with open(merged_file_path, 'wb') as f:
            merger.write(f)
        merger.close()

        # Return the merged PDF file to the user in a new browser tab
        if os.path.exists(merged_file_path):
            return send_file(merged_file_path, mimetype='application/pdf', as_attachment=False)
        else:
            abort(404)


    # If the request method is GET, return the HTML form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




