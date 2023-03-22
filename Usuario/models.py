from django.db import models
from django.core.exceptions import ValidationError

#Validadores:
def validate_gender(value):
    gender = value.lower()
    if gender != "mujer" and gender != "hombre":
        raise ValidationError({"message: ": "Solo genero tradicionales"})

#Modelo del Usuario
class User(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    identification = models.CharField(max_length=40, blank=False)
    email = models.EmailField(blank=False)
    cellphone = models.CharField(max_length=10, default='0000000000')
    address = models.CharField(max_length=50, blank=False)
    residence = models.CharField(max_length=50, blank=True, default='')
    marital_status = models.CharField(max_length=30, blank=False)
    date_birth = models.DateField(blank=False)
    gender = models.CharField(max_length=10, validators=[validate_gender], blank=False)
    neighborhood = models.CharField(max_length=50, blank=True, default='')
    social_status = models.IntegerField(blank=False)

    class Meta:
        db_table = "User"
    
    def __str__(self):
        return '%d  %s  %s' % (self.code, self.name, self.identification)


class Student(models.Model):
    code_student = models.ForeignKey('User', on_delete=models.CASCADE)
    academy_program = models.IntegerField(blank=False)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return '%d-%d' % (self.code_student.code, self.academy_program)

class Professor(models.Model):
    code_professor = models.ForeignKey('User', on_delete=models.CASCADE)
    faculty = models.CharField(max_length=40, blank=False)
    position = models.CharField(max_length=40, blank=False)

    class Meta:
        db_table = "Professor"

    def __str__(self):
        return str(self.code_professor)