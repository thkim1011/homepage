from jinja2 import Environment, FileSystemLoader, select_autoescape
import mistune
from homepage.jinja_plugin import plugin_jinja
import re
import os
import shutil


class BaseRenderer:
    def __init__(self, source_dir, output_dir):
        self.source_dir = source_dir
        self.output_dir = output_dir

    def _render_file(self, rel_path):
        raise NotImplementedError(
            "Child class must implement _render_file method")

    def _traverse_directory(self, map_fn):
        def traverse_directory_helper(source_dir, output_dir, map_fn,
                                      rel_path):
            for filename in os.listdir(os.path.join(source_dir, rel_path)):
                filepath = os.path.join(source_dir, rel_path, filename)
                if os.path.isdir(filepath):
                    output_dirpath = os.path.join(
                        output_dir, rel_path, filename)
                    if not os.path.isdir(output_dirpath):
                        os.mkdir(output_dirpath)
                    traverse_directory_helper(
                        source_dir, output_dir, map_fn, os.path.join(rel_path,
                                                                     filename))
                else:
                    map_fn(os.path.join(rel_path, filename))
        traverse_directory_helper(self.source_dir, self.output_dir, map_fn, '')

    def render(self):
        def map_fn(rel_path): return self._render_file(rel_path)
        self._traverse_directory(map_fn)


class JinjaRenderer(BaseRenderer):
    def __init__(self, source_dir, output_dir):
        super().__init__(source_dir, output_dir)
        self.env = Environment(
            loader=FileSystemLoader(source_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def _render_file(self, rel_path):
        filename = os.path.basename(rel_path)
        source_filepath = os.path.join(self.source_dir, rel_path)
        output_filepath = os.path.join(self.output_dir, rel_path)
        if re.match(r'.*\.html', filename):
            with open(source_filepath, 'r') as source_file,\
                    open(output_filepath, 'w') as output_file:
                if filename == 'template.html':
                    print("Is template file")
                else:
                    print("Rendering {0}".format(filename))
                    template = self.env.get_template(filename)
                    output_file.write(template.render())
        else:
            shutil.copyfile(source_filepath, output_filepath)


class MarkdownRenderer(BaseRenderer):
    def __init__(self, source_dir, output_dir):
        super().__init__(source_dir, output_dir)
        self.md = mistune.create_markdown(plugins=[plugin_jinja])

    def _render_file(self, rel_path):
        filename = os.path.basename(rel_path)
        source_filepath = os.path.join(self.source_dir, rel_path)
        output_filepath = os.path.join(self.output_dir, rel_path)

        if re.match(r'.*\.md', filename):
            with open(source_filepath, 'r') as source_file,\
                    open(output_filepath, 'w') as output_file:
                output_file.write(self.md(source_file.read()))
        else:
            shutil.copyfile(source_filepath, output_filepath)
