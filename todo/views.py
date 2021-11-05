from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoModel
# Create your views here.

# Retrieve
def index(request):
	todos 		= TodoModel.objects.all()
	
	context = {
		"todos":todos
	}
	return render(request, 'index.html',context)

# Create
def createTodo(request):
	if request.method =="POST":
		body 		= request.POST.get("body")
		new_todo  	= TodoModel.objects.create(todo_body=body)
		new_todo.save()
		return redirect("todo:index")

# Update
def updateTodo(request):
	if request.method =='POST':
		body 		= request.POST.get('todo_id')
		update_todo	= TodoModel.objects.get(id=body)
		update_todo.finished = True
		update_todo.save()
		return redirect('todo:index')

# Delete
def deleteTodo(request):
	if request.method =='POST':
		body 		= request.POST.get('todo_id')
		delete_todo = TodoModel.objects.get(id=body)
		delete_todo.delete()
		return redirect('todo:index')


	
