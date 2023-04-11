from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import LogoutView  # Встроенный метод для выхода(Она же работает и на вход) LOL
from django.conf import settings

# as_view() тут нужен для регистрации класса.
urlpatterns = [
    # Маршрут: главной страницы
    path('', MainView.as_view(), name='index'),

    # Маршрут: !!! Два маршрута делаю для себя !!!
    # path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    re_path(r'^blog/(?P<slug>\D+)', PostDetailView.as_view(), name='post_detail'),

    # Маршрут: страницы регистрации, 2 варианта пути.
    # path('signup/', SignUpView.as_view(), name='signup'),
    re_path(r'^signup', SignUpView.as_view(), name='signup'),

    # Маршрут: страницы авторизации, 2 варианта.
    # path('signin/', SignInView.as_view(), name='signin'),
    re_path(r'^signin/', SignInView.as_view(), name='signin'),

    # Маршрут: выхода из учетной записи при нажатии на 'Выход', внутренний метод работы с моделью User,2 варианта.
    # path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout', ),
    re_path(r'^signout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),

    # Маршрут: страницы обратной связи, 2 варианта.
    # path('contact/', FeedBackView.as_view(), name='contact'),
    re_path(r'^contact/', FeedBackView.as_view(), name='contact'),

    # Маршрут: страницы благодарности за написанное письмо.
    # path('contact/success/', SuccessView.as_view(), name='success'),
    re_path(r'^contact/success/', SuccessView.as_view(), name='success'),

    # Маршрут: страницы поиска, 2 варианта.
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    re_path(r'^search/', SearchResultsView.as_view(), name='search_results'),
]
