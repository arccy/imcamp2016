#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

genders = (('M', '男'), ('F', '女'), ('O', '其他'))
grades = (('1', '高一'), ('2', '高二'), ('3', '高三'), ('O', '其他 (請在自介說明'))
sizes = (('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L','L'), ('XL', 'XL'))
bloods = (('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'))
foods = (('M', '葷'), ('V','素'))
hows = (('W', '上網搜尋'), ('FB', '臉書'), ('F', '朋友'), ('C', '班宣'), ('O', '其他'), ('D', '杜鵑花'))
    
class SignUp(models.Model):
    name = models.CharField(max_length = 20)
    gender = models.CharField(choices = genders, max_length = 1)
    birthday = models.DateField()
    ssn = models.CharField(max_length = 10)
    phone = models.CharField(max_length = 10)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 20)
    contact_phone = models.CharField(max_length = 10)
    blood = models.CharField(choices = bloods, max_length = 10)
    food = models.CharField(choices = foods, max_length = 10)
    allergy = models.CharField(max_length = 100, blank = True)
    medical = models.CharField(max_length = 100, blank = True)
    size = models.CharField(choices = sizes, max_length = 10)
    school = models.CharField(max_length = 20)
    grade = models.CharField(choices = grades, max_length = 10)
    mugshot = models.ImageField(upload_to='uploads/mugshot/')
    lifeshot = models.ImageField(upload_to='uploads/lifeshot/')
    interests = models.TextField(max_length = 1000)
    experiences = models.TextField(max_length = 1000)
    motivations = models.TextField(max_length = 1000)
    how = models.CharField(choices = hows, max_length = 100)
    group = models.TextField(max_length = 100, blank = True)
    special = models.BooleanField(blank = True)
    proof = models.FileField(upload_to='uploads/proof/', blank = True)
    
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
            'size': ('營服尺寸(XS,S,M,L,XL)'),
            'school': ('就讀學校'),
            'grade': ('年級'),
            'mugshot': ('大頭照'),
            'lifeshot': ('個人生活照'),
            'interests': ('自介 (個人興趣或特質)'),
            'experiences': ('特殊經歷(社團活動、工作經驗或其他特殊事蹟等,限國高中時期)'),
            'motivations': ('報名動機及期待收穫'),
            'how': ('你從何處得知臺大資管營'),
            'group': ('申請二人4800/三人4700團報優惠'),
            'special': ('申請家境清寒報名費減免'),
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
            'special': ('為協助家境清寒學生能參與本次活動，上傳相關證明文件並錄取後，得以2000元報名費參與本次活動。'),
            'proof': (''),
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'XXX'}),
            'ssn': forms.TextInput(attrs={'placeholder': 'A123456789'}),
            'phone': forms.TextInput(attrs={'placeholder': '0912345678'}),
            'email': forms.TextInput(attrs={'placeholder': 'signup@ntu.im'}),
            'address': forms.TextInput(attrs={'placeholder': '10617 臺北市羅斯福路四段一號'}),
            'contact': forms.TextInput(attrs={'placeholder': 'XXX (父親/兒子)'}),
            'contact_phone': forms.TextInput(attrs={'placeholder': '0987654321'}),
            'school': forms.TextInput(attrs={'placeholder': 'XX高中'}),
#            'interests': forms.TextInput(attrs={'placeholder': 'my interests are...'}),
#            'experiences': forms.TextInput(attrs={'placeholder': 'my experiences are...'}),
#            'motivations': forms.TextInput(attrs={'placeholder': 'my motivations are...'}),
            'group': forms.TextInput(attrs={'placeholder': 'AXX, BXX, CXX'}),
        }
        
