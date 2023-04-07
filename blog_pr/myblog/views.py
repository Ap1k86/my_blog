from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q  # нужна для построения QuerySet "Магия"


# Основная страница.
class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'myblog/home.html', context={
            'page_obj': page_obj
        })


# Страница поста.
class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'myblog/post_detail.html', context={
            'post': post,
            'last_posts': last_posts,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'myblog/post_detail.html', context={
            'comment_form': comment_form
        })


# Обработка формы регистрации.
class SignUpView(View):
    # Для гет запроса
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })

    # Для пост запроса.
    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():  # Проверяем форму на валидность(соответствие)
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signup.html', context={
            'form': form,
        })


# Обработка формы авторизации !!!
class SignInView(View):
    # Обработка гет запроса
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })

    # Обработка пост запроса.
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'myblog/signin.html', context={
            'form': form,
        })


# Вьюшка для обработки страницы обратной связи.
class FeedBackView(View):
    # Обработка GET Запроса
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'myblog/contact.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    # Обработка POST запроса.
    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(f'От {name} | {subject}', message, from_email, ['7082265@gmail.com'])  # Почта КУДА отправлять
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'myblog/contact.html', context={
            'form': form,
        })


# Обработка страницы благодарности.
class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myblog/success.html', context={
            'title': 'Спасибо'
        })


# Обработка страницы поиска.
class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')  # АААААААААААА
        results = ""
        if query:
            results = Post.objects.filter(
                Q(h1__icontains=query) | Q(content__icontains=query)  # Добавить Teg для поиска.
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myblog/search.html', context={
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        })
