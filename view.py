from app import app
from app import db
from flask import render_template, request, redirect, url_for
from forms import *
import datetime
#from werkzeug.utils import secure_filename
#import os
#from tcx_parser import parsetcx
from modules import Moves, UserDetails, Plan
#import pymysql
#pymysql.install_as_MySQLdb


#@app.route('/', methods=['GET', 'POST'])
#def index():
#    form = Uploadform()
#    if request.method == "POST":
##TODO Here to do check of file type and file exist
#            filename = secure_filename(form.fileName.data.filename)
#            form.fileName.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#
#            parsetcx(os.path.join(app.config['UPLOAD_FOLDER'] + filename), 1)
#            return redirect(url_for('uploaded_file'))
##Test moves table.
#    moves =  Moves.query.order_by('Date desc', 'Time desc').limit(10).all()
#    return render_template('index.html', moves = moves, form = form, title = 'Mymoves', Header = 'Mymoves', Small = 'upload .tcx file')


# This is a sample chart with sample.js
#http://localhost/sample_chart
@app.route('/sample_chart')
def sample_chart():
    legend = 'Planned Weekly TSS'
#    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#    values = [160, 190, 210, 160, 190, 210, 230, 160, 210]
    
    values = Plan.query.all()

    return render_template('sample_chart.html', values = values, legend = legend)

@app.route('/')
#http://localhost/plan
@app.route('/plan', methods=['POST', 'GET'])
def plan():
    if request.method == 'POST':
        weeknumber = request.form['weeknumber']
        tsscompleted = request.form['tsscompleted']
        try:
            db.session.query(Plan).filter_by(Week=weeknumber).update({'TSScompl': tsscompleted})
            db.session.commit()
        except:
            print('can not do this')
        return redirect(url_for('plan'))
    form = UpdatePlan()

    value = Plan.query.all()

    legend = 'Weekly TSS plan'
    date_today = datetime.date.today()

    return render_template('plan.html', n = value, d = date_today, legend = legend, form=form)



#http://localhost/create_plan
@app.route('/create_plan', methods=['POST', 'GET'])
def create_plan():
    if request.method == 'POST':
        startdate = request.form['startdate']
        truestartdate = datetime.datetime.strptime(startdate, '%Y-%m-%d').date()
        tssplanweek = []
        for x in range(52):
            tssplanweek.append(request.form['tssplanweek' + str(x)])

        try:

            db.session.query(testPlan).delete()
            db.session.commit()
            for x in range(52):
                plan = Plan(Date=(truestartdate + datetime.timedelta(days=7)*x), Week= x + 1, TSSplan= tssplanweek[x], TSScompl=0)
                db.session.add(plan)
                db.session.commit()

        except:
            print('Can not do this')
        return redirect(url_for('plan'))
    form = CreatePlan()

    return render_template( 'create_plan.html', form=form)






#http://localhost/user
@app.route('/user')
def user():
    userdetail = UserDetails.query.first()
    return render_template('User.html', title = 'User Details', userdetail = userdetail)

#@app.route('/Edit', methods=['POST', 'GET'])
#def Edit():
#    form = UserEdit()
#    if form.validate_on_submit():
#        g.user.Name = form.Name.data
#        g.user.Age = form.Age.data
#        g.user.Weight = form.Weight.data
#        db.session.add(g.user)
#        db.session.commit()
#        flash('Your changes have been saved.')
#        return redirect(url_for('edit'))
#    else:
#        form.Name.data = g.user.Name
#        form.Age.data = g.user.Age
#        form.Weight.data = g.user.Weight
#    return render_template('Edit.html', form = form)


#@app.route('/login')
#def login():
#
#    return render_template("login.html", title = 'Login page', Header = 'Login page', Small = ' test login' )



#@app.route('/upload', methods=['POST', 'GET'])
#def upload():
#    form = Uploadform()
#    if request.method == "POST":
##TODO Here to do check of file type and file exist
#            filename = secure_filename(form.fileName.data.filename)
#            form.fileName.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#
#            parsetcx(os.path.join(app.config['UPLOAD_FOLDER'] + filename), 1)
#            return redirect(url_for('uploaded_file'))
#
#    return render_template("upload.html", form = form, title = 'Upload page', Header = 'Upload file', Small = 'upload .tcx file')



#@app.route('/uploaded_file')
#def uploaded_file():
#    return render_template('uploaded_file.html', title = 'upload successfull')



#def allowed_file(filename):
#    return '.' in filename and \
#        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
