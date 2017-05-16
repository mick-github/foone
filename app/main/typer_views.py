from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from app.util.decorators import permission_required
from . import forms
from .models import Problem
from ..account.models import Permission


@login_required
@permission_required(Permission.CREATE)
def add_problem():
    form = forms.QuestionForm()
    if form.validate_on_submit():
        # add the problem into the database
        prob = Problem(
            question=form.question.data,
            explain=form.explain.data,
            answer=form.answer.data,
            unit=form.unit.data,
            grade=form.grade.data,
            tags=form.tags.data
        )
        prob.save()
        flash('The problem has been uploaded successfully')
        return redirect(url_for('typer.add_problem'))
    return render_template('main/add_problem.html', form=form)