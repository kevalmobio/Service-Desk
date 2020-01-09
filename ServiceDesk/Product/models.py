from django.db import models
from django.urls import reverse
import uuid 
from django.contrib.auth.models import User 
from datetime import date


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a item genre (e.g. laptop, P.C etc.)"
        )
    # Company_Name = models.CharField(
    #     max_length=50,help_text="Enter Company_Name (e.g Accer ,Sony ,Mi , Apple)")
    # product_id = models.CharField(
    #     max_length = 50,help_text="Enter product detaail (e.g model number)")

    def __str__(self):
        return self.name


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular Ticket")
    Subject = models.CharField(max_length=200)
    Agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one Agent, but Agents can have multiple books
    # Agent as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    bill_number = models.CharField('bill_number', max_length=13)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    due_back = models.DateField(null=True, blank=True)




    TICKET_SEVERITY = (
        ('1', 'urgent'),
        ('2', 'Medium'),
        ('3', 'Low')
        )
    ticket_severity = models.CharField(
        max_length=1,
        choices=TICKET_SEVERITY,
        blank=True,
        default='2',
        help_text='Ticket Severity')

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

        display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('ticket-detail', args=[str(self.id)])

    def __str__(self):
        return self.Subject

class TicketInstance(models.Model):
    
    ticket = models.ForeignKey('Ticket',on_delete=models.SET_NULL, null=True)
    Note = models.CharField(max_length=200)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

   

    TICKET_STATUS = (
        ('M', 'Maintenance'),
        ('C', 'Closed'),
        ('A', 'Available'),
    )

    status = models.CharField(
        max_length=1,
        choices=TICKET_STATUS,
        blank=True,
        default='d',
        help_text='Ticket availability')

    def __str__(self):
    	return '{0} ({1})'.format(self.id, self.ticket.Subject)


class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,default="")

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        
        return reverse('Agent-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)

# class technician(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=254,default="")

