#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template
from app.bpurls import mainBP
from app.common.xsk_mysql_utils import *


@mainBP.route('/', methods=['GET'])
@mainBP.route('/main',methods=['GET'])
def main():
    context = {}
    context["title"] = "青岛尚文"
    context["content"] = "尚文教学资源管理平台"
    return render_template('main/index.html', **context)



