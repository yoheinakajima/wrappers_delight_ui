from flask import render_template, request, render_template_string
from app import app
from wrappers_delight.analytics import query_log_with_ai
import json
import ndjson

@app.template_filter('to_pretty_json')
def to_pretty_json(data):
    return json.dumps(data, indent=4, sort_keys=True, default=str)

@app.route('/', methods=['GET', 'POST'])
def index():
    logs = []

    if request.method == 'POST':
        user_query = request.form.get('user_query')

        # Get the result directly as a DataFrame
        result_df = query_log_with_ai(user_query)
        
        # Convert the DataFrame to a list of dictionaries for rendering in the template
        logs_list = result_df.to_dict(orient='records')
        
        # Update each dictionary to contain the pretty-printed params
        for log in logs_list:
            if 'params' in log:
                log['params'] = json.dumps(log['params'], indent=4)
        
        logs = logs_list

    return render_template('index.html', logs=logs)

@app.route('/reflections', methods=['GET'])
def reflections():
    # Read the reflections from the ndjson file
    with open("prompt_reflections.ndjson", "r") as file:
        reflections = ndjson.load(file)
    
    # Convert JSON strings in the reflection data to actual JSON objects
    for ref in reflections:
        ref['reflection'] = json.loads(ref['reflection'])

    return render_template('reflections.html', reflections=reflections)