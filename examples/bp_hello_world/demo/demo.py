# -*- coding: utf-8 -*-
# @Date    : 2016/1/16 17:10
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/
# @Version : $Id$
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

demo = Blueprint('demo', __name__,
                 template_folder='templates')


@demo.route('/', defaults={'page': 'index'})
@demo.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
