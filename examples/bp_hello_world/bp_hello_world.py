# -*- coding: utf-8 -*-
# @Date    : 2016/1/16 16:58
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/
# @Version : $Id$

from flask import Flask
from demo import demo

app = Flask(__name__)

app.register_blueprint(demo)
app.register_blueprint(demo, url_prefix='/pages')


if __name__ == '__main__':
    app.run()
