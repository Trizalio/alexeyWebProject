from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.auth.models import User
from ask.models import question, answer
import random
import datetime

class Command(BaseCommand):
    args = '<ask_id ask_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        if args[0] == 'create':
            self.create(args[1], args[2])
        else:
            print "Command not found!"

    def create(self, model, count):
        if model == "User":
            self.createUser(count)
        elif model == "question":
            self.createQuestion(count)
        elif model == "answer":
            self.createAnswer(count)
        else:
            print "Not found model!"
    def createUser(self, count):
        for i in range(int(count)):
            name = random.choice(["Bender1","Bender2","Bender3","Bender4","Bender5"]) + str(i + 120) + str(i + 120)
            email = random.choice(["gmail"]) + random.choice(["yandex"]) + '@' + 'mail.ru'
            password = random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"])
            now = datetime.datetime.now()
            user = User.objects.create_user(username = name, email = email, password = password)
            user.save()
            print ("User created!")
    def createQuestion(self, count):
        for i in range(int(count)):
            now = datetime.datetime.now()
            header1 = random.choice("wvwvdwwferfdzfs") + random.choice("qdkgorjcscddfsfsdfl") + random.choice("dqjfiqjfksvjwm") + str(i)
            id = 1
            question1 = question(header = header1, text = "ololololololo",  creationdate = now, creator_id = id)
            question1.save()
            print ("Question created!")
    def createAnswer(self, count):
        for i in range(int(count)):
            now = datetime.datetime.now()
            mycontent = random.choice("weklnvfwklnvwlkvnw") + random.choice("fewljvowevn") + random.choice("fiojweoifhwdw") + str(i)
            creator_q = 1
            question_q = random.choice(["11","15","16","17","18"])
            answer1 = answer(text = mycontent, question_id = question_q, creator_id = creator_q, date = now, correctanswer = 0)
            answer1.save()
            print ("Answer created!")

