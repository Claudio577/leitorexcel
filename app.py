import streamlit as st
import pandas as pd

st.title("📊 Leitor de Excel – Identificação de Notas Baixas")

st.write("Envie um arquivo Excel (.xlsx) contendo uma coluna chamada **nota**.")

# Upload do Excel
arquivo = st.file_uploader("Envie o arquivo Excel:", type=["xlsx"])

if arquivo:
    # Lê o arquivo Excel
    df = pd.read_excel(arquivo)

    st.subheader("📄 Pré-visualização da tabela:")
    st.dataframe(df)

    # Verifica se existe a coluna 'nota'
    if "nota" not in df.columns:
        st.error("❌ A planilha deve conter uma coluna chamada **nota**.")
        st.stop()

    # Campo para definir nota limite
    nota_min = st.number_input(
        "Mostrar alunos com nota abaixo de:",
        min_value=0.0,
        max_value=10.0,
        value=6.0
    )

    # Bo
