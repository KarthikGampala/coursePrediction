# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import MySQLdb as mysql

# Create your views here.
from django.http import HttpResponse


def course_reg(request,student_id):
	db = mysql.connect("139.59.25.79","admin","Iiit_s@123","ase")
	cur = db.cursor()
	if request.method == "POST":
		course_sel = request.POST.get('course_sel', None)
		print(course_sel)
	cur.execute("select * from dept_type;")
	type_course = []
	for row in cur.fetchall():
		type_course.append(row)

	"""
	cur1 = db.cursor()
	cur1.execute("select * from academic_prog_batch_sem_course where Academic_Prog_Batch_Sem_Course_Type=1;")
	type_course = []
	for row in cur.fetchall():
		type_course.append(row)
	"""

	return render(request, "course_registraion.html", context={'type': type_course})