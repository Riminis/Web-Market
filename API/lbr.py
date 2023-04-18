from API.lbr_settings import *


db_session.global_init("../db/all.db")


def create_user(login, password, email, status='usr', tgm='Z'):
    user = User()
    user.login = login
    user.hashed_password = password_crypt(password)
    user.email = email
    user.status = status
    if tgm != 'Z':
        user.telegram_id = tgm
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()


def get_login(id=0, email=''):
    db_sess = db_session.create_session()
    if email != '':
        for i in db_sess.query(User).filter(User.email == email):
            db_sess.close()
            return i.__repr__().split(' *** ')[1]
    elif id != 0:
        for i in db_sess.query(User).filter(User.id == id):
            db_sess.close()
            return i.__repr__().split(' *** ')[1]
    db_sess.close()
    return None


def get_email(id=0, login=''):
    db_sess = db_session.create_session()
    if login != '':
        for i in db_sess.query(User).filter(User.login == login):
            db_sess.close()
            return i.__repr__().split(' *** ')[2]
    elif id != 0:
        for i in db_sess.query(User).filter(User.id == id):
            db_sess.close()
            return i.__repr__().split(' *** ')[2]
    db_sess.close()
    return None


def get_id(login, email, password):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.login == login, User.email == email).first()

    if password_encrypt(user.__repr__().split(' *** ')[3]) == password:
        db_sess.close()
        return user.__repr__().split(' *** ')[0]

    db_sess.close()
    return 'Неверный пароль'


def get_password(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return password_encrypt(i.__repr__().split(' *** ')[3])


def get_status(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[4]


def get_telegram_id(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[5]


def get_current_id(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[6]


def get_history_id(id):
    db_sess = db_session.create_session()
    for i in db_sess.query(User).filter(User.id == id):
        db_sess.close()
        return i.__repr__().split(' *** ')[7]


def change_param(id, param, new_val):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    if param == 1:
        user.login = new_val
    elif param == 2:
        user.email = new_val
    elif param == 3:
        user.hashed_password = password_crypt(new_val)
    elif param == 4:
        user.status = new_val
    elif param == 5:
        user.telegram_id = new_val
    elif param == 6:
        user.current_id = new_val
    elif param == 7:
        user.history_id = new_val
    db_sess.commit()
    db_sess.close()