from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.auth.models import User
from ask.models import question, answer
from django.core.management import setup_environ
from mysite1.settings import DATABASES
import random
import datetime
import os
import sys
setup_environ(settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite1.settings")
for i in range(int(10)):
    name = random.choice(["Bender1","Bender2","Bender3","Bender4","Bender5"])
    email = random.choice(["gmail"]) + random.choice(["yandex"]) + '@' + 'mail.ru'
    password = random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"])
    now = datetime.datetime.now()
    user = User.objects.create_user(username = name, email = email, password = password, time_joined = now)
    user.save()
for i in range(int(10)):
    now = datetime.datetime.now()
    header1 = random.choice("wvwvdwwferfdzfs") + random.choice("qdkgorjcscddfsfsdfl") + random.choice("dqjfiqjfksvjwm") + str(i)
    creator_id = 322
    question = question(header = header1, text = "ololololololo",  creationdate = now, creator = creator_id)
    question.save()
for i in range(int(10)):
    now = datetime.datetime.now()
    mycontent = random.choice("weklnvfwklnvwlkvnw") + random.choice("fewljvowevn") + random.choice("fiojweoifhwdw") + str(i)
    creator_q = 322
    question_id = 322
    answer = answer(text = mycontent, creator = creator_id, questionid = question_id, date = now, correctanswer = 0)
    answer.save()
#please work!!!!
