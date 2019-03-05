from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=3,label='标题',min_length=2,error_messages={"min_length":'标题字符段不符合要求！'},empty_value='控制')
    content = forms.CharField(widget=forms.Textarea,label='内容')
    email = forms.EmailField(label='邮箱')
    reply = forms.BooleanField(required=False,label='回复')