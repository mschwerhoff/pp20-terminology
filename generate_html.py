import markdown
import codecs
import jinja2
import pathlib

input_file = codecs.open("terminology.md", mode="r", encoding="utf-8")
text = input_file.read()

html = markdown.markdown(
    text,
    output_format="html5", 
    tab_length=2,
    extensions=['def_list'])

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
jinja_template = jinja_env.get_template("web/template.html")
jinja_output = jinja_template.render(content=html)

pathlib.Path("target").mkdir(parents=True, exist_ok=True)

output_file = codecs.open(
    "target/terminology.html",
    "w",
    encoding="utf-8",
    errors="xmlcharrefreplace")

output_file.write(jinja_output)
