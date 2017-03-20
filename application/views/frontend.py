# coding=utf-8
from flask import Blueprint, render_template, request, url_for, redirect
from application.tasks.celery_tasks import calc
from application.tasks.scheduler_tasks import call_get_html
from application.extensions.scheduler import scheduler
from application.models.results import Results
from application.models.tasks import Tasks
from application.extensions.database import database


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/')
def index():
    calc.delay(1, 2)
    return 'hello world'


@frontend_blueprint.route('/sched')
def sched():
    scheduler.add_job('test', trigger='interval', seconds=5, func=call_get_html, args=('http://www.baidu.com/', ))


@frontend_blueprint.route('/tasks')
def tasks():
    result = Tasks.query.all()
    return render_template('tasks.html', result=result)


@frontend_blueprint.route('/tasks/switch/<int:task_id>')
def tasks_switch(task_id):
    task = Tasks.query.filter_by(task_id=task_id).first()
    if task.status:
        task.status = False
    else:
        task.status = True
    database.session.add(task)
    database.session.commit()

    if task.status:
        scheduler.add_job(
            id=str(task_id),
            trigger='interval',
            minutes=1,
            func=call_get_html,
            args=(task.url, ),
        )
    else:
        try:
            scheduler.delete_job(id=str(task_id))
        except Exception, e:
            print e
    return redirect(url_for('frontend.tasks'))


@frontend_blueprint.route('/tasks_add', methods=['GET', 'POST'])
def tasks_add():
    url = request.form.get('url')
    if url:
        task = Tasks()
        task.url = url
        database.session.add(task)
        database.session.commit()
    return render_template('tasks_add.html')


@frontend_blueprint.route('/results')
def results():
    data = Results.query.order_by(Results.created_at.desc()).all()
    return render_template('results.html', data=data)
