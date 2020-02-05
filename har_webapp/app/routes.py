from flask import render_template, flash, redirect, request
from app import app
from app.form import HAR_Form
from io import StringIO
import classify


@app.route('/')
@app.route('/index')
def index():
    return redirect('/har')


@app.route('/har', methods=['GET', 'POST'])
def har():
    form = HAR_Form()
    raw_data = StringIO(request.form.get('raw_data'))
    error = False

    if form.validate_on_submit():
        try:
            output = classify.perform_har_classification(raw_data)
        except ValueError:
            output = "Unable to Classify Activity"
            error = True
        return render_template('classification.html', output=output, status=error)    
    return render_template('har.html', form=form)