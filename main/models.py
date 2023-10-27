from django.db import models

# Create your models here.
class News(models.Model):
    category_choices = (
        ("الفريق الأول", "first team"),
        ("الطائرة", "volleyball"),
        ("الأكاديمية", "academy"),
        ("النادي", "club",),
    )
    title = models.CharField(max_length=2000)
    text = models.TextField()
    image = models.ImageField(upload_to='images/%y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_hero = models.BooleanField(default=False, null=True)
    category = models.CharField(max_length=100, choices=category_choices)
    
    def __str__(self):
        return self.title   

class Media(models.Model):
    category_choices = (
        ("الملخصات", "highligts"),
        ("الأرشيف", "archieve"),
        ("لقاءات إعلامية", "meetings"),
        ("الطائرة", "volleyball",),
    )
    title = models.CharField(max_length=2000)
    video = models.FileField(upload_to='videos/%y/%m/%d', null=True)
    thumbnail = models.ImageField(upload_to='images/%y/%m/%d', null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=category_choices)
    
    def __str__(self):
        return self.title   

class Player(models.Model):
    position_choices = (
        ( "حارس مرمى", "GK"),
        ("مدافع", "DF"),
        ("متوسط ميدان", "MD"),
        ("مهاجم", "ST"),
        ("المدرب", "M"),
        ("الطاقم الفني", "S"),
    )
    category_choices = (
        ("الفريق الأول", "first team"),
        ("الطائرة", "volleyball"),
    )
    name = models.CharField(max_length=1000)
    category = models.CharField(max_length=100, choices=category_choices, null=True)
    image = models.ImageField(upload_to='images/%y/%m/%d', null=True, blank=True)
    number = models.CharField(max_length=2)
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=position_choices)
    join = models.DateField()
    text = models.TextField()
    
    def __str__(self):
        return self.name   


class Match(models.Model):
    match_choices = (
        ("home", "home"),
        ("away", "away"),

    )
    title = models.CharField(max_length=200)
    homeORaway = models.CharField(max_length=100, choices=match_choices, null=True)
    stadium = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='images/%y/%m/%d', null=True,)
    date = models.DateTimeField()
    competition = models.ImageField(upload_to='images/%y/%m/%d', null=True,)

    vName = models.CharField(max_length=500)
    vLogo = models.ImageField(upload_to='images/%y/%m/%d', null=True,)
    vResult = models.CharField(max_length=1, null=True, blank=True)
    sResult = models.CharField(max_length=1, null=True, blank=True)
    vGoals = models.TextField(null=True, blank=True)
    sGoals = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title