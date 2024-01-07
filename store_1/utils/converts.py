from django.urls import converters
class UsernameConvert:
    regex='[a-zA-Z_-]{5,20}'
    def to_python(self,value):
        return value