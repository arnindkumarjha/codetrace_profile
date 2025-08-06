from ydata-profiling import ProfileReport
import sweetviz as sv
import pandas as pd
import os

def generate_profiling_reports(csv_file_path):
    # Load the data
    data = pd.read_csv(csv_file_path)

    # Generate Pandas Profiling report
    profile = ProfileReport(data, title="Pandas Profiling Report", explorative=True)
    profile_file_path = os.path.join('reports', 'pandas_profiling_report.html')
    profile.to_file(profile_file_path)

    # Generate SweetViz report
    sweetviz_report = sv.analyze(data)
    sweetviz_report_file_path = os.path.join('reports', 'sweetviz_report.html')
    sweetviz_report.show_html(sweetviz_report_file_path)

if __name__ == "__main__":
    csv_file = os.path.join('data', 'sample_ui_data.csv')
    generate_profiling_reports(csv_file)