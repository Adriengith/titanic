import os

def creation_architucture(project_name):
    os.system(f"mkdir {project_name}")
    os.system(f"touch {project_name}/__init__.py")
    os.system(f"touch {project_name}/preprocessing.py")
    os.system(f"touch {project_name}/pipeline.py")
    os.system(f"touch {project_name}/get_data.py")
    os.system(f"touch {project_name}/ml.py")
    os.system(f"touch setup.py")
    os.system(f"mkdir notebooks")
    os.system(f"mkdir api")
    os.system(f"mkdir data")
    os.system(f"touch api/fast.py")
    os.system(f"touch README.md")
    os.system(f"touch requierements.txt")

creation_architucture('titanic')