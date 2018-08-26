#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template
from app.bpurls import teachingBP
from app.common.xsk_mysql_utils import *
from app.common.util import *
from flask import request


@teachingBP.route('/students/', methods=['GET'])
def students():
    context = {}
    context["title"] = "xsk-学生管理"
    context["content"] = ''
    context["warning"] = ""
    return render_template('teachingResources/index.html', **context)


@teachingBP.route('/show/students/', methods=['GET'])
def students_show():
    """
    获取学生的数量
    :return:
    """

    """提取参数"""
    pageSize = request.args.get("pageSize")
    offset = request.args.get("offset")
    sort = request.args.get("sort")
    sortOrder = request.args.get("sortOrder")
    """根据偏移量和每一页人数进行数据库的查询工作"""
    students = get_students_onepage(pageSize, offset)

    """格式化数据"""
    def format(student):
        return {
            "student_id": student.id,
            "student_name": student.student_name,
            "student_age": student.student_age,
            "student_sex": get_sex(student.student_sex),
            "student_phone": student.student_phone,
            "student_ID": student.student_ID,
            "student_info": student.student_info,
            "student_create": student.create_datetime,
        }

    rows = list(map(format, students))
    total = get_students_total()
    return json.dumps({
        "rows": rows,
        "total": total,
    }, cls=DateEncoder)


# @teachingBP.route('/students/add/', methods=['GET'])
def student_add():
    """
    表单的方式提交学生信息
    :return:
    """
    student = {
        "student_name": "测试2",
        "student_age": 22,
        "student_sex": 0,
        "student_phone": "13608932761",
        "student_ID": "370887199208237621",
        "student_info": "CCIE，缴费，等待开课通知",
        "status": 1
    }
    res = add_student_single(**student)
    return res


@teachingBP.route('/students/adds/', methods=['GET'])
def student_adds():
    """
    表单的方式批量提交学生信息
    :return:
    """
    students =[{
        "student_name": "测试5",
        "student_age": 23,
        "student_sex": 0,
        "student_phone": "149148181116",
        "student_ID": "37068419960825872236",
        "student_info": "记录学生信息，信息不详",
        "status": 0
    }, {
        "student_name": "测试6",
        "student_age": 29,
        "student_sex": 1,
        "student_phone": "149148181117",
        "student_ID": "37068419960825872237",
        "student_info": "记录学生信息，信息不详",
        "status": 0
    }, {
        "student_name": "测试7",
        "student_age": 32,
        "student_sex": 1,
        "student_phone": "149148181118",
        "student_ID": "37068419960825872238",
        "student_info": "记录学生信息，信息不详",
        "status": 0
    }, {
        "student_name": "测试8",
        "student_age": 32,
        "student_sex": 1,
        "student_phone": "149148181119",
        "student_ID": "37068419960825872239",
        "student_info": "记录学生信息，信息不详",
        "status": 0
    }, {
        "student_name": "测试9",
        "student_age": 22,
        "student_sex": 1,
        "student_phone": "149148181120",
        "student_ID": "3706841996082587224X",
        "student_info": "记录学生信息，信息不详",
        "status": 0
    },
    ]
    res = add_student_multiple(students)
    return str({"msg": res})