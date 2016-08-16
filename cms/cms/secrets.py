# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@rg9pkvll(j&l2uw(g^-k0qa0h*)m11efzr=_f#p6214-#nb6g'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forum',
        'USER': 'nrogers',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
