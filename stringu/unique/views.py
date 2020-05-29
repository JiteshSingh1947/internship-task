
from django.shortcuts import render
from .forms import HomeForm
\

def get(request):
	form=HomeForm()
	return render(request, 'home/home.html', { 'form': form })

def ask_string(request):
	text=None
	form = HomeForm(request.POST or None ) 
	if form.is_valid():
		text=form.cleaned_data['post']
		all_freq = {} 
  
		for i in text: 
			if i in all_freq: 
				all_freq[i] += 1
			else: 
				all_freq[i] = 1
  
# printing result  
		print ("Count of all characters in strings are is :\n "
                                        +  str(all_freq)) 


	args={ 'form': form ,'text':text,'all_freq':all_freq}
	return render(request,  'home/home.html', args)
	