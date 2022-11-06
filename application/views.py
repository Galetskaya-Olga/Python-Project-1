from datetime import datetime
from urllib.parse import parse_qs
from django.shortcuts import redirect, render
from .forms import AddComment, AddOrder
from .models import Author, Comment, Order


# Create your views here.
def home(request):
    print('НОМЕ PAGE')
    return render(request, 'home.html')


def order(request):  #все кнопки заказов
    print('ORDER PAGE')
    order = Order()
    return render(request, 'order.html', {'order': order})


def add_order(request):
    print('ADD ORDER PAGE')
    if request.method == 'POST':
        add_order=AddOrder(request.POST, request.FILES)
        if add_order.is_valid():
            order = Order()
            order.author = Author.objects.get(email=request.user.email)
            order.date_of_order = datetime.now()
            order.order_adress = add_order.cleaned_data['order_adress']
            order.order_tel = add_order.cleaned_data['order_tel']
            order.order_description = add_order.cleaned_data['order_description']
            order.order_type = add_order.cleaned_data['order_type']
            order.save()
            return redirect('done_order')
    else:
        add_order = AddOrder() # создается пустая форма для заказа
    return render(request, 'add_order.html', {'add_order': add_order})    

def done_order(request):
    print('DONE ORDER PAGE')
    done_order = Order()
    return render(request, 'done_order.html', {'done_order': done_order})


def comments(request):  #все отзывы
    all_comments = Comment.objects.all().order_by('-date_of_creation')
    print('COMMENTS PAGE')
    return render(request, 'comments.html', {'comments': all_comments})
 

def comment(request, id):  #один комментарий-отзыв по id
    try:
        one_comment = Comment.objects.get(id=id)
    except:
        one_comment = ''    
    print(f'1 COMMENT PAGE with id {id}')
    return render(request, 'comment.html', {'comment': one_comment})


def add_comment(request):
    if request.method == "POST":
        add_comment = AddComment(request.POST, request.FILES)  # создается новая форма с данными
        if add_comment.is_valid():  # Проверка формы
            comment = Comment()
            comment.author = Author.objects.get(email=request.user.email)
            comment.date_of_creation = datetime.now()
            comment.title = add_comment.cleaned_data['title']
            #comment.subtitle = add_comment.cleaned_data['subtitle']
            comment.content = add_comment.cleaned_data['content']
            if comment.image:
                comment.image = add_comment.cleaned_data['image']
            comment.save()
            return redirect('comments')
    else:
        add_comment = AddComment() # создается пустая форма
    return render(request, 'add_comment.html', {'add_comment': add_comment})