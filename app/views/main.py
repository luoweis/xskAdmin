#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template
from app.bpurls import mainBP



@mainBP.route('/', methods=['GET'])
@mainBP.route('/main', methods=['GET'])
def main():
    context = {}
    context["title"] = "XSK"
    context["content"] = "管理平台"
    return render_template('main/index.html', **context)



