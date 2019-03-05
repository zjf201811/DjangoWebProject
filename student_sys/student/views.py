from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse,redirect
from .models import Student
from .forms import StudentForm
from django.http.request import QueryDict
from django.views import View


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students
        }
        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect(reverse('index'))
        context=self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)




# def index(request):
#     students = Student.get_all()
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('index'))
#     else:
#         form = StudentForm()
#     context = {
#         'student': students,
#         'form': form
#     }
#     return render(request, 'index.html', context=context)
