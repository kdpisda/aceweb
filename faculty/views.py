from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

@csrf_exempt
def signup_faculty(request):
	if request.user.is_authenticated():
		link1='<div class="dropdown"><button class="dropbtn">PROFILE</button><div class="dropdown-content">'
		link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
		link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
		return render (request,'index.html',{'link1':link1,'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('faculty_id'))
				designation=str(request.POST.get('designation'))
				print designation
				education=str(request.POST.get('education'))
				area_of_interest=str(request.POST.get('area_of_interest'))
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/faculty_images/'
					os.mkdir(os.path.join(folder))
				except Exception,e:
					print e
					pass
				print "image=",image_name
				url=folder+login_id+image_name
				fout = open(url, 'wb+')
				file_content = request.FILES.get('photo').read()
				fout.write(file_content)
				fout.close()
				other_details=str(request.POST.get('other_details'))
				print other_details
				password=str(request.POST.get('password'))
				print password
				try:
					faculty_data_row=faculty_data.objects.get(faculty_id=login_id)
					setattr(faculty_data_row,'designation',str(designation))
					setattr(faculty_data_row,'education',str(education))
					setattr(faculty_data_row,'area_of_interest',str(area_of_interest))
					setattr(faculty_data_row,'other_details',str(other_details))
					setattr(faculty_data_row,'photo',url)
					faculty_data_row.save()
					User.objects.create_user(username=login_id,password=password)
					return render(request,'login.html',{'msg':'Sign up done','link2':'<a href="/login/">LOGIN</a>'})
				except Exception,e:
					print e
					return render(request,'login.html',{'msg':'Invalid login id','link2':'<a href="/login/">LOGIN</a>'})
			except:
				return render(request,'login.html',{'msg':'Data not get','link2':'<a href="/login/">LOGIN</a>'})


def faculty_profile(request,faculty_id):
	try:
		JSON_response={}
		JSON_response['login_id']=faculty_id
		faculty_data_row=faculty_data.objects.get(faculty_id=faculty_id)
		JSON_response['name']=faculty_data_row.name
		JSON_response['mobile']=faculty_data_row.mobile
		JSON_response['email']=faculty_data_row.email
		JSON_response['designation']=faculty_data_row.designation
		photo=str(faculty_data_row.photo)
		photo_url=' src='+'"/'+photo+'"'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['education']=faculty_data_row.education
		JSON_response['area_of_interest']=faculty_data_row.area_of_interest
		JSON_response['other_details']=faculty_data_row.other_details
		if request.user.is_authenticated():
			login_id=str(request.user)
			link1='<div class="dropdown"><button class="dropbtn">PROFILE</button><div class="dropdown-content">'
			link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
			link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
			JSON_response['link1']=link1
			JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
			if login_id==faculty_id:
				edit_url=str(request.scheme+'://'+request.get_host()+'/edit_faculty_profile/')
				edit='<a href="'+edit_url+'"'+' class="btn btn-default" style="float:right">Edit</a>'
				JSON_response['edit']=edit
		else:
			JSON_response['link2']='<a href="/login/">LOGIN</a>'
		return render(request,'show_faculty_profile.html',JSON_response)
	except Exception,e:
		print e
		link1='<div class="dropdown"><button class="dropbtn">PROFILE</button><div class="dropdown-content">'
		link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
		link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
		return render(request,'show_faculty_profile.html',{'msg':'something occur try again','link1':link1,'link2':'<a href="/logout/">LOGOUT</a>'})


@login_required
def faculty_group_profile(request):
	try:
		for o in faculty_data.objects.all():
			return HttpResponse('whole faculty data will be passed at once')
	except:
		return HttpResponse('something occur please try again')


@login_required
@csrf_exempt
def edit_faculty_profile(request):
	if request.method=='POST':
		try:
			faculty_data_row=faculty_data.objects.get(faculty_id=str(request.user))
			education=str(request.POST.get('education'))
			print education
			designation=str(request.POST.get('designation'))
			area_of_interest=str(request.POST.get('area_of_interest'))
			other_details=str(request.POST.get('other_details'))
			try:
				image_name=request.FILES.get('photo').name
				try:
					folder = 'media/faculty_images/'
					os.mkdir(os.path.join(folder))
				except Exception,e:
					print e
					pass
				print "image=",image_name
				url=folder+faculty_data_row.faculty_id+image_name
				fout = open(url, 'wb+')
				file_content = request.FILES.get('photo').read()
				fout.write(file_content)
				fout.close()
				setattr(faculty_data_row,'photo',url)
			except:
				pass
			setattr(faculty_data_row,'education',education)
			setattr(faculty_data_row,'designation',designation)
			setattr(faculty_data_row,'area_of_interest',area_of_interest)
			setattr(faculty_data_row,'other_details',other_details)
			#resume pending
			faculty_data_row.save()
			redirect_url='/faculty_view/'+str(request.user)
			return HttpResponseRedirect(redirect_url)
		except:
			link1='<div class="dropdown"><button class="dropbtn">PROFILE</button><div class="dropdown-content">'
			link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
			link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
			return render (request,'edit_faculty_profile.html',{'msg':'something occur please try again','link1':link1,'link2':'<a href="/logout/">LOGOUT</a>'})
	else:
		faculty_data_row=faculty_data.objects.get(faculty_id=str(request.user))
		JSON_response={}
		JSON_response['faculty_id']=faculty_data_row.faculty_id
		JSON_response['name']=faculty_data_row.name
		JSON_response['mobile']=faculty_data_row.mobile
		JSON_response['email']=faculty_data_row.email
		JSON_response['designation']=faculty_data_row.designation
		photo=str(faculty_data_row.photo)
		photo_url='<img src='+'"/'+photo+'"'+'>'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['education']=faculty_data_row.education
		JSON_response['area_of_interest']=faculty_data_row.area_of_interest
		JSON_response['other_details']=faculty_data_row.other_details
		link1='<div class="dropdown"><button class="dropbtn">PROFILE</button><div class="dropdown-content">'
		link1+='<a href="/student_view/'+str(request.user)+'" >MY PROFILE</a>'
		link1+='<a href="/students_profile">STUDENTS</a><a href="/alumni_profile">ALUMNI</a></div></div>'
		JSON_response['link1']=link1
		JSON_response['link2']='<a href="/logout/">LOGOUT</a>'
		return render (request,'edit_faculty_profile.html',JSON_response)



# Create your views here.


# Create your views here.
