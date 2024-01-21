from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
def EmailValidator(value):
    if '@' not in value:
        raise ValidationError("Email should contain @")

class fieldsLearning1(models.Model):
    name=models.CharField(max_length=20, null=False, error_messages={'max_length':'Name field is required custom'})
    age=models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(100)])
    address=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=50,validators=[EmailValidator])
    phone=models.IntegerField()
    personal_number=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        db_table="fieldsLearning3"

class common(models.Model):
    shop_name=models.CharField(max_length=200,unique=True, blank=True,)

    class Meta:
        abstract=True

class modellearning1(common):
    CHOISE_OPTIONs=[(1,'First'),(2,'Second'),(3,'Third')]
    choisce=models.CharField(max_length=200,choices=CHOISE_OPTIONs,default='1')

    class Meta:
        db_table="modellearningmodel"
class modellearning2(common):
    CHOICE_OPTIONS = (
        ('number', (
            ('1', 'First'),
            ('2', 'Second'),
            ('3', 'Third'),
        )),
        ('string', (
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
        )),
    )
    choice = models.CharField(max_length=200, choices=CHOICE_OPTIONS, default='1')
    column=models.CharField(max_length=200, db_column='customName', blank=True, null=True)

def age_validator(value):
    if value<18:
        raise ValidationError("Age should be greater than 18")
class modellearning3(models.Model):
    age=models.IntegerField(validators=[age_validator],error_messages={'invalid':'Age field is required'})

class timedate(models.Model):
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    datetime=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=200, unique_for_date='date')


class Department(models.Model):
    name=models.CharField(max_length=200)

class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)


class common(models.Model):
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Adharnumber(common):
    adhar_no=models.IntegerField(unique=True, editable=False)
class citison(common):
    name=models.CharField(max_length=200)
    adharnumber=models.OneToOneField(Adharnumber, on_delete=models.DO_NOTHING, related_name='human')

class tag(common):
    name=models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

class books(common):
    name=models.CharField(max_length=200)
    tags=models.ManyToManyField(tag, related_name='books')

    def __str__(self):
        return self.name

class Blog(common):
    name=models.CharField(max_length=200)
    tagline=models.TextField()

class Author(common):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    

class Entry1(common):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline=models.CharField(max_length=200)
    body_text=models.TextField()
    authors=models.ManyToManyField(Author)
    pub_date=models.DateField()
    rationg=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.headline

class latest(models.Model):
    date1=models.DateField()
    date2=models.DateField()

class age(models.Model):
    numer=models.IntegerField()

class RetailDetails(models.Model):
    price=models.IntegerField()

class Price(models.Model):
    actual_price=models.IntegerField()
    offer_price=models.IntegerField()
    discount_price=models.IntegerField()
    retail=models.ForeignKey(RetailDetails, on_delete=models.SET_DEFAULT, default=0, related_name='retails', null=True, blank=True)
