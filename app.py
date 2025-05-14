from flask import Flask, render_template, send_file
import markdown
import os
from weasyprint import HTML
import io

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
    pdf_file = io.BytesIO()
    HTML(string=rendered).write_pdf(pdf_file)
    pdf_file.seek(0)
    return send_file(pdf_file, as_attachment=True, download_name='cv.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)

