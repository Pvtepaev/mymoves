class Configuration(object):
    HOST = '0.0.0.0'
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'you-ill-ever-guess'
    UPLOAD_FOLDER = '/home/loki/trainingpeaks/upload/'
    ALLOWED_EXTENSIONS = set(['tcx'])
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:qazwsx@192.168.14.3:3306/mymoves'
#    SQLALCHEMY_BINDS = {
#        'mymoves': 'mysql://root:qazwsx@192.168.14.4:3306/mymoves'
#    }
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'qazwsx'
    DATABASE = 'mymoves'
