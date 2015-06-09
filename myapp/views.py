from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib import auth
from .models import Subject
import graph
from django.template.context_processors import csrf

# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def login_required(func):
   print 'Start login_req'
   def func_wrapper(request):
       if not request.user.is_authenticated():
           print 'Sending redirect'
           return HttpResponseRedirect("/myapp/login")
       else: return func(request)
   return func_wrapper


def login(request):
    if request.method == 'GET':
        return render(request,'myapp/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/myapp/mainpage")
        else:
            return HttpResponseRedirect("/myapp/errpage_not_auth")

def back_to_login(request):
    return HttpResponseRedirect("/myapp/login/")

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/myapp/back_to_login/")

@login_required
def mainpage(request):
    return render(request,'myapp/mainpage.html')

def errpage_not_auth(request):
    return render(request,'myapp/errpage_not_auth.html')

@login_required
def plan_page(request):
    chosen_list = []
    for key in xrange(0, 20, 2):
        if unicode(key) in request.POST:
            chosen_list.append(int(request.POST[unicode(key)]))
        else: break
    output, plan, norm, za_spec, obr = graph.create_plan(request.POST['specialization'], request.POST['department'], chosen_list)

    template = loader.get_template('myapp/plan_page.html')
    context = RequestContext(request, {'output': output, 'plan': plan, 'norm': norm, 'za_spec': za_spec, 'obr': obr})
    return HttpResponse(template.render(context))

@login_required
def choice(request):
    choice_list = graph.get_subjects_for_choice(request.POST['specialization'], request.POST['department'])
    template = loader.get_template('myapp/choice.html')
    choice_t = []
    for i in xrange(0, len(choice_list), 2):
        choice_t.append([i, choice_list[i], choice_list[i + 1]])
    context = RequestContext(request, {'choice_t': choice_t})
    return HttpResponse(template.render(context))

from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from models import User


class RegistrationForm(UserCreationForm):
	username = forms.CharField(
		label='Username',
		help_text='',
		max_length=50,
		required=True,
	)
	email = forms.EmailField(
		label='Email',
		help_text='',
		required=True,
	)

	password1 = forms.CharField(
		label='Password',
		help_text='',
		required=True,
		widget=forms.PasswordInput,
	)

	password2 = forms.CharField(
		label='Password confirmation',
		help_text='',
		required=True,
		widget=forms.PasswordInput,
	)
	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'password1',
			'password2',
		)
	def clean_password1(self):
		password1 = self.cleaned_data['password1']
		q_letters = len(password1)
		if q_letters < 6:
			raise forms.ValidationError("Password can not be less than 6 symbols.")
		return password1

	def clean_username(self):
		username = self.cleaned_data['username']
		q_letters = len(username)
		if q_letters < 3:
			raise forms.ValidationError("Login can not be less than 3 symbols.")
		return username


class RegisterFormView(FormView):

    form_class = RegistrationForm

    success_url = "login/"

    template_name = "myapp/registration.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)


@login_required
def contacts(request):
    return render(request,'myapp/contacts.html')

@login_required
def info(request):
    return render(request,'myapp/info.html')

@login_required
def export_to_excel(request):
    return