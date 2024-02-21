from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file is provided in the request
        if 'file' not in request.files:
            return render_template('code_box.html', error='No file provided')

        file = request.files['file']

        # Check if the file has a valid extension
        if file.filename == '' or not allowed_file(file.filename):
            return render_template('code_box.html', error='Invalid file type')

        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Process the image (you can replace this with your image processing function)
        # processed_output = process_image(file_path)

        # Read the JavaScript file
        js_file_path = 'static/code_file.js'  # Replace with your actual JS file path
        js_content = "kfff"
        with open(js_file_path, 'r') as js_file:
            js_content = js_file.read()
            # js_content = "kfff"
            # print(js_content)
            # Render the template with the processed output and JS content
    return render_template('code_box.html',  js_content=js_content)

    return render_template('code_box.html')

def process_image(file_path):
    # Replace this function with your image processing logic
    # Example: Read image, perform processing, and return output
    return f'Image processed. File path: {file_path}'

if __name__ == '__main__':
    app.run(debug=True)
