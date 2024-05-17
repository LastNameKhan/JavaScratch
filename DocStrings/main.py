def format_name(f_name,l_name):
    """Take the First and last anem and format it to 
    return the title case version of the name."""
    return f_name + " " + l_name

output = format_name(name = "Aman", last = "Khan")
# format_name() Hover over it and it's going to show the DocString or the documentation of that function
print(output)