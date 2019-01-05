class Configuration(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'you-ill-ever-guess'
    UPLOAD_FOLDER = '/home/loki/trainingpeaks/upload/'
    ALLOWED_EXTENSIONS = set(['tcx'])
    SQLALCHEMY_DATABASE_URI = 'mysql://root:qazwsx@127.0.0.1:3306/mymoves'
    SQLALCHEMY_BINDS = {
        'mymoves': 'mysql://root:qazwsx@127.0.0.1:3306/mymoves'
    }
    DATABASE_USER = 'root'
    DATABASE_PASSWORD = 'qazwsx'
    DATABASE = 'mymoves'
