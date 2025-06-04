from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Group
from django.views.generic import DetailView
from .forms import PostForm

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        context['posts'] = self.object.post_set.all()
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.group = self.get_object()
            post.author = request.user
            post.save()
        return self.get(request, *args, **kwargs)

@login_required
def join_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.members.add(request.user)
    return redirect('group_list')

class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description', 'is_private']
    template_name = 'groups/create.html'
    success_url = '/groups/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
