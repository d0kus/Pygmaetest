import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

#Task1
data_dir = '../../data'
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, 'students_scores.csv')


names = ['Aisha', 'Daniyar', 'Zarina', 'Arman', 'Gulnur',
 'Bekzat', 'Saltanat', 'Nursultan', 'Madina', 'Yerlan',
 'Aizat', 'Timur', 'Moldir', 'Azat', 'Diana',
 'Sanzhar', 'Ainur', 'Marat', 'Kamila', 'Dauren']
genders = ['Female','Male','Female','Male','Female',
 'Male','Female','Male','Female','Male',
 'Female','Male','Female','Male','Female',
 'Male','Female','Male','Female','Male']
groups = ['SE-101','SE-101','SE-102','SE-102','SE-103',
 'SE-103','SE-101','SE-102','SE-103','SE-101',
 'SE-102','SE-103','SE-101','SE-102','SE-103',
 'SE-101','SE-102','SE-103','SE-101','SE-102']
with open(filepath, 'w', newline='') as f:
 writer = csv.writer(f)
 writer.writerow(['student_id','name','gender','group',
 'math_score','python_score','english_score'])
 for i, name in enumerate(names):
    writer.writerow([
        i + 1, name, genders[i], groups[i],
        random.randint(45, 100),
        random.randint(40, 100),
        random.randint(50, 100)
 ])
print(f'Dataset saved to: {os.path.abspath(filepath)}')

if os.path.exists(filepath):
    print(f"File found: {filepath}.")
    print(f"Absolute path: {os.path.abspath(filepath)}", end='\n\n')
else:
    print("Error: File not found.", end="\n\n")
    exit()

#Task2
with open(filepath, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    print(f'Fields: {reader.fieldnames}')

    all_data = list(reader)

    for i in range(5):
        print(f'Row: {i+1}: {all_data[i]}')

    print(f'Total students: {len(all_data)}')
print("\n")

#Task3a
df = pd.read_csv(filepath)
print("DataFrame Preview")
print(df.head(), end='\n\n')

print("DataFrame Shape")
print(df.shape, end='\n\n')

print("Column data types")
print(df.dtypes, end='\n\n')

#Task3b
print("DataFrame Summary Statistics")
print(df.describe(), end='\n\n')

score_columns = ['math_score', 'python_score', 'english_score']

print('Score analysis')
for col in score_columns:
    col_mean = df[col].mean()
    col_median = df[col].median()
    col_std = df[col].std()

    print(f'{col} stats')
    print(f'Mean: {col_mean:.2f}')
    print(f'Median: {col_median:.2f}')
    print(f'Standard Deviation: {col_std:.2f}')
print()

#Task3c
df['average_score'] = df[score_columns].mean(axis=1).round(2)
print('Updated dataframe')
print(df[['name', 'group', 'average_score']])
print()

#Task3d
high_score = df[df['average_score'] >=75]
print('Highest scorers')
print(high_score[['name', 'average_score']])
print()

se101 = df[df['group'] == 'SE-101']
print('Students from SE-101')
print(se101[['name','group', 'average_score']])
print()

#Task3e
group_means = df.groupby('group')[score_columns].mean().round(2)
print('Mean scores per group')
print(group_means, end='\n\n')

gender_means = df.groupby('gender')[['average_score']].mean()
print('Mean scores per gender')
print(gender_means, end='\n\n')

#Task4
# Plot 1: Bar chart
group_avg = df.groupby('group')['average_score'].mean()
plt.figure(figsize=(8, 5))

plt.bar(group_avg.index, group_avg.values, color=['#3498DB','#E74C3C','#2ECC71'])

plt.title('Average Score by Study Group')
plt.xlabel('Study Group')
plt.ylabel('Average Score')
plt.savefig(os.path.join(data_dir, 'bar_group_avg.png'), dpi=150, bbox_inches='tight')
plt.show()

# Plot 2: Histogram
plt.figure(figsize=(8, 5))

plt.hist(df['python_score'], bins=10, color='#9B59B6', edgecolor='white')

plt.title('Distribution of Python Scores')
plt.xlabel('Python Score')
plt.ylabel('Number of Students')
plt.savefig(os.path.join(data_dir, 'hist_python_scores.png'), dpi=150, bbox_inches='tight')
plt.show()

# Plot 3: Box plot
plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x='gender', y='average_score', hue='gender', palette='Set2', legend=False)

plt.title('Score Distribution by Gender')
plt.savefig(os.path.join(data_dir, 'box_gender_scores.png'), dpi=150, bbox_inches='tight')
plt.show()

# Plot 4: Heatmap
plt.figure(figsize=(8, 6))

corr = df[['math_score','python_score','english_score','average_score']].corr()

sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')

plt.title('Correlation Matrix of Student Scores')
plt.savefig(os.path.join(data_dir, 'heatmap_correlation.png'), dpi=150, bbox_inches='tight')
plt.show()







