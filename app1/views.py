# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from app1.models import *
from app1.forms import *

def main(request):
	if request.method == "POST":
		if "confirmLogin" in request.POST:
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data["username"]
				password = form.cleaned_data["password"]
				user = auth.authenticate(username=username, password=password)
				if user is not None and user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('/aquariums/')
				else:
					return render(request, 'login.html', {'error': True})
		if "confirmRegister" in request.POST:
			form = RegisterForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data["username"]
				password = form.cleaned_data["password"]
				user = User.objects.create_user(username=username, password=password)
		return HttpResponseRedirect('/')
	else:
		req=request.GET.get("act")
		if req=="login":
			return render(request, 'login.html')
		if req=="logout":
			auth.logout(request)
			return HttpResponseRedirect('/')
		if req=="reg":
			return render(request, 'register.html')
	return render(request, 'main.html', RequestContext(request))

@login_required
def aquariums(request):
	form = NewAquarium()
	if request.method == "POST":
		if "addNewAquarium" in request.POST:
			aquarium = NewAquarium(request.POST).save(commit=False)
			aquarium.User = request.user
			aquarium.save()
		'''
			form = NewAquarium(request.POST)
			if form.is_valid():
				name = form.cleaned_data["name"]
				volume = form.cleaned_data["volume"]
				newAquarium=Aquarium.objects.create(User=request.user, Name=name, Volume=volume)
				newAquarium.save()
		'''
		if "editAquarium" in request.POST:
			form = EditAquarium(request.POST)
			if form.is_valid():
				name = form.cleaned_data["name"]
				volume = form.cleaned_data["volume"]
				aquarium=Aquarium.objects.get(id=request.GET.get("id"))
				aquarium.Name=name
				aquarium.Volume=volume
				aquarium.save()
	else:
		req=request.GET.get("act")
		req2=request.GET.get("id")
		if req=="new":
			return render(request, 'newaquarium.html', {'form': form})
#			return HttpResponseRedirect('/aquariums/new')
		if req=="delete":
			req3=request.GET.get("answer")
			if not req3:
				return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user),'req2': req2, 'action': "delete", 'description': "Удалить?", 'action_id': 1, 'ref': request.META.get('HTTP_REFERER')})
			else:
				if req3=="yes":
					Aquarium.objects.filter(id=req2).delete()
				return HttpResponseRedirect('./')
		if req=="edit":
			if req2:
				aquarium=Aquarium.objects.get(id=req2)
				if aquarium:
					name=aquarium.Name
					volume=aquarium.Volume
					return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user), 'id': req2, 'action': "edit", 'action_id': 2, 'ref': request.META.get('HTTP_REFERER')})
#		if request.POST.get('iterate'):
#			return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user) })
		if req=="clean":
			req3=request.GET.get("answer")
			if not req3:
				return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user),'req2': req2, 'action': "clean", 'description': "Очистить аквариум?", 'action_id': 1, 'ref': request.META.get('HTTP_REFERER')})
			else:
				if req3=="yes":
					FishList=Fish.objects.filter(Aquarium=Aquarium.objects.filter(id=req2))
					if FishList:
						FishList.delete()
				return HttpResponseRedirect('./')
		if req=="fishlist":
			if req2:
				req3=request.GET.get("page")
				if not req3:
					req3=1
				FishList=Fish.objects.filter(Aquarium=Aquarium.objects.get(id=req2))
				paginator=Paginator(FishList, 15)
				try:
					FishPage=paginator.page(req3)
				except PageNotAnInteger:
					contacts = paginator.page(1)
				except EmptyPage:
					contacts = paginator.page(paginator.num_pages)
				if int(req3)==1:
					back=paginator.num_pages
				else:
					back=int(req3)-1
				if int(req3)==paginator.num_pages:
					next=1
				else:
					next=int(req3)+1
				return render(request, 'fishlist.html', {'req2': req2, 'back': back, 'next': next, 'fish_list': FishPage, 'fishTypes': FishType.objects.all()})
		if req=="iterate":
			if req2:
				aquarium=Aquarium.objects.get(id=req2)
				aquarium.Iterate(1)
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	
	return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user), 'action_id': 0, 'form': form})

