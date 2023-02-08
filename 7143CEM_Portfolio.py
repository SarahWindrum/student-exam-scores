# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Understanding the dataset 
exam_performance = pd.read_csv('StudentPerformance.csv')
print(exam_performance.parental_education.unique())
print(exam_performance.columns)
print(exam_performance.head())
print(exam_performance.dtypes)

# Question: what is the relationship between parental education and exam scores?
education_order = ["1 some high school", "2 high school", "3 some college", "4 associate's degree",
                   "5 bachelor's degree", "6 master's degree"]
student_counts = exam_performance['parental_education'].value_counts()

# Calculating averages to represent on stacked bar chart with matplotlib
average_scores_subset = exam_performance[['parental_education', 'math_score', 'reading_score', 'writing_score']]
print(average_scores_subset)
average_scores = average_scores_subset.groupby('parental_education').mean()
print(average_scores)
print(average_scores.describe())
print(type(average_scores))
plt.figure()
average_scores.plot(kind="bar", stacked=True, width=0.8)
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Exam Score')
plt.title('Student Exam Scores categorised by Parental Education')
plt.legend(['Math Average', 'Reading Average', 'Writing Average'], loc='lower left', ncol = 3)
plt.show()

# Stacked bar chart with Seaborn
import seaborn as sns
plt.figure()

sns.set(style="darkgrid")
sns.barplot(x='parental_education', y='math_score', data=average_scores_subset, order=education_order)
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Maths Exam Score')
plt.title('Student Exam Scores categorised by Parental Education')
plt.xticks(rotation=60)
plt.show()

# Stacked bar chart with plotly
import plotly.express as px

fig = px.bar(average_scores, y=["math_score", "reading_score", "writing_score"], title="Student Exam Scores categorised by Parental Education",
             labels={'value': 'Average Exam Score', 'parental_education': 'Parental Level of Education'})
fig.write_html("Student_Scores_Parent_Education.html", auto_open=True)

# Scatterplot to explore correlation between reading score & writing score
plt.figure()
plt.scatter('reading_score', 'writing_score', data=exam_performance, 
         marker='o', cmap="Blues", alpha=0.5)
plt.xlabel("Reading Exam Scores")
plt.ylabel("Writing Exam Scores")
plt.title("Relationship between Reading & Writing Exam Scores")
plt.show()
# Would show visually better using jitter

# Scatterplot with Seaborn
sns.regplot(x=exam_performance["reading_score"], y=exam_performance["writing_score"], marker='+', fit_reg=False, 
            scatter_kws={"color":"darkred","alpha":0.5,"s":75})
# Adding in gender
sns.lmplot(x="reading_score", y="writing_score", data=exam_performance, hue='gender', legend=False, fit_reg=False)
plt.legend(loc='lower right')

# Scatterplot with plotly (gender and scores)
fig = px.scatter(exam_performancw, x="reading_score", y="writing_score", 
                 title="Relationship between Reading & Writing Exam Scores",
                 color="gender", hover_data=["math_score"])
fig.write_html("Student_Scores_Literacy.html", auto_open=True)

plt.title("Relationship between Reading & Writing Exam Scores")




