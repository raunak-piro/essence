from django import template

register = template.Library()

@register.filter(name='orderStatus')
def orderStatus(Request,num):
    if (num==0):
        return "Order Palced"
    elif (num == 1):
        return "Not Packed"
    elif (num == 2):
        return "Packed"
    elif (num == 3):
        return "Redy To Dispatch"
    elif (num == 4):
        return "Dispatched"
    elif (num == 5):
        return "Out for Delevery"
    elif (num == 6):
        return "Delevered"
    elif (num == 7):
        return "Cancelled"



@register.filter(name='paymentStatus')
def paymentStatus(Request,num):
    if (num==0):
        return "Pending"
    else :
        return "Done"
    



@register.filter(name='paymentMode')
def paymentMode(Request,num):
    if (num==0):
        return "COD"
    else :
        return "Net Banking"
    