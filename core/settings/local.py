from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', 
                default='tqf=kn-qld^p5ln!8=*qca_t4x1ch4=#5@u-ev9-f9fcrhlp_6')

DEBUG = env.bool('DJANGO_DEBUG', default=True)