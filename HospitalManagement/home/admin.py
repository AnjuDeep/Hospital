from django.contrib import admin
from .models import Departments,Doctors,Booking,Contactenquiry
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(Booking, BookingAdmin)
class EnquiryAdmin(admin.ModelAdmin):
    list_display= ('id','enq_type','c_name','c_email','c_phone','c_address','c_country','c_message')
admin.site.register(Contactenquiry,EnquiryAdmin)
