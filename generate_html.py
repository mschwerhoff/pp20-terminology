import markdown
import codecs
import jinja2
import pathlib
import time
import git

input_file = codecs.open("terminology.md", mode="r", encoding="utf-8")
text = input_file.read()

html = markdown.markdown(
    text,
    output_format="html5", 
    tab_length=2,
    extensions=['def_list', 'admonition'])

local_git_repo = git.Repo(search_parent_directories=True)
local_git_sha = local_git_repo.head.object.hexsha

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
jinja_template = jinja_env.get_template("web/template.html")

jinja_output = jinja_template.render(
  content=html,
  last_updated=time.strftime("%Y-%m-%d %H:%M GMT", time.gmtime()),
  git_revision=local_git_sha[:10],
  github_revision_url="https://github.com/mschwerhoff/pp20-terminology/commit/%s" % local_git_sha,
  github_repository_url="https://github.com/mschwerhoff/pp20-terminology")

pathlib.Path("target").mkdir(parents=True, exist_ok=True)

output_file = codecs.open(
    "target/terminology.html",
    "w",
    encoding="utf-8",
    errors="xmlcharrefreplace")

output_file.write(jinja_output)
