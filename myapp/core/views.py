from django.db.models import Q
from django.shortcuts import render


# Create your views here.
def base(request):
    context = {}
    return render(request, 'core/base.html', context)

def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def organizer_dashboard(request):
    context = {}
    return render(request, 'core/organizer_dashboard.html', context)

def participant_dashboard(request):
    context = {}
    return render(request, 'core/participant_dashboard.html', context)

def login(request):
    context = {}
    return render(request, 'users/login.html', context)

def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)

def register_organizer(request):
    context = {}
    return render(request, 'users/register_organizer.html', context)

def teacher_participant(request):
    context = {}
    return render(request, 'user/teacher_participant.html', context)

def organizer_panding(request):
    context = {}
    return render(request, 'user/organizer_pending.html', context)

# def students(request):
#     # Все студенты
#     students_all = Student.objects.all()

#     # По айдишнику
#     try:
#         students_get = Student.objects.get(id=1)
#     except Student.DoesNotExist:
#         students_get = None

#     # Первый и последний
#     students_first = Student.objects.order_by("last_name").first()
#     students_last = Student.objects.order_by("last_name").last()

#     # Кол-во студентов
#     students_count = Student.objects.count()


#     # Фильтрация по группе
#     students_filter_group = Student.objects.filter(
#         group__name = "410Б"
#     )

#     # Исключение из группы
#     students_exclude_group = Student.objects.exclude(
#         group__name = "410Б"
#     )

#     # Поиск по части фамилии
#     students_contains = Student.objects.filter(
#         last_name__icontains = "ов"
#     )

#     # Поиск по нескольким условиям
#     students_in = Student.objects.filter(
#         last_name__in = ["410", "410Б"]
#     )

#     # Сложное условие через Q 
#     students_q = Student.objects.filter(
#         Q(group__name = "410") | Q(group__name = "410Б")
#     )

#     # Собираем всё в контекст и возвращаем шаблон
#     context = {
#         'students_all': students_all,
#         'student_get': students_get,
#         'student_first': students_first,
#         'student_last': students_last,
#         'students_count': students_count,
#         'students_filter_group': students_filter_group,
#         'students_exclude_group': students_exclude_group,
#         'students_contains': students_contains,
#         'students_q': students_q,
#     }
    
#     return render(request, 'core/students.html', context)

