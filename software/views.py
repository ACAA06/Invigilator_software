from django.shortcuts import render,redirect
import xlrd
import os
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate,login
from .models import fdetail,Exam,Department,f_sem,Available,allotment,Rooms
from django.core.files.storage import FileSystemStorage
import pandas as pd
import numpy as np

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def mail(a):

    for i in a:
        emails = []
        if i.fid.email not in emails:
            emails.append(i.fid.email)
        print(emails)
        s=''
        s+=i.fid.username+' '+i.date+' '+i.time+' '+i.ename+' '+i.semester+' '+i.sname+' '+i.roomno.roomno
        res=send_mail('subject', 'You have been allotted for invigilation duty.'+'\n'+s+'\n'+'For alteration please login into your account.', 'clementjoe99@gmail.com',
                emails)
        print(res)

def altermail(a):
        emails = []
        if a.fid.email not in emails:
            emails.append(a.fid.email)
        print(emails)
        s=''
        s+=a.fid.username+' '+a.date+' '+a.time+' '+a.ename+' '+a.semester+' '+a.sname+' '+a.roomno.roomno
        res=send_mail('subject', 'You have been allotted for invigilation duty.'+'\n'+s+'\n'+'For alteration please login into your account.', 'clementjoe99@gmail.com',
                emails)
        res = send_mail('subject',
                        'Alteration details!!!' + '\n' + s + '\n',
                        'clementjoe99@gmail.com',
                        'clementjoe99@gmail.com')
        print(res)


def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_staff :
                return redirect('dashboard')
            else:
                return redirect('fdashboard')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,"login.html")

def dashboard(request):
    if auth.user_logged_in:
        return render(request,"dashboard.html")
    else:
        messages.info(request, "U haven't logged in")
        return redirect('login')
def fdashboard(request):
    if auth.user_logged_in:
        return render(request,"facultydash.html")
    else:
        messages.info(request, "U haven't logged in")
        return redirect('login')
def session(request):
    auth.logout(request)
    return redirect('login')

