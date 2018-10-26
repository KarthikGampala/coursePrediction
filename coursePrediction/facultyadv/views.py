# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

import MySQLdb as mysql
db = mysql.connect("139.59.25.79","admin","Iiit_s@123","ase")
class Dbclass: 
    def __init__(self):
        self.cursor = db.cursor()
    def executeQuery(self,query):
        if self.cursor.execute(query):
            return 1
        else:
            return 0
    def fetch(self,param):
        if param=='1':
            self.result = self.cursor.fetchone()
            if self.result:
                return self.result
            else:
                print "The cursor is empty"
        if param=='*':
            self.result = self.cursor.fetchall()
            if self.result:
                return self.result
            else:
                print "The cursor is empty"


def index(request):
    cur = Dbclass()
    cur.executeQuery("select s.Student_Id,s.Student_First_Name,s.Student_Middle_Name,s.Student_Last_name,Student_Cur_Sem from student as s where s.Student_Id in (select Distinct Student_Sem_Course_Reg_Student_Id from student_sem_course_reg where Student_Sem_Course_Reg_Reg_Status=0);")
    a = cur.fetch('*')
    a = map(list,a)
    for i in range(len(a)):
        name = ''
        if a[i][2]:
            name = str(a[i][1]+" "+a[i][2]+" "+a[i][3])
        else:
            name = a[i][1]+" "+a[i][3]
        a[i][1]=name
        del a[i][2]
        del a[i][2]

        cur1 = Dbclass()
        cur1.executeQuery("select Student_Sem_Course_Reg_Batch_Sem_Course from student_sem_course_reg where Student_Sem_Course_Reg_Student_Id="+a[i][0]+";")
        b = cur1.fetch('*')
        courses = []
        s = 0
        for j in b:
            cur2 = Dbclass()
            if cur2.executeQuery("select a.Academic_Prog_Batch_Sem_Course_Credits,ac.Academic_Course_Name from academic_prog_batch_sem_course as a inner join academic_course as ac on a.Academic_Prog_Batch_Sem_Course=ac.Academic_Course_Id where Academic_Course_Id="+str(j[0])+";"):
                c = cur2.fetch('*')
                #print(c[0][0])
                s+=int(c[0][0])
                courses.append(c[0][1])
        a[i].append(courses)
        a[i].append(s)        
    #print a
    #print su
    #return HttpResponse("ehk")
    return render(request,"applications.html",context = {'courses':a})    

def approve(request, student_id):
    cur = Dbclass()
    cur.executeQuery("update student_sem_course_reg set Student_Sem_Course_Reg_Reg_Status=1 where Student_Sem_Course_Reg_Student_Id=" + student_id + ";")
    db.commit()
    return redirect("/facultyadv/")

def disapprove(request, student_id, suggest):
    cur = Dbclass()
    
    print(suggest, student_id)
    cur.executeQuery("update student_sem_course_reg set Student_Sem_Course_Reg_Reg_Status=2,Student_Sem_Course_Reg_Student_Suggesstion="+suggest+" where Student_Sem_Course_Reg_Student_Id=" + student_id + ";")
    db.commit()
    return redirect("/facultyadv/")