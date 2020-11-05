from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,#固定
    'disable_existing_loggers':False,

    #ロガー設定
    'loggers': {
        #Djangoが使用するロガー
        'django': {
            'handlers':['console'],
            'level':'INFO',
        },
        #diaryアプリが使用するロガー
        'diary': {
            'handlers':['console'],
            'level':'DEBUG',
        }
    },
    #ハンドラの設定
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    #フォーマッタの設定
    'formatters': {
        'dev': {
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}