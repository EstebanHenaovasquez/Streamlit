import streamlit as st

st.title("💿 Discografía de Bad Bunny")

st.write("""
Bad Bunny ha lanzado varios álbumes exitosos que han marcado la música latina.
""")

st.image(
    "https://tercerparlante.com/wp-content/uploads/2025/01/DeBI-TiRAR-MaS-FOToS-Bad-bunny-2025-001-1-scaled.jpg",
    caption="X 100pre (2018)",
    use_container_width=True
)

# Menú interno
opcion = st.radio("Explorar:", ["Álbumes", "Colaboraciones", "Estilo"])

if opcion == "Álbumes":
    st.info("""
    **Principales álbumes de estudio:**
    
    - 🎵 *X 100pre* (2018)  
      Su primer álbum, con éxitos como *Estamos Bien* y *Caro*.  
      Fue incluido en la lista de los 500 mejores álbumes de todos los tiempos por la revista Rolling Stone.
    
    - 🎵 *YHLQMDLG* (2020) (*Yo Hago Lo Que Me Da La Gana*)  
      Considerado uno de los mejores discos de reguetón moderno.  
      Incluye temas como *Safaera* y *La Difícil*. Fue un fenómeno global en Spotify.
    
    - 🎵 *El Último Tour del Mundo* (2020)  
      Marcó un giro experimental en su carrera, con fusiones de rock, trap y reguetón.  
      Incluye *Dakiti* y *Booker T*. Se convirtió en el **primer álbum en español en ser #1 en el Billboard 200**.
    
    - 🎵 *Un Verano Sin Ti* (2022)  
      El álbum más reproducido en la historia de Spotify.  
      Combina ritmos caribeños, reguetón, dembow y baladas urbanas.  
      Temas como *Tití Me Preguntó* y *Me Porto Bonito* fueron himnos mundiales.
    """)

elif opcion == "Colaboraciones":
    st.success("""
    Bad Bunny ha trabajado con una amplia variedad de artistas, mostrando su versatilidad:
    
    - 🤝 Con J Balvin: álbum colaborativo *Oasis* (2019), con éxitos como *Qué Pretendes*.  
    - 🎶 Con Drake: *Mía* (2018), su primera gran colaboración internacional.  
    - 💃 Con Rosalía: *La Noche de Anoche* (2020), mezcla reguetón con flamenco.  
    - 🔥 Con Daddy Yankee y Anuel AA: *Sola y Vacía* y colaboraciones que consolidaron su liderazgo en el género.  
    - 🌍 Con artistas anglo: Post Malone, Cardi B (*I Like It*), The Weeknd (*La Noche de Anoche* versión remix).  

    Sus colaboraciones lo han convertido en un artista global que rompe barreras de idioma y género musical.
    """)

elif opcion == "Estilo":
    st.warning("""
    El estilo musical de Bad Bunny se caracteriza por su **versatilidad e innovación**:
    
    - 🎧 **Reguetón clásico:** mantiene la esencia del perreo, pero modernizado (*Safaera*, *Me Porto Bonito*).  
    - 🎤 **Trap latino:** pionero en popularizar este subgénero en el mundo hispanohablante (*Soy Peor*).  
    - 🎸 **Fusión con rock y alternativo:** canciones como *Maldita Pobreza* muestran su lado experimental.  
    - 🏝️ **Ritmos caribeños y tropicales:** dembow, bachata y baladas urbanas en *Un Verano Sin Ti*.  
    - 👗 **Identidad artística:** rompe estereotipos de género en la moda y la música, usando estilos únicos y mensajes sociales.  

    Su capacidad para **adaptarse y reinventarse** es lo que lo ha convertido en un fenómeno cultural y no solo musical.
    """)
