from django.urls import path, re_path

from . import views
from .views import *

urlpatterns = [
    path('', glavn, name='glavn'),
    path('glavn', glavn, name='glavn'),

    path('amyr', amyr, name='amyr'),
    path('azov', azov, name='azov'),
    path('anapa', anapa, name='anapa'),
    path('arzamas', arzamas, name='arzamas'),
    path('bataysk', bataysk, name='bataysk'),
    path('blagov', blagov, name='blagov'),
    path('bogych', bogych, name='bogych'),
    path('bolgol', bolgol, name='bolgol'),
    path('volgogr', volgogr, name='volgogr'),
    path('vogogrobl', vogogrobl, name='vogogrobl'),
    path('volgod', volgod, name='volgod'),
    path('voron', voron, name='voron'),
    path('voronobl', voronobl, name='voronobl'),
    path('gelendg', gelendg, name='gelendg'),
    path('gorod', gorod, name='gorod'),
    path('gork', gork, name='gork'),
    path('groz', groz, name='groz'),
    path('dagom', dagom, name='dagom'),
    path('gelez', gelez, name='gelez'),
    path('irk', irk, name='irk'),
    path('irkobl', irkobl, name='irkobl'),
    path('kam', kam, name='kam'),
    path('kisl', kisl, name='kisl'),
    path('kost', kost, name='kost'),
    path('krasn', krasn, name='krasn'),
    path('krasnobl', krasnobl, name='krasnobl'),

    path('mezmay', mezmay, name='mezmay'),
    path('miha', miha, name='miha'),
    path('nevin', nevin, name='nevin'),
    path('nign', nign, name='nign'),
    path('nignobl', nignobl, name='nignobl'),
    path('news', news, name='news'),
    path('novocher', novocher, name='novocher'),
    path('travel', travel, name='travel'),
    path('pyatig', pyatig, name='pyatig'),
    path('regions', regions, name='regions'),

    path('rostovdon', rostovdon, name='rostovdon'),
    path('rostovobl', rostovobl, name='rostovobl'),
    path('salsk', salsk, name='salsk'),
    path('piter', piter, name='piter'),
    path('sochi', sochi, name='sochi'),
    path('stavr', stavr, name='stavr'),
    path('tagan', tagan, name='tagan'),
    path('talakan', talakan, name='talakan'),
    path('taman', taman, name='taman'),
    path('tnda', tnda, name='tnda'),
    path('chechn', chechn, name='chechn'),
    path('login', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('me', me, name='me'),
    path('logout', doLogout, name='logout'),
    path('buytyr', buytyr, name='buytyr'),



]