def addfaculty(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        join_date=request.POST['join_date']
        emailid=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        is_staff=0
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('addfaculty')
        elif User.objects.filter(email=emailid).exists():
            messages.info(request,'email already exists')
            return redirect('addfaculty')
        else:
            user1=User.objects.create_user(username=username,password=password,email=emailid,first_name=fname,last_name=lname,date_joined=join_date)
            user1.save()
            return redirect('dashboard')
    else:
        return render(request,'addfaculty.html')

def addtimetable(request):
    if request.method=="POST":
        username=request.POST['username']
        nod=request.POST['nod']
        tt=request.FILES['tt']
        did=request.POST['did']
        #print(tt)
        fs = FileSystemStorage()
        filename = fs.save(tt.name, tt)  # saves the file to `media` folder
        user1=fdetail(fid=User.objects.get(username=username),countofduties=nod,timetable=tt.name,did=Department.objects.get(did=did))
        user1.save()
        year(tt.name,User.objects.get(username=username))
        return redirect('dashboard')
    else:
        uid=User.objects.filter(is_staff=0)
        return render(request,'addtimetable.html',{'uid':uid})

def addexam(request):
    if request.method=="POST":
        ett = request.FILES['ett']
        year=request.POST['year']
        eid = request.POST['eid']
        # print(tt)
        fs = FileSystemStorage()
        filename = fs.save(ett.name, ett)  # saves the file to `media` folder
        exam1 = Exam(etimetable=ett.name,eid=eid,year=year)
        exam1.save()
        return redirect('dashboard')
    else:
        return render(request,'addexam.html')

def allotfaculty(request):
    if request.method=="POST" and request.POST['submit']!="0":
        et = request.POST['submit']
        ex = Exam.objects.get(etimetable=et)
        if ex.allot==False:
                path1 = os.path.join(BASE_DIR, 'ftimetable/')
                fl=[]
                eday=[]
                edate=[]
                etime=[]
                available = []
                et=request.POST['submit']
                ex=Exam.objects.get(etimetable=et)
                bool=ex.allot
                ex.allot=True
                ex.save()
                yea=ex.year
                if yea==1:
                    year='I'
                elif yea==2:
                    year='II'
                elif yea==3:
                    year='III'
                elif yea == 4:
                    year = 'IV'
                f = f_sem.objects.filter(semester=year)
                for i in f:
                    available.append(fdetail.objects.get(fid=i.fid).fid.username)
                df1 = pd.read_csv(path1+et)
                semester = df1['semester']
                semester = list(dict.fromkeys(semester))
                faculty=f_sem.objects.values('fid').get(semester=semester[0])
                print(faculty)
                for z in range(len(df1)):
                    x1 = df1['time'][z]
                    etime.append(x1)
                    start, end = x1.split('-')
                    if float(start) > 8.40 and float(start) <= 9.30:
                        start = 1
                    elif float(start) > 9.30 and float(start) <= 10.20:
                        start = 2
                    elif float(start) > 10.20 and float(start)<= 11.10:
                        start = 3
                    elif float(start) > 11.20 and float(start) <= 12.10:
                        start = 4
                    elif float(start) > 12.10 and float(start) <= 13.00:
                        start = 5
                    elif float(start) > 14.0 and float(start) <= 14.50:
                        start = 6
                    elif float(start) > 14.50 and float(start) <= 15.40:
                        start = 7
                    elif float(start) > 15.40 and float(start) <= 16.30:
                        start = 8
                    elif float(start) > 16.30 and float(start) <= 17.20:
                        start = 9

                    if float(end) > 8.40 and float(end) <= 9.30:
                        end = 1
                    elif float(end) > 9.30 and float(end) <= 10.20:
                        end = 2
                    elif float(end) > 10.20 and float(end) <= 11.10:
                        end = 3
                    elif float(end) > 11.20 and float(end) <= 12.10:
                        end = 4
                    elif float(end) > 12.10 and float(end) <= 13.00:
                        end = 5
                    elif float(end) > 14.0 and float(end) <= 14.50:
                        end = 6
                    elif float(end) > 14.50 and float(end) <= 15.40:
                        end = 7
                    elif float(end) > 15.40 and float(end) <= 16.30:
                        end = 8
                    elif float(end) > 16.30 and float(end) <= 17.20:
                        end = 9
                    day = df1['day'][z]
                    date=df1['date'][z]
                    eday.append(day)
                    edate.append(date)
                    q = "I Sem"
                    w = "II Sem"
                    e = "III Sem"
                    r = "IV Sem"
                    t = "V Sem"
                    p = "VI Sem"
                    u = "VII Sem"
                    o = "VIII Sem"
                    f2=fdetail.objects.all()
                    available2 = []
                    for j in available:
                        available2.append(j)
                    for i in f2:
                        if i.fid.username not in available:
                            #fl.append(fdetail.objects.get(fid=i.fid).fid.username)
                            df = pd.read_csv(path1+str(fdetail.objects.get(fid=i.fid).timetable))
                            if (day == 'mon'):
                                day = 1
                            elif (day == 'tue'):
                                day = 2
                            elif (day == 'wed'):
                                day = 3
                            elif (day == 'thurs'):
                                day = 4
                            elif (day == 'fri'):
                                day = 5
                            elif (day == 'sat'):
                                day = 1
                            x = df.loc[day - 1]
                            flag = 0
                            # print(x)
                            #print(start)
                            #print(end)
                            #print(range(start, end))
                            for j in range(start, end + 1):
                                y = str(x[j])
                                # print(type(y))
                                if y != 'nan':
                                    # print(i)
                                    if yea==1:
                                        if q not in y and w not in y:
                                            flag=1
                                    elif yea==2:
                                        if e not in y and r not in y:
                                            flag=1
                                    elif yea==3:
                                        if t not in y and p not in y:
                                            flag=1
                                    elif yea==4:
                                        if u not in y and o not in y:
                                            flag=1
                            if flag==0:
                                available2.append(fdetail.objects.get(fid=i.fid).fid.username)
                    for j in available2:
                        avail = Available(date=date, Time=x1, fid=User.objects.get(username=j))
                        avail.save()
                    fl.append(available2)
                    print(fl)
                a = Available.objects.all()
                udates=[]
                for i in a:
                    if i.date not in udates:
                        udates.append(i.date)
                        for z in range(len(df1)):
                            if df1['date'][z]==i.date and df1['time'][z]==i.Time:
                                print(type(User.objects.get(username=fdetail.objects.get(fid_id=i.fid_id).fid.username).id))
                                all=allotment(date=i.date, time=i.Time, fid=User.objects.get(username=fdetail.objects.get(fid_id=i.fid_id).fid.username), ename=df1['exam_name'][z],sname=df1['subj_id'][z],semester=df1['semester'][z],roomno=Rooms.objects.get(roomno='A-102'))
                                all.save()
                                c=fdetail.objects.get(fid_id=i.fid_id)
                                c.countofduties=c.countofduties+1
                                c.save()
                return render(request,'allotment.html',{'fl':fl,'etime':etime,'edate':edate,'eday':eday,'leng': range(len(df1)),'bool': bool})


        else:
            return render(request, 'allotment.html',
                          {
                           'bool': ex.allot})
            #return render(request,'')
    elif request.method!='POST':
        exam1=Exam.objects.values('etimetable')

        a=Exam.objects.get(etimetable=exam1[0]['etimetable'])
        print(a.allot)
        return render(request,'allotfaculty.html',{'ename':exam1})
    else:
        a = allotment.objects.all()
        mail(a)
        return render(request, 'allotmentt.html', {'a': a})


def allot(request):
    if request.method=="POST":

        print(request.POST)
    else:
        return render(request,'allotment.html')

def allotmentlist(request):
    user=request.user
    print(user.id)
    a=allotment.objects.filter(fid_id=user.id)
    return render(request,'fallotment.html',{'a':a})
def alteration(request):
    user=request.user
    i=request.POST['alter']
    print(i)
    available=Available.objects.filter(date=i)
    ao=allotment.objects.get(date=i,fid_id=user.id)
    print(available)
    flag=0
    if available.exists():
        for j in available:
            print(str(j.fid_id) + " " + str(user.id))
            if j.fid_id != user.id:
                try:
                    all = allotment.objects.get(fid_id=j.fid_id, date=i)
                    if all.exists():
                        flag=1
                        continue
                except:
                    flag = 0
                    ao.fid_id = j.fid_id
                    ao.alter = True
                    z = ao.save()
                    return render(request, 'alteration.html', {'a': 'Requested faculty!!'})
            else:
                flag=1
    else:
        return render(request, 'alteration.html', {'a': 'Faculties unavailable'})
    if flag == 1:
        return render(request, 'alteration.html', {'a': 'Faculties unavailable'})

def accept(request):
    user=request.user
    i=request.POST['accept']
    print(i)
    available=Available.objects.filter(date=i)
    ao=allotment.objects.get(date=i,fid_id=user.id)
    ao.alter = False
    z = ao.save()
    print(available)
    flag=0
    return render(request, 'alteration.html', {'a': 'Accepted'})


def decline(request):
    user=request.user
    i=request.POST['decline']
    print(i)
    available=Available.objects.filter(date=i)
    ao=allotment.objects.get(date=i,fid_id=user.id)
    print(available)
    flag=0
    if available.exists():
        for j in available:
            print(str(j.fid_id) + " " + str(user.id))
            if j.fid_id != user.id:
                try:
                    all = allotment.objects.get(fid_id=j.fid_id, date=i)
                    if all.exists():
                        flag=1
                        continue
                except:
                    c = fdetail.objects.get(fid_id=user.id)
                    c.countofduties = c.countofduties - 1
                    c.save()
                    c = fdetail.objects.get(fid_id=j.fid_id)
                    c.countofduties = c.countofduties + 1
                    c.save()
                    ao.fid_id = j.fid_id
                    ao.alter = False
                    z = ao.save()
                    print(z)
                    altermail(allotment.objects.get(fid_id=j.fid_id, date=i))
                    flag = 0
                    return render(request, 'alteration.html', {'a': 'Declined Successfully'})
            else:
                flag=1
    else:
        return render(request, 'alteration.html', {'a': 'Faculties unavailable to decline'})
    if flag == 1:
        return render(request, 'alteration.html', {'a': 'Faculties unavailable to decline'})


def year(fname,fd):
    path1 = os.path.join(BASE_DIR, 'ftimetable/' + fname)
    df = pd.read_csv(path1)
    q = "I Sem"
    w = "II Sem"
    e = "III Sem"
    r = "IV Sem"
    t = "V Sem"
    p = "VI Sem"
    u = "VII Sem"
    o = "VIII Sem"
    l=[]
    for i in range(5):
        x = df.loc[i]
        # print(x)
        for j in range(1, 11):
            y = x[j]
            y = str(y)
            # print(y)
            if r in y:
                l.append("IV")
                # print(4)
            elif o in y:
                l.append("VIII")
                # print(3)
            elif u in y:
                # print(2)
                l.append("VII")
            elif p in y:
                l.append("VI")
                # print(1)
            elif t in y:
                l.append("V")
                # print(4)
            elif e in y:
                l.append("III")
                # print(3)
            elif w in y:
                # print(2)
                l.append("II")
            elif q in y:
                l.append("I")
                # print(1)
    #print(l)
    mylist = list(dict.fromkeys(l))
    if len(mylist)==1:
        for i in mylist:
            z=f_sem(fid=fdetail.objects.get(fid=fd),semester=i)
            z.save()
