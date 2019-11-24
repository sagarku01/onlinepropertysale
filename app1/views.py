from django.shortcuts import render
from .models import Employee, Appartment, Plots, User


def login(request):
    return render(request, 'login.html')


def welcome(request):
    user = request.POST.get('login')
    psw = request.POST.get('password')
    data = User.objects.filter(name=user)
    for x in data:
        pswd = x.password
    if data:
        if psw == pswd:
            return render(request, 'welcome.html', {'show': data})
        else:
            return render(request, 'login.html', {'message': 'Invalid Password'})
    else:
        return render(request, 'login.html', {'message': "Invalid Username"})


def home(request):
    return render(request, 'welcome.html')


def logout(request):
    return render(request, 'login.html')


def adduser(request):
    id_no = 0
    try:
        res = User.objects.all()[::-1][0]
        id_no = int(res.id_no) + 1
    except IndexError:
        id_no = 3000
    return render(request, 'adduser.html', {'id': id_no})


def usersave(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')
    idno = request.POST.get('idno')
    User(name=uname, password=password, id_no=idno).save()
    return render(request, 'welcome.html', {'add': 'User Added'})


def viewuser(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')
    idno = request.POST.get('idno')
    User(name=uname, password=password, id_no=idno).save()
    user = User.objects.all()
    return render(request, 'viewuser.html', {"user": user, 'update': 'Password Updated'})


def viewUser(request):
    user = User.objects.all()
    return render(request, 'viewuser.html', {"user": user})


def changepass(request):
    user = User.objects.all()
    return render(request, 'changepass.html', {'user': user})


def updateuser(request):
    id_no = request.GET.get('id_no')
    upd = User.objects.get(id_no=id_no)
    return render(request, 'updateuser.html', {"data": upd})


def delete(request):
    user = User.objects.all()
    return render(request, 'deleteuser.html', {'del': user})


def deleteuser(request):
    id = request.GET.get('id_no')
    User.objects.filter(id_no=id).delete()
    return render(request, 'deleteuser.html', {"message": "User Deleted"})


def aboutus(request):
    return render(request, 'aboutus.html')


def plotreg(request):
    reg = 0
    try:
        res = Plots.objects.all()[::-1][0]
        reg = int(res.regno) + 1
    except IndexError:
        reg = 1000
    return render(request, 'plotreg.html', {'regno': reg})


def saveplot(request):
    regno = request.POST.get('regno')
    plotno = request.POST.get('plotno')
    roadno = request.POST.get('roadno')
    surveyno = request.POST.get('surveyno')
    costpersqyard = request.POST.get("costpersqyard")
    otherexp = request.POST.get('otherexp')
    boundary = request.POST.get('boundary')
    facing = request.POST.get('facing')
    status = request.POST.get('status')
    totalcost = request.POST.get('totalcost')
    photo = request.FILES['photo']
    Plots(regno=regno, plotno=plotno, roadno=roadno, surveyno=surveyno, costpersqyard=costpersqyard, otherexp=otherexp,
          boundary=boundary, facing=facing, status=status, totalcost=totalcost, photo=photo).save()
    return render(request, 'Welcomepage.html', {'data': "New Plot Added"})


def viewplot(request):
    plot = Plots.objects.all()
    return render(request, "viewplot.html", {'plot': plot})


def editplot(request):
    return render(request, 'editplot.html')


def editplotno(request):
    plot = request.POST.get('plotno')
    edit = Plots.objects.filter(plotno=plot)
    for x in edit:
        plot_no = x.plotno
    if edit:
        if plot == plot_no:
            return render(request, 'viewoneplotdata.html', {'data': edit})
        else:
            return render(request, 'viewoneplotdata.html', {'data': edit})
    else:
        return render(request, 'editplot.html', {'message': "Invalid PlotNo"})


def updateplot(request):
    regno = request.POST.get('regno')
    plotno = request.POST.get('plotno')
    roadno = request.POST.get('roadno')
    surveyno = request.POST.get('surveyno')
    costpersqyard = request.POST.get("costpersqyard")
    otherexp = request.POST.get('otherexp')
    boundary = request.POST.get('boundary')
    facing = request.POST.get('facing')
    status = request.POST.get('status')
    totalcost = request.POST.get('totalcost')
    photo = request.FILES['photo']
    Plots(regno=regno, plotno=plotno, roadno=roadno, surveyno=surveyno, costpersqyard=costpersqyard, otherexp=otherexp,
          boundary=boundary, facing=facing, status=status, totalcost=totalcost, photo=photo).save()
    plot = Plots.objects.all()
    return render(request, 'viewplot.html', {'data': "Plot Data Updated", 'plot': plot})


def updateplotnumber(request):
    plot_no = request.GET.get('plotno')
    update = Plots.objects.get(plotno=plot_no)
    return render(request, 'viewoneplot.html', {'data': update})


def deleteplot(request):
    plot = request.GET.get('plotno')
    Plots.objects.filter(plotno=plot).delete()
    return render(request, 'deleteplot.html', {"message": "Plot Data Deleted"})


def appartmentreg(request):
    reg = 0
    try:
        res = Appartment.objects.all()[::-1][0]
        reg = int(res.regno) + 1
    except IndexError:
        reg = 999
    return render(request, 'appreg.html', {'regno': reg})


def saveappartment(request):
    regno = request.POST.get('regno')
    plotno = request.POST.get('appart_no')
    roadno = request.POST.get('roadno')
    surveyno = request.POST.get('surveyno')
    costpersqyard = request.POST.get("costpersqyard")
    otherexp = request.POST.get('otherexp')
    facing = request.POST.get('facing')
    status = request.POST.get('status')
    totalcost = request.POST.get('totalcost')
    photo = request.FILES['photo']
    Appartment(regno=regno, appart_no=plotno, roadno=roadno, surveyno=surveyno, costpersqyard=costpersqyard, otherexp=otherexp,
               facing=facing, status=status, totalcost=totalcost, photo=photo).save()
    return render(request, 'appartmentpage.html', {'data': "New Apartment Added"})


def viewappartment(request):
    plot = Appartment.objects.all()
    return render(request, "viewappatment.html", {'plot': plot})


def editappartment(request):
    return render(request, 'editappartment.html')


def editappno(request):
    plot = request.POST.get('plotno')
    edit = Appartment.objects.filter(appart_no=plot)
    for x in edit:
        plot_no = x.appart_no
    if edit:
        if plot == plot_no:
            return render(request, 'viewoneappdata.html', {'data': edit})
        else:
            return render(request, 'viewoneappdata.html', {'data': edit})
    else:
        return render(request, 'editappartment.html', {'message': "Invalid Apartment No"})


def updateappnumber(request):
    plot_no = request.GET.get('plotno')
    update = Appartment.objects.get(appart_no=plot_no)
    return render(request, 'viewoneapp.html', {'data': update})


def updateapp(request):
    regno = request.POST.get('regno')
    plotno = request.POST.get('appart_no')
    roadno = request.POST.get('roadno')
    surveyno = request.POST.get('surveyno')
    costpersqyard = request.POST.get("costpersqyard")
    otherexp = request.POST.get('otherexp')
    facing = request.POST.get('facing')
    status = request.POST.get('status')
    totalcost = request.POST.get('totalcost')
    photo = request.FILES['photo']
    Appartment(regno=regno, appart_no=plotno, roadno=roadno, surveyno=surveyno, costpersqyard=costpersqyard, otherexp=otherexp,
               facing=facing, status=status, totalcost=totalcost, photo=photo).save()
    plot = Appartment.objects.all()
    return render(request, 'viewappatment.html', {'data': "Apartment Data Updated", 'plot': plot})


def deleteapp(request):
    plot = request.GET.get('plotno')
    Appartment.objects.filter(appart_no=plot).delete()
    return render(request, 'deleteapp.html', {"message": "Apartment Data Deleted"})


def empreg(request):
    reg = 0
    try:
        res = Employee.objects.all()[::-1][0]
        reg = int(res.id_no) + 1
    except IndexError:
        reg = 2001
    return render(request, 'empreg.html', {'regno': reg})


def saveemployee(request):
    idno = request.POST.get('idno')
    name = request.POST.get('name')
    email = request.POST.get('mailid')
    location = request.POST.get('location')
    doj = request.POST.get("doj")
    role = request.POST.get('role')
    remarks = request.POST.get('remarks')
    photo = request.FILES['photo']
    Employee(id_no=idno, name=name, mailid=email, location=location, 
             doj=doj, role=role, remarks=remarks, photo=photo).save()
    return render(request, 'Employeepage.html', {'data': "New Employee Added"})


def viewemp(request):
    plot = Employee.objects.all()
    return render(request, "viewemployee.html", {'plot': plot})


def editemp(request):
    return render(request, 'editemployee.html')


def editempno(request):
    idno = request.POST.get('idno')
    editemp = Employee.objects.filter(id_no=idno)
    for x in editemp:
        plot_no = x.id_no
    if editemp:
        if idno == plot_no:
            return render(request, 'viewoneempdata.html', {'data': editemp})
        else:
            return render(request, 'viewoneempdata.html', {'data': editemp})
    else:
        return render(request, 'editemployee.html', {'message': "Invalid IdNo"})


def updateempnumber(request):
    id_no = request.GET.get('idno')
    update = Employee.objects.get(id_no=id_no)
    return render(request, 'viewoneemp.html', {'data': update})


def updateemp(request):
    idno = request.POST.get('idno')
    name = request.POST.get('name')
    email = request.POST.get('mailid')
    location = request.POST.get('location')
    doj = request.POST.get("doj")
    role = request.POST.get('role')
    remarks = request.POST.get('remarks')
    photo = request.FILES['photo']
    Employee(id_no=idno, name=name, mailid=email, location=location,
             doj=doj, role=role, remarks=remarks, photo=photo).save()
    plot = Employee.objects.all()
    return render(request, 'viewemployee.html', {'data': "Employee Data Updated", 'plot': plot})


def deleteemp(request):
    idno = request.GET.get('idno')
    Employee.objects.filter(id_no=idno).delete()
    return render(request, 'deleteemp.html', {"message": "Employee Data Deleted"})


def signup(request):
    return render(request, 'signup.html')


def savesignup(request):
    name = request.POST['login']
    password = request.POST['conf_password']
    password_n = request.POST['password']
    if password_n == password:
        User(name=name, password=password).save()
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')
