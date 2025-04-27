#############################################################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px


###### INICIO | INTRODUCAO ######
#Configuracoes iniciais
st.set_page_config(page_title="Análise de Performance por Departamento", layout="wide")
st.title('📊 Análise de Performance e Gastos por Departamento')

#Storytelling ...


###### INICIO | DATAFRAME - INTRODUZIR ######
#Carregando os dados
df = pd.read_csv('employee_performance.csv')
st.subheader('Amostra dos Dados')
st.dataframe(df.sample(10))

#Copia de seguranca
copiaDF = df.copy()
###### FIM | DATAFRAME - INTRODUZIR ######



###### INICIO | SIDEBAR ######
st.sidebar.header("test")
departamentos = df['Department'].unique()

#Filtro multiselect
departamento_selecionado = st.sidebar.multiselect(
    "Selecione o Departamento:",
    options=departamentos,
    default=departamentos
)
###### FIM | SIDEBAR ######



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


#Configurando graficos
sns.set(style="whitegrid", palette="muted")


# Dividir a tela em duas colunas
col1, col2 = st.columns(2)
# Exibir os gráficos nas colunas
with col1:
            ###### INICIO | BARRA VERTICAL - GASTO POR DEPARTAMENTO ######
            st.subheader('Gasto Total por Departamento (Salários)')
            gastoPorDepartamento = copiaDF.groupby('Department')['Salary'].sum().sort_values(ascending=False)
            st.bar_chart(gastoPorDepartamento)
            ###### FIM | BARRA VERTICAL - GASTO POR DEPARTAMENTO ######

with col2:
            ###### INICIO | BARRA HORIZONTAL - HORAS DE TREINAMENTO POR DEPARTAMENTO ######
            st.subheader('Total de Horas de Treinamento por Departamento')
            hours_by_department = copiaDF.groupby('Department')['Training_Hours'].sum().sort_values(ascending=False)

            fig = go.Figure(go.Bar(
                        x=hours_by_department.values,
                        y=hours_by_department.index,
                        orientation='h')
               )
            st.plotly_chart(fig,
                        theme="streamlit"
               )
            ###### FIM | BARRA HORIZONTAL - HORAS DE TREINAMENTO POR DEPARTAMENTO ######




###### INICIO | LINHA - MEDIA DE HORAS DE TREINAMENTO vs MEDIA DE PERFORMANCE POR DEPARTAMENTO ######
st.subheader('Relação entre Horas de Treinamento e Performance')

#Agrupamento de dados
agg_df = copiaDF.groupby('Department').agg({
    'Training_Hours': 'mean',
    'Performance_Score': 'mean'
}).reset_index()

fig = px.line(
    agg_df,
    x='Training_Hours',
    y='Performance_Score',
    color='Department',
    markers=True
)

fig.update_layout(
    xaxis_title='Média de Horas de Treinamento',
    yaxis_title='Média de Performance',
    template='plotly_dark',
    width=800,
    height=500,
    legend_title='Departamento'
)

st.plotly_chart(fig, use_container_width=True)
###### FIM | LINHA - RELAÇÃO ENTRE HORAS DE TREINAMENTO E PERFORMANCE POR DEPARTAMENTO ######




###### INICIO | GRAFICO - SALARIO MEDIO POR DEPARTAMENTO ######
st.subheader('Salário Médio por Departamento')

#Agrupando os dados
salario_df = copiaDF.groupby('Department').agg({
    'Salary': 'mean'
}).reset_index()

fig = px.bar(
    salario_df,
    x='Salary',
    y='Department',
    orientation='h',          #barras horizontais
    color='Department',       #cores por departamento
    text_auto='.2s'           #valores nas barras
)

fig.update_layout(
    xaxis_title='Salário Médio (R$)',
    yaxis_title='Departamento',
    template='plotly_dark',    #'plotly_white'
    width=800,
    height=500,
    showlegend=False          #remove legenda
)

st.plotly_chart(fig, use_container_width=True)
###### FIM | GRAFICO - SALARIO MEDIO POR DEPARTAMENTO ######


#############################################################################################################################
