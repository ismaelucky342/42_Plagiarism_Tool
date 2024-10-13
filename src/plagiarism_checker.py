import os
import difflib
import numpy as np

import matplotlib.pyplot as plt

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def compare_files(file1, file2):
    content1 = read_file(file1)
    content2 = read_file(file2)
    diff = difflib.SequenceMatcher(None, content1, content2)
    return diff.ratio()

def generate_heatmap(similarity_matrix, project_files, comparison_files):
    fig, ax = plt.subplots()
    cax = ax.matshow(similarity_matrix, cmap='hot')
    plt.colorbar(cax)
    ax.set_xticks(np.arange(len(comparison_files)))
    ax.set_yticks(np.arange(len(project_files)))
    ax.set_xticklabels(comparison_files, rotation=90)
    ax.set_yticklabels(project_files)
    plt.xlabel('Comparison Repos')
    plt.ylabel('Project Files')
    plt.title('Plagiarism Heatmap')
    plt.show()

def plagiarism_checker(project_dir, comparison_dir):
    project_files = [os.path.join(project_dir, f) for f in os.listdir(project_dir) if os.path.isfile(os.path.join(project_dir, f))]
    comparison_files = [os.path.join(comparison_dir, f) for f in os.listdir(comparison_dir) if os.path.isfile(os.path.join(comparison_dir, f))]

    similarity_matrix = np.zeros((len(project_files), len(comparison_files)))

    for i, project_file in enumerate(project_files):
        for j, comparison_file in enumerate(comparison_files):
            similarity_matrix[i, j] = compare_files(project_file, comparison_file)

    generate_heatmap(similarity_matrix, project_files, comparison_files)

    avg_similarity = np.mean(similarity_matrix)
    print(f"Average similarity: {avg_similarity * 100:.2f}%")
    print("Similarity matrix:")
    print(similarity_matrix)

if __name__ == "__main__":
    project_dir = 'projects'
    comparison_dir = 'comparison_repos'
    plagiarism_checker(project_dir, comparison_dir)