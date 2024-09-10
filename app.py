from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from io import BytesIO
from data_processing.preprocessing import pipeline_all_sheets_as_excel, pipeline_all_sheets_as_json
import os

app = Flask(__name__)

CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from the backend!'})

@app.route('/api/process-excel/json', methods=['POST'])
def process_excel_json():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400 
    
    file = request.files['file']
    try:
        output = pipeline_all_sheets_as_json(file)
        return jsonify(output)

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/api/process-excel', methods=['POST'])
def process_excel():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400  # Bad request for missing file
    
    file = request.files['file']
    try:
        output = pipeline_all_sheets_as_excel(file)
        return send_file(output, 
                         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                         as_attachment=True, 
                         download_name='processed_file.xlsx')

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/sample/sales', methods=['GET'])
def get_sample_sales_report():
    try:
        return send_file('data_processing/assets/sales-report-august-sample.xlsx', 
                         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                         as_attachment=True, 
                         download_name='sample-sales-report.xlsx')

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
            
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
