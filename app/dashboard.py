
import streamlit as st
import pandas as pd

from src.read import get_results


st.set_page_config(
    page_title="Math Functions ETL",
    page_icon="📊",
    layout="wide"
)

st.title("Math Functions ETL Dashboard")
st.write("Consulta los resultados almacenados en SQLite.")

try:
    results = get_results()

    if results:
        df = pd.DataFrame(results)

        st.metric("Total de registros", len(df))

        operations = ["Todas"] + sorted(
            df["operation"].dropna().unique().tolist()
        )

        selected_operation = st.selectbox(
        "Filtrar por operación",
        operations)

        if selected_operation == "Todas":
            filtered_df = df
        else:
            filtered_df = df[df["operation"] == selected_operation]

        st.dataframe(filtered_df, use_container_width=True)     
    else:
        st.info("No hay resultados disponibles.")

except Exception:
    st.error("No fue posible consultar los resultados.")