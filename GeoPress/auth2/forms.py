from django.contrib.auth.forms import UserCreationForm # Django 内置了用户注册表单
from .models import User # 继承的扩展用户

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User #此处指自建的auth2.User
        fields = ("username", "email")#UserCreationForm 中只指定了 fields = ("username",)，即用户名，此外还有两个字段密码和确认密码在 UserCreationForm 的属性中指定。所以默认的表单渲染后只有用户名（username）、密码、确认密码三个表单控件。我们还希望用户注册时提供邮箱地址，所以在 fields 中增加了 email 字段。