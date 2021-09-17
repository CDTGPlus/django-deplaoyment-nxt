from django import template

register = template.Library()

#write a function to act as custom template filter 

#note! since a fucntion is being called into another function call, a decorator can be used to register original function
@register.filter(name='cut')
def cut(value,arg):
    #This will cut all values of arg from the string 
    return value.replace(arg,'')

#pass the function 
#register.filter('cut',cut)