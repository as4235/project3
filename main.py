from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user

from . import db
from .models import record

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/Calculator')
@login_required
def Calculator():
    return render_template('Calculator.html', name=current_user.name)


@main.route('/')
@login_required
def show_numbers():
    alldata = record.query.filter_by(user_id=current_user.id).all()
    return render_template('Calculator.html', all_data=alldata)


@main.route('/delete/<int:name>')
def delete(name):
    to_delete = record.query.get_or_404(name)
    try:
        db.session.delete(to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return render_template('Calculator.html')


@main.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    if request.method == 'POST':
        data = request.form['data'].replace(" ", "")
        operation = request.form['operation']
        if operation == 'mean':
            from project.calc import pmean
            result = float(pmean(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'mode':
            from project.calc import mode
            result = float(mode(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'median':
            from project.calc import median
            result = float(median(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'standard deviation':
            from project.calc import stddev
            result = float(stddev(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'variance':
            from project.calc import variance
            result = float(variance(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'z score':
            from project.calc import zscore
            result = zscore(data)
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'population correlation coefficient':
            from project.calc import popcorcoeff
            result = float(popcorcoeff(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'confidence interval':
            from project.calc import confint
            result = confint(data)
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'population variance':
            from project.calc import pvar
            result = float(pvar(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'sin':
            from project.calc import sin
            result = float(sin(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'cos':
            from project.calc import cos
            result = float(cos(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
        elif operation == 'tan':
            from project.calc import tan
            result = float(tan(data))
            history = record(name=current_user.name, numbers=data, operation=operation, result=result)
            try:
                db.session.add(history)
                db.session.commit()
                return render_template('Calculator.html', result=result)
            except:
                return render_template('Calculator.html', result=result)
