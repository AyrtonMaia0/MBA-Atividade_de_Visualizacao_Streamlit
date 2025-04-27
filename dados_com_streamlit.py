#############################################################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


###### INICIO | INTRODUCAO ######
#Configuracoes iniciais
st.set_page_config(page_title="Análise de Performance por Departamento", layout="wide")
st.title('📊 Análise de Performance e Gastos por Departamento')

#Storytelling ...


###### INICIO | SIDEBAR ######
st.sidebar.header("teste")

#Filter 1
#with st.sidebar:
#    st.[df.Department]
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


#Configurando graficos
sns.set(style="whitegrid", palette="muted")


# Dividir a tela em duas colunas
col1, col2 = st.columns(2)
# Exibir os gráficos nas colunas
with col1:
            ###### INICIO | GRAFICO - GASTO POR DEPARTAMENTO ######
            st.subheader('Gasto Total por Departamento (Salários)')
            gastoPorDepartamento = copiaDF.groupby('Department')['Salary'].sum().sort_values(ascending=False)
            st.bar_chart(gastoPorDepartamento)
            ###### FIM | GRAFICO - GASTO POR DEPARTAMENTO ######

with col2:
            ###### INICIO | GRAFICO - HORAS DE TREINAMENTO POR DEPARTAMENTO ######
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
            ###### FIM | GRAFICO - HORAS DE TREINAMENTO POR DEPARTAMENTO ######





###### INICIO | GRAFICO - MEDIA DE HORAS DE TREINAMENTO vs MEDIA DE PERFORMANCE POR DEPARTAMENTO ######
st.subheader('Média de Horas de Treinamento vs. Performance')

# Agrupando os dados
agg_df = copiaDF.groupby('Department').agg({
    'Training_Hours': 'mean',
    'Performance_Score': 'mean'
}).sort_values('Training_Hours', ascending=False)

# Criando gráfico interativo com Plotly
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=agg_df.index,
    y=agg_df['Training_Hours'],
    mode='lines+markers',
    name='Horas de Treinamento (Média)',
    line=dict(color='blue')
))

fig.add_trace(go.Scatter(
    x=agg_df.index,
    y=agg_df['Performance_Score'],
    mode='lines+markers',
    name='Performance Score (Média)',
    line=dict(color='green')
))

fig.update_layout(
    title='Média de Horas de Treinamento vs. Média de Performance por Departamento',
    xaxis_title='Departamento',
    yaxis_title='Média',
    legend_title='Métricas',
    xaxis=dict(tickangle=-45),
    template='plotly_white'
)

st.plotly_chart(fig, theme="streamlit")
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
