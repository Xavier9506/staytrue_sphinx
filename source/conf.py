# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'staytrue'
copyright = '2026, xavier'
author = 'xavier'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']
html_theme_options = {
    "rightsidebar": "false",
}
# 确保certificates目录被复制到构建输出目录
import os
import shutil
def copy_certificates(app, exception):
    if exception:
        return
    # 复制各个模组的certificates目录到构建输出目录
    modules_dir = os.path.join(app.srcdir, 'modules')
    build_dir = app.outdir
    for module_name in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_name)
        if os.path.isdir(module_path):
            certs_dir = os.path.join(module_path, 'certificates')
            if os.path.exists(certs_dir):
                dest_dir = os.path.join(build_dir, 'modules', module_name, 'certificates')
                os.makedirs(dest_dir, exist_ok=True)
                for cert_file in os.listdir(certs_dir):
                    src_file = os.path.join(certs_dir, cert_file)
                    dest_file = os.path.join(dest_dir, cert_file)
                    try:
                        # 直接复制，不删除目标文件
                        shutil.copy(src_file, dest_file)
                    except Exception as e:
                        print(f"复制证书文件失败: {e}")
                        # 继续执行，不中断整个构建过程

def setup(app):
    app.connect('build-finished', copy_certificates)

# EPUB options
epub_show_urls = 'inline'