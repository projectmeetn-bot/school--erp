from django.contrib import admin
from .models import Attendance, AttendanceDetail

class AttendanceDetailInline(admin.TabularInline):
    model = AttendanceDetail
    extra = 0
    
@admin.register(Attendance)
class AttendacneAdmin(admin.ModelAdmin):
    list_display = ('classroom' , 'date' , 'created_at')
    search_fields = ('classroom__name',)
    list_filter = ('date' , 'classroom')
    inlines = [AttendanceDetailInline]
    
@admin.register(AttendanceDetail)
class AttendacneDetailAdmin(admin.ModelAdmin):
    list_display = ('student' , 'attendance' , 'status')
    list_filter = ('status',)
    search_fields = ('student__name',)