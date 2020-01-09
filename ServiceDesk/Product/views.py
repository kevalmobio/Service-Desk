from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User,auth,Group
# from django.contrib.auth.decorators import login_required ,user_passes_test
# from .models import Ticket,TicketInstance
from django.http import HttpResponse














# from django.http import  HttpResponse
# from . models import Destination










# def LoginView(request):



# 	# return render(request, 'login.html')
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']


# 		user = auth.authenticate(username= username,password = password)
# 		if user is not None:
# 			auth.login(request,user)
# 			return	redirect('agent')
# 		else:
# 			messages.info(request,'invalid credantials')
# 			return redirect("login")


# 	else:
# 		return render(request,'login.html')

# @login_required()
# def agent(request):
 	
#  	Tickets= Ticket.objects.all()
#  	Ticket_Instances = TicketInstance.objects.all() 
#  	Avail_Number = str(TicketInstance.objects.filter(status = 'A').count())
#  	Closed_Number = str(TicketInstance.objects.filter(status = 'C').count())
#  	Maintenance_Number = str(TicketInstance.objects.filter(status = 'M').count())
#  	Users = User.objects.all()
#  	# if Ticket_Instances.ticket_id == Tickets.id:
#  	# 	Avail_Ticket = Tickets.id
#  	Available = []
#  	Closed = [] 
#  	Maintenance = []
#  	for i in Ticket_Instances:
#  		for j in Tickets:
#  			if(i.ticket_id == j.id) and i.status == 'A':
#  				Available.append(i.ticket_id)
#  			if(i.ticket_id == j.id) and i.status == 'M':
#  				Closed.append(i.ticket_id)
#  			if(i.ticket_id == j.id) and i.status == 'C':
#  				Maintenance.append(i.ticket_id)
 	
#  	print(Ticket_Instances.values())




 				

#  	return	render(request, 'agent.html', {'Users':Users,'Avail_Number':Avail_Number,'Closed_Number':Closed_Number,'Maintenance_Number':Maintenance_Number,'Available':Available, 'Closed':Closed, 'Maintenance':Maintenance, 'Tickets' : Tickets, 'Ticket_Instances':Ticket_Instances})


# def home(request):

# 	return	render(request,'home.html')




# select * from user where user="user_name" and groups = "Manager"



