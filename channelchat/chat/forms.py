from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import channel, chat
from django import forms

#Sign up form
class addUserForm(ModelForm):
	username = forms.CharField(label=False, widget = forms.TextInput(attrs = {'placeholder': 'Username'}) )
	email = forms.CharField(label=False, widget = forms.TextInput(attrs = {'placeholder': 'Email'}) )
	password = forms.CharField(label=False, widget = forms.PasswordInput(attrs = {'placeholder': 'Password'}) )
	confirm_password= forms.CharField(label=False, widget=forms.PasswordInput(attrs = {'placeholder': 'Confirm Password'}))
	class Meta:
		model = User
		fields = ['username','email', 'password',]

	def clean(self):
		cleaned_data = super(addUserForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)


#creating channel form
class addChannelForm(ModelForm):
	name = forms.CharField(label=False, widget = forms.TextInput(attrs = {'placeholder': 'Name of channel'}))
	class Meta:
		model = channel
		fields = ['name']

#creating chat form
class addChatForm(ModelForm):
	content = forms.CharField(label=False, widget = forms.TextInput(attrs = {'placeholder': 'Type message', 'class':'write_msg'}) )
	class Meta:
		model = chat
		fields = ['content']
