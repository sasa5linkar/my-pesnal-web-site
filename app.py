from flask import Flask, render_template, send_file
import markdown
import pdfkit
import os

app = Flask(__name__)

@app.route('/')
def home():
    with open('Saša Petalinkar - CV.md', encoding='utf-8') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['extra', 'smarty'])
    return render_template('cv.html', content=html_content)

@app.route('/download')
def download_pdf():
    with open('Saša Petalinkar - CV.md', encoding='utf-8') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['extra', 'smarty'])
    rendered = render_template('cv.html', content=html_content)
    pdf_path = 'cv.pdf'
    pdfkit.from_string(rendered, pdf_path, options={
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    })
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

