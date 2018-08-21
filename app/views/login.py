#!/usr/bin/env python
# -*- coding=utf-8 -*-
from flask import render_template
from app.bpurls import authBP


@authBP.route('/login/', methods=['GET'])
def login():
    pass
