from .forms import CommentForm
from django.views.generic import TemplateView
from django.shortcuts import redirect,render


class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')
        title = request.POST.get('title')

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.title = title
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
            'title': title,
        }
        return self.render_to_response(context)

    # def get(self, request,*args,**kwargs):
    #     context = {}
    #     comment_form = CommentForm(request.POST)
    #     context.update({
    #         'form': comment_form
    #     })
    #     return render(request, self.template_name, context=context)
