#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import jsonify
from app.common.code import Code


def return_result(data=None, code=Code.SUCCESS):
    return jsonify({
        "code": code,
        "data": data,
        "msg": Code.msg.get(code),
    })