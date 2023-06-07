from flask import render_template, flash, redirect, url_for

from app.models import Printer
from flask_login import current_user, login_required
from . import bp

from app.models import Printer, User
from app.forms import PrinterForm

@bp.route('/printer', methods=['GET', 'POST'])
@login_required
def printer():
    form=PrinterForm()
    if form.validate_on_submit():
        p = Printer(company=form.company.data, name=form.name.data, description=form.description.data)
        p.user_id = current_user.user_id
        p.commit()
        flash(f'Printer has been registered to {c.author}')
        return redirect(url_for('printers.user_page', username=current_user.username))
    return render_template('printers.j2', form=form)

@bp.route('/username/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.j2', title=username, user=user)