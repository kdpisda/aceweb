from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os

@csrf_exempt
def signup_student(request):
	if request.user.is_authenticated():
		return render (request,'welcome.html')
	else:
		if request.method=="POST":
			try:
				response={}
				login_id=str(request.POST.get('roll_no'))
				print login_id
				sem=str(request.POST.get('sem'))
				print sem
				github_url=str(request.POST.get('github_url'))
				linkedin_url=str(request.POST.get('linkedin_url'))
				# image=request.FILES.get('photo').name
				try:
				# 	folder = 'media/student_images/'+roll_no+'/'
				# 	os.mkdir(os.path.join(folder))
				# 	break
				# except:
				# 	response['success']=False
				# print "image=",image
				# fout = open(folder+image, 'w')
				# file_content = request.FILES.get('photo').read()
				# fout.write(file_content)
				# fout.close()
					skill=str(request.POST.get('skill'))
					password=str(request.POST.get('password'))
					# try:
					student_data_row=student_data.objects.get(roll_no=login_id)
					setattr(student_data_row,'sem',str(sem))
					setattr(student_data_row,'github_url',str(github_url))
					setattr(student_data_row,'linkedin_url',str(linkedin_url))
					setattr(student_data_row,'skill',str(skill))
					#image pending
					student_data_row.save()
					User.objects.create_user(username=login_id,password=password)
				except:
					return HttpResponse('Invalid login id')
			except:
				return HttpResponse("Data not get")


@login_required
def student_profile(request,roll_no):
	try:
		JSON_response={}
		login_id=str(request.user)
		if login_id==roll_no:
			JSON_response['login_id']=login_id
			student_data_row=student_data.objects.get(roll_no=roll_no)
			JSON_response['name']=student_data_row.name
			JSON_response['mobile']=student_data_row.mobile
			JSON_response['email']=student_data_row.email
			JSON_response['sem']=student_data_row.sem
			photo=str(student_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['skill']=student_data_row.skill
			JSON_response['linkedin_url']=student_data_row.linkedin_url
			JSON_response['github_url']=student_data_row.github_url
			edit='<a href="'+str(request.scheme+'://'+request.get_host()+'/edit_student_profile/')+'">edit your profile</a>'
			JSON_response['edit']=edit
		else:
			print login_id
			JSON_response['login_id']=roll_no
			student_data_row=student_data.objects.get(roll_no=roll_no)
			JSON_response['name']=student_data_row.name
			JSON_response['mobile']=student_data_row.mobile
			JSON_response['email']=student_data_row.email
			JSON_response['sem']=student_data_row.sem
			photo=str(student_data_row.photo)
			photo_url='<img src='+'"/media/'+photo+'"'+'>'
			JSON_response['photo']=photo_url
			print photo_url
			JSON_response['skill']=student_data_row.skill
			JSON_response['linkedin_url']=student_data_row.linkedin_url
			JSON_response['github_url']=student_data_row.github_url
		print JSON_response
		return render(request,'show_profile.html',JSON_response)
	except:
		return HttpResponse("Wrong roll_no entered")


@login_required
def student_group_profile(request):
	try:
		key=str(request.GET.get('key'))
		value=str(request.GET.get('value'))
		if(key=='roll_no'):
			link='/student_view/'+value
			return HttpResponseRedirect(str(link))
		else:
			if key=='name':
				count = student_data.objects.filter(name=value).count()
				if count==0:
					return render(request,'profile.html',{'msg':'no profile found for such name'})
				else:
					for o in student_data.objects.filter(name=value):
						return HttpResponse('profile html code will be passed as context in render')
			else:
				if key=='sem':
					count = student_data.objects.filter(sem=value).count()
					if count==0:
						return render(request,'profile.html',{'msg':'please enter correct semester'})
					else:
						for o in student_data.objects.filter(sem=value):
							return HttpResponse('profile html code will be passed as context in render')
				else:
					return HttpResponse('please choose field from give list')
	except:
		return HttpResponse('something occur please try again')


@login_required
@csrf_exempt
def edit_student_profile(request):
	if request.method=='POST':
		try:
			student_data_row=student_data.objects.get(roll_no=str(request.user))
			skill=str(request.POST.get('skill'))
			linkedin_url=str(request.POST.get('linkedin_url'))
			github_url=str(request.POST.get('github_url'))
			#image pending
			setattr(student_data_row,'skill',skill)
			setattr(student_data_row,'linkedin_url',linkedin_url)
			setattr(student_data_row,'github_url',github_url)
			#image pending
			student_data_row.save()
			return HttpResponse('redirect him to his own profile')
		except:
			return HttpResponse('something occur please try again')
	else:
		student_data_row=student_data.objects.get(roll_no=str(request.user))
		JSON_response={}
		JSON_response['roll_no']=student_data_row.roll_no
		JSON_response['name']=student_data_row.name
		JSON_response['mobile']=student_data_row.mobile
		JSON_response['email']=student_data_row.email
		JSON_response['sem']=student_data_row.sem
		photo=str(student_data_row.photo)
		photo_url='<img src='+'"/media/'+photo+'"'+'>'
		JSON_response['photo']=photo_url
		print photo_url
		JSON_response['skill']=student_data_row.skill
		JSON_response['linkedin_url']=student_data_row.linkedin_url
		JSON_response['github_url']=student_data_row.github_url
		return render (request,'edit_student_profile.html',JSON_response)
# Create your views here.