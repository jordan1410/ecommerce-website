from flask import Blueprint, render_template, request, flash
from .forms import PhobForm, OEMForm, Nine9Form, One69Form
from .parseForm import parseForm
from app.extensions import db

formsBP = Blueprint('formsBP', __name__,
                    static_folder="/app/static", template_folder="templates")


@formsBP.route('/phob-form/', methods=["GET", "POST"])
def phobForm():
    form = PhobForm()
    if request.method == "POST":
        if form.validate_on_submit():

            # form responses
            form = request.form
            formData, dbData = parseForm(form)

            # add form responses to database
            db.session.add(dbData)
            db.session.commit()

            # return user responses
            return render_template('confirmation.html', response=formData)
        else:
            # responses did not pass validation
            flash(
                "Please make sure you have correctly completed the form and all required boxes are marked", category="error")
            return render_template('phob-form.html', form=form)

    else:
        return render_template('phob-form.html', form=form)


@formsBP.route('/oem-form/', methods=["GET", "POST"])
def oemForm():
    form = OEMForm()
    if request.method == "POST":
        if form.validate_on_submit():

            # form responses
            form = request.form
            formData, dbData = parseForm(form)

            # add form responses to database
            db.session.add(dbData)
            db.session.commit()

            # return user responses
            return render_template('confirmation.html', response=formData)
        else:
            # responses did not pass validation
            flash(
                "Please make sure you have correctly completed the form and all required boxes are marked", category="error")
            return render_template('oem-form.html', form=form)

    else:
        return render_template('oem-form.html', form=form)


@formsBP.route('/169-form/', methods=["GET", "POST"])
def one69Form():
    form = One69Form()
    if request.method == "POST":
        if form.validate_on_submit():

            # form responses
            form = request.form
            formData, dbData = parseForm(form)

            # add form responses to database
            db.session.add(dbData)
            db.session.commit()

            # return user responses
            return render_template('confirmation.html', response=formData)
        else:
            # responses did not pass validation
            flash(
                "Please make sure you have correctly completed the form and all required boxes are marked", category="error")
            return render_template('169-form.html', form=form)
    else:
        return render_template('169-form.html', form=form)


@formsBP.route('/99-form/', methods=["GET", "POST"])
def nine9Form():
    form = Nine9Form()
    if request.method == "POST":
        if form.validate_on_submit():

            # form responses
            form = request.form
            formData, dbData = parseForm(form)

            # add form responses to database
            db.session.add(dbData)
            db.session.commit()

            # return user responses
            return render_template('confirmation.html', response=formData)
        else:
            # responses did not pass validation
            flash(
                "Please make sure you have correctly completed the form and all required boxes are marked", category="error")
            return render_template('99-form.html', form=form)
    else:
        return render_template('99-form.html', form=form)
