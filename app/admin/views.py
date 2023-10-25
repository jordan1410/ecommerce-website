from .moveOrder import moveOrder, dbToData
from .forms import AdminLogin, AdminOrders
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from sqlalchemy import desc
import bcrypt
from app.extensions import db

adminBP = Blueprint('adminBP', __name__,
                    static_folder="/app/static", template_folder="templates")


@adminBP.route('/admin-login/', methods=["GET", "POST"])
def adminLogin():
    form = AdminLogin()
    if request.method == "POST":
        if form.validate_on_submit():
            # Login process:
            # Get inputted password
            # Uses bcrypt to verify accurate password
            # if isUser:
            #     login_user(user, remember=False)
            #     flash("You have been logged in, welcome")
            #     return redirect(url_for('adminBP.adminHome'))
            # else:
            #     flash("Wrong password, please try again", category="info")
            #     return render_template('admin-login.html', form=form)
            pass
        else:
            flash(
                "Please make sure you have entered your password correctly", category="error")
            return render_template('admin-login.html', form=form)
    else:
        return render_template('admin-login.html', form=form)


@adminBP.route('/admin-logout/', methods=["GET"])
@login_required
def adminLogout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for("homeBP.index"))


@adminBP.route('/admin-home/', methods=["GET"])
@login_required
def adminHome():
    return render_template('admin-home.html')


@adminBP.route('/pending/', methods=["GET", "POST"])
@login_required
def pendingOrders():
    form = AdminOrders()
    pending = dbToData()
    if request.method == "POST":
        if form.validate_on_submit():
            moveData = None

            if request.form.get('confirmed'):
                moveData = request.form['confirmed']

            elif request.form.get('employee'):
                moveData = request.form['employee']

            elif request.form.get('delete'):
                moveData = request.form['delete']

            id = request.form['id']
            page = 'pending'

            moveOrder()

            return render_template('pending.html', form=form, pendingData=pending)
        else:
            flash(
                "Please make sure you have correctly sent your order", category="error")
            return render_template('pending.html', form=form, pendingData=pending)
    else:
        return render_template('pending.html', form=form, pendingData=pending)


@adminBP.route('/confirmed/', methods=["GET", "POST"])
@login_required
def confirmedOrders():
    form = AdminOrders()
    confirmed = dbToData()
    if request.method == "POST":
        if form.validate_on_submit():
            moveData = None

            if request.form.get('completed'):
                moveData = request.form['completed']

            elif request.form.get('employee'):
                moveData = request.form['employee']

            elif request.form.get('delete'):
                moveData = request.form['delete']

            id = request.form["id"]
            page = "confirmed"

            moveOrder()

            return render_template('confirmed.html', form=form, confirmedData=confirmed)
        else:
            flash(
                "Please make sure you have correctly sent your order", category="error")
            return render_template('confirmed.html', form=form, confirmedData=confirmed)
    else:
        return render_template('confirmed.html', form=form, confirmedData=confirmed)


@adminBP.route('/employee/', methods=["GET", "POST"])
@login_required
def employeeOrders():
    form = AdminOrders()
    confirmed = dbToData()
    if request.method == "POST":
        if form.validate_on_submit():
            moveData = None

            if request.form.get('completed'):
                moveData = request.form['completed']

            elif request.form.get('delete'):
                moveData = request.form['delete']

            id = request.form["id"]
            page = "employee"

            moveOrder()

            return render_template('employee.html', form=form, confirmedData=confirmed)
        else:
            flash(
                "Please make sure you have correctly sent your order", category="error")
            return render_template('employee.html', form=form, confirmedData=confirmed)
    else:
        return render_template('employee.html', form=form, confirmedData=confirmed)


@adminBP.route('/completed/', methods=["GET"])
@login_required
def completedOrders():
    completed = dbToData()

    return render_template('completed.html', completedOrders=completed)
