from jinja2 import Template
import os


# Return rendered configuration
def gen(my, jj2):
    f = open(jj2, 'r')
    temp = f.read()
    f.close()

    template = Template(temp)
    os.environ['APP_NAME'] = my['conf_name']
    my['env'] = os.environ

    return template.render(my=my)
