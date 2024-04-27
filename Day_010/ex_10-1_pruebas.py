
# Functions with outputs

def format_name(f_name, l_name):
    formated_f_name = str(f_name).title()
    formated_l_name = str(l_name).title()
    formated_name = formated_f_name + " " + formated_l_name
    return formated_name


name = format_name("JoSE luis", "cOLoma")
print(name)
