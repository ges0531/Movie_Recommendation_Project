from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):  # 정보 저장

    class Meta:
        model = User
        fields = ('username', 'email', )



class CustomAuthenticationForm(AuthenticationForm):  # 정보 인증 (예외케이스로 생각)
    class Meta:
        model = User
