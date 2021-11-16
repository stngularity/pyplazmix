from setuptools import setup


readme = ''
with open('README.md') as f:
	readme = f.read()

requirement = [
	"requests_html",
	"ujson"
]

setup(
	name="pyplazmix",
	author="The Singularity",
	version="0.0.1",
	description="A python wrapper for PlazmixAPI",
	long_description=readme,
	long_description_content_type="text/markdown",
	install_requires=requirement,
	python_requires='>=3.9.0',
	classifiers=[
		"Programming Language :: Python :: 3.9"
	]
)