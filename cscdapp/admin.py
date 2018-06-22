# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import ratting_master_scale,Company_nature,Issuer_industry,Credit_environment,Bond_type,Guarantor_type,Guarantee_type,\
    Guarantee_strength,Collateral_depend,Collateral_type,Collateral_control,Collateral_environment,Bond_rating_scale_lgd
from django.contrib import admin
class Company_natureAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Company_natureAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct
# Register your models here.
class Issuer_industryAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Issuer_industryAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Credit_environmentAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Credit_environmentAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Bond_typeAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Bond_typeAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Guarantor_typeAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Guarantor_typeAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Guarantee_typeAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Guarantee_typeAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Guarantee_strengthAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Guarantee_strengthAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Collateral_dependAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Collateral_dependAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Collateral_typeAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Collateral_typeAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Collateral_controlAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Collateral_controlAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Collateral_environmentAdmin(admin.ModelAdmin):
    list_display = ('Type','Coefficient',)
    search_fields = ('Type',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Collateral_environmentAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct

class Bond_rating_scale_lgdAdmin(admin.ModelAdmin):
    list_display = ('Scale_grade','low_bound','upper_bound',)
    search_fields = ('Scale_grade',)
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct =super(Bond_rating_scale_lgdAdmin,self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_str =str(search_term)
            queryset |=self.model.objects.filter(user =search_term_as_str)
        except:
            pass
        return queryset,use_distinct


admin.site.register(Bond_rating_scale_lgd,Bond_rating_scale_lgdAdmin)
admin.site.register(Company_nature,Company_natureAdmin)
admin.site.register(Issuer_industry,Issuer_industryAdmin)
admin.site.register(Guarantee_strength,Guarantee_strengthAdmin)
admin.site.register(Guarantee_type,Guarantee_typeAdmin)
admin.site.register(Guarantor_type,Guarantor_typeAdmin)
admin.site.register(Collateral_control,Collateral_controlAdmin)
admin.site.register(Collateral_depend,Collateral_dependAdmin)
admin.site.register(Collateral_environment,Collateral_environmentAdmin)
admin.site.register(Collateral_type,Collateral_typeAdmin)
admin.site.register(Bond_type,Bond_typeAdmin)
admin.site.register(Credit_environment,Collateral_environmentAdmin)
