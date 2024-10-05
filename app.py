
import ydata_profiling as ydp
from flask import Flask, request, render_template, send_file
import pandas as pd
import io
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    csv_file = request.files['csv_file']
    if csv_file:
        df = pd.read_csv(csv_file)
        profile = ydp.ProfileReport(df, title="Data Analysis Report")
        output_stream = io.BytesIO()
        file_path = "report.html"

        if os.path.exists(file_path):
            os.remove(file_path)
                
        profile.to_file('report.html')
        output_stream.seek(0)
        return send_file("report.html")
    else:
        return "Please upload a CSV file."

if __name__ == '__main__':
    app.run()