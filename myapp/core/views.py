from django.db.models import Q
from django.shortcuts import render

from .models import Student

# Create your views here.
def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def about(request):
    context = {}
    return render(request, 'core/about.html', context)

def students(request):
    # Все студенты
    students_all = Student.objects.all()

    # По айдишнику
    try:
        students_get = Student.objects.get(id=1)
    except:
        students_get = Student.DoesNotExist

    # Первый и последний
    students_first = Student.objects.order_by("last_name").first
    students_last = Student.objects.order_by("last_name").last

    # Кол-во студентов
    students_count = Student.objects.count()


    # Фильтрация по группе
    students_filter = Student.objects.filter(
        group__name = "410Б"
    )

    # Исключение из группы
    students_filter = Student.objects.exclude(
        group__name = "410Б"
    )

    # Поиск по части фамилии
    students_contains = Student.objects.filter(
        last_name__icontains = "ов"
    )

    # Поиск по нескольким условиям
    students_in = Student.objects.filter(
        last_name__in = ["410", "410Б"]
    )

    # Сложное условие через Q 
    students_q = Student.objects.filter(
        Q(group__name = "410") | Q(group__name = "410Б")
    )

