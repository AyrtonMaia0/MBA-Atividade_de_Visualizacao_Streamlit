#############################################################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


###### INICIO | INTRODUCAO ######
#Configuracoes iniciais
st.set_page_config(page_title="Análise de Performance por Departamento", layout="wide")
st.title('📊 Análise de Performance e Gastos por Departamento')

#Storytelling ...


###### INICIO | SIDEBAR ######
st.sidebar.header("teste")

#Filter 1
with st.sidebar:
    select_box = st.selectbox(
        "Escolha um dos Departamentos",
        (df['Department'])
    )
###### FIM | SIDEBAR ######


###### INICIO | DATAFRAME - INTRODUZIR ######
#Carregando os dados
df = pd.read_csv('employee_performance.csv')
st.subheader('Amostra dos Dados')
st.dataframe(df.sample(10))

#Copia de seguranca
copiaDF = df.copy()
###### FIM | DATAFRAME - INTRODUZIR ######

###### INICIO | DATAFRAME - INFORMAÇÕES ######
#st.subheader('Informações do Dataset')
#buffer = copiaDF.info()
#st.text(buffer)
###### FIM | DATAFRAME - INFORMAÇÕES ######


###### INICIO | DATAFRAME - VALORES NULOS ######
#Verificando valores nulos
st.subheader('Valores Nulos por Coluna')
st.write(copiaDF.isna().sum())
###### FIM | DATAFRAME - VALORES NULOS ######


###### INICIO | GRAFICO - GASTO POR DEPARTAMENTO ######
st.subheader('Gasto Total por Departamento (Salários)')
gastoPorDepartamento = copiaDF.groupby('Department')['Salary'].sum().sort_values(ascending=False)
st.bar_chart(gastoPorDepartamento)
###### FIM | GRAFICO - GASTO POR DEPARTAMENTO ######


#Configurando graficos
sns.set(style="whitegrid", palette="muted")


###### INICIO | GRAFICO - HORAS DE TREINAMENTO POR DEPARTAMENTO ######
st.subheader('Total de Horas de Treinamento por Departamento')
hours_by_department = copiaDF.groupby('Department')['Training_Hours'].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(x=hours_by_department.values, y=hours_by_department.index, palette="viridis", ax=ax1)
ax1.set_title('Total de Horas de Treinamento por Departamento')
ax1.set_xlabel('Horas Totais')
ax1.set_ylabel('Departamento')
st.pyplot(fig1)
###### FIM | GRAFICO - HORAS DE TREINAMENTO POR DEPARTAMENTO ######


###### INICIO | GRAFICO - MEDIA DE HORAS DE TREINAMENTO vs MEDIA DE PERFORMANCE POR DEPARTAMENTO ######
#Relacao entre Horas Gastas e Performance - Media por Departamento
st.subheader('Média de Horas de Treinamento vs. Performance')

agg_df = copiaDF.groupby('Department').agg({
    'Training_Hours': 'mean',
    'Performance_Score': 'mean'
}).sort_values('Training_Hours', ascending=False)

fig2, ax2 = plt.subplots(figsize=(12,6))
sns.lineplot(data=agg_df, markers=True, dashes=False, ax=ax2)
ax2.set_title('Média de Horas de Treinamento vs. Média de Performance por Departamento')
ax2.set_xlabel('Departamento')
ax2.set_ylabel('Média')
ax2.grid(True)
ax2.set_xticklabels(agg_df.index, rotation=45)
st.pyplot(fig2)
###### FIM | GRAFICO - MEDIA DE HORAS DE TREINAMENTO vs MEDIA DE PERFORMANCE POR DEPARTAMENTO ######


###### INICIO | GRAFICO - SALARIO MEDIO POR DEPARTAMENTO ######
st.subheader('Salário Médio por Departamento')

salary_by_department = copiaDF.groupby('Department')['Salary'].mean().sort_values(ascending=False)

fig3, ax3 = plt.subplots(figsize=(10,6))
sns.barplot(x=salary_by_department.values, y=salary_by_department.index, palette="rocket", ax=ax3)
ax3.set_title('Salário Médio por Departamento')
ax3.set_xlabel('Salário Médio (R$)')
ax3.set_ylabel('Departamento')
st.pyplot(fig3)
###### FIM | GRAFICO - SALARIO MEDIO POR DEPARTAMENTO ######


#############################################################################################################################
