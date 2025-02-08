import pandas as pd
import streamlit as st
import plotly.express as px


#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#.\av\Scripts\activate

# lista de datasets disponíveis
datasets = {
    "Salary": "data-dashboard-streamlit/dir/1_Salary/Salary.csv",
    "Fitness": "data-dashboard-streamlit/dir/2_Fitness/Fitness.csv",
    "MotorCO2": "data-dashboard-streamlit/dir/3_MotorCO2/FuelConsumptionCo2.csv",
    "Insurance": "data-dashboard-streamlit/dir/4_Insurance/insurance.csv",
    "Bike_rent": "data-dashboard-streamlit/dir/5_Bike_rent/Bike_rent.csv",
    "kc_house_data": "data-dashboard-streamlit/dir/6_kc_house_data/kc_house_data.csv",
}

# interface do Streamlit
st.title("Dashboard Interativo de Análise de Dados")

# coluna lateral
with st.sidebar:
    dataset_name = st.selectbox("Escolha um dataset", list(datasets.keys()))
    st.download_button(
        label="Baixar dados originais",
        data=open(datasets[dataset_name], "rb").read(),
        file_name=f"{dataset_name}.csv",
        mime="text/csv",
    )

# carregar dados
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

df = load_data(datasets[dataset_name])

# limpeza básica
df = df.drop_duplicates()
df = df.dropna()

# conteúdo principal
tab1, tab2, tab3 = st.tabs(["Prévia dos Dados", "Estatísticas Descritivas", "Visualização de Dados"])

with tab1:
    st.write(df.head())

with tab2:
    st.write(df.describe())

with tab3:
    if dataset_name == "Salary":
        fig = px.histogram(df, x="Salary", color="Gender", title="Distribuição Salarial por Gênero")
    elif dataset_name == "Fitness":
        fig = px.scatter(df, x="step_count", y="calories_burned", color="mood", title="Correlação entre Passos e Calorias Queimadas")
    elif dataset_name == "MotorCO2":
        fig = px.scatter(df, x="FUELCONSUMPTION_COMB", y="CO2EMISSIONS", color="ENGINESIZE", title="Consumo de Combustível vs Emissões de CO2")
    elif dataset_name == "Insurance":
        fig = px.box(df, x="smoker", y="charges", title="Impacto do Hábito de Fumar no Custo do Seguro")
    elif dataset_name == "Bike_rent":
        fig = px.line(df, x="dteday", y="cnt", title="Padrões de Aluguel de Biculas ao Longo do Tempo")
    elif dataset_name == "kc_house_data":
        fig = px.scatter(df, x="sqft_living", y="price", title="Tamanho da Casa vs Preço")
    st.plotly_chart(fig)

# download dos dados filtrados
st.download_button(
    label="Baixar dados filtrados",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name=f"{dataset_name}_filtrado.csv",
    mime="text/csv",
)
