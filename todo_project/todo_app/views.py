from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo:list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo:list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_app/todo_confirm_delete.html'
    success_url = reverse_lazy('todo:list')

def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo:list')