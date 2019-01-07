from app import app
from app import db
from flask import render_template, request, redirect, url_for
#from forms import Uploadform, UserEdit
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

@app.route('/plan')
def plan():
	value = Plan.query.all()
	return render_template( 'plan.html', n = value)

@app.route('/create_plan')
def create_plan():
	return render_template( 'create_plan.html')

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
