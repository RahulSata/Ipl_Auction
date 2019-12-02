from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from test_app.models import *
import time

#from django.core.exceptions import ObjectDoesNotException
def login(request):
	c={}
	c.update(csrf(request))
	return render(request,'login.html',c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	

	if(username=="admin" and password=="admin111"):
		return HttpResponseRedirect('/backend/')

	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin/')
	else:
		return HttpResponseRedirect('/invalidlogin/')

	
def loggedin(request):
	own_players=player.objects.filter(player_team=request.user.username)
	players=player.objects.all().order_by('-player_time')
	try:
		p1=player.objects.get(player_status=True)
		return render(request,'loggedin.html',{"p1":p1,"n":range((18-request.user.login.team_cur_players)),"imagee": str(request.user.login.team_logo).split('/',1)[-1],"perteam":request.user.login,"players":players,"own_players":own_players})
	except player.DoesNotExist:
		return render(request,'loggedin.html',{"n":range((18-request.user.login.team_cur_players)),"imagee": str(request.user.login.team_logo).split('/',1)[-1],"perteam":request.user.login,"players":players,"own_players":own_players})

def get_all_players(request):
	players=player.objects.all()
	return render(request,'all_players.html',{"players": players})

def logout(request):
	auth.logout(request) 
	return render_to_response('logout.html')

def backend(request):
	players=player.objects.all()
	print(players)
	return render(request,'backend.html',{"players":players})

def add_price(request):
	cur_price=request.POST.get('hidden')
	cur_price=float(cur_price)
	if(cur_price>=10):
		amt = 1.0
	elif(cur_price>=4.0):
		amt=0.5
	elif(cur_price>=1.0):
		amt=0.1
	else:
		amt=0.05
	
	current=cur_price+amt
	p2= player.objects.filter(player_name=request.POST.get('playername'))
	p2.update(player_soldprice=current)
	p1= player.objects.get(player_name=request.POST.get('playername'))
	return render(request,'one_player.html',{"p1":p1})

def refresh(request):
	p3=player.objects.all()
	p3.update(player_status=False)
	p1=player.objects.get(player_name=request.POST.get('playername'))
	print(p1.player_name)
	p2=player.objects.filter(player_name=request.POST.get('playername'))
	p2.update(player_status=True)
	return render(request,'one_player.html',{"p1":p1})

def change_db(request):
	#print(request.user.username)
	t1=User.objects.get(first_name=request.POST.get('teamname'))
	team = Login.objects.filter(user=t1)
	team1 = Login.objects.get(user=t1)
	baught_players= team1.team_cur_players
	baught_players=baught_players + 1
	baught_ruppe  = team1.team_ruppe 
	baught_ruppe  = baught_ruppe - float(request.POST.get('playerprice'))
	print(baught_ruppe)
	team.update(team_cur_players=baught_players,team_ruppe=baught_ruppe)
	p1=player.objects.filter(player_name=request.POST.get('playername'))
	now=time.strftime("%Y-%m-%d %H:%M")
	p1.update(player_time=now)
	p1.update(player_status=False)
	p1.update(player_team=request.POST.get('teamname'))
	players=player.objects.all()
	return render(request,'backend.html',{"players":players})

def cur_bid(request):
	try:
		p1= player.objects.get(player_status=True)
		return render(request,'cur_bid.html',{"p1":p1})
	except player.DoesNotExist:
		own_players=player.objects.filter(player_team=request.user.username)
		players=player.objects.all().order_by('-player_time')
		return render(request)