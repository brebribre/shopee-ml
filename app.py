from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
from io import BytesIO
from data_processing.preprocessing import pipeline_all_sheets
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://shopee-ml-frontend.vercel.app"}}, supports_credentials=True)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from the backend!'})

@app.route('/api/process-excel', methods=['POST'])
@cross_origin(origin='https://shopee-ml-frontend.vercel.app', supports_credentials=True)
def process_excel():
    if 'file' not in request.files:
        return {'error': 'No file provided'}, 400
    file = request.files['file']
    try:
        output = pipeline_all_sheets(file)
        response = send_file(output, 
                 mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                 as_attachment=True, 
                 download_name='processed_file.xlsx')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(e)
        return {'error': str(e)}, 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
