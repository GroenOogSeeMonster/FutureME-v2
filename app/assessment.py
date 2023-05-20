from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from . import db
from .user.models import Assessment1Result

assessment = Blueprint('assessment', __name__)

@assessment.route('/assessment1', methods=['GET', 'POST'])
@login_required
def assessment1():
    if request.method == 'POST':
        answer1 = request.form.get('answer1')
        answer2 = request.form.get('answer2')
        answer3 = request.form.get('answer3')
        result = Assessment1Result(user_id=current_user.id, answer1=answer1, answer2=answer2, answer3=answer3)
        db.session.add(result)
        db.session.commit()
        return redirect(url_for('assessment.assessment2'))
    return render_template("main/assessment_1.html")  # This page should contain your form for the writing exercise

@assessment.route('/assessment2', methods=['GET', 'POST'])
@login_required
def assessment2():
    if request.method == 'POST':
        # Gather answers from the form
        answers = request.form.getlist('answers[]')

        # Save each answer to the database
        for i, answer in enumerate(answers):
            new_result = AssessmentResult(user_id=current_user.id, assessment_type=f'Writing_Q{i + 1}',
                                          result=answer)
            db.session.add(new_result)
        db.session.commit()

        flash('Writing exercise completed!', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template("assessment_2.html")  # This page should contain your form for the writing exercise


@assessment.route('/assessment3', methods=['GET', 'POST'])
@login_required
def assessment3():
    if request.method == 'POST':
        # Gather answers from the form
        answers = request.form.getlist('answers[]')

        # Convert answers to integer and calculate the result
        int_answers = list(map(int, answers))
        result = calculate_via_result(int_answers)  # This is a placeholder for your scoring function

        # Save result to database
        new_result = AssessmentResult(user_id=current_user.id, assessment_type='Assessment3', result=result)
        db.session.add(new_result)
        db.session.commit()

        flash('Assessment completed!', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template("assessment_3.html")  # This page should contain your form for the survey


@assessment.route('/assessment4', methods=['GET', 'POST'])
@login_required
def assessment4():
    if request.method == 'POST':
        # Gather answers from the form
        answers = request.form.getlist('answers[]')

        # Convert answers to integer and calculate the result
        int_answers = list(map(int, answers))
        result = calculate_via_result(int_answers)  # This is a placeholder for your scoring function

        # Save result to database
        new_result = AssessmentResult(user_id=current_user.id, assessment_type='Assessment4', result=result)
        db.session.add(new_result)
        db.session.commit()

        flash('Assessment completed!', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template("assessment_4.html")  # This page should contain your form for the survey