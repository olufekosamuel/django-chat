from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import channel, chat 
from django.contrib.auth import authenticate, login, logout as chat_logout
from django.contrib.auth.hashers import make_password
from .forms import addUserForm, addChannelForm, addChatForm
from rest_framework import status, viewsets
from .serializers import addChatSerializer

#Api view for creating and viewing chats
class IndexViewSet(viewsets.ModelViewSet):
	queryset = chat.objects.all()
	serializer_class = addChatSerializer

#index view handles list of channels and chats in each channel
def index(request, channel_id=None):
	user = request.user.id
	if(request.method == "POST"):
		form = addChatForm(request.POST)
		if request.user.is_authenticated:
			chan = channel.objects.get(id = channel_id)
			if form.is_valid():
				chat = form.save(commit=False)
				chat.channel = chan
				chat.user = request.user
				chat.save()
				return HttpResponseRedirect('/channel/'+channel_id)
			else:
				form = addUserForm()
		else:
			return HttpResponse('you cannot access this page!')
		context = {
			'form': form,
		}
	else:
		if channel_id is not None:
			channels = channel.objects.filter(id = channel_id)
			chat = True
			form = addChatForm()
		else:
			channels = channel.objects.all()
			chat = False
			form = None

		context = {
			'channels': channels,
			'form': form,
			'chat': chat,
		}
		
	return render(request, 'index.html', context)

#registration page for users
def add_user(request):
	if(request.method == "POST"):
		form = addUserForm(request.POST)
		if form.is_valid():
			
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
		
			user.password = make_password(password)
			user.save()
			return HttpResponseRedirect('/')
		else:
			form = addUserForm()

	else:
		form = addUserForm()

	return render(request, 'registration/register.html', {'form': form})

#for creating channels
def create_channel(request):
	if(request.method == "POST"):
		form = addChannelForm(request.POST)
		if form.is_valid():
			channel = form.save(commit=False)
			form.save()	
			return HttpResponseRedirect('/')
		else:
			form = addChannelForm()
	else:
		form = addChannelForm()

	return render(request, 'registration/create_channel.html', {'form': form})

#handles logging users out
def logout(request):
	chat_logout(request)
	return HttpResponseRedirect('/')