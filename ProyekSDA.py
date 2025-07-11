import pandas as pd

file_path = r"D:\Dokumen\punya jiann\Project\PROJECT SDA\heart disease.csv"
df = pd.read_csv(file_path)

df_info = df.info()
df_head = df.head()
df_description = df.describe(include='all')

df_info, df_head, df_description

df_clean = df.copy()

thal_unique = df_clean['thal'].unique()
ca_unique = df_clean['ca'].unique()

thal_unique, ca_unique

import numpy as np

df_clean['thal'] = df_clean['thal'].replace(0, np.nan)
df_clean['ca'] = df_clean['ca'].replace(4, np.nan)

df_clean = df_clean.dropna()

df_subset = df_clean.sample(n=30, random_state=42)

df_subset.reset_index(drop=True).head()

import matplotlib.pyplot as plt
import seaborn as sns

numerical_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']

fig_num, axes_num = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
axes_num = axes_num.flatten()

for i, col in enumerate(numerical_cols):
    sns.histplot(df[col], bins=20, kde=True, ax=axes_num[i], color='skyblue')
    axes_num[i].set_title(f'Distribusi {col}')
    
if len(numerical_cols) % 2 != 0:
    axes_num[-1].axis('off')

fig_num.tight_layout()

fig_cat, axes_cat = plt.subplots(nrows=3, ncols=3, figsize=(18, 12))
axes_cat = axes_cat.flatten()

for i, col in enumerate(categorical_cols):
    sns.countplot(x=df[col], ax=axes_cat[i], palette='Set2')
    axes_cat[i].set_title(f'Distribusi {col}')
    
if len(categorical_cols) % 3 != 0:
    for j in range(len(categorical_cols), len(axes_cat)):
        axes_cat[j].axis('off')

fig_cat.tight_layout()

plt.show()

class Node:
    def __init__(self, attribute=None, threshold=None, left=None, right=None, result=None, is_greater=False, is_equal=False):
        self.attribute = attribute
        self.threshold = threshold
        self.left = left
        self.right = right
        self.result = result
        self.is_greater = is_greater
        self.is_equal = is_equal

    def is_leaf(self):
        return self.result is not None

def build_tree():
    
    root = Node('cp', 1)
    root.left = Node('thal', 2)
    root.right = Node('oldpeak', 1.5)
    
    root.left.left = Node(result='Tidak')
    root.left.right = Node('age', 50, is_greater=True)
    root.right.left = Node(result='Tidak')
    root.right.right = Node('exang', 1, is_equal=True)
    
    root.left.right.left = Node(result='Tidak')
    root.left.right.right = Node(result='Ada')
    root.right.right.left = Node(result='Tidak')
    root.right.right.right = Node(result='Ada')

    return root

def traverse_tree(node, data):
    if node.is_leaf():
        return node.result
    attribute_value = data.get(node.attribute, None)
    if attribute_value is None:
        return "Data tidak lengkap"
    if attribute_value <= node.threshold:
        return traverse_tree(node.left, data)
    else:
        return traverse_tree(node.right, data)
def print_tree(node, indent=""):
    if node.is_leaf():
        print(indent + "└── " + node.result)
    else:
        if node.is_equal:
            comparison = "=="
        elif node.is_greater:
            comparison = ">"
        else:
            comparison = "<="
        print(indent + f"[{node.attribute} {comparison} {node.threshold}]")
        if node.left:
            print(indent + "├── Left:")
            print_tree(node.left, indent + "│   ")
        if node.right:
            print(indent + "└── Right:")
            print_tree(node.right, indent + "    ")

if __name__ == "__main__":
    tree = build_tree()
    print("Struktur Pohon Keputusan:")
    print_tree(tree)
    sample_data = {
        'cp': 0,
        'thal': 2,
        'age': 55,
        'oldpeak': 1.2,
        'exang': 0
    }
    result = traverse_tree(tree, sample_data)
    print(f"Hasil diagnosis: {result}")

root = build_tree()

pasienA = {'cp': 0, 'thal': 2, 'age': 55, 'exang': 0, 'oldpeak': 1.0}
pasienB = {'cp': 2, 'thal': 3, 'age': 40, 'exang': 1, 'oldpeak': 3.5}
pasienC = {'cp': 2, 'thal': 2, 'age': 35, 'exang': 0, 'oldpeak': 1.0}

print("Pasien A:", traverse_tree(root, pasienA))
print("Pasien B:", traverse_tree(root, pasienB))
print("Pasien C:", traverse_tree(root, pasienC))

import streamlit as st

# Decision Tree
class Node:
    def __init__(self, attribute=None, threshold=None, left=None, right=None, result=None, is_greater=False, is_equal=False):
        self.attribute = attribute
        self.threshold = threshold
        self.left = left
        self.right = right
        self.result = result
        self.is_greater = is_greater
        self.is_equal = is_equal

    def is_leaf(self):
        return self.result is not None

def build_tree():
    root = Node('cp', 1)
    root.left = Node('thal', 2)
    root.right = Node('oldpeak', 1.5)
    root.left.left = Node(result='Diagnosa menunjukkan bahwa tidak ditemukan indikasi penyakit jantung')
    root.left.right = Node('age', 50, is_greater=True)
    root.right.left = Node(result='Diagnosa menunjukkan bahwa tidak ditemukan indikasi penyakit jantung')
    root.right.right = Node('exang', 1, is_equal=True)
    root.left.right.left = Node(result='Diagnosa menunjukkan bahwa tidak ditemukan indikasi penyakit jantung')
    root.left.right.right = Node(result='Diagnosa menunjukkan bahwa ditemukan indikasi penyakit jantung')
    root.right.right.left = Node(result='Diagnosa menunjukkan bahwa tidak ditemukan indikasi penyakit jantung')
    root.right.right.right = Node(result='Diagnosa menunjukkan bahwa ditemukan indikasi penyakit jantung')
    return root

def traverse_tree(node, data):
    if node.is_leaf():

        return node.result
    attribute_value = data.get(node.attribute, None)
    if attribute_value is None:
        return "Data tidak lengkap"
    if node.is_equal:
        if attribute_value == node.threshold:
            return traverse_tree(node.right, data)
        else:
            return traverse_tree(node.left, data)
    elif node.is_greater:
        if attribute_value > node.threshold:
            return traverse_tree(node.right, data)
        else:
            return traverse_tree(node.left, data)
    else:
        if attribute_value <= node.threshold:
            return traverse_tree(node.left, data)
        else:
            return traverse_tree(node.right, data)

# --- Kode Streamlit ---
st.title("Aplikasi Klasifikasi Gejala Penyakit Jantung")

st.write("Masukkan data gejala pasien:")

cp = st.number_input("Chest Pain Type (Tipe Nyeri Dada)", min_value=0, max_value=3, value=0)
thal = st.number_input("Thal (Kelainan Darah)", min_value=0, max_value=3, value=2)
age = st.number_input("Age (Umur)", min_value=1, max_value=120, value=55)
oldpeak = st.number_input("Oldpeak (Tingkat Depresi )", min_value=0.0, max_value=10.0, value=1.2, step=0.1)
exang = st.number_input("Exang(Nyeri Dada Saat Berolahraga)", min_value=0, max_value=1, value=0)

if st.button("Diagnosa"):
    data = {
        'cp': cp,
        'thal': thal,
        'age': age,
        'oldpeak': oldpeak,
        'exang': exang
    }
    tree = build_tree()
    result = traverse_tree(tree, data)
    st.success(f"Hasil diagnosis: {result}")
