from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse
from .models import Message
from .forms import UserMessageForm, UserMessageFormFa
from django.contrib import messages


class Home(View):
	form_class = UserMessageForm
	template_name = 'blog/home.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		url = reverse('blog:home')
		if form.is_valid():
				cd = form.cleaned_data
				a = Message.objects.create(name=cd['name'], L_name=cd['L_name'], email=cd['email'], message_body=cd['message_body'])
				a.save()
				messages.success(request, 'your message submitted successfully', 'success')
				return redirect(f"{url}#msgSubmit")
		return render(request, self.template_name, {'form': form})

class Home_W(View):
	form_class = UserMessageForm
	template_name = 'blog/home-w.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		url = reverse('blog:home-w')
		if form.is_valid():
				cd = form.cleaned_data
				a = Message.objects.create(name=cd['name'], L_name=cd['L_name'], email=cd['email'], message_body=cd['message_body'])
				a.save()
				messages.success(request, 'your message submitted successfully', 'success')
				return redirect(f"{url}#msgSubmit")
		return render(request, self.template_name, {'form': form})	

class Home_FA(View):
	form_class = UserMessageFormFa
	template_name = 'blog/home-fa.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		url = reverse('blog:home-fa')
		if form.is_valid():
				cd = form.cleaned_data
				a = Message.objects.create(name=cd['name'], L_name=cd['L_name'], email=cd['email'], message_body=cd['message_body'])
				a.save()
				messages.success(request, 'پیام شما با موفقیت ثبت شد.', 'success')
				return redirect(f"{url}#msgSubmit")
		return render(request, self.template_name, {'form': form})		

class Home_FA_W(View):
	form_class = UserMessageFormFa
	template_name = 'blog/home-fa-w.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		url = reverse('blog:home-fa-w')
		if form.is_valid():
				cd = form.cleaned_data
				a = Message.objects.create(name=cd['name'], L_name=cd['L_name'], email=cd['email'], message_body=cd['message_body'])
				a.save()
				messages.success(request, 'پیام شما با موفقیت ثبت شد.', 'success')
				return redirect(f"{url}#msgSubmit")
		return render(request, self.template_name, {'form': form})		