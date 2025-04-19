import os

folders = [
    "notebooks/supervised-learning",
    "notebooks/unsupervised-learning",
    "notebooks/deep-learning",
    "projects/titanic-survival-prediction",
    "projects/image-classifier",
    "datasets/sample_images",
    "resources"
]

files = [
    "README.md",
    "requirements.txt",
    "notebooks/supervised-learning/linear_regression.ipynb",
    "notebooks/supervised-learning/logistic_regression.ipynb",
    "notebooks/supervised-learning/decision_trees.ipynb",
    "notebooks/unsupervised-learning/k_means.ipynb",
    "notebooks/unsupervised-learning/pca.ipynb",
    "notebooks/deep-learning/neural_networks.ipynb",
    "notebooks/deep-learning/cnn.ipynb",
    "notebooks/deep-learning/rnn.ipynb",
    "projects/titanic-survival-prediction/titanic.ipynb",
    "projects/titanic-survival-prediction/README.md",
    "projects/image-classifier/classifier.ipynb",
    "projects/image-classifier/README.md",
    "datasets/titanic.csv",
    "datasets/sample_images/cat.jpg",
    "datasets/sample_images/dog.jpg",
    "resources/books.md",
    "resources/courses.md",
    "resources/cheatsheets.md",
    "resources/links.md"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("📁 Machine Learning repo structure created.")
