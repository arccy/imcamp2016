from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

genders = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
grades = (('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('O', 'Other'))
sizes = (('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L','L'), ('XL', 'XL'))
bloods = (('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'))
foods = (('M', 'Meat'), ('V','Veg'))
hows = (('W', 'Webpage'), ('FB', 'Facebook'), ('F', 'Friends'), ('O', 'Other'))
    
class SignUp(models.Model):
    name = models.CharField(max_length = 20)
    gender = models.CharField(choices = genders, max_length = 10)
    birthday = models.DateField()
    ssn = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 10)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 20)
    contact_phone = models.CharField(max_length = 10)
    blood = models.CharField(choices = bloods, max_length = 10)
    food = models.CharField(choices = foods, max_length = 10)
    allergy = models.CharField(max_length = 100)
    medical = models.CharField(max_length = 100)
    size = models.CharField(choices = sizes, max_length = 10)
    school = models.CharField(max_length = 20)
    grade = models.CharField(choices = grades, max_length = 10)
    mugshot = models.ImageField(upload_to='uploads/mugshot/')
    lifeshot = models.ImageField(upload_to='uploads/lifeshot/')
    interests = models.TextField(max_length = 1000)
    experiences = models.TextField(max_length = 1000)
    motivations = models.TextField(max_length = 1000)
    how = models.CharField(choices = hows, max_length = 100)
    group = models.TextField(max_length = 1000)
    poor = models.TextField(max_length = 1000)
    proof = models.FileField(upload_to='uploads/proof/')
    
class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'
        labels = {
            'name': ('姓名'),
            'gender': ('性別'),
            'birthday': ('出生年月日'),
            'ssn': ('身份證字號'),
            'phone': ('聯絡電話'),
            'email': ('常用email'),
            'address': ('通訊地址'),
            'contact': ('緊急聯絡人姓名及關係'),
            'contact_phone': ('緊急聯絡人電話'),
            'blood': ('血型'),
            'food': ('是否吃素'),
            'allergy': ('特殊飲食需求'),
            'medical': ('特殊疾病'),
            'size': ('營服尺寸(XS,S,M,L,XL,2L)'),
            'school': ('就讀學校'),
            'grade': ('年級'),
            'mugshot': ('大頭照'),
            'lifeshot': ('個人生活照'),
            'interests': ('個人興趣或特質'),
            'experiences': ('特殊經歷(社團活動、工作經驗或其他特殊事蹟等,限國高中時期)'),
            'motivations': ('報名動機及期待收穫'),
            'how': ('你從何處得知臺大資管營'),
            'group': ('申請三人團報優惠'),
            'poor': ('申請家境清寒報名費減免'),
            'proof': ('相關證明文件'),
        }
        help_texts = {
            'name': (''),
            'gender': (''),
            'birthday': (''),
            'ssn': (''),
            'phone': (''),
            'email': (''),
            'address': (''),
            'contact': (''),
            'contact_phone': (''),
            'blood': (''),
            'food': (''),
            'allergy': (''),
            'medical': (''),
            'size': (''),
            'school': (''),
            'grade': (''),
            'mugshot': (''),
            'lifeshot': (''),
            'interests': (''),
            'experiences': (''),
            'motivations': (''),
            'how': (''),
            'group': (''),
            'poor': (''),
            'proof': (''),
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'XXX'}),
            'ssn': forms.TextInput(attrs={'placeholder': 'A123456789'}),
            'phone': forms.TextInput(attrs={'placeholder': '0912345678'}),
            'email': forms.TextInput(attrs={'placeholder': 'signup@ntu.im'}),
            'address': forms.TextInput(attrs={'placeholder': 'somewhere @ somewhere'}),
            'contact': forms.TextInput(attrs={'placeholder': 'XXX (父親/兒子)'}),
            'contact_phone': forms.TextInput(attrs={'placeholder': '0987654321'}),
            'school': forms.TextInput(attrs={'placeholder': 'XX高中'}),
#            'interests': forms.TextInput(attrs={'placeholder': 'my interests are...'}),
#            'experiences': forms.TextInput(attrs={'placeholder': 'my experiences are...'}),
#            'motivations': forms.TextInput(attrs={'placeholder': 'my motivations are...'}),
            'group': forms.TextInput(attrs={'placeholder': 'AXX, BXX, CXX'}),
        }
        