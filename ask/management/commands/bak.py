from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.auth.models import User
from ask.models import question, answer
import random
import datetime

class Command(BaseCommand):
    args = '<ask_id ask_id ...>'
    help = 'Closes the specified poll for voting'
    def handle(self, *args):
        if args[0] == "User":
            self.createUser(args[1])
        elif args[0] == "question":
            self.createQuestion(args[1])
        elif args[0] == "answer":
            self.createAnswer(args[1])
        else:
            print "Not found model!"
    def createUser(self, count):
        for i in range(int(count)):
            name = random.choice(["Bender1","Bender2","Bender3","Bender4","Bender5"]) + str(i + 120)
            email = random.choice(["gmail"]) + random.choice(["yandex"]) + '@' + 'mail.ru'
            password = random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"]) + random.choice(["qwerty"])
            now = datetime.datetime.now()
            user = User.objects.create_user(username = name, email = email, password = password,)
            user.save()
            print ("User created!")
    def createQuestion(self, count):
        for i in range(int(count)):
            now = datetime.datetime.now()
            header1 = random.choice("wvwvdwwferfdzfs") + random.choice("qdkgorjcscddfsfsdfl") + random.choice("dqjfiqjfksvjwm") + str(i)
            creator_id = 322
            question = question(header = header1, text = "ololololololo",  creationdate = now, creator = creator_id)
            question.save()
            print ("Question created!")
    def createAnswer(self, count):
        for i in range(int(count)):
            now = datetime.datetime.now()
            mycontent = random.choice("weklnvfwklnvwlkvnw") + random.choice("fewljvowevn") + random.choice("fiojweoifhwdw") + str(i)
            creator_q = 322
            question_id = 1024
            answer = answer(text = mycontent, creator = creator_id, questionid = question_id, date = now, correctanswer = 0)
            answer.save()
            print ("Answer created!")

