from django.urls import path, re_path


from users.views import RegistrUserView, AllUsersView, DeletePutPatchUserView

# urls модуля users для работы с пользователями
urlpatterns = [
    path('register/', RegistrUserView.as_view()),
    path('<int:id>/', DeletePutPatchUserView.as_view()),
    path('', AllUsersView.as_view()),
]