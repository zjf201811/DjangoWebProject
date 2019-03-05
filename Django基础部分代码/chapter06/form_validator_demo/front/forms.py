#encoding: utf-8
from django import forms
from django.core import validators
from .models import User

class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors

class MyForm(BaseForm):
    # email = forms.EmailField(error_messages={"invalid":"请输入正确的邮箱！"})
    # price = forms.FloatField(error_messages={"invalid":"请输入浮点类型！"})
    # personal_website = forms.URLField(error_messages={"invalid":"请输入正确格式的个人网站！",'required':"请输入个人网站！"})

    # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确格式的邮箱！')])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确格式的手机号码！')])


class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}',message='请输入正确格式的手机号码！')])
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message='%s已经被注册！'%telephone)
        # 如果验证没有问题，一定要记得把telephone返回回去
        return telephone

    # {
    #     'telephone':[
    #         '请输入正确格式的手机号码！',
    #         '请输入手机号码！'
    #     ],
    #     'pwd1': [
    #         '密码最大长度不能超过16',
    #         '两次密码不一致！'
    #     ]
    # }


    def clean(self):
        # 如果来到了clean方法，说明之前每一个字段都验证成功了
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码输入不一致！')
        return cleaned_data
