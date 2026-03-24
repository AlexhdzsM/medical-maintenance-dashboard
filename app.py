
import streamlit as st
import pandas as pd

st.title("🏥 Medical Maintenance Dashboard")

# Cargar datos
df = pd.read_csv("data/data.csv")

st.subheader("Dataset")
st.dataframe(df)

# Filtro por equipo
equipment = st.multiselect(
    "Selecciona tipo de equipo",
    df["equipment_type"].unique(),
    default=df["equipment_type"].unique()
)

filtered_df = df[df["equipment_type"].isin(equipment)]



st.subheader("Datos filtrados")
st.dataframe(filtered_df)

st.subheader("Métricas")

total_downtime = filtered_df["downtime_hours"].sum()
total_cost = filtered_df["cost"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Downtime total", f"{total_downtime} hrs")

with col2:
    st.metric("Costo total", f"${total_cost}")

avg_downtime = filtered_df["downtime_hours"].mean()

st.metric("Promedio downtime por falla", f"{avg_downtime:.1f} hrs")

st.subheader("Downtime total por equipo")

downtime_by_equipment = filtered_df.groupby("equipment_type")["downtime_hours"].sum()

st.bar_chart(downtime_by_equipment)




st.subheader("Tipo de fallas")

failure_counts = filtered_df["failure_type"].value_counts()

st.bar_chart(failure_counts)

st.subheader("Insight")

worst_equipment = df.groupby("equipment_type")["downtime_hours"].sum().idxmax()

st.subheader("Insight clave")

worst_equipment = df.groupby("equipment_type")["downtime_hours"].sum().idxmax()
worst_value = df.groupby("equipment_type")["downtime_hours"].sum().max()

st.write(
    f"El equipo {worst_equipment} concentra el mayor downtime ({worst_value} hrs), "
    "lo que sugiere priorizar mantenimiento o evaluar costos de reemplazo."
)



st.subheader("Costo vs Downtime")

comparison = df.groupby("equipment_type")[["downtime_hours", "cost"]].sum()

st.dataframe(comparison.style.highlight_max(axis=0))