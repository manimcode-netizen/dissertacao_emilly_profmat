"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D37 – Associar informações em listas/tabelas
            simples aos gráficos que as representam e vice-versa
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Uso       : Dissertação de Mestrado Profissional em Matemática
Fundamento: Phillips, Norris e Macnab (2010) – princípios de
            visualização matemática eficaz para aprendizagem
=======================================================================

CENAS (renderizar individualmente ou em sequência):
  1. Abertura              – Apresentação do descritor D37
  2. CenaConceito          – O que são gráficos e tabelas?
  3. CenaBarras            – Tabela → Gráfico de barras
  4. CenaLinhas            – Lista → Gráfico de linhas
  5. CenaPizza             – Tabela → Gráfico de setores (pizza)
  6. CenaViceVersa         – Gráfico → Leitura e interpretação da tabela
  7. Encerramento          – Síntese e estratégias
  8. LogoEmillyMayre       – Identidade visual da professora

RENDERIZAÇÃO:
  # Teste rápido (480p)
  manim -pql d37_graficos_tabelas.py Abertura

  # Alta qualidade para dissertação (1080p)
  manim -pqh d37_graficos_tabelas.py Abertura

  # Renderizar todas as cenas em sequência (PowerShell):
  foreach ($c in @("Abertura","CenaConceito","CenaBarras","CenaLinhas",
    "CenaPizza","CenaViceVersa","Encerramento","LogoEmillyMayre")) {
      manim -pqh d37_graficos_tabelas.py $c }
