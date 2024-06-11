from flask import Flask, render_template, request, jsonify
import pandas as pd
from college_predictor import list_of_colleges, category

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    cutoff_str = request.form['Cutoff']
    
    try:
        original_marks = float(cutoff_str)
    except ValueError:
        return render_template('error.html', message="Invalid cutoff value. Please enter a valid number.")
    
    course = request.form['course']
    caste = request.form['Community']
    
    # Load your dataset
    data = pd.read_csv('D:\\College Predictor Tool-PickMyCareer\\College-Predictor-Tool-PickMyCareer\\ogdata.csv')
    
    # Process the data using your function from college_predictor.py
    filtered_colleges = list_of_colleges(original_marks, course, caste, data)
    count = len(filtered_colleges)
    
    if count > 0:
        min_cutoff = filtered_colleges[caste].min()
        max_cutoff = filtered_colleges[caste].max()
    else:
        min_cutoff = max_cutoff = None
    
    # Get top colleges based on highest cutoff across all courses
    top_colleges_all = data.copy()
    top_colleges_all = top_colleges_all[['College Code', 'College Name', 'Branch Name', 'Branch Code', caste]]
    top_colleges_all = top_colleges_all.sort_values(by=caste, ascending=False)
    
    # Filter top colleges based on the selected course
    top_colleges_course = top_colleges_all[top_colleges_all['Branch Name'].isin(category(course))]

    # Pass the original cutoff value, cutoff range, and other data to the results template
    return render_template(
        'results.html', 
        filtered_colleges=filtered_colleges.to_dict(orient='records'), 
        top_colleges=top_colleges_course.to_dict(orient='records'),
        caste=caste, 
        count=count, 
        min_cutoff=min_cutoff, 
        max_cutoff=max_cutoff,
        original_marks=original_marks  # Pass original cutoff value to template
    )

@app.route('/filter_colleges')
def filter_colleges():
    course = request.args.get('course')
    caste = request.args.get('caste', 'OC')  # Assuming 'OC' as default caste if not provided
    original_marks = request.args.get('original_marks', 0)  # Assuming 0 as default marks if not provided

    # Load your dataset
    data = pd.read_csv('D:\\College Predictor Tool-PickMyCareer\\College-Predictor-Tool-PickMyCareer\\ogdata.csv')
    
    # Filter colleges based on the selected course
    filtered_colleges = data[data['Branch Name'] == course]
    
    if not filtered_colleges.empty:
        min_cutoff = filtered_colleges[caste].min()
        max_cutoff = filtered_colleges[caste].max()
    else:
        min_cutoff = max_cutoff = None

    data = {
        "filtered_colleges": filtered_colleges.to_dict(orient='records'),
        "count": len(filtered_colleges),
        "caste": caste,
        "original_marks": original_marks,
        "min_cutoff": min_cutoff,
        "max_cutoff": max_cutoff
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
