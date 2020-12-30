from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Dress
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DressForm,DressUpdateForm
from django.contrib.auth.decorators import login_required

class DressListView(ListView):
	model = Dress

class DressDetailView(DetailView):
	model = Dress

class DressDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Dress
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		return True

class DressCreateView(LoginRequiredMixin,CreateView):
	model = Dress
	fields = [
		'name' ,
		'price' ,
		'quantity',
		'image',
		'description' ,
		'variety',
	]



@login_required
def DressUpdateView(request,pk):
	if request.method == 'POST':
		form = DressUpdateForm(request.POST,request.FILES,instance=Dress.objects.get(pk=pk))
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DressUpdateForm()
	cnxt= {
	'form' : form
	}
	return render(request,'dress/update.html',cnxt)

def search(request,variety):
	object_list = Dress.objects.filter(variety=variety)
	cnxt = {
	'object_list' : object_list ,
	}
	# count = Dress.objects.filter(variety=variety).count()
	# if object_list.count() > 1:
	# 	return render(request,'dress/search.html',cnxt)
	# else :
	# 	return render(request,'dress/dress_list.html',cnxt)
	return render(request,'dress/dress_list.html',cnxt)


def about(request):
	return render(request,'dress/about.html',{})
def home(request):
	object_list = Dress.objects.order_by('-id')[:3]
	cnxt = {
	'object_list' : object_list ,
	}
	return render(request,'dress/home.html',cnxt)