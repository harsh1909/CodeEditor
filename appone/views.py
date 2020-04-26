from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from .forms import Form_Input,Form_Output
import string
import random
from .database import exist_in_db,create_entry_in_db,submit_data,fetch_source_code
# Create your views here.
def new(request):
	print("hello form new")
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	while True:
		code_id = ''.join(random.choice(chars) for _ in range(8))
		if not exist_in_db(code_id):
			break
	create_entry_in_db(code_id)
	url = '/'+ code_id
	return HttpResponseRedirect(url)

def indextest(request,code_id):
	src = fetch_source_code(code_id)
	form = Form_Input(text=src)
	form_out = Form_Output(text="")

	if request.method=="POST":
		form = Form_Input(request.POST,text="")
		form_out = Form_Output(request.POST,text="")

		if form.is_valid():
			source = form.cleaned_data['code_input']
			c_input = form.cleaned_data['custom_input']
			lang = form.cleaned_data['language']
			action = form.cleaned_data['action']

			if action=="save_request":
				update_db(code_id,source)

			else:

				API_RUN_URL = "https://api.hackerearth.com/v3/code/run/"
				API_CLIENT_SECRET_KEY = "f8c321f549d832c1be38f82f0a26defc886cd079"

				
				

				data = {'client_secret': API_CLIENT_SECRET_KEY, 'source': source,'input':c_input,'async': 0, 'lang': lang}
				# Make the API request here
				response = requests.post(API_RUN_URL, data = data).json()
				print(response)

				
				if response["compile_status"]=="OK":
					print("output:::: ",response["run_status"]["output"])
					form_out = Form_Output(text=(response["run_status"]["output"]+response["run_status"]["stderr"]))
					#return HttpResponse(response["run_status"]["output_html"])

				else:
					
					print(response["compile_status"])
					form_out = Form_Output(text=response["compile_status"])
					#return HttpResponse(response["compile_status"])

				#return HttpResponse("THANKx")



	dict = {'input':form,'output':form_out}
	return render(request,'appone/home.html',context=dict)


def update_db(code_id,source):
	print("in DB UPDATE FUNTION: ",code_id,source)
	submit_data([code_id,source])