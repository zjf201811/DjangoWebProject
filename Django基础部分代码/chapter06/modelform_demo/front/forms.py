#encoding: utf-8
from django import forms
from .models import Book,User

class AddBookForm(forms.ModelForm):
    def clean_page(self):
        page = self.cleaned_data.get('page')
        if page > 100:
            raise forms.ValidationError('页数不能大于100！')
        return page

    class Meta:
        model = Book
        # fields和exclude必须定义一个
        fields = "__all__"
        # fields = ['title','page']
        # exclude = ['price']
        error_messages = {
            'page':{
                'required': '请传入page参数！',
                'invalid': '请输入一个可用的page参数！'
            },
            'title': {
                'max_length': 'title不能超过100个字符！'
            },
            'price': {
                'max_value': '图书价格不能超过100元！'
            }
        }

class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码输入不一致！')
        return cleaned_data

    class Meta:
        model = User
        exclude = ['password']
