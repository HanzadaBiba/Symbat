from django.contrib import admin

# Register your models here.
from home.models import Method,Order
class MethodAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':['name',]}
admin.site.register(Method,MethodAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name','oblis','city','author','method']
    list_filter = ['author','method']
admin.site.register(Order,OrderAdmin)