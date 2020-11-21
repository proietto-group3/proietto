from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from inbox.models import Message
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

@login_required
def inbox(request):
    user = request.user
    self = None
    # user = self.get.Object()
    messages = Message.get_messages(self, user=user)
    # user = self.get.Object()
    active_user = None  # nie wiem czy to zadziala, czy jest potrzebne, ani gdzie system rozpoznaje ze uzytkownik jest aktywny (user.Profile) #TODO ({% if user.is_authenticated %}
    incoming = None
    context = {}
    if messages:
        message = messages[0]
        active_user = message["user"].username
        incoming = Message.objects.filter(user=user, recipient=message["user"])
        incoming.update(is_read=True)

        for message in messages:
            if message["username"].username == active_user:
                message["unread"] = 0

        context = {"incoming": incoming, "messages": messages, "active_user": active_user, }

    template = loader.get_template("inbox/inbox.html")

    return HttpResponse(template.render(context, request))


@login_required
def incoming(request, username):
    user = request.user
    messages = Message.get_messages(user=user)
    active_incoming = username
    incoming = Message.objects.filter(user=user, recipient__username=username)
    incoming.update(is_read=True)

    for message in messages:
        if message["user"].username == username:
            message["unread"] = 0

    context = {"incoming": incoming, "messages": messages, "active_incoming": active_incoming, }

    template = loader.get_template("inbox/inbox.html")

    return HttpResponse(template.render(context, request))


@login_required
def send_message(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == 'POST':
        to_user = User.objects.get(username=to_user_username)
        Message.send_message(from_user, to_user, body)
        return redirect('inbox')
    else:
        HttpResponseBadRequest()


@login_required
def user_search(request):
    query = request.GET.get('q')
    context = {}

    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Pagination
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
        }

    template = loader.get_template('inbox/search_user.html')

    return HttpResponse(template.render(context, request))


@login_required
def NewConversation(request, username):
    from_user = request.user
    body = "Says Hello!"

    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('usersearch')
    if from_user != to_user:
        Message.send_message(from_user, to_user, body)
    return redirect('inbox')
