from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import User, Friend
from django.contrib import messages

def index(request):
    return render(request, "poke/index.html")

def register(request):
    result = User.objects.validate_registration(request.POST)
    print result, type(result)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/dashboard')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def increment(request, user_id):
    poking2 = User.objects.get(id=request.session['user_id'])
    poked2 = User.objects.get(id=user_id)
    Friend.objects.create(poking = poking2, poked = poked2)
    return redirect('/dashboard')

def dashboard(request):
    try:
        request.session['user_id']
    except:
        return redirect('/')

    otherfriends = User.objects.exclude(id=request.session['user_id'])
    otherfriends_poked_you = User.objects.get(id=request.session['user_id']).poketake.all()

    counter = 0
    for count in otherfriends:
        if count.pokeamount.count > 0:
            counter += 1

    context = {
        "welcome": User.objects.get(id = request.session['user_id']),
        "otherfriends": otherfriends.all(),
        "counter": counter,
    }
    return render(request, 'poke/dashboard.html', context)
