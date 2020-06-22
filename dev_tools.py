from IPython.display import display_html

# ***** CONSTANTS *****

random_state = 115

# ***** FUNCTIONS ***** 

def display_side_by_side(*args):
    html_str=''
    for df in args:
        html_str+=df.to_html() + "||"
    display_html(html_str.replace('table','table style="display:inline"'),raw=True)