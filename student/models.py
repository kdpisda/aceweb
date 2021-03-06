from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class student_data(models.Model):
	roll_no=models.CharField(primary_key=True,null=False,blank=False,max_length=20)
	name=models.CharField(max_length=200)
	# sem_choices=(
	# 	(1,"1st semester"),
	# 	(2,"2nd semester"),
	# 	(3,"3rd semester"),
	# 	(4,"4th semester"),
	# 	(5,"5th semester"),
	# 	(6,"6th semester"),
	# 	(7,"7th semester"),
	# 	(8,"8th semester"),
	# 	)
	sem=models.IntegerField(default=0)
	mobile=models.CharField(max_length=10,blank=True,null=True)
	email=models.CharField(max_length=200,blank=True,null=True)
	linkedin_url=models.CharField(max_length=500,blank=True,null=True)
	github_url=models.CharField(max_length=500,blank=True,null=True)
	photo=models.ImageField(upload_to='student_images/',default="media/default.png")
	skill=HTMLField()

# 	def __unicode__(self):
# 		return str(self.roll_no)

# class skill_data(models.Model):
# 	roll_no=models.ForeignKey(student_data)
# 	skill=models.CharField(max_length=200,blank=True,null=True)




# Create your models here.
