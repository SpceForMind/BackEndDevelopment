from flask import Flask, url_for, request, render_template, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = "uploads/"
ALLOWED_EXT = set(['txt', 'xlsx', 'odt'])
app = Flask(__name__, static_url_path = '/static/')
'''
    Set path to directory with uploads files
'''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXT
'''
    Route for upload file
    reuquest.files['<name_from_form>'] -> <file>
    <file>.save(<path>) - save file
    <file>.filename - name of file which was sending from client
'''
@app.route(r'/upload/', methods = ['GET', 'POST'])
def upload_file():
    '''
        Upload file
    '''
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        if f and allowed_file(f.filename):
            f.save(os.path.join("/var/www/FlaskApp/FlaskApp", app.config['UPLOAD_FOLDER'], filename))
    '''
        Send html file with form 
    '''
    return app.send_static_file('upload_form.html')
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
