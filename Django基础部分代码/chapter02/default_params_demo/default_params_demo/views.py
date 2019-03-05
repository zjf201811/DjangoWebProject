from django.http import HttpResponse

book_list = [
    '三国演义',
    '水浒传',
    '西游记',
    '红楼梦'
]

def books(request,page=0):
    return HttpResponse(book_list[page])