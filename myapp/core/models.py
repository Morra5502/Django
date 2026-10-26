from django.db import models


# Модель для группы
class Group(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


# Модель оценки с choices
class Mark(models.Model):
    GRADE_CHOICES = [
        (2, 'Неудовлетворительно'),
        (3, 'Удовлетворительно'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
        ('зачтено', 'Зачтено'),
        ('не зачтено', 'Не зачтено'),
        ('не аттестовано', 'Не аттестовано'),
    ]
    
    grade = models.CharField(choices=GRADE_CHOICES)

    def __str__(self):
        return str(self.grade)


# Модель дисциплины
class Discipline(models.Model):
    name = models.CharField(max_length=200)
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (семестр {self.semester})"


# Модель студента
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# Промежуточная модель для связи ManyToMany
class StudentDiscipline(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='disciplines')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='students')
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='student_disciplines')

    class Meta:
        unique_together = ('student', 'discipline')

    def __str__(self):
        return f"{self.student} - {self.discipline}: {self.mark}"