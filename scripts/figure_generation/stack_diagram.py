import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import requests
from io import BytesIO
import os


def generate_tech_stack_grid():
    # Define the technologies to display
    technologies = [
        {"name": "Python", "category": "Language", "placeholder": "python.png"},
        {"name": "TensorFlow", "category": "ML", "placeholder": "tensorflow.png"},
        {"name": "PyTorch", "category": "ML", "placeholder": "pytorch.png"},
        {"name": "Flask", "category": "Backend", "placeholder": "flask.png"},
        {"name": "React", "category": "Frontend", "placeholder": "react.png"},
        {"name": "Docker", "category": "DevOps", "placeholder": "docker.png"},
        {"name": "Kubernetes", "category": "DevOps",
            "placeholder": "kubernetes.png"},
        {"name": "AWS", "category": "Cloud", "placeholder": "aws.png"},
        {"name": "Azure", "category": "Cloud", "placeholder": "azure.png"},
        {"name": "PostgreSQL", "category": "Database",
            "placeholder": "postgresql.png"},
        {"name": "MongoDB", "category": "Database", "placeholder": "mongodb.
