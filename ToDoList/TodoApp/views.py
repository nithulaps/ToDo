from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
from .forms import TodoForm

# Create your views here.

#-----------------ADD TITLE WITH DISPLAY------------------
def index(request):
	listall=todo.objects.filter(check_status=False).order_by('title')
	form=TodoForm()

	if request.method=='POST':
		form=TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	content={'listall':listall,'form':form}
	return render(request,"todo.html",content)

#-----------------UPDATE TITLE ------------------
def updatelist(request,idno):
	task=todo.objects.get(id=idno)
	form=TodoForm(instance=task)
	if request.method=='POST':
		form=TodoForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect('/') 
	content={'form':form}
	return render(request,"update.html",content)

#-----------------DELETE TITLE ------------------
# def deletelist(request,idno):
# 	item=todo.objects.get(id=idno)
# 	if request.method=='POST':
# 		item.delete()
# 		return redirect('/')
# 	content={'item':item}
# 	return render(request,"delete.html",content)

