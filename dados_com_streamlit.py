# -*- coding: utf-8 -*-

# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv('employee_performance.csv')
#df.sample(10)

copiaDF = df.copy()

#copiaDF.info()

#copiaDF.isna().sum()

gastoPorDepartamento = copiaDF.groupby('Department')['Salary'].sum()
#gastoPorDepartamento

#######################################################
st.title('Teste')

#Configurando graficos
sns.set(style="whitegrid", palette="muted")

#Horas de Treinamento por Departamento
hours_by_department = copiaDF.groupby('Department')['Training_Hours'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=hours_by_department.values, y=hours_by_department.index, palette="viridis")
plt.title('Total de Horas de Treinamento por Departamento')
plt.xlabel('Horas Totais')
plt.ylabel('Departamento')
plt.tight_layout()
st.write(plt.show())

#Relacao entre Horas Gastas e Performance
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Training_Hours', y='Performance_Score', hue='Department', palette='tab10', s=100)
plt.title('Horas de Treinamento vs. Performance por Departamento')
plt.xlabel('Horas de Treinamento')
plt.ylabel('Performance')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#Salario medio por Departamento
salary_by_department = copiaDF.groupby('Department')['Salary'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=salary_by_department.values, y=salary_by_department.index, palette="rocket")
plt.title('Salário Médio por Departamento')
plt.xlabel('Salário Médio (R$)')
plt.ylabel('Departamento')
plt.tight_layout()
plt.show()



