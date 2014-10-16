from django.shortcuts import render_to_response, get_object_or_404
from ask.models import question, answer
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from ask.forms import questionForm, answerForm
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from django.contrib import auth

def home(request, str1 = 'anonim'):
        q_all = question.objects.all().order_by('-creationdate')
        if str1 == 'popular':
            q_all = question.objects.all().order_by('-creationdate').order_by('-rating')
        paginator = Paginator(q_all, 20)
        q_list = paginator.page(1).object_list
        page = request.GET.get('page')
        try:
                q_list = paginator.page(page)
        except PageNotAnInteger:
                q_list = paginator.page(1)
        except EmptyPage:
                q_list = paginator.page(paginator.num_pages)
        if request.user.is_authenticated():
            if str1 == 'ok_register':
                return render_to_response('base.html', {'q_list': q_list,
                                                    'ok_register': True,
                                                    'anonim': False,
                                                    'username': request.user.username,
                                                    'id': request.user.id,
                                                    })
            if str1 == 'ok_login':
                return render_to_response('base.html', {'q_list': q_list,
                                                        'username': request.user.username,
                                                        'id': request.user.id,
                                                        'ok_login': True,
                                                        'anonim': False,
                                                        })
            if str1 == 'ok_question':
                return render_to_response('base.html', {'q_list': q_list,
                                                        'username': request.user.username,
                                                        'id': request.user.id,
                                                        'ok_question': True,
                                                        'anonim': False,

                                                        })
            else:
                return render_to_response('base.html', {'q_list': q_list,
                                                        'username': request.user.username,
                                                        'id': request.user.id,
                                                        'anonim': False,
                                                       })
        if str1 == 'error_add_question':
            return render_to_response('base.html', {'q_list': q_list,
                                                    'anonim': True,
                                                    'error_add_question': True,
                                                    })
        if str1 == 'error_add_answer':
            return render_to_response('base.html', {'q_list': q_list,
                                                    'username': request.user.username,
                                                    'id': request.user.id,
                                                    'anonim': True,
                                                    'error_add_answer': True,
                                                     })

        if str1 == 'ok_logout':
            return render_to_response('base.html', {'q_list': q_list,
                                                    'anonim': True,

                                                    })
        else:
            return render_to_response('base.html', {'q_list': q_list,
                                                    'anonim': True,
                                                    })

def profile(request, username_id):
    user = User.objects.get(pk =  username_id)
    q_all = question.objects.filter(creator = username_id).order_by('-creationdate')
    a_all = answer.objects.filter(creator = username_id).order_by('-date')
    paginator_q = Paginator(q_all, 20)
    paginator_a = Paginator(a_all, 30)
    q_list = paginator_q.page(1).object_list
    a_list = paginator_a.page(1).object_list
    page = request.GET.get('page')
    try:
        q_list = paginator_q.page(page)
        a_list = paginator_a.page(page)
    except PageNotAnInteger:
        q_list = paginator_q.page(1)
        a_list = paginator_a.page(1)
    except EmptyPage:
        q_list = paginator_q.page(paginator_q.num_pages)
        a_list = paginator_a.page(paginator_a.num_pages)
    if request.user.is_authenticated():
        return render_to_response('profile_user.html', {'q_list': q_list,
                                                        'a_list': a_list,
                                                        'anonim': False,
                                                        'username': request.user.username,
                                                        'name': user.username,
                                                        'email': user.email,
                                                        'id': request.user.id,
                                                        })
    else:
        return render_to_response('profile_user.html', {'q_list': q_list,
                                                        'a_list': a_list,
                                                        'anonim': True,
                                                        'name': user.username,
                                                        'email': user.email,
                                                       })

def add_question(request):
    if request.user.is_authenticated():
        now = datetime.datetime.now()
        if request.method == 'POST':
            form = questionForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                question1 = question(header = cd['title'], text = cd['content'], creator = request.user, rating = 0, creationdate = now)
                question1.save()
                return HttpResponseRedirect('/home/ok_question/')
            else:
                context= {'form': form,
                          'username': request.user.username,
                          'id': request.user.id}

                context.update(csrf(request))
                return render_to_response('add_question.html', context)
        else:
            form = questionForm()
            context =  {'form': form,
                        'username': request.user.username,
                        'id': request.user.id,
                        }
            context.update(csrf(request))
            return render_to_response('add_question.html', context)
    else:
        return HttpResponseRedirect('/home/error_add_question/')

def add_answer(request, question_id, str2 = 0):
    now = datetime.datetime.now()
    a_all = answer.objects.filter(question_id = question_id)
    q = question.objects.get(pk = question_id)
    paginator = Paginator(a_all, 30)
    a_list = paginator.page(1).object_list
    page = request.GET.get('page')
    try:
        a_list = paginator.page(page)
    except PageNotAnInteger:
        a_list = paginator.page(1)
    except EmptyPage:
        a_list = paginator.page(paginator.num_pages)
    if request.user.is_authenticated():
        if str2 == 'ok_answer':
            context = {
                'question_id': question_id,
                'a_list': a_list,
                'q': q,
                'ok_answer': True,
                'username': request.user.username,
                'id': request.user.id,
                'anonim': False,
                }
            context.update(csrf(request))
            return  render_to_response('add_answer.html', context)
        if request.method == 'POST':
            form = answerForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                answer1 = answer(text = cd['content'], question_id = question_id,  creator = request.user, rating = 0, date = now, correctanswer = 0)
                answer1.save()
                return HttpResponseRedirect('/add/answer/'+ str(question_id)+'/ok_answer/')
            else:
                context = {'form': form,
                           'question_id':question_id,
                           'a_list':a_list,
                           'q': q,
                           'anonim': False,
                           'username': request.user.username,
                           'id': request.user.id,
                           }
                context.update(csrf(request))
                return render_to_response('add_answer.html', context)
        else:
            form = answerForm()
            context = {'form': form,
                       'question_id': question_id,
                       'a_list': a_list,
                       'q': q,
                       'anonim': False,
                       'username': request.user.username,
                       'id': request.user.id,

                       }
            context.update(csrf(request))
            return render_to_response('add_answer.html', context)
    if  str2 == 'anonim':
        context = {'question_id':question_id,
                   'a_list':a_list,
                   'q': q,
                   'anonim': True,
                   }
        context.update(csrf(request))
        return render_to_response('add_answer.html', context)
    else:
        return HttpResponseRedirect('/home/error_add_answer/')

def about(request):
    return render_to_response('about.html')

def error404(request):
    return render_to_response('404.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], "email@email.email", cd["password1"])
            user.is_active = True
            user.save()
            auth.login(request, auth.authenticate(username = cd['username'], password = cd['password1']))
            return HttpResponseRedirect('/home/ok_register/')
        else:
            context = {'form': form}
            context.update(csrf(request))
            return render_to_response('registration/create_user.html', context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        context.update(csrf(request))
        return render_to_response('registration/create_user.html', context)
