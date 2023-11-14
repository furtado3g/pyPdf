import flask
from flask import request,make_response
import pdfkit
app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def generate_pdf_from_html():
    options = {
        'page-size': 'A4',
        'margin-top': '0.35in',
        'margin-right': '0.35in',
        'margin-bottom': '0.35in',
        'margin-left': '0.35in',
        'enable-javascript': True,
        'javascript-delay': 500,
        'encoding': 'UTF-8',
    }
    if request.method == 'POST':
        pdf = pdfkit.from_url(request.form['url'],options=options)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = \
            'inline; filename=%s.pdf' % 'yourfilename'
        return response
    else:
        return {'error': 'request method not supported'}
    
@app.route('/form')
def form():
    return flask.render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)