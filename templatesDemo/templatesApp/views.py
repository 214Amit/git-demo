from django.shortcuts import render
# from django.http import HttpResponse

def renderTemplate(request):
    myDict = {"Name":"Amit"}
    return render(request, 'templatesApp/firstTemplate.html', myDict)
# Create your views here.
def renderEmployee(request):
    empDetail = {"id":123, "Name": "Ajit", "sal": 100000}
    return render(request,'templatesApp/empTemplate.html', empDetail)
