from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect


bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_mypro():
    return '어서와 플라스크는 처음이지?'

'''
@bp.route('/')
def index():
    question_list1 = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html',question_list=question_list1)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question1 = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html',question=question1)
'''
@bp.route('/')
def index():
    return redirect(url_for('question._list'))
