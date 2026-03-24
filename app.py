import pandas as pd
import streamlit as st
import plotly.express as px
import sqlite3

# CONFIG 
st.set_page_config(layout="wide")

# CORES 
ROXO = "#6C5DD3"
ROXO_ESCURO = "#3B2F8C"
ROXO_CLARO = "#8A7BFF"
FUNDO = "#0b0f1a"
CARD = "#151a2e"

# CSS 
st.markdown(f"""

<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}

.stApp {{
    background: linear-gradient(135deg, {FUNDO}, #11172a);
    font-family: 'Inter', sans-serif;
    color: white;
}}

.block-container {{
    padding: 2rem 3rem;
}}

div[data-testid="stElementContainer"]:has(.card) 
    
 {{
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
    border: none !important;
}}

div[data-testid="stMarkdownContainer"]:has(.card) {{
    padding: 0 !important;
    margin: 0 !important;
    }}

/* CARD  */
.card {{
    background: {CARD};
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    text-align: center;
    transition: all 0.3s ease;
}}

.card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(108, 93, 211, 0.5),
                0 0 60px rgba(108, 93, 211, 0.3);
}}

.card-title {{
    font-size: 18px;
    opacity: 0.7;
    margin-bottom: 0px;
}}

.metric {{
    font-size: 34px;
    font-weight: 600;
}}

.label {{
    font-size: 13px;
    opacity: 0.7;
}}

.sidebar {{
    background: #0f1424;
    padding: 25px;
    border-radius: 18px;
    height: 90vh;
}}

.stButton>button {{
    background-color: {ROXO_ESCURO};
    color: white;
    border-radius: 10px;
    border: none;
}}

.stButton>button:hover {{
    background-color: {ROXO};
}}
</style>
""", unsafe_allow_html=True)

# KPI
def card_kpi(title, value):
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{title}</div>
        <div class="metric">{value}</div>
    </div>
    """, unsafe_allow_html=True)

#  DATA 
conn = sqlite3.connect("livros.db")
df = pd.read_sql_query("SELECT * FROM livros", conn)

# LAYOUT 
sidebar, main = st.columns([1, 4])

# SIDEBAR 
with sidebar:
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)

    st.markdown("## Dashboard")

    genero = st.multiselect(
        "Gênero",
        df['genero'].unique(),
        default=df['genero'].unique()
    )
    df = df[df['genero'].isin(genero)]

    autor = st.multiselect(
        "Autor",
        df['autor'].unique(),
        default=df['autor'].unique()
    )
    df = df[df['autor'].isin(autor)]

    nota_min = st.slider(
        "Nota mínima",
        min_value=float(df['nota'].min()),
        max_value=float(df['nota'].max()),
        value=float(df['nota'].min()),
        step=0.1
    )
    df = df[df['nota'] >= nota_min]

    st.markdown('</div>', unsafe_allow_html=True)

# MAIN 
with main:

    st.title("Visão geral")

    # KPIs 
    c1, c2, c3 = st.columns(3)

    with c1:
        card_kpi("Total de livros", len(df))

    with c2:
        card_kpi("Nota média", f"{df['nota'].mean():.2f}")

    with c3:
        card_kpi("Páginas médias", f"{df['paginas'].mean():.0f}")

    st.markdown("<br>", unsafe_allow_html=True)

    
    g1, g2 = st.columns([2, 1])

    with g1:
        st.markdown('<div class="card"><div class="card-title">Relação entre páginas e avaliação</div>', unsafe_allow_html=True)

        fig = px.scatter(
            df,
            x="paginas",
            y="nota",
            hover_data=["titulo", "autor"],
        )

        
        fig.update_traces(
            mode="markers",
            marker=dict(
                size=df["nota"] * 3,
                color=ROXO,
                line=dict(width=1, color=ROXO_CLARO),
                opacity=0.85
            ),
            hovertemplate="<b>%{customdata[0]}</b><br>%{customdata[1]}<extra></extra>",
            customdata=df[["titulo", "autor"]]
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            hovermode="closest"
        )

        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with g2:
        st.markdown('<div class="card"><div class="card-title">Distribuição de gêneros</div>', unsafe_allow_html=True)

        genero_count = df['genero'].value_counts().reset_index()
        genero_count.columns = ['genero', 'qtd']

        fig2 = px.pie(
            genero_count,
            names='genero',
            values='qtd',
            hole=0.6,
            color_discrete_sequence=[ROXO, ROXO_CLARO, ROXO_ESCURO]
        )

        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)")

        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    g3, g4 = st.columns(2)

    with g3:
        st.markdown('<div class="card"><div class="card-title">Tendência de avaliação por páginas</div>', unsafe_allow_html=True)

        fig3 = px.line(
            df.sort_values("paginas"),
            x="paginas",
            y="nota",
            color_discrete_sequence=[ROXO]
        )

        fig3.update_traces(line=dict(width=3))

        fig3.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")

        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with g4:
        st.markdown('<div class="card"><div class="card-title">Distribuição das notas por gênero</div>', unsafe_allow_html=True)

        fig4 = px.box(
            df,
            x="genero",
            y="nota",
            color_discrete_sequence=[ROXO]
        )

        fig4.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)")

        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-title">Base de dados filtrada</div>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)