from django import forms
from .models import Message

class UserMessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('name', 'L_name', 'email', 'message_body')
		labels = {
			'name' : '',
			'L_name' : '',
			'email' : '',
			'message_body' : ''
		}
		widgets = {
			'name' : forms.TextInput(attrs={'placeholder': 'First Name' ,'class' : 'contact-name form-control'}),
			'L_name' : forms.TextInput(attrs={'placeholder': 'Last Name' ,'class' : 'contact-email form-control'}),
			'email' : forms.EmailInput(attrs={'placeholder': 'Your Email' ,'class' : 'contact-subject form-control'}),
			'message_body' : forms.Textarea(attrs={'placeholder': 'Your Message' ,'class' : 'contact-message'}),
		}

class UserMessageFormFa(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('name', 'L_name', 'email', 'message_body')
		labels = {
			'name' : '',
			'L_name' : '',
			'email' : '',
			'message_body' : ''
		}
		widgets = {
			'name' : forms.TextInput(attrs={'placeholder': 'نام' ,'class' : 'contact-name form-control'}),
			'L_name' : forms.TextInput(attrs={'placeholder': 'نام خانوادگی' ,'class' : 'contact-email form-control'}),
			'email' : forms.EmailInput(attrs={'placeholder': 'ایمیل' ,'class' : 'contact-subject form-control'}),
			'message_body' : forms.Textarea(attrs={'placeholder': 'متن پیام' ,'class' : 'contact-message'}),
		}