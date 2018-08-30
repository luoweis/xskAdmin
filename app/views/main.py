#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template
from app.bpurls import mainBP
from flask_login import login_required

@mainBP.route('/', methods=['GET'])
@mainBP.route('/main', methods=['GET'])
# @login_required
def main():
    context = {}
    context["title"] = "XSK"
    context["content"] = "管理平台"
    context["mds"] = [
        {
            "level": "bg-info",
            "title": "TOTAL PV",
            "count": "45K",
            "info": "测试数据，PV"
        },{
            "level": "bg-danger",
            "title": "TOTAL UV",
            "count": "20K",
            "info": "测试数据，UV"
        },{
            "level": "bg-success",
            "title": "TOTAL IP",
            "count": "10K",
            "info": "测试数据，IP"
        },{
            "level": "bg-info",
            "title": "TOTAL hit",
            "count": "100K",
            "info": "测试数据，hit"
        },

    ]
    return render_template('main/index.html', **context)



