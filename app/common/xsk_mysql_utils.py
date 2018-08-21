#!/usr/bin/env python
# -*- coding=utf-8 -*-
from app.models.XSK import XSKStudent,XSKTeacher,XSKClass
from app import db


def add_student_single(**kwargs):
    """
    一次只增加一个学生的信息，写入数据库中
    :param kwargs:
    :return:
    """
    """判断添加的元素是否存在"""
    waring = ""
    if XSKStudent.query.filter_by(student_ID=kwargs.get("student_ID")).all():
        return {"msg": "该学生已经注册了信息"}
    try:
        xsk_student = XSKStudent(**kwargs)
        db.session.add(xsk_student)
        db.session.commit()
    except Exception as error:
        return {"error_msg": error}
    else:
        return {"msg": "添加成功"}

def add_student_multiple(*args):
    pass


def get_students_limit(num=10):
    """
    定义获取学生表信息的数量
    :param num:
    :return:
    """
    students_10 = XSKStudent.query.limit(num)
    return students_10
