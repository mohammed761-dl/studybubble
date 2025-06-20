from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Group, Post
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)

    # Handle post submission by professors
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.role == 'professor':
            content = request.POST.get('content', '')
            file = request.FILES.get('file')
            image = request.FILES.get('image')
            Post.objects.create(
                group=group,
                author=request.user,
                content=content,
                file=file,
                image=image
            )
            return redirect('group-detail', pk=pk)

    posts = group.posts.order_by('-created_at')
    return render(request, 'groups/group_detail.html', {
        'group': group,
        'posts': posts
    })


@login_required
def my_groups(request):
    groups = Group.objects.filter(members=request.user)
    return render(request, 'groups/my_groups.html', {'groups': groups})


@login_required
def join_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.members.add(request.user)
    return redirect('group-list')

@login_required
def leave_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.members.remove(request.user)
    return redirect('group-list')

class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'groups/group_list.html'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description']
    template_name = 'groups/group_create.html'
    success_url = reverse_lazy('group-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name', 'description']
    template_name = 'groups/group_update.html'
    success_url = reverse_lazy('group-list')

class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/group_confirm_delete.html'
    success_url = reverse_lazy('group-list')
