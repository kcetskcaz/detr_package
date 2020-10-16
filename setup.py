import setuptools

print(setuptools.find_packages('detr'))

setuptools.setup(
    name="detr", # Replace with your own username
    version="0.0.1",
    author="Me",
    author_email="author@example.com",
    description="A small example package",
    packages=['detr'] + [f'detr.{x}' for x in setuptools.find_packages('detr')]
)
