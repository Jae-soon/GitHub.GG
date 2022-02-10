from project import dbModule


class inp():
    def update(self, ck_user, input_fwer, input_fwing, input_rep, input_present_date, input_id):
        # ck_user.past_fwer = ck_user.present_fwer
        # ck_user.present_fwer = input_fwer
        # ck_user.fwer_inc = abs(ck_user.present_fwer - ck_user.past_fwer)
        # ck_user.past_fwing = ck_user.present_fwing
        # ck_user.present_fwing = input_fwing
        # ck_user.fwing_inc = abs(ck_user.present_fwing - ck_user.past_fwing)
        # ck_user.past_rep = ck_user.present_rep
        # ck_user.present_rep = input_rep
        # ck_user.rep_inc = abs(ck_user.present_rep - ck_user.past_rep)
        # ck_user.past_date = ck_user.present_date
        # ck_user.present_date = input_present_date
        # db.session.commit()
        # user = User.query.filter(User.id == input_id)

        ########################################################################################
        db_class = dbModule.Database()
        fwer_inc = input_fwer - ck_user['present_fwer']
        fwing_inc = input_fwing - ck_user['present_fwing']
        rep_inc = input_rep - ck_user['present_rep']
        past_date = ck_user['present_date']
        update_sql = """UPDATE User SET past_fwer = '%d', present_fwer = '%d', fwer_inc = '%d',
            past_fwing = '%d', present_fwing = '%d', fwing_inc = '%d', past_rep = '%d', 
            present_rep = '%d', rep_inc = '%d', past_date = '%s', present_date = '%s' WHERE id = '%s'
        """ % (ck_user['present_fwer'], input_fwer, fwer_inc, ck_user['present_fwing'], input_fwing,
            fwing_inc, ck_user['present_rep'], input_rep, rep_inc, past_date, input_present_date, ck_user['id'])
        sql2 = "SELECT * FROM User WHERE id = '%s'"% (input_id)

        db_class.execute(update_sql)
        db_class.commit()
        user = db_class.executeAll(sql2)
        #########################################################################################
        return user

    def insert(self, input_id, input_name, input_bio, input_email, input_fwer, input_fwing, input_rep, input_present_date):
        # input_user = User(id=input_id, name=input_name, bio=input_bio, email=input_email, present_fwer=input_fwer,
        #                   past_fwer=0, fwer_inc=(input_fwer - 0), present_fwing=input_fwing, past_fwing=0,
        #                   fwing_inc=(input_fwing - 0), present_rep=input_rep, past_rep=0,
        #                   rep_inc=(input_rep - 0), past_date=None, present_date=input_present_date)
        # db.session.add(input_user)
        # db.session.commit()

        # user = User.query.filter(User.id == input_id)
        
        ########################################################################################
        db_class = dbModule.Database()
        sql = """INSERT INTO User (id, name, bio, email, past_fwer, present_fwer, fwer_inc, past_fwing, present_fwing, fwing_inc, past_rep, 
            present_rep, rep_inc, past_date, present_date) VALUES('%s', '%s', '%s', '%s', '%d',
            '%d', '%d', '%d', '%d', '%d', 
            '%d', '%d', '%d', '%s', '%s'
            );""" % (input_id, input_name, input_bio, input_email, 0, input_fwer, input_fwer, 0,
            input_fwing, input_fwing, 0, input_rep, input_rep, None, input_present_date)
        sql2 = "SELECT * FROM User WHERE id = '%s'" %(input_id)
        db_class.execute(sql)
        db_class.commit()
        user = db_class.executeAll(sql2)
        ########################################################################################
        return user