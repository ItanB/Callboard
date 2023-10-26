from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ad, Reply
from .forms import AdForm, ReplyForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import response
from django.urls import reverse
from .filters import AdFilter


class AdList(ListView):
    model = Ad
    ordering = '-id'
    template_name = 'list.html'
    context_object_name = 'ads'
    paginate_by = 10


class AdDetail(DetailView):
    model = Ad
    template_name = 'addetails.html'
    context_object_name = 'fullad'


class CreateAd(LoginRequiredMixin, CreateView):
    form_class = AdForm
    model = Ad
    template_name = 'create.html'
    context_object_name = 'create'
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.save()
        return super().form_valid(form)


class AdUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdForm
    model = Ad
    template_name = 'adupdate.html'
    context_object_name = 'update'
    success_url = reverse_lazy("list")


class AdDelete(LoginRequiredMixin, DeleteView):
    model = Ad
    template_name = 'addelete.html'
    success_url = reverse_lazy("list")


class ReplyList(ListView):
    model = Reply
    form_class = ReplyForm
    template_name = 'replies.html'
    context_object_name = 'replies'


class ReplyCreate(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'up_create.html'
    context_object_name = 'reply_create'

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.author = self.request.user
        reply.save()
        return super().form_valid(form)


class ReplyUpdate(LoginRequiredMixin, UpdateView):
    model = Reply
    fields = '__all__'
    template_name = 'up_create.html'
    context_object_name = 'reply_update'


def delete_reply(self, pk):
    reply = Reply.objects.get(id=pk)
    reply.delete()
    return redirect('board')


@login_required()
def accept_reply(request, pk):
    reply = Reply.objects.get(id=pk)
    reply.accept = True
    reply.save()
    send_mail(
        subject=f'Отлик принят.',
        message=f'Ваш отклик на пост "{response.ads.title}" принят',
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[response.user.email]
    )
    return HttpResponseRedirect(reverse('response_list'))


def delete_post(self, pk):
    reply = Reply.objects.get(id=pk)
    reply.delete()
    return redirect('board')


class PostSearch(ListView):
    model = Ad
    ordering = 'title'
    template_name = 'search.html'
    context_object_name = 'search'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.filterset = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AccountDetail(LoginRequiredMixin, ListView):
    model = Ad
    fields = '__all__'
    template_name = 'account.html'
    context_object_name = 'account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts_to_author = Ad.objects.filter(author=self.request.user)
        context['posts_to_author'] = posts_to_author
        return context
