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

#gastoPorDepartamento = copiaDF.groupby('Department')['Salary'].sum()
#gastoPorDepartamento

#######################################################
st.title('Teste')

#Configurando graficos
sns.set(style="whitegrid", palette="muted")


st.header('Total de Horas de Treinamento por Departamento')
#Horas de Treinamento por Departamento
hours_by_department = copiaDF.groupby('Department')['Training_Hours'].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(x=hours_by_department.values, y=hours_by_department.index, palette="viridis", ax=ax1)
ax1.set_title('Total de Horas de Treinamento por Departamento')
ax1.set_xlabel('Horas Totais')
ax1.set_ylabel('Departamento')
st.pyplot(fig1)





#############################################################################################