@login_required
def fish(request):
	if request.method == "POST":
		if "addFishToList" in request.POST:
			form = NewFish(request.POST)
			if form.is_valid():
				selectedType = form.cleaned_data["fishTypeList"]
				count = form.cleaned_data["count"]
				req=request.GET.get("id")
				for i in range(0, count):
					newFish=Fish.objects.create(FishTypeKey=selectedType, Aquarium=Aquarium.objects.get(id=req))
					newFish.Name="Fish"+str(newFish.id)
					newFish.save()
				return HttpResponseRedirect('/aquariums/?act=fishlist&id='+str(req))
		if "fishType" in request.POST:
			form = NewFish(request.POST)
			if form.is_valid():
				selectedType = form.cleaned_data["fishTypeList"]
				return render(request, "viewfishtype.html", {"fishType": selectedType, "req3": request.GET.get("aqua")})
		if "fishToAquarium" in request.POST:
			aquariumList=Aquarium.objects.filter(User=request.user)
			aquarium=int(request.POST.get('select'))
			thisFish=Fish.objects.get(id=request.GET.get("id"))
			thisFish.Aquarium=aquariumList[aquarium-1]
			thisFish.save()
			req=request.GET.get("aqua")
			return HttpResponseRedirect('/aquariums/?act=fishlist&id='+str(req))
	else:
		req=request.GET.get("act")
		req2=request.GET.get("id")
		if req=="new":
			req3=request.GET.get("aqua")
			if req3:
				form=NewFish()
				return render(request, 'newfish.html', {'req3': req3, 'form': form})
#			return HttpResponseRedirect('/aquariums/new')
		if req=="delete":
			req3=request.GET.get("answer")
			if not req3:
				return render(request, 'delete.html', {'req2': req2, 'action': "delete", 'description': "Удалить?", 'ref': request.META.get('HTTP_REFERER')})
			else:
				if req3=="yes":
					aquarium = Fish.objects.get(id=req2).Aquarium
					Fish.objects.filter(id=req2).delete()
				return HttpResponseRedirect("/aquariums/?act=fishlist&id="+str(aquarium.id))
		if req=="toaquarium":
			if req2:
				aquarium = Fish.objects.get(id=req2).Aquarium
				req3 = aquarium.id	
				return render(request, 'fishtoaquarium.html', {'aquarium_list': Aquarium.objects.filter(User=request.user), 'req2': req2, 'req3': req3 })
#		if request.POST.get('iterate'):
#			return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user) })
		if req=="fishlist":
			if req2:
				return render(request, 'fishlist.html', {'req2': req2})
	
	return render(request, 'aquariums.html', {'aquarium_list': Aquarium.objects.filter(User=request.user) })

@login_required
def fishChangeAquarium(request, fish_id):
	thisFish=Fish.objects.get(id=fish_id)
	thisAquarium=Aquarium.objects.get(id=thisFish.Aquarium.id)
	if thisAquarium.User <> request.user:
		raise Http404()
		
	aquariumList=Aquarium.objects.filter(User=request.user)
#		aquariumList.exclude(thisAquarium)
	if request.method == 'POST':
		if request.POST.get('toFishList'):
			return HttpResponseRedirect('/fishlist/'+ str(thisAquarium.id))
		if request.POST.get('changeAquarium'):
			id=int(request.POST.get('select'))
			thisFish.Aquarium=aquariumList[id-1]
			thisFish.save()
			return HttpResponseRedirect('/fishlist/'+ str(thisAquarium.id))
		
		return HttpResponseRedirect('/')
	else:
		return render(request, 'fish.html', { 'aquarium_list': aquariumList })

#	raise Http404()
'''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
'''