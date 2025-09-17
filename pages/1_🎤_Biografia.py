import streamlit as st

st.title("🎤 Biografía de Bad Bunny")

st.write("""
**Benito Antonio Martínez Ocasio**, conocido artísticamente como **Bad Bunny**, nació en Puerto Rico en 1994.
Es cantante, compositor y productor de música urbana, reconocido por revolucionar el reguetón y el trap latino.
""")

st.image(
    "https://cdn0.celebritax.com/sites/default/files/styles/rectangle_blur_1200x900/public/1551650095-legisladora-chilena-arremete-contra-bad-bunny-su-presentacion-vina-mar-2019.jpg",
    caption="Bad Bunny en 2019",
    use_container_width=True
)

# Menú interno
opcion = st.radio("Explorar:", ["Infancia", "Carrera", "Reconocimientos"])
if opcion == "Infancia":
    st.info("""
            Benito Antonio Martínez Ocasio nació el **10 de marzo de 1994 en Vega Baja, Puerto Rico**.  
            Desde niño mostró gran interés por la música, especialmente por el reguetón y el rap latino.  
            Cantaba en el coro de la iglesia y, en su adolescencia, comenzó a experimentar subiendo canciones 
            a **SoundCloud**, donde ganó notoriedad de manera orgánica.  
            Su apodo "Bad Bunny" nació de una foto de su infancia disfrazado de conejo con una expresión molesta.
            """)
elif opcion == "Carrera":
    st.success("""
                - **2016:** Publicó el sencillo "Soy Peor", que lo posicionó como una nueva figura del trap latino.  
                - **2017-2018:** Colaboró con artistas como J Balvin, Cardi B y Drake, aumentando su reconocimiento mundial.  
                - **2018:** Lanzó su primer álbum, *X 100pre*, consolidando su estilo único y experimental.  
                - **2020:** Con *YHLQMDLG* rompió récords de streaming y se convirtió en el álbum en español más exitoso en Spotify.  
                - **2022:** Con *Un Verano Sin Ti*, se mantuvo como el artista más escuchado a nivel global en Spotify por tres años consecutivos.  
            Además, ha incursionado en la **lucha libre (WWE)** y el **cine** (película *Bullet Train* junto a Brad Pitt).
               """)
elif opcion == "Reconocimientos":
    st.warning("""
    Bad Bunny ha recibido numerosos premios y reconocimientos:  
    - 🏆 **Grammy Awards:** Mejor Álbum de Música Urbana por *El Último Tour del Mundo* (2022).  
    - 🏆 **Grammy Latinos:** Múltiples galardones incluyendo Álbum del Año y Mejor Álbum de Música Urbana.  
    - 🎶 **Billboard Music Awards:** Artista Latino del Año en varias ediciones.  
    - 🌍 En 2020, 2021 y 2022 fue el **artista más escuchado en Spotify a nivel global**.  
    - 💡 Considerado como un innovador de la música urbana por mezclar reguetón, trap, rock, pop y hasta géneros alternativos.  
    """)
