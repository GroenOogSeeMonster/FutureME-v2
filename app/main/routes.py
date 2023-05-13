from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.forms import RoutineForm
from app.models import Assessment, Routine

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = RoutineForm()
    if form.validate_on_submit():
        routine = Routine(body=form.body.data, user=current_user)
        db.session.add(routine)
        db.session.commit()
        flash('Your routine has been created!')
        return redirect(url_for('main.home'))
    routines = current_user.routines.order_by(Routine.timestamp.desc()).all()
    assessments = Assessment.query.all()
    return render_template('main/home.html', form=form, routines=routines, assessments=assessments)

from app.main.forms import SurveyForm
from app.models import Question, Response

@bp.route('/assessment/1', methods=['GET', 'POST'])
@login_required
def assessment_1():
    form = SurveyForm()
    question = Question.query.order_by(func.rand()).first()
    if form.validate_on_submit():
        response = Response(user=current_user, question=question, answer=form.response.data)
        db.session.add(response)
        db.session.commit()
        return redirect(url_for('main.assessment_1'))
    return render_template('main/assessment_1.html', form=form, question=question)

from app.main.forms import WritingForm
from app.models import Prompt, WritingResponse

@bp.route('/assessment/2', methods=['GET', 'POST'])
@login_required
def assessment_2():
    form = WritingForm()
    prompt = Prompt.query.order_by(func.rand()).first()
    if form.validate_on_submit():
        response = WritingResponse(user=current_user, prompt=prompt, answer=form.response.data)
        db.session.add(response)
        db.session.commit()
        return redirect(url_for('main.assessment_2'))
    return render_template('main/assessment_2.html', form=form, prompt=prompt)

from app.main.forms import GoalForm
from app.models import GoalCategory, Goal

@bp.route('/assessment/3', methods=['GET', 'POST'])
@login_required
def assessment_3():
    form = GoalForm()
    category = GoalCategory.query.order_by(func.rand()).first()
    if form.validate_on_submit():
        goal = Goal(user=current_user, category=category, text=form.goal.data, notes=form.notes.data)
        db.session.add(goal)
        db.session.commit()
        return redirect(url_for('main.assessment_3'))
    return render_template('main/assessment_3.html', form=form, category=category)

from app.main.forms import JournalEntryForm
from app.models import JournalEntry, Goal

@bp.route('/assessment/4', methods=['GET', 'POST'])
@login_required
def assessment_4():
    form = JournalEntryForm()
    goal = Goal.query.filter_by(user=current_user).order_by(func.rand()).first()
    if form.validate_on_submit():
        entry = JournalEntry(goal=goal, description=form.description.data)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main.assessment_4'))
    return render_template('main/assessment_4.html', form=form, goal=goal)

from app.main.forms import RoutineForm
from app.models import Routine

@bp.route('/routine', methods=['GET', 'POST'])
@login_required
def routine():
    form = RoutineForm()
    if form.validate_on_submit():
        routine = Routine(user=current_user, day_of_week=form.day_of_week.data, start_time=form.start_time.data, end_time=form.end_time.data, activity=form.activity.data)
        db.session.add(routine)
        db.session.commit()
        return redirect(url_for('main.routine'))
    routines = current_user.routines.order_by(Routine.day_of_week, Routine.start_time).all()
    return render_template('main/routine.html', form=form, routines=routines)

from flask import send_file
from app.models import Goal

@bp.route('/schedule', methods=['GET'])
@login_required
def schedule():
    routines = current_user.routines.order_by(Routine.day_of_week, Routine.start_time).all()
    goals = current_user.goals.all()
    return render_template('main/schedule.html', routines=routines, goals=goals)

@bp.route('/download_goals', methods=['GET'])
@login_required
def download_goals():
    # Prepare PDF of goals
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    goals = current_user.goals.all()
    for i, goal in enumerate(goals):
        p.drawString(100, 800 - i * 100, f"{goal.category}: {goal.goal}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename='goals.pdf', mimetype='application/pdf')

@bp.route('/tasks_and_goals', methods=['GET', 'POST'])
@login_required
def tasks_and_goals():
    task_form = UncompletedTaskForm()
    goal_form = GoalForm()
    if task_form.validate_on_submit():
        task = UncompletedTask(user=current_user, task=task_form.task.data)
        db.session.add(task)
        db.session.commit()
    if goal_form.validate_on_submit():
        goal = Goal(user=current_user, goal=goal_form.goal.data, description=goal_form.description.data)
        db.session.add(goal)
        db.session.commit()
    tasks = current_user.uncompleted_tasks.all()
    goals = current_user.goals.all()
    return render_template('main/tasks_and_goals.html', task_form=task_form, goal_form=goal_form, tasks=tasks, goals=goals)

@bp.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    form = ScheduleForm()
    if form.validate_on_submit():
        schedule = Schedule(user=current_user, day=form.day.data, hour=int(form.hour.data), activity=form.activity.data)
        db.session.add(schedule)
        db.session.commit()
        flash('Your schedule has been updated.')
    schedules = current_user.schedules.order_by(Schedule.day, Schedule.hour).all()
    return render_template('main/schedule.html', form=form, schedules=schedules)