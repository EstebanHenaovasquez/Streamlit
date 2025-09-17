import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Análisis de Bad Bunny")

# Datos ficticios de ejemplo
data = {
    "Álbum": ["X 100pre", "YHLQMDLG", "El Último Tour del Mundo", "Un Verano Sin Ti"],
    "Año": [2018, 2020, 2020, 2022],
    "Canciones": [15, 20, 16, 23],
    "Streams (billones)": [3.5, 8.0, 6.2, 12.5]
}
df = pd.DataFrame(data)

st.write("### Discografía con número de canciones y streams (ejemplo)")
st.dataframe(df)

# --- Gráfico de barras ---
st.write("#### Número de canciones por álbum")
fig, ax = plt.subplots()
ax.bar(df["Álbum"], df["Canciones"], color="purple")
ax.set_ylabel("Canciones")
st.pyplot(fig)

# --- Gráfico de líneas ---
st.write("#### Streams acumulados por álbum")
fig, ax = plt.subplots()
ax.plot(df["Álbum"], df["Streams (billones)"], marker="o", color="green")
ax.set_ylabel("Streams (billones)")
st.pyplot(fig)

# --- Gráfico circular ---
st.write("#### Proporción de streams por álbum")
fig, ax = plt.subplots()
ax.pie(df["Streams (billones)"], labels=df["Álbum"], autopct="%1.1f%%")
st.pyplot(fig)

# Explicación
st.write("""
**Interpretación:**
- *Un Verano Sin Ti* es el álbum más escuchado en plataformas digitales.
- *YHLQMDLG* fue un gran éxito con un alto número de streams.
- Los primeros álbumes marcaron su estilo, pero los más recientes consolidaron su fama mundial.
""")
