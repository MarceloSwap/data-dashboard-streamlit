import pandas as pd
import streamlit as st
import plotly.express as px

# lista de datasets disponíveis
datasets = {
    "Salary": "C:/Users/marce/OneDrive/Documentos/projeto/dir/1_Salary/Salary.csv",
    "Fitness": "C:/Users/marce/OneDrive/Documentos/projeto/dir/2_Fitness/Fitness.csv",
    "MotorCO2": "C:/Users/marce/OneDrive/Documentos/projeto/dir/3_MotorCO2/FuelConsumptionCo2.csv",
    "Insurance": "C:/Users/marce/OneDrive/Documentos/projeto/dir/4_Insurance/insurance.csv",
    "Bike_rent": "C:/Users/marce/OneDrive/Documentos/projeto/dir/5_Bike_rent/Bike_rent.csv",
    "kc_house_data": "C:/Users/marce/OneDrive/Documentos/projeto/dir/6_kc_house_data/kc_house_data.csv",
}

# interface do Streamlit
st.title("Dashboard Interativo de Análise de Dados")

# Escolher o dataset
dataset_name = st.selectbox("Escolha um dataset", list(datasets.keys()))

# carregar os dados
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

df = load_data(datasets[dataset_name])

st.subheader("Prévia dos Dados")
st.write(df.head())

# Limpeza básica
df = df.drop_duplicates()
df = df.dropna()

# Estatísticas descritivas
st.subheader("Estatísticas Descritivas")
st.write(df.describe())

# Visualizações
st.subheader("Visualização de Dados")

if dataset_name == "Salary":
    fig = px.histogram(df, x="Salary", color="Gender", title="Distribuição Salarial por Gênero")
    st.plotly_chart(fig)
    
elif dataset_name == "Fitness":
    fig = px.scatter(df, x="Steps", y="Calories", color="Gender", title="Correlação entre Passos e Calorias Queimadas")
    st.plotly_chart(fig)
    
elif dataset_name == "MotorCO2":
    fig = px.scatter(df, x="Fuel Consumption", y="CO2 Emissions", color="Engine Size", title="Consumo de Combustível vs Emissões de CO2")
    st.plotly_chart(fig)
    
elif dataset_name == "Insurance":
    fig = px.box(df, x="smoker", y="charges", title="Impacto do Hábito de Fumar no Custo do Seguro")
    st.plotly_chart(fig)
    
elif dataset_name == "Bike_rent":
    fig = px.line(df, x="Date", y="Count", title="Padrões de Aluguel de Bicicletas ao Longo do Tempo")
    st.plotly_chart(fig)
    
elif dataset_name == "kc_house_data":
    fig = px.scatter(df, x="sqft_living", y="price", title="Tamanho da Casa vs Preço")
    st.plotly_chart(fig)

# Download dos dados filtrados
st.subheader("Baixar os Dados Filtrados")
st.download_button(
    label="Baixar CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name=f"{dataset_name}_cleaned.csv",
    mime="text/csv",
)

#st.write("Criado por Marcelo usando Streamlit 🚀")
