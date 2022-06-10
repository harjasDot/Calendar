from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from cal_app.models import fun
# Create your views here.
# def home(request,year,month):
#     month=month.capitalize()
#     month_n=int(list(calendar.month_name).index(month))
#     cal=HTMLCalendar().formatmonth(year,month_n)
#     context={
#         "year":year,
#         "month":month_n,
#         "cal":cal,
#     }
#     return render(request,'home.html',context)

def base(request):
    if request.method=='POST':
        year=request.POST['name_year']
        month=request.POST['name_month']
        year=int(year)
        month_new=month.capitalize()
        month_n=int(list(calendar.month_name).index(month_new))
        cal=HTMLCalendar().formatmonth(year,month_n)
        context={
        "year":year,
        "month":month_n,
        "cal":cal,
        }
        return render(request,'home.html',context)
        
    return render(request,'base.html')