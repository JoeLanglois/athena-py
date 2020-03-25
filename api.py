from flask import Flask, request, jsonify
from athena.reports import Amounts, MonthData
from athena.extractor import Extractor
from athena.store import ReportStore

from main import generate_report

app = Flask(__name__)
store = ReportStore()

def parse_file_get():
    return jsonify({})

def parse_file_post():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({'error': 'No file sent'})
    
    num_opened_days = int(request.form.get('number_of_days'))
    file = request.files['file']
    report = generate_report(file, days_opened=num_opened_days)
    store.store(report, report.get('month')[0], report.get('month')[1]ter)
    return jsonify(report)

@app.route('/parse', methods=["GET", "POST"])
def parse_file():
    if request.method == "GET":
        return parse_file_get()
    else:
        return parse_file_post()