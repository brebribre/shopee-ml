from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS
from io import BytesIO
from data_processing.preprocessing import pipeline_all_sheets

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from the backend!'})

@app.route('/api/process-excel', methods=['POST'])
def process_excel():
    if 'file' not in request.files:
        return {'error': 'No file provided'}, 400
    file = request.files['file']
    try:
        # Process the file using the pipeline (returns an Excel file in-memory)
        output = pipeline_all_sheets(file)
        # Return the processed file as a response
        return send_file(output, 
                 mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                 as_attachment=True, 
                 download_name='processed_file.xlsx')
    except Exception as e:
        return {'error': str(e)}, 500
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)