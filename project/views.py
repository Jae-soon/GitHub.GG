from flask import Blueprint, session, escape, make_response, render_template, request, redirect, url_for
import pymysql
from project import dbModule
from project import crawler
from project import inp

bp = Blueprint('main', __name__, url_prefix='/')
user_list = list()

@bp.route('/')
def input():
    return render_template('input.html')

@bp.route('/search_history')
def search_history():
    id = request.cookies.get('userId')
    user_list.append(id)
    user_list.reverse()
    history_list = user_list[:10]
    return render_template('find.html', history_list=history_list)

@bp.route('/search_init')
def search_init():
    user_list.clear()
    return render_template('find.html', user_list=user_list)

@bp.route('/user', methods=['POST', 'GET'])
def user_detail():
    if request.method == 'GET':
        # 입력된 값
        input_id = request.args.get('user_id')
        
        get = crawler.crawler()
        dml = inp.inp()
        db = dbModule.Database()

        driver = get.driver(input_id)

        input_name = get.name(driver)
        input_bio = get.bio(driver)
        input_email = get.email(driver)
        input_fwer = get.fwer(driver)
        input_fwing = get.fwing(driver)
        input_rep = get.rep(driver)
        input_present_date = get.date()
        driver.quit()

        # input values
        count = 0
        sql = "SELECT * FROM User"
        check_user = db.executeAll(sql)
        
        for ck_user in check_user:
            count += 1
            if ck_user['id'] == input_id:
                user = dml.update(ck_user, input_fwer, input_fwing, input_rep, input_present_date, input_id)
                resp = make_response(render_template('user_list.html', user=user))
                resp.set_cookie('userId', input_id)
                return resp

        if count == len(check_user):
            user = dml.insert(input_id, input_name, input_bio, input_email, input_fwer, input_fwing, input_rep, input_present_date)
            resp = make_response(render_template('user_list.html', user=user))
            resp.set_cookie('userId', input_id)
            return resp