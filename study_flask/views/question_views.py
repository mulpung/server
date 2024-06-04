from flask import Blueprint, render_template

from ..models.models import Question

bp = Blueprint('question', __name__,url_prefix='/question')

@bp.route('/list/')
def _list():
    question_list1 = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',question_list=question_list1)

@bp.route('detail/<int:question_id>/')
def detail(question_id):
    question1 = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question1)