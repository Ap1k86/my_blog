from django.urls import path, re_path
from .views import *
from django.contrib.auth.views import LogoutView  # Встроенный метод для выхода(Она же работает и на вход) LOL
from django.conf import settings
from django.conf.urls.static import static
from myblog import views

# as_view() тут нужен для регистрации класса.
urlpatterns = [
                  # Маршрут: главной страницы
                  path('', MainView.as_view(), name='index'),

                  # Маршрут: страницы детализации поста.!!! Два маршрута делаю для себя !!!
                  path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
                  # re_path(r'^blog/(?P<slug>\D+)', PostDetailView.as_view(), name='post_detail'),

                  # Маршрут: страницы регистрации
                  # path('signup/', SignUpView.as_view(), name='signup'),
                  re_path(r'^signup', SignUpView.as_view(), name='signup'),

                  # Маршрут: страницы авторизации
                  # path('signin/', SignInView.as_view(), name='signin'),
                  re_path(r'^signin/', SignInView.as_view(), name='signin'),

                  # Маршрут: выход из учетной записи, внутренний метод работы с моделью User,2 варианта.
                  # path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
                  re_path(r'^signout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
                          name='signout'),

                  # Маршрут: страницы обратной связи
                  path('contact/', FeedBackView.as_view(), name='contact'),
                  # re_path(r'^contact/', FeedBackView.as_view(), name='contact'),

                  # Маршрут: страницы благодарности за написанное письмо.
                  path('contact/success/', SuccessView.as_view(), name='success'),
                  # re_path(r'^contact/success/', SuccessView.as_view(), name='success'),

                  # Маршрут: страницы поиска, 2 варианта.
                  # path('search/', SearchResultsView.as_view(), name='search_results'),
                  re_path(r'^search/', SearchResultsView.as_view(), name='search_results'),

                  # Маршрут: страницы поиска, 2 варианта.
                  # path('search/', SearchResultsView.as_view(), name='search_results'),
                  re_path(r'^search_forum/', SearchResultsForumView.as_view(), name='search_results_forum'),

                  # Маршрут: страницы форума, 2 варианта.
                  path('forum/', ForumView.as_view(), name='forum'),
                  # re_path(r'^forum', ForumView.as_view(), name='forum'),

                  # Маршрут: страницы благодарности за написанный пост.
                  path('forum/add_theme/success_post/', SuccessPostView.as_view(), name='success_post'),
                  # re_path(r'^forum/success/', SuccessPostView.as_view(), name='success_post'),

                  # Маршрут: Страница добавления поста на форум.
                  path('forum/add_theme/', AddTheme.as_view(), name='theme_add'),
                  # re_path(r'^forum/add_theme/', AddTheme.as_view(), name='theme_add'),

                  # # Маршрут: страницы детализации поста на форуме.
                  path('forum/<slug>/', ForumDetailView.as_view(), name='forum_detail'),
                  # re_path(r'^forum/(?P<slug>\D+)', ForumDetailView.as_view(), name='forum_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
