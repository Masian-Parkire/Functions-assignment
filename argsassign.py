#A function named concatenate_args that takes any number 
# of string arguments in positional arguments format and 
# concatenates them into a single string

def concatenate_args(*mystring):
    new_string=(" ")
    for string in mystring:
        new_string+= string
    return new_string  

#A function named concatenate_kwargs that takes
# any number of string arguments in keyword arguments  
# format and concatenates them into a single string  


def concatenate_kwargs(**strings):
    str=""
    for key,value in strings.items():
        str +=(f"{key},{value}, ")
    return str
 