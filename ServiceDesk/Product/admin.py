from django.contrib import admin
from .models import Agent, Genre, Ticket, TicketInstance
from django.contrib import admin 
from django.http import HttpResponse
admin.site.register(Genre)
from django.contrib.sessions.models import Session

admin.site.site_header = 'Ace Gizmos' 
admin.site.index_title = "Welcome to Ace gizmos"


class TicketsInline(admin.TabularInline):
    model = Ticket


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    
    list_display = ('first_name',
    				'last_name',
    				'email'
                    )
    fields = ['first_name', 'last_name','email']
    # inlines = [TicketsInline,]


class TicketInstanceInline(admin.TabularInline):
    model = TicketInstance


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id','Subject', 'Agent', 'display_genre', )
    # inlines = [TicketInstanceInline,]


admin.site.register(Ticket, TicketAdmin)


@admin.register(TicketInstance)
class TicketInstanceAdmin(admin.ModelAdmin):
    
    list_display = ('ticket', 'borrower', 'status')