from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q  # нужна для построения QuerySet "Магия"


# https://docs.djangoproject.com/en/4.2/topics/class-based-views/
# Основная страница.
class MainView(View):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        posts_forum = ForumPost.objects.all()

        paginator = Paginator(posts, 6)
        paginator_forum = Paginator(posts_forum, 6)

        page_number = request.GET.get('page')
        page_number_forum = request.GET.get('page')

        page_obj = paginator.get_page(page_number)
        page_obj_forum = paginator_forum.get_page(page_number_forum)

        context = {
            'page_obj': page_obj,
            'page_obj_forum': page_obj_forum,
        }
        return render(request, 'myblog/home.html', context=context)


# Страница поста.
class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        context = {
            'post': post,
            'last_posts': last_posts,
            'comment_form': comment_form
        }
        return render(request, 'myblog/post_detail.html', context=context)

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        context = {
            'comment_form': comment_form
        }
        return render(request, 'myblog/post_detail.html', context=context)


# Обработка формы регистрации.
class SignUpView(View):
    # Для гет запроса
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        context = {
            'form': form,
        }
        return render(request, 'myblog/signup.html', context=context)

    # Для пост запроса.
    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():  # Проверяем форму на валидность(соответствие)
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form,
        }
        return render(request, 'myblog/signup.html', context=context)


# Обработка формы авторизации !!!
class SignInView(View):
    # Обработка гет запроса
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        context = {
            'form': form,
        }
        return render(request, 'myblog/signin.html', context=context)

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
        context = {
            'form': form,
        }
        return render(request, 'myblog/signin.html', context=context)


# Вьюшка для обработки страницы обратной связи.
class FeedBackView(View):
    # Обработка GET Запроса
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        context = {
            'form': form,
            'title': 'Написать мне'  # То что пишет в хедере
        }
        return render(request, 'myblog/contact.html', context=context)

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
        context = {
            'form': form,
        }
        return render(request, 'myblog/contact.html', context=context)


# Обработка страницы благодарности.
class SuccessView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Спасибо'
        }
        return render(request, 'myblog/success.html', context=context)


# Обработка страницы поиска.
class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')  # АААААААААААА
        results = ""  # Без этой хрени выдаёт ошибку.
        if query:
            results = Post.objects.filter(
                # Ищем по заголовку 'h1' и специальному полю 'keyword'
                Q(h1__icontains=query) | Q(keyword__icontains=query)
            )
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'title': 'Поиск',
            'results': page_obj,
            'count': paginator.count
        }
        return render(request, 'myblog/search.html', context=context)


# Обработка страницы форуму
class ForumView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        posts_forum = ForumPost.objects.all()

        paginator = Paginator(posts, 6)
        paginator_forum = Paginator(posts_forum, 6)

        page_number = request.GET.get('page')
        page_number_forum = request.GET.get('page')

        page_obj = paginator.get_page(page_number)
        page_obj_forum = paginator_forum.get_page(page_number_forum)

        context = {
            'title': 'Форум',
            'page_obj': page_obj,
            'page_obj_forum': page_obj_forum,
        }
        return render(request, 'myblog/forum.html', context=context)


#
class ForumDetailView(View):
    def get(self, request):
        context = {
            'title': 'Форум'  # То что пишет в хедере
        }
        return render(request, 'myblog/forum.html', context=context)

    def post(self, request):
        context = {
            'title': 'Форум'  # То что пишет в хедере
        }
        return render(request, 'myblog/forum.html', context=context)
