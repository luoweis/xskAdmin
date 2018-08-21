#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template
from app.bpurls import teachingBP
from app.common.xsk_mysql_utils import *


@teachingBP.route('/students/', methods=['GET'])
def students():
    context = {}
    context["title"] = "运维开发平台2.0"
    context["content"] = "DevOps2.0"
    student = {
        "student_name": "张三",
        "student_age": 20,
        "student_sex": 0,
        "student_phone": "13678726548",
        "student_ID": "370684199403249876",
        "student_info": "记录学生信息，但未激活",
        "status": 0
    }

    waring = add_student_single(**student)
    students_10 = get_students_limit(10)
    context["students_10"] = students_10
    context["warning"] = waring
    return render_template('teachingResources/index.html', **context)
