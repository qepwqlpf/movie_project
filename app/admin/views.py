#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    : views.py
# @author  : Jaxon
# @software: PyCharm
# @datetime: 9/26 026 下午 07:34


from app.admin import admin
from flask import render_template, redirect, url_for


# 调用蓝图（定义视图）
# 定义控制面板视图
@admin.route("/")
def index():
    return render_template("admin/index.html")


# 定义登录视图
@admin.route("/login/")
def login():
    return render_template("admin/login.html")


# 定义登出视图
@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.login"))


# 定义修改密码视图
@admin.route("/pwd/")
def pwd():
    return render_template("admin/pwd.html")


# 定义添加标签视图
@admin.route("/tag/add/")
def tag_add():
    return render_template("admin/tag_add.html")


# 定义标签列表视图
@admin.route("/tag/list/")
def tag_list():
    return render_template("admin/tag_list.html")


# 定义添加电影视图
@admin.route("/movie/add/")
def movie_add():
    return render_template("admin/movie_add.html")


# 定义电影列表视图
@admin.route("/movie/list/")
def movie_list():
    return render_template("admin/movie_list.html")


# 定义添加预告视图
@admin.route("/preview/add/")
def preview_add():
    return render_template("admin/preview_add.html")


# 定义预告列表视图
@admin.route("/preview/list/")
def preview_list():
    return render_template("admin/preview_list.html")


# 定义会员列表视图
@admin.route("/user/list/")
def user_list():
    return render_template("admin/user_list.html")


# 定义查看会员视图
@admin.route("/user/view/")
def user_view():
    return render_template("admin/user_view.html")


# 定义评论列表视图
@admin.route("/comment/list/")
def comment_list():
    return render_template("admin/comment_list.html")


# 定义收藏列表视图
@admin.route("/moviecol/list/")
def moviecol_list():
    return render_template("admin/moviecol_list.html")


# 定义操作日志列表视图
@admin.route("/oplog/list/")
def oplog_list():
    return render_template("admin/oplog_list.html")


# 定义管理员登录日志列表视图
@admin.route("/adminloginlog/list/")
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")


# 定义会员登录日志列表视图
@admin.route("/userloginlog/list/")
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")


# 定义添加权限视图
@admin.route("/auth/add/")
def auth_add():
    return render_template("admin/auth_add.html")


# 定义权限列表视图
@admin.route("/auth/list/")
def auth_list():
    return render_template("admin/auth_list.html")


# 定义添加角色视图
@admin.route("/role/add/")
def role_add():
    return render_template("admin/role_add.html")


# 定义角色列表视图
@admin.route("/role/list/")
def role_list():
    return render_template("admin/role_list.html")
