from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Drawing
from . import db
import json
from io import BytesIO


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    return render_template("home.html", user=current_user)

@views.route('/whiteboard', methods=['GET', 'POST'])
@login_required
def whiteboard():
    if request.method=='POST':
        drawing = request.form.get('save')
        new_drawing = Drawing(data=drawing, user_id=current_user.id)
        db.session.add(new_drawing)
        db.session.commit()
        flash('Drawing saved to your home gallery!', category = 'success')
    return render_template("whiteboard.html", user=current_user)


@views.route('/delete-drawing', methods=['POST'])
def delete_drawing():
    drawing = json.loads(request.data)
    drawingId = drawing['drawingId']
    drawing = Drawing.query.get(drawingId)
    if drawing:
        if drawing.user_id == current_user.id:
            db.session.delete(drawing)
            db.session.commit()
    return jsonify({})