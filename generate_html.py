import markdown
import codecs
import jinja2
import pathlib
import time

def render_recursively(template, **kwargs):
  prev_result = None
  result = template.render(**kwargs)

  while result != prev_result:
    prev_result = result
    template = jinja2.Template(prev_result)
    result = template.render(**kwargs)
    
  return result

input_file = codecs.open("terminology.md", mode="r", encoding="utf-8")
text = input_file.read()

html = markdown.markdown(
    text,
    output_format="html5", 
    tab_length=2,
    extensions=['def_list', 'admonition'])

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
jinja_template = jinja_env.get_template("web/template.html")

jinja_output = render_recursively(
  jinja_template, 
  content=html,
  last_updated=time.strftime("%Y-%m-%d %H:%M GMT", time.gmtime()))

# jinja_output = jinja_template.render(
#     content=html)

# jinja_output = jinja2.Template(jinja_output).render(last_updated="NOW")

pathlib.Path("target").mkdir(parents=True, exist_ok=True)

output_file = codecs.open(
    "target/terminology.html",
    "w",
    encoding="utf-8",
    errors="xmlcharrefreplace")

output_file.write(jinja_output)
