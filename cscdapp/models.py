# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.
class Company_nature(models.Model):#企业性质表
    Type = models.CharField('企业性质类型',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Issuer_industry(models.Model):#发行人行业表
    Type = models.CharField('发行人行业类型',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Credit_environment(models.Model):#信用环境
    Type = models.CharField('信用环境',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type


class Bond_type(models.Model):#债项类型表
    Type = models.CharField('债项类型',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Guarantor_type(models.Model):#担保人类型
    Type = models.CharField('担保人类型',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type


class Guarantee_type(models.Model):#担保类型表
    Type = models.CharField('担保类型',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Guarantee_strength(models.Model):#担保强度表
    Type = models.CharField('担保强度',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Collateral_type(models.Model):#抵质押品类型表
    Type = models.CharField('抵质押品类型',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Collateral_depend(models.Model):#抵质押品独立性表
    Type = models.CharField('抵质押品独立性',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class Collateral_control(models.Model):#抵质押品控制力表
    Type = models.CharField('抵质押品控制力',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type


class Collateral_environment(models.Model):#抵质押品执法环境表

    Type = models.CharField('抵质押品执法环境',max_length=50)
    Coefficient = models.FloatField("系数",max_length=50)
    #verification = models.CharField("验证码",max_length=50)
    def __unicode__(self):
        return self.Type

class ratting_master_scale(models.Model):#主标尺表
    Ratting = models.CharField('评级结果',max_length=50)
    Min_val = models.FloatField('最小值',max_length=50)
    Max_val = models.FloatField('最大值',max_length=50)
    def __unicode__(self):
        return self.Ratting
class Bond_rating_scale_lgd(models.Model):#债券评级映射
    Scale_grade = models.CharField('LGD级别',max_length=50)
    low_bound = models.FloatField('下界',max_length=50)
    upper_bound = models.FloatField('上界',max_length=50)
    def __unicode__(self):
        return self.Scale_grade



class AddForm(forms.Form):
    a = forms.CharField()