=======================================================================
"""

from manim import *
import numpy as np

# =======================================================================
# PALETA SEMÂNTICA GLOBAL (uso consistente em todas as cenas)
# =======================================================================
# COR_TITULO   → YELLOW   : títulos e cabeçalhos
# COR_TABELA   → BLUE_D   : tabelas, listas e dados
# COR_GRAFICO  → GREEN_B  : elementos dos gráficos (barras, linhas)
# COR_DESTAQUE → ORANGE   : valores em evidência e anotações
# COR_TEXTO    → WHITE    : textos explicativos gerais


# =======================================================================
# CENA 1 – ABERTURA
# Objetivo pedagógico: situar o aluno no contexto avaliativo e temático
# =======================================================================
class Abertura(Scene):
    """
    Conceito : Contextualização do Descritor D37 – SAEB
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Apresentar o tema, o contexto avaliativo e a estrutura
               da animação ao aluno.
    """

    def construct(self):
        # --- Faixa superior de identificação institucional ---
        faixa = Rectangle(
            width=14, height=1.1,
            fill_color=BLUE_E, fill_opacity=1,
            stroke_width=0
        ).to_edge(UP, buff=0)

        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())

        self.add(faixa, inst)

        # --- Título central ---
        titulo_d36 = Text(
            "Descritor D37",
            color=YELLOW, font_size=52, weight=BOLD
        ).move_to(UP * 2.0)

        subtitulo = Text(
            "Associar informações de listas e tabelas\naos gráficos que as representam e vice-versa",
            color=WHITE, font_size=28, line_spacing=1.3
        ).next_to(titulo_d36, DOWN, buff=0.45)

        self.play(Write(titulo_d36), run_time=1.8)
        self.wait(0.4)
        self.play(FadeIn(subtitulo, shift=UP * 0.2), run_time=1.4)
        self.wait(1.2)

        # --- Linha separadora ---
        linha = Line(LEFT * 5, RIGHT * 5, color=YELLOW, stroke_width=1.5)
        linha.next_to(subtitulo, DOWN, buff=0.5)
        self.play(Create(linha), run_time=1.0)

        # --- Índice de cenas ---
        topicos = VGroup(
            Text("1. O que são gráficos e tabelas?",      color=WHITE, font_size=24),
            Text("2. Tabela → Gráfico de Barras",          color=WHITE, font_size=24),
            Text("3. Lista → Gráfico de Linhas",            color=WHITE, font_size=24),
            Text("4. Tabela → Gráfico de Setores",          color=WHITE, font_size=24),
            Text("5. Do Gráfico à Tabela (vice-versa)",     color=WHITE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        topicos.next_to(linha, DOWN, buff=0.15)
        topicos.shift(LEFT * 0.3)

        # Marcadores coloridos à esquerda de cada tópico
        dots_group = VGroup()
        for t in topicos:
            dot = Dot(color=ORANGE, radius=0.07).next_to(t, LEFT, buff=0.18)
            dots_group.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.65)

        self.wait(2.5)
        self.play(FadeOut(VGroup(titulo_d36, subtitulo, linha, topicos, dots_group)), run_time=1.2)


# =======================================================================
# CENA 2 – CONCEITO
# Objetivo pedagógico: diferenciar listas, tabelas e gráficos como
#                      formas de representar a mesma informação
# =======================================================================
class CenaConceito(Scene):
    """
    Conceito : O que são gráficos, listas e tabelas?
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Mostrar que lista, tabela e gráfico são representações
               equivalentes de um mesmo conjunto de dados.
    """

    def construct(self):
        # --- Cabeçalho fixo ---
        cab = Text("Diferentes formas de representar dados",
                   color=YELLOW, font_size=32, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.8, RIGHT * 5.8, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- ETAPA 1: Situação-problema ---
        contexto = Text(
            "Quantos livros cada aluno leu no mês?",
            color=WHITE, font_size=28
        ).next_to(linha_cab, DOWN, buff=0.5)
        self.play(FadeIn(contexto, shift=UP * 0.15), run_time=1.2)
        self.wait(1.5)

        # --- ETAPA 2: LISTA ---
        lista_titulo = Text("LISTA", color=BLUE_B, font_size=26, weight=BOLD)
        lista_items = VGroup(
            Text("• Ana: 4 livros",   color=WHITE, font_size=22),
            Text("• Bruno: 7 livros", color=WHITE, font_size=22),
            Text("• Carla: 5 livros", color=WHITE, font_size=22),
            Text("• Diego: 3 livros", color=WHITE, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        lista_grupo = VGroup(lista_titulo, lista_items).arrange(DOWN, buff=0.2)
        lista_grupo.move_to(LEFT * 3.8 + DOWN * 0.3)

        borda_lista = SurroundingRectangle(
            lista_grupo, color=BLUE_B, buff=0.25, corner_radius=0.1
        )

        self.play(FadeOut(contexto), run_time=0.6)
        self.play(Write(lista_titulo), run_time=0.8)
        for item in lista_items:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.5)
        self.play(Create(borda_lista), run_time=0.7)
        self.wait(1.0)

        # --- Seta de transição: Lista → Tabela ---
        # Seta entre borda_lista e tabela, com espaço suficiente
        seta1 = Arrow(
            LEFT * 1.2 + DOWN * 0.3,
            LEFT * 0.1 + DOWN * 0.3,
            color=ORANGE, buff=0
        )
        label_seta1 = Text("organiza", color=ORANGE, font_size=18)
        label_seta1.next_to(seta1, UP, buff=0.1)
        self.play(GrowArrow(seta1), FadeIn(label_seta1), run_time=0.9)

        # --- ETAPA 3: TABELA --- posicionada mais à direita para não sobrepor seta
        tab_titulo = Text("TABELA", color=GREEN_B, font_size=26, weight=BOLD)

        linhas_tab = VGroup()
        dados = [("Aluno", "Livros"), ("Ana", "4"),
                 ("Bruno", "7"), ("Carla", "5"), ("Diego", "3")]
        cores_linha = [GREEN_B, WHITE, WHITE, WHITE, WHITE]

        for i, (aluno, qtd) in enumerate(dados):
            t_aluno = Text(aluno, color=cores_linha[i], font_size=20)
            t_qtd   = Text(qtd,   color=cores_linha[i], font_size=20)
            linha_r = VGroup(t_aluno, t_qtd).arrange(RIGHT, buff=1.2)
            linhas_tab.add(linha_r)

        linhas_tab.arrange(DOWN, buff=0.22)

        # Alinha todas as células pelo X fixo do cabeçalho (linha 0)
        x_col1 = linhas_tab[0][0].get_center()[0]
        x_col2 = linhas_tab[0][1].get_center()[0]
        for linha_r in linhas_tab[1:]:
            linha_r[0].set_x(x_col1)
            linha_r[1].set_x(x_col2)

        tabela_grupo = VGroup(tab_titulo, linhas_tab)
        tabela_grupo.arrange(DOWN, buff=0.18)
        tabela_grupo.move_to(RIGHT * 2.8 + DOWN * 0.3)

        borda_tab = SurroundingRectangle(
            tabela_grupo, color=GREEN_B, buff=0.25, corner_radius=0.1
        )

        self.play(Write(tab_titulo), run_time=0.8)
        for linha_r in linhas_tab:
            self.play(FadeIn(linha_r, shift=RIGHT * 0.1), run_time=0.45)
        self.play(Create(borda_tab), run_time=0.7)
        self.wait(1.2)

        # --- Mensagem de síntese ---
        sintese = Text(
            "Lista e tabela guardam os mesmos dados —\n"
            "apenas organizados de forma diferente!",
            color=ORANGE, font_size=24, line_spacing=1.3
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(sintese), run_time=1.1)
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(lista_grupo, borda_lista, seta1, label_seta1,
                           tabela_grupo, borda_tab, sintese, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 3 – TABELA → GRÁFICO DE BARRAS
# Objetivo pedagógico: construir visualmente um gráfico de barras a
#                      partir de uma tabela de dados
# =======================================================================
class CenaBarras(Scene):
    """
    Conceito : Construção do gráfico de barras a partir de uma tabela
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Associar cada linha da tabela a uma barra do gráfico,
               percebendo a correspondência direta entre os valores.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Tabela  →  Gráfico de Barras",
                   color=YELLOW, font_size=34, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.8, RIGHT * 5.8, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.4)

        # --- Dados da situação ---
        dados = {
            "Ana":   4,
            "Bruno": 7,
            "Carla": 5,
            "Diego": 3,
        }
        nomes  = list(dados.keys())
        valores = list(dados.values())
        cores_barras = [BLUE_B, GREEN_B, ORANGE, RED_B]

        # --- ETAPA 1: Tabela à esquerda ---
        tab_titulo = Text("Livros lidos por aluno", color=WHITE, font_size=20, weight=BOLD)

        linhas_tab = VGroup()
        cab_row = VGroup(
            Text("Aluno",  color=YELLOW, font_size=19, weight=BOLD),
            Text("Livros", color=YELLOW, font_size=19, weight=BOLD)
        ).arrange(RIGHT, buff=1.4)
        linhas_tab.add(cab_row)

        for i, (nome, val) in enumerate(dados.items()):
            t_nome = Text(nome,     color=cores_barras[i], font_size=19)
            t_val  = Text(str(val), color=cores_barras[i], font_size=19)
            row = VGroup(t_nome, t_val).arrange(RIGHT, buff=1.4)
            linhas_tab.add(row)

        linhas_tab.arrange(DOWN, buff=0.22)
        # Alinha todas as células pelo X do cabeçalho
        x_col1 = cab_row[0].get_center()[0]
        x_col2 = cab_row[1].get_center()[0]
        for row in linhas_tab[1:]:
            row[0].set_x(x_col1)
            row[1].set_x(x_col2)

        tabela_grupo = VGroup(tab_titulo, linhas_tab)
        tabela_grupo.arrange(DOWN, buff=0.2)
        tabela_grupo.move_to(LEFT * 4.2 + DOWN * 0.3)
        borda_tab = SurroundingRectangle(
            tabela_grupo, color=BLUE_D, buff=0.25, corner_radius=0.1
        )

        self.play(Write(tab_titulo), run_time=0.9)
        self.play(Create(borda_tab), run_time=0.5)
        for row in linhas_tab:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.45)
        self.wait(1.0)

        # --- Seta central ---
        seta = Arrow(
            LEFT * 1.8 + DOWN * 0.3,
            LEFT * 0.4 + DOWN * 0.3,
            color=ORANGE, buff=0, stroke_width=3
        )
        label_seta = Text("representa", color=ORANGE, font_size=20)
        label_seta.next_to(seta, UP, buff=0.1)
        self.play(GrowArrow(seta), FadeIn(label_seta), run_time=1.0)
        self.wait(0.5)

        # --- ETAPA 2: Gráfico de barras à direita ---
        # Eixos
        orig = np.array([0.5, -2.5, 0])
        eixo_x = Arrow(orig, orig + RIGHT * 4.2, color=WHITE, buff=0, stroke_width=2)
        eixo_y = Arrow(orig, orig + UP * 3.8,    color=WHITE, buff=0, stroke_width=2)

        # Rótulos eixo Y
        escala = VGroup()
        for v in [2, 4, 6, 8]:
            tick = Line(orig + UP * (v * 0.44) + LEFT * 0.1,
                        orig + UP * (v * 0.44) + RIGHT * 0.1,
                        color=WHITE, stroke_width=1.5)
            lbl  = Text(str(v), color=WHITE, font_size=16)
            lbl.next_to(tick, LEFT, buff=0.1)
            escala.add(tick, lbl)

        self.play(Create(eixo_x), Create(eixo_y), run_time=1.0)
        self.play(FadeIn(escala), run_time=0.8)

        # Barras — crescem de baixo para cima (uma por vez)
        barras_grupo = VGroup()
        labels_barras = VGroup()
        larg = 0.55
        gap  = 0.88

        for i, (nome, val) in enumerate(dados.items()):
            altura = val * 0.44
            x_pos  = orig[0] + gap * (i + 0.7)
            barra  = Rectangle(
                width=larg, height=altura,
                fill_color=cores_barras[i], fill_opacity=0.85,
                stroke_color=WHITE, stroke_width=1.2
            )
            barra.move_to(
                np.array([x_pos, orig[1] + altura / 2, 0])
            )

            # Valor no topo da barra
            lbl_val = Text(str(val), color=cores_barras[i],
                           font_size=18, weight=BOLD)
            lbl_val.next_to(barra, UP, buff=0.08)

            # Nome abaixo do eixo
            lbl_nome = Text(nome, color=WHITE, font_size=16)
            lbl_nome.move_to(np.array([x_pos, orig[1] - 0.28, 0]))

            barras_grupo.add(barra)
            labels_barras.add(lbl_val, lbl_nome)

            # Animação: destaque na linha da tabela → cresce a barra
            self.play(
                linhas_tab[i + 1].animate.set_color(cores_barras[i]),
                run_time=0.4
            )
            self.play(
                GrowFromEdge(barra, DOWN),
                FadeIn(lbl_val), FadeIn(lbl_nome),
                run_time=1.1
            )
            self.wait(0.3)

        # Título do gráfico
        titulo_graf = Text("Livros lidos por aluno",
                           color=WHITE, font_size=20, weight=BOLD)
        titulo_graf.move_to(np.array([orig[0] + 2.1, orig[1] + 4.1, 0]))
        self.play(FadeIn(titulo_graf), run_time=0.8)
        self.wait(2.0)

        # --- Mensagem pedagógica ---
        msg = Text(
            "Cada linha da tabela corresponde a uma barra do gráfico!",
            color=ORANGE, font_size=22
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(msg), run_time=1.0)
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(tabela_grupo, borda_tab, seta, label_seta,
                           eixo_x, eixo_y, escala, barras_grupo,
                           labels_barras, titulo_graf, msg, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 4 – LISTA → GRÁFICO DE LINHAS
# Objetivo pedagógico: associar uma lista de dados temporais ao gráfico
#                      de linhas que representa sua variação
# =======================================================================
class CenaLinhas(Scene):
    """
    Conceito : Construção do gráfico de linhas a partir de uma lista
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Mostrar como dados de variação ao longo do tempo
               se traduzem em um gráfico de linhas.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Lista  →  Gráfico de Linhas",
                   color=YELLOW, font_size=34, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.8, RIGHT * 5.8, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.4)

        # --- Dados: temperatura média mensal (Jan a Jun) ---
        meses  = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
        temps  = [32,    30,    28,    25,    22,    20   ]
        COR_LN = GREEN_B

        # --- ETAPA 1: Lista de dados ---
        lista_titulo = Text("Temperatura média (°C)",
                            color=WHITE, font_size=22, weight=BOLD)
        items_lista = VGroup()
        for m, t in zip(meses, temps):
            item = Text(f"• {m}: {t} °C", color=WHITE, font_size=20)
            items_lista.add(item)
        items_lista.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        lista_grupo = VGroup(lista_titulo, items_lista)
        lista_grupo.arrange(DOWN, buff=0.2)
        lista_grupo.move_to(LEFT * 4.5 + DOWN * 0.2)
        borda_lista = SurroundingRectangle(
            lista_grupo, color=BLUE_D, buff=0.22, corner_radius=0.1
        )

        self.play(Write(lista_titulo), Create(borda_lista), run_time=0.9)
        for it in items_lista:
            self.play(FadeIn(it, shift=RIGHT * 0.1), run_time=0.4)
        self.wait(0.8)

        # --- Seta ---
        seta = Arrow(LEFT * 2.0 + DOWN * 0.2, LEFT * 0.5 + DOWN * 0.2,
                     color=ORANGE, buff=0, stroke_width=3)
        label_seta = Text("representa", color=ORANGE, font_size=20)
        label_seta.next_to(seta, UP, buff=0.1)
        self.play(GrowArrow(seta), FadeIn(label_seta), run_time=0.9)

        # --- ETAPA 2: Gráfico de linhas ---
        # Origem do gráfico: lado direito da tela, bem contida verticalmente
        orig     = np.array([0.2, -1.8, 0])
        escala_x = 0.72   # espaço horizontal por mês
        escala_y = 0.16   # espaço vertical por grau Celsius

        # Valor mínimo do eixo Y (base do gráfico = 18 °C)
        y_min = 18

        eixo_x = Arrow(orig, orig + RIGHT * 4.8,
                       color=WHITE, buff=0, stroke_width=2)
        eixo_y = Arrow(orig, orig + UP * 3.2,
                       color=WHITE, buff=0, stroke_width=2)

        # Rótulos eixo X (meses) — abaixo do eixo
        labels_x = VGroup()
        for i, m in enumerate(meses):
            lbl = Text(m, color=WHITE, font_size=16)
            lbl.move_to(orig + RIGHT * (i + 0.7) * escala_x + DOWN * 0.32)
            labels_x.add(lbl)

        # Rótulos eixo Y — marcas de referência a cada 5 °C
        labels_y = VGroup()
        for v in [20, 25, 30, 35]:
            y_pos = (v - y_min) * escala_y
            tick = Line(
                orig + UP * y_pos + LEFT * 0.12,
                orig + UP * y_pos + RIGHT * 0.12,
                color=WHITE, stroke_width=1.2
            )
            lbl = Text(f"{v}°", color=WHITE, font_size=15)
            lbl.next_to(tick, LEFT, buff=0.12)
            labels_y.add(tick, lbl)

        self.play(Create(eixo_x), Create(eixo_y), run_time=1.0)
        self.play(FadeIn(labels_x), FadeIn(labels_y), run_time=0.7)

        # Calcula coordenadas dos pontos — todas dentro dos eixos
        pontos_coords = []
        for i, t in enumerate(temps):
            x = orig[0] + (i + 0.7) * escala_x
            y = orig[1] + (t - y_min) * escala_y
            pontos_coords.append(np.array([x, y, 0]))

        # Anima ponto a ponto, iluminando item correspondente da lista
        dots      = VGroup()
        segmentos = VGroup()
        for i, (coord, item) in enumerate(zip(pontos_coords, items_lista)):
            dot = Dot(coord, color=ORANGE, radius=0.1)
            dots.add(dot)
            self.play(
                item.animate.set_color(ORANGE),
                GrowFromCenter(dot),
                run_time=0.6
            )
            if i > 0:
                seg = Line(pontos_coords[i - 1], coord,
                           color=COR_LN, stroke_width=2.5)
                segmentos.add(seg)
                self.play(Create(seg), run_time=0.65)

        # Rótulos dos valores acima de cada ponto
        vals_graf = VGroup()
        for coord, t in zip(pontos_coords, temps):
            v_lbl = Text(f"{t}°", color=ORANGE, font_size=15)
            v_lbl.next_to(coord, UP, buff=0.12)
            vals_graf.add(v_lbl)
        self.play(FadeIn(vals_graf), run_time=0.7)

        # Título do gráfico — posicionado acima dos eixos, dentro da tela
        titulo_graf = Text("Temperatura média (°C) — Jan a Jun",
                           color=WHITE, font_size=18, weight=BOLD)
        titulo_graf.next_to(eixo_y, UP, buff=0.15)
        titulo_graf.shift(RIGHT * 1.8)
        self.play(FadeIn(titulo_graf), run_time=0.8)

        self.wait(1.5)

        # --- Mensagem pedagógica ---
        msg = Text(
            "Cada item da lista vira um ponto no gráfico de linhas!",
            color=ORANGE, font_size=22
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(msg), run_time=1.0)
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(lista_grupo, borda_lista, seta, label_seta,
                           eixo_x, eixo_y, labels_x, labels_y,
                           dots, segmentos, vals_graf,
                           titulo_graf, msg, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 5 – TABELA → GRÁFICO DE SETORES (PIZZA)
# Objetivo pedagógico: associar proporções de uma tabela ao gráfico
#                      de setores que as representa
# =======================================================================
class CenaPizza(Scene):
    """
    Conceito : Construção do gráfico de setores a partir de uma tabela
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Associar percentuais de uma tabela a setores circulares,
               percebendo que o tamanho de cada setor é proporcional
               ao valor correspondente.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Tabela  →  Gráfico de Setores",
                   color=YELLOW, font_size=34, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.8, RIGHT * 5.8, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.4)

        # --- Dados ---
        categorias    = ["A pé", "Bicicleta", "Ônibus", "Carro"]
        percentuais   = [40,      15,           30,       15    ]
        cores_setores = [BLUE_B, GREEN_B, ORANGE, RED_B]

        # =============================================================
        # ETAPA 1: TABELA — colunas alinhadas por posição X fixa
        # =============================================================
        tab_titulo = Text("Transporte para a escola",
                          color=WHITE, font_size=20, weight=BOLD)

        # =============================================================
        # TABELA: colunas alinhadas por X absoluto após posicionamento
        # "Meio" alinhado com os nomes dos transportes; "%" alinhado entre si
        # =============================================================
        cab_meio = Text("Meio",       color=YELLOW, font_size=18, weight=BOLD)
        cab_pct  = Text("Percentual", color=YELLOW, font_size=18, weight=BOLD)
        cab_row  = VGroup(cab_meio, cab_pct).arrange(RIGHT, buff=1.4)

        rows_dados = []
        for cat, pct, cor in zip(categorias, percentuais, cores_setores):
            t_cat = Text(cat,       color=cor, font_size=18)
            t_pct = Text(f"{pct}%", color=cor, font_size=18)
            row   = VGroup(t_cat, t_pct).arrange(RIGHT, buff=1.4)
            rows_dados.append(row)

        todas_linhas = VGroup(cab_row, *rows_dados)
        todas_linhas.arrange(DOWN, buff=0.26)

        # Alinha coluna esquerda (Meio/nomes) e coluna direita (%) pelo X do cabeçalho
        x_col1 = cab_meio.get_center()[0]
        x_col2 = cab_pct.get_center()[0]
        for row in rows_dados:
            row[0].set_x(x_col1)   # nome do transporte alinhado com "Meio"
            row[1].set_x(x_col2)   # percentual alinhado com "Percentual"

        tabela_grupo = VGroup(tab_titulo, todas_linhas)
        tabela_grupo.arrange(DOWN, buff=0.22)
        tabela_grupo.move_to(LEFT * 4.1 + DOWN * 0.2)
        borda_tab = SurroundingRectangle(
            tabela_grupo, color=BLUE_D, buff=0.28, corner_radius=0.1
        )

        self.play(Write(tab_titulo), Create(borda_tab), run_time=0.9)
        for ln in todas_linhas:
            self.play(FadeIn(ln, shift=RIGHT * 0.1), run_time=0.42)
        self.wait(0.8)

        # --- Seta — posicionada no espaço entre tabela e gráfico ---
        seta = Arrow(np.array([-1.5, -0.2, 0]), np.array([0.8, -0.2, 0]),
                     color=ORANGE, buff=0, stroke_width=3)
        label_seta = Text("representa", color=ORANGE, font_size=20)
        label_seta.next_to(seta, UP, buff=0.12)
        self.play(GrowArrow(seta), FadeIn(label_seta), run_time=0.9)

        # =============================================================
        # ETAPA 2: GRÁFICO DE SETORES — usa Polygon (sem bugs de Sector)
        # Centro mais baixo para não sobrepor título do gráfico
        # =============================================================
        centro = np.array([3.2, -0.6, 0])
        raio   = 1.65

        def make_setor(cx, cy, r, ang_ini, ang_fim, cor, op=0.90, n=60):
            pts = [np.array([cx, cy, 0])]
            for k in range(n + 1):
                a = ang_ini + (ang_fim - ang_ini) * k / n
                pts.append(np.array([cx + r*np.cos(a), cy + r*np.sin(a), 0]))
            return Polygon(*pts, fill_color=cor, fill_opacity=op,
                           stroke_color=WHITE, stroke_width=1.8)

        titulo_graf = Text("Transporte para a escola",
                           color=WHITE, font_size=19, weight=BOLD)
        titulo_graf.move_to(centro + UP * (raio + 0.35))

        circulo_base = Circle(
            radius=raio, fill_color=GREY_D, fill_opacity=0.4,
            stroke_color=WHITE, stroke_width=2
        ).move_to(centro)
        self.play(GrowFromCenter(circulo_base), FadeIn(titulo_graf), run_time=1.1)
        self.wait(0.5)

        # Pré-calcula ângulos (sentido horário a partir do topo)
        setores_lista = []
        labels_pct    = VGroup()
        legendas_grp  = VGroup()
        ang_atual = PI / 2

        for cat, pct, cor in zip(categorias, percentuais, cores_setores):
            ang_setor = (pct / 100) * TAU
            ang_fim   = ang_atual - ang_setor

            setor = make_setor(centro[0], centro[1], raio, ang_fim, ang_atual, cor)
            setor.set_opacity(0)
            setores_lista.append(setor)

            ang_meio = (ang_atual + ang_fim) / 2
            lx = centro[0] + raio * 0.62 * np.cos(ang_meio)
            ly = centro[1] + raio * 0.62 * np.sin(ang_meio)
            lbl = Text(f"{pct}%", color=WHITE, font_size=17, weight=BOLD)
            lbl.move_to(np.array([lx, ly, 0]))
            lbl.set_opacity(0)
            labels_pct.add(lbl)

            quad = Square(side_length=0.22, fill_color=cor,
                          fill_opacity=1, stroke_width=0)
            txt  = Text(cat, color=WHITE, font_size=16)
            legendas_grp.add(VGroup(quad, txt).arrange(RIGHT, buff=0.12))

            ang_atual = ang_fim

        setores_grp = VGroup(*setores_lista)
        self.add(setores_grp, labels_pct)

        # Anima setor a setor sincronizado com a tabela
        for i in range(len(categorias)):
            self.play(
                todas_linhas[i + 1].animate.set_color(cores_setores[i]),
                run_time=0.35
            )
            self.play(
                setores_lista[i].animate.set_opacity(1),
                labels_pct[i].animate.set_opacity(1),
                run_time=0.9
            )
            self.wait(0.2)

        # Legendas à direita do círculo
        legendas_grp.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        legendas_grp.next_to(circulo_base, RIGHT, buff=0.45)
        self.play(FadeIn(legendas_grp), run_time=0.9)
        self.wait(1.2)

        # --- Mensagem pedagógica ---
        msg = Text(
            "O tamanho do setor é proporcional ao percentual!",
            color=ORANGE, font_size=22
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(msg), run_time=1.0)
        self.wait(2.5)

        # FadeOut completo
        self.play(
            FadeOut(VGroup(tabela_grupo, borda_tab, seta, label_seta,
                           circulo_base, setores_grp, labels_pct,
                           legendas_grp, titulo_graf, msg, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 6 – GRÁFICO → TABELA (VICE-VERSA)
# Objetivo pedagógico: mostrar que a leitura do gráfico permite
#                      reconstruir a tabela original de dados
# =======================================================================
class CenaViceVersa(Scene):
    """
    Conceito : Leitura de gráfico para preenchimento de tabela
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : A partir de um gráfico de barras, identificar os valores
               e associá-los à tabela correspondente.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Do Gráfico à Tabela  (vice-versa)",
                   color=YELLOW, font_size=32, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.8, RIGHT * 5.8, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.4)

        # --- Situação-problema ---
        enunciado = Text(
            "Observe o gráfico abaixo e complete a tabela:",
            color=WHITE, font_size=24
        ).next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(enunciado), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(enunciado), run_time=0.6)

        # --- ETAPA 1: Gráfico de barras (dado) ---
        materias  = ["Port.", "Mat.", "Ciên.", "Hist."]
        notas     = [8,        6,      9,       7     ]
        cores_mat = [BLUE_B, GREEN_B, ORANGE, RED_B]

        orig  = np.array([-5.5, -2.6, 0])
        esc_y = 0.37
        larg  = 0.55
        gap   = 0.88

        eixo_x = Arrow(orig, orig + RIGHT * 4.5, color=WHITE, buff=0, stroke_width=2)
        eixo_y = Arrow(orig, orig + UP * 4.2,    color=WHITE, buff=0, stroke_width=2)

        esc_labels = VGroup()
        for v in [2, 4, 6, 8, 10]:
            tick = Line(orig + UP * v * esc_y + LEFT * 0.1,
                        orig + UP * v * esc_y + RIGHT * 0.1,
                        color=WHITE, stroke_width=1.2)
            lbl  = Text(str(v), color=WHITE, font_size=15)
            lbl.next_to(tick, LEFT, buff=0.08)
            esc_labels.add(tick, lbl)

        self.play(Create(eixo_x), Create(eixo_y), run_time=1.0)
        self.play(FadeIn(esc_labels), run_time=0.6)

        barras_grp    = VGroup()
        labels_bar_grp = VGroup()
        pontos_topo   = []

        for i, (mat, nota, cor) in enumerate(zip(materias, notas, cores_mat)):
            altura = nota * esc_y
            x_pos  = orig[0] + gap * (i + 0.7)
            barra  = Rectangle(
                width=larg, height=altura,
                fill_color=cor, fill_opacity=0.85,
                stroke_color=WHITE, stroke_width=1.2
            ).move_to(np.array([x_pos, orig[1] + altura / 2, 0]))

            lbl_mat = Text(mat,       color=WHITE,  font_size=15)
            lbl_val = Text(str(nota), color=cor,    font_size=16, weight=BOLD)
            lbl_mat.move_to(np.array([x_pos, orig[1] - 0.28, 0]))
            lbl_val.next_to(barra, UP, buff=0.07)

            barras_grp.add(barra)
            labels_bar_grp.add(lbl_mat, lbl_val)
            pontos_topo.append(np.array([x_pos, orig[1] + altura + 0.05, 0]))

            self.play(GrowFromEdge(barra, DOWN),
                      FadeIn(lbl_mat), FadeIn(lbl_val), run_time=0.8)

        titulo_graf = Text("Notas por disciplina",
                           color=WHITE, font_size=20, weight=BOLD)
        titulo_graf.move_to(orig + RIGHT * 2.0 + UP * 4.5)
        self.play(FadeIn(titulo_graf), run_time=0.7)
        self.wait(1.0)

        # --- Seta ---
        seta = Arrow(orig + RIGHT * 5.0 + UP * 1.0,
                     orig + RIGHT * 6.2 + UP * 1.0,
                     color=ORANGE, buff=0, stroke_width=3)
        label_seta = Text("lemos", color=ORANGE, font_size=20)
        label_seta.next_to(seta, UP, buff=0.1)
        self.play(GrowArrow(seta), FadeIn(label_seta), run_time=0.9)

        # --- ETAPA 2: Tabela reconstruída ---
        tab_titulo = Text("Notas por disciplina",
                          color=WHITE, font_size=20, weight=BOLD)
        linhas_tab = VGroup()
        cab_row = VGroup(
            Text("Disciplina", color=YELLOW, font_size=18, weight=BOLD),
            Text("Nota",       color=YELLOW, font_size=18, weight=BOLD)
        ).arrange(RIGHT, buff=1.4)
        linhas_tab.add(cab_row)

        for i, (mat, nota, cor) in enumerate(zip(materias, notas, cores_mat)):
            row = VGroup(
                Text(mat,       color=cor, font_size=18),
                Text(str(nota), color=cor, font_size=18)
            ).arrange(RIGHT, buff=1.4)
            linhas_tab.add(row)

        linhas_tab.arrange(DOWN, buff=0.24)
        # Alinha colunas pelo X do cabeçalho
        x_col1 = cab_row[0].get_center()[0]
        x_col2 = cab_row[1].get_center()[0]
        for row in linhas_tab[1:]:
            row[0].set_x(x_col1)
            row[1].set_x(x_col2)
        tabela_grupo = VGroup(tab_titulo, linhas_tab)
        tabela_grupo.arrange(DOWN, buff=0.2)
        tabela_grupo.move_to(np.array([4.5, -0.3, 0]))
        borda_tab = SurroundingRectangle(
            tabela_grupo, color=GREEN_B, buff=0.22, corner_radius=0.1
        )

        self.play(Write(tab_titulo), Create(borda_tab), run_time=0.9)

        # Anima: seta aponta para barra → linha da tabela aparece
        for i, (row, ptopo, cor) in enumerate(
                zip(linhas_tab[1:], pontos_topo, cores_mat)):

            seta_leitura = CurvedArrow(
                ptopo,
                row.get_left() + LEFT * 0.1,
                color=cor, angle=-0.5, stroke_width=1.8
            )
            self.play(Create(seta_leitura), run_time=0.5)
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.6)
            self.play(FadeOut(seta_leitura), run_time=0.3)

        self.wait(1.5)

        # --- Mensagem pedagógica ---
        msg = Text(
            "Ler o gráfico com atenção nos permite reconstruir a tabela!",
            color=ORANGE, font_size=21
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(msg), run_time=1.0)
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(eixo_x, eixo_y, esc_labels, barras_grp,
                           labels_bar_grp, titulo_graf, seta, label_seta,
                           tabela_grupo, borda_tab, msg, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 7 – ENCERRAMENTO
# Objetivo pedagógico: consolidar as estratégias para o D37
# =======================================================================
class Encerramento(Scene):
    """
    Conceito : Síntese do Descritor D37
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Consolidar as correspondências entre listas, tabelas e
               gráficos, e apresentar estratégias de resolução.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Síntese — Descritor D37",
                   color=YELLOW, font_size=36, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.5, RIGHT * 5.5, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- Mapa de correspondências ---
        mapa_titulo = Text(
            "Lista / Tabela  ↔  Gráfico",
            color=GREEN_B, font_size=34, weight=BOLD
        ).next_to(linha_cab, DOWN, buff=0.4)
        box_mapa = SurroundingRectangle(
            mapa_titulo, color=GREEN_B, buff=0.18, corner_radius=0.1
        )
        self.play(Write(mapa_titulo), Create(box_mapa), run_time=1.2)
        self.wait(0.8)

        # --- Correspondências visuais ---
        corr_titulo = Text("Correspondências-chave:",
                           color=WHITE, font_size=24)
        corr_titulo.next_to(box_mapa, DOWN, buff=0.45)
        self.play(FadeIn(corr_titulo), run_time=0.9)

        correspondencias = VGroup(
            Text("Cada linha da tabela  →  uma barra (ou ponto) no gráfico",
                 color=BLUE_B, font_size=21),
            Text("Percentual da tabela  →  tamanho do setor no gráfico de pizza",
                 color=GREEN_B, font_size=21),
            Text("Valor mais alto na tabela  →  barra mais alta no gráfico",
                 color=ORANGE, font_size=21),
            Text("Lendo as alturas das barras  →  reconstruímos a tabela",
                 color=RED_B,  font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        correspondencias.next_to(corr_titulo, DOWN, buff=0.28)

        dots_corr = VGroup()
        for i, c in enumerate(correspondencias):
            dot = Dot(color=c.color, radius=0.07).next_to(c, LEFT, buff=0.12)
            dots_corr.add(dot)
            self.play(FadeIn(dot), FadeIn(c, shift=RIGHT * 0.1), run_time=0.7)

        self.wait(1.2)

        # --- Estratégias ---
        strat_titulo = Text("Estratégias para o D37:",
                            color=WHITE, font_size=22)
        strat_titulo.next_to(correspondencias, DOWN, buff=0.4)
        self.play(FadeIn(strat_titulo), run_time=0.8)

        estrategias = VGroup(
            Text("1. Identifique o tipo de gráfico e seus eixos",
                 color=WHITE, font_size=20),
            Text("2. Relacione cada categoria da tabela ao elemento visual",
                 color=ORANGE, font_size=20),
            Text("3. Verifique se os valores são absolutos ou percentuais",
                 color=ORANGE, font_size=20),
            Text("4. Confira a escala antes de concluir o valor",
                 color=WHITE, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        estrategias.next_to(strat_titulo, DOWN, buff=0.2)

        dots_strat = VGroup()
        for i, e in enumerate(estrategias):
            dot = Dot(
                color=GREEN_B if i % 2 == 0 else ORANGE, radius=0.07
            ).next_to(e, LEFT, buff=0.12)
            dots_strat.add(dot)
            self.play(FadeIn(dot), FadeIn(e, shift=RIGHT * 0.1), run_time=0.65)

        self.wait(2.0)

        # --- Fade final — inclui todos os dots explicitamente ---
        self.play(
            FadeOut(VGroup(cab, linha_cab, mapa_titulo, box_mapa,
                           corr_titulo, correspondencias, dots_corr,
                           strat_titulo, estrategias, dots_strat)),
            run_time=1.5
        )


# =======================================================================
# LOGO – Identidade visual da Prof.ª Emilly Mayre
# =======================================================================
class LogoEmillyMayre(Scene):
    """Objetivo: Exibir a identidade visual da professora."""

    def construct(self):
        ESCURO_L = "#1a1a2e"
        DOURADO  = "#C8A84B"
        CINZA_L  = "#888899"

        bg = Rectangle(width=16, height=9,
                       fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.add(bg)

        a = 1.9

        def inf_h(t):
            d = 1 + np.sin(t) ** 2
            return np.array([a * np.cos(t) / d,
                             a * np.sin(t) * np.cos(t) / d, 0])

        def inf_v(t):
            d = 1 + np.sin(t) ** 2
            return np.array([a * np.sin(t) * np.cos(t) / d,
                             a * np.cos(t) / d, 0])

        logo_h = ParametricFunction(
            inf_h, t_range=[0, TAU],
            color="#3a3a5c", stroke_width=2.5
        ).move_to(UP * 0.5)

        logo_v = ParametricFunction(
            inf_v, t_range=[0, TAU],
            color="#9999bb", stroke_width=2.5
        ).move_to(UP * 0.5)

        circ = Circle(
            radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
            color=ESCURO_L, stroke_width=0
        ).move_to(UP * 0.5)

        em = Text("EM", color=WHITE, font_size=22,
                  weight=BOLD).move_to(circ.get_center())

        nome = Text("Emilly Mayre", color=ESCURO_L,
                    font_size=28, weight=BOLD)
        nome.next_to(VGroup(logo_h, logo_v), DOWN, buff=0.55)

        linha = Line(LEFT * 1.6, RIGHT * 1.6,
                     color=DOURADO, stroke_width=3.5)
        linha.next_to(nome, DOWN, buff=0.16)

        cargo = Text("PROFESSORA DE MATEMÁTICA",
                     color=CINZA_L, font_size=14)
        cargo.next_to(linha, DOWN, buff=0.18)

        # Animação da logo
        self.play(Create(logo_h), run_time=2.0)
        self.wait(0.3)
        self.play(Create(logo_v), run_time=2.0)
        self.wait(0.3)
        self.play(GrowFromCenter(circ), run_time=0.7)
        self.play(Write(em), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(nome, shift=UP * 0.15), run_time=0.8)
        self.play(Create(linha), run_time=0.5)
        self.play(FadeIn(cargo), run_time=0.6)
        self.wait(0.4)

        simbolo = VGroup(logo_h, logo_v, circ, em)
        self.play(simbolo.animate.scale(1.06), run_time=0.4)
        self.play(simbolo.animate.scale(1 / 1.06), run_time=0.35)
        self.wait(3.5)
