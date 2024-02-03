def format_name(f_name, l_name):
    formated_l = l_name.title()
    formated_f = f_name.title()
    return f"{formated_f} {formated_l}"


formated_str = format_name("JOhn", "DOE")

print(formated_str)
