from django.contrib.auth import logout, authenticate, login

from django.shortcuts import render, redirect
from django.views.generic import CreateView

from blog.forms import LoginForm, RegisterForm, CommentForm
from blog.models import Comments


# Create your views here.


def glavn(request):
    return render(request, 'Site1/Главная.html')


def azov(request):
    return render(request, 'Site1/Азов.html')


def amyr(request):
    return render(request, 'Site1/Амурская-область.html')


def anapa(request):
    return render(request, 'Site1/Анапа.html')


def arzamas(request):
    return render(request, 'Site1/Авторизация.html')


def bataysk(request):
    return render(request, 'Site1/Батайск.html')


def blagov(request):
    return render(request, 'Site1/Благовещенск.html')


def bogych(request):
    return render(request, 'Site1/Богучар.html')


def bolgol(request):
    return render(request, 'Site1/Большое-Голоустное.html')


def volgogr(request):
    return render(request, 'Site1/Волгоград.html')


def vogogrobl(request):
    return render(request, 'Site1/Волгоградская-область.html')


def volgod(request):
    return render(request, 'Site1/Волгодонск.html')


def voron(request):
    return render(request, 'Site1/Воронеж.html')


def voronobl(request):
    return render(request, 'Site1/Воронежская-область.html')


def gelendg(request):
    return render(request, 'Site1/Геленджик.html')


def gorod(request):
    return render(request, 'Site1/Городец.html')


def gork(request):
    return render(request, 'Site1/Горячий-Ключ.html')


def groz(request):
    return render(request, 'Site1/Грозный.html')


def dagom(request):
    return render(request, 'Site1/Дагомыс.html')


def gelez(request):
    return render(request, 'Site1/Железноводск.html')


def irk(request):
    return render(request, 'Site1/Иркутск.html')


def irkobl(request):
    return render(request, 'Site1/Иркутская-область.html')


def kam(request):
    return render(request, 'Site1/Камышин.html')


def kisl(request):
    return render(request, 'Site1/Кисловодск.html')


def kost(request):
    return render(request, 'Site1/Костомарово.html')


def krasn(request):
    return render(request, 'Site1/Краснодар.html')


def krasnobl(request):
    return render(request, 'Site1/Краснодарский-край.html')


def mezmay(request):
    return render(request, 'Site1/Мезмай.html')


def miha(request):
    return render(request, 'Site1/Михайловка.html')


def nevin(request):
    return render(request, 'Site1/Невинномысск.html')


def nign(request):
    return render(request, 'Site1/Нижний-Новгород.html')


def nignobl(request):
    return render(request, 'Site1/Нижегородская-область.html')


def news(request):
    return render(request, 'Site1/Новости.html')


def novocher(request):
    return render(request, 'Site1/Новочеркасск.html')


def travel(request):
    return render(request, 'Site1/Путеводитель.html')


def pyatig(request):
    return render(request, 'Site1/Пятигорск.html')


def regions(request):
    return render(request, 'Site1/Регионы.html')


def rostovdon(request):
    return render(request, 'Site1/Ростов-на-Дону.html')


def rostovobl(request):
    return render(request, 'Site1/Ростовская-область.html')


def salsk(request):
    return render(request, 'Site1/Сальск.html')


def piter(request):
    return render(request, 'Site1/Санкт-Петербург.html')


def sochi(request):
    return render(request, 'Site1/Сочи.html')


def stavr(request):
    return render(request, 'Site1/Ставропольский-край.html')


def tagan(request):
    return render(request, 'Site1/Таганрог.html')


def talakan(request):
    return render(request, 'Site1/Талакан.html')


def taman(request):
    return render(request, 'Site1/Тамань.html')


def tnda(request):
    return render(request, 'Site1/Тында.html')


def chechn(request):
    return render(request, 'Site1/Чеченская-республика.html')


def buytyr(request):

    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
    else:
        form = CommentForm()
    return render(request, 'Site1/Купить-тур.html', {'comments': Comments.objects.all(), 'form': form})







def base(request):
    return render(base, 'base.html')



def me(request):
    # если не авторизован, то редирект на страницу входа
    if not request.user.is_authenticated:
        return redirect('login')
    # рендерим шаблон и передаем туда объект пользователя
    return render(request, 'Site1/Главная.html', {'user': request.user})


# выход
def doLogout(request):
    # вызываем функцию django.contrib.auth.logout и делаем редирект на страницу входа
    logout(request)
    return redirect('login')


# страница входа
def loginPage(request):
    # инициализируем объект класса формы
    form = LoginForm()

    # обрабатываем случай отправки формы на этот адрес
    if request.method == 'POST':

        # заполянем объект данными, полученными из запроса
        form = LoginForm(request.POST)

        # проверяем валидность формы
        if form.is_valid():
            # пытаемся авторизовать пользователя
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # если существует пользователь с таким именем и паролем,
                # то сохраняем авторизацию и делаем редирект
                login(request, user)
                return redirect('me')
            else:
                # иначе возвращаем ошибку
                form.add_error(None, 'Неверные данные!')

    # рендерим шаблон и передаем туда объект формы
    return render(request, 'Site1/Авторизация.html', {'form': form})


def registerPage(request):
    # инициализируем объект формы
    form = RegisterForm()

    if request.method == 'POST':
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
    # ренедерим шаблон и передаем объект формы
    return render(request, 'Site1/Регистрация.html', {'form': form})


