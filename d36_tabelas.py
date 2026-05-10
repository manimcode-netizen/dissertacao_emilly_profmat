"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D36 – Resolver Problemas Envolvendo Informações
            Apresentadas em Tabelas e/ou Gráficos
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Uso       : Dissertação de Mestrado Profissional em Matemática
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT (coordenadas Manim: centro = 0,0  |  tela: x[-7,7] y[-4,4])
  Faixa SAEB  : y ∈ [3.0, 4.0]   → nunca sobrepor
  Título cena : y = 2.55
  Linha sep   : y = 2.1
  Conteúdo    : y ∈ [-2.7, 1.85]  → gráficos/tabelas aqui
  Cálculo     : y ≈ -2.85
  Resposta    : y = -3.4          → acima da barra do player
=======================================================================
RENDERIZAÇÃO:
  manim -pql d36_v3.py Abertura
  manim -pqh d36_v3.py Abertura

  foreach ($c in @("Abertura","CenaTabela","CenaGraficoBarras",
    "CenaGraficoLinhas","CenaProblema1","CenaProblema2",
    "Encerramento","LogoEmillyMayre")) {
      manim -pqh d36_v3.py $c }
=======================================================================
"""

from manim import *
import numpy as np

# -----------------------------------------------------------------------
# CONSTANTES DE LAYOUT
# -----------------------------------------------------------------------
Y_FAIXA_CY  =  3.50   # centro da faixa institucional
Y_TITULO    =  2.55   # centro do título da cena
Y_LINHA_SEP =  2.10   # linha separadora amarela
Y_GRAF_TOPO =  1.80   # topo máximo de qualquer gráfico/tabela
Y_CALCULO   = -2.55   # centro do bloco de cálculo
Y_RESPOSTA  = -3.40   # resposta final – acima da barra do player


def cabecalho(scene, texto_titulo):
    """Faixa SAEB + título + linha separadora. Retorna os 4 objetos."""
    faixa = Rectangle(
        width=14.4, height=1.05,
        fill_color=BLUE_E, fill_opacity=1, stroke_width=0
    ).move_to(np.array([0, Y_FAIXA_CY, 0]))

    inst = Text(
        "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
        color=WHITE, font_size=22
    ).move_to(faixa.get_center())

    cab = Text(texto_titulo, color=YELLOW, font_size=36, weight=BOLD)
    cab.move_to(np.array([0, Y_TITULO, 0]))

    linha_sep = Line(
        np.array([-6.2, Y_LINHA_SEP, 0]),
        np.array([ 6.2, Y_LINHA_SEP, 0]),
        color=YELLOW, stroke_width=1.2
    )

    scene.add(faixa, inst)
    scene.play(Write(cab), Create(linha_sep), run_time=1.1)
    scene.wait(0.3)
    return faixa, inst, cab, linha_sep


# =======================================================================
# CENA 1 – ABERTURA
# FIX: subtítulo menor + FadeOut antes dos tópicos para evitar sobreposição
# =======================================================================
class Abertura(Scene):
    def construct(self):
        faixa = Rectangle(
            width=14.4, height=1.05,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        # Título + subtítulo ficam na metade superior, depois saem
        titulo_d36 = Text("Descritor D36", color=YELLOW, font_size=52, weight=BOLD)
        titulo_d36.move_to(np.array([0, 1.4, 0]))

        subtitulo = Text(
            "Resolver problemas envolvendo informações\napresentadas em tabelas e/ou gráficos",
            color=WHITE, font_size=26, line_spacing=1.3
        ).next_to(titulo_d36, DOWN, buff=0.4)

        self.play(Write(titulo_d36), run_time=1.6)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)

        # FadeOut do título+subtítulo ANTES de mostrar os tópicos
        self.play(FadeOut(VGroup(titulo_d36, subtitulo)), run_time=0.9)
        self.wait(0.2)

        # Linha separadora + tópicos ocupam a tela inteira sem colisão
        linha = Line(
            np.array([-5.5, 1.5, 0]), np.array([5.5, 1.5, 0]),
            color=YELLOW, stroke_width=1.5
        )
        self.play(Create(linha), run_time=0.7)

        topicos = VGroup(
            Text("1. Como ler uma Tabela?",           color=WHITE, font_size=25),
            Text("2. Gráfico de Barras",              color=WHITE, font_size=25),
            Text("3. Gráfico de Linhas",              color=WHITE, font_size=25),
            Text("4. Problema: Comparação em Tabela", color=WHITE, font_size=25),
            Text("5. Problema: Gráfico de Setores",   color=WHITE, font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        topicos.next_to(linha, DOWN, buff=0.30)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        dots_group = VGroup()
        for t in topicos:
            dot = Dot(color=ORANGE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots_group.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.55)

        self.wait(2.5)
        self.play(FadeOut(VGroup(linha, topicos, dots_group)), run_time=1.0)


# =======================================================================
# CENA 2 – LEITURA DE TABELA
# =======================================================================
class CenaTabela(Scene):
    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Como ler uma Tabela?")

        intro = Text(
            "Uma tabela organiza dados em linhas e colunas,\n"
            "facilitando a comparação e leitura de informações.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.2, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(intro), run_time=0.7)

        # Título da tabela logo abaixo da linha sep
        titulo_tab = Text(
            "Venda de sorvetes por sabor – Julho",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.65, 0]))
        self.play(FadeIn(titulo_tab), run_time=0.7)

        headers = ["Sabor", "Quantidade vendida"]
        dados   = [["Chocolate","340"],["Morango","210"],
                   ["Creme","180"],["Limão","270"]]
        col_w   = [3.2, 3.6]
        row_h   = 0.58
        n_rows  = len(dados) + 1
        n_cols  = 2
        tab_topo = 1.22   # topo da primeira linha

        cells = VGroup()
        texts = VGroup()
        for r in range(n_rows):
            for c in range(n_cols):
                cx = -sum(col_w)/2 + sum(col_w[:c]) + col_w[c]/2
                cy = tab_topo - row_h/2 - r * row_h
                if r == 0:
                    fc, fo, tc = BLUE_E, 0.92, YELLOW
                else:
                    fc  = BLUE_D
                    fo  = 0.30 if r % 2 == 0 else 0.15
                    tc  = WHITE
                cell = Rectangle(
                    width=col_w[c], height=row_h,
                    fill_color=fc, fill_opacity=fo,
                    stroke_color=WHITE, stroke_width=1.5
                ).move_to(np.array([cx, cy, 0]))
                cells.add(cell)
                lbl = Text(
                    headers[c] if r == 0 else dados[r-1][c],
                    color=tc, font_size=22,
                    weight=BOLD if r == 0 else NORMAL
                ).move_to(np.array([cx, cy, 0]))
                texts.add(lbl)

        self.play(FadeIn(VGroup(*cells[:n_cols])),
                  Write(VGroup(*texts[:n_cols])), run_time=0.9)
        for r in range(1, n_rows):
            self.play(
                FadeIn(VGroup(*cells[r*n_cols:(r+1)*n_cols])),
                Write(VGroup(*texts[r*n_cols:(r+1)*n_cols])),
                run_time=0.55
            )
        self.wait(1.0)

        # Destaque: Chocolate (r=1,c=1) → idx = n_cols*1+1 = 3
        idx_dest = n_cols * 1 + 1
        destaque_box = SurroundingRectangle(
            texts[idx_dest], color=ORANGE, buff=0.1, corner_radius=0.06
        )
        destaque_lbl = Text(
            "Chocolate foi o mais vendido!",
            color=ORANGE, font_size=24
        ).move_to(np.array([0, -2.55, 0]))
        self.play(Create(destaque_box), run_time=0.6)
        self.play(FadeIn(destaque_lbl), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            cab, linha_sep, titulo_tab, cells, texts,
            destaque_box, destaque_lbl
        )), run_time=1.0)


# =======================================================================
# CENA 3 – GRÁFICO DE BARRAS
# =======================================================================
class CenaGraficoBarras(Scene):
    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Gráfico de Barras")

        defn = Text(
            "O gráfico de barras usa retângulos para\n"
            "representar e comparar quantidades.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.0, 0]))
        self.play(FadeIn(defn), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(defn), run_time=0.7)

        titulo_graf = Text(
            "Alunos por modalidade esportiva – Escola ABC",
            color=WHITE, font_size=22
        ).move_to(np.array([0.8, 1.72, 0]))
        self.play(FadeIn(titulo_graf), run_time=0.7)

        categorias = ["Futebol","Vôlei","Basquete","Natação","Tênis"]
        valores    = [85, 60, 45, 70, 30]

        orig    = np.array([-2.6, -2.7, 0])
        eixo_h  = 3.8
        bar_w   = 0.80
        gap     = 0.40
        v_max   = 100

        eixo_x_len = len(categorias) * (bar_w + gap) + 0.2
        ax_x = Line(orig, orig + RIGHT * eixo_x_len, color=WHITE, stroke_width=2)
        ax_y = Line(orig, orig + UP * (eixo_h + 0.15), color=WHITE, stroke_width=2)
        self.play(Create(ax_x), Create(ax_y), run_time=0.9)

        marcas_y = VGroup()
        for v in [0, 20, 40, 60, 80, 100]:
            y = orig[1] + v * eixo_h / v_max
            tick = Line(
                np.array([orig[0]-0.12, y, 0]),
                np.array([orig[0],      y, 0]),
                color=WHITE, stroke_width=1.2
            )
            lbl = Text(str(v), color=WHITE, font_size=16).next_to(tick, LEFT, buff=0.08)
            marcas_y.add(tick, lbl)
        self.add(marcas_y)

        lbl_y = Text("Nº de alunos", color=WHITE, font_size=17).rotate(PI/2)
        lbl_y.move_to(np.array([orig[0]-1.0, orig[1] + eixo_h/2, 0]))
        self.add(lbl_y)

        barras   = VGroup()
        cats_lbl = VGroup()
        vals_lbl = VGroup()
        for i, (cat, val) in enumerate(zip(categorias, valores)):
            x_c   = orig[0] + (i + 0.5) * (bar_w + gap) + 0.1
            h     = val * eixo_h / v_max
            barra = Rectangle(
                width=bar_w, height=h,
                fill_color=BLUE_D, fill_opacity=0.88,
                stroke_color=WHITE, stroke_width=1.4
            ).move_to(np.array([x_c, orig[1] + h/2, 0]))
            barras.add(barra)

            cl = Text(cat, color=WHITE, font_size=17)
            cl.move_to(np.array([x_c, orig[1] - 0.28, 0]))
            cats_lbl.add(cl)

            vl = Text(str(val), color=ORANGE, font_size=18, weight=BOLD)
            vl.next_to(barra, UP, buff=0.07)
            vals_lbl.add(vl)

        for barra, cl, vl in zip(barras, cats_lbl, vals_lbl):
            self.play(GrowFromEdge(barra, DOWN), FadeIn(cl), run_time=0.60)
            self.play(FadeIn(vl), run_time=0.22)

        self.wait(0.8)

        idx_max = valores.index(max(valores))
        dest = SurroundingRectangle(barras[idx_max], color=ORANGE, buff=0.07)
        obs  = Text(
            "Futebol: categoria com mais alunos (85)!",
            color=ORANGE, font_size=22
        ).move_to(np.array([0, Y_RESPOSTA, 0]))
        self.play(Create(dest), run_time=0.6)
        self.play(FadeIn(obs), run_time=0.6)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, titulo_graf, ax_x, ax_y, marcas_y,
            lbl_y, barras, cats_lbl, vals_lbl, dest, obs
        )), run_time=1.0)


# =======================================================================
# CENA 4 – GRÁFICO DE LINHAS
# FIX: rótulo "Máx" deslocado para direita (não cai sobre eixo Y)
# =======================================================================
class CenaGraficoLinhas(Scene):
    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Gráfico de Linhas")

        quando = Text(
            "Use gráfico de linhas para mostrar como\n"
            "um valor muda ao longo do tempo.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.0, 0]))
        self.play(FadeIn(quando), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(quando), run_time=0.7)

        titulo_graf = Text(
            "Temperatura média mensal (°C) – Cidade X",
            color=WHITE, font_size=22
        ).move_to(np.array([0.6, 1.72, 0]))
        self.play(FadeIn(titulo_graf), run_time=0.7)

        meses = ["Jan","Fev","Mar","Abr","Mai","Jun",
                 "Jul","Ago","Set","Out","Nov","Dez"]
        temps = [30, 29, 27, 24, 21, 18, 17, 19, 22, 25, 27, 29]
        t_min, t_max = 10, 35

        orig     = np.array([-5.2, -2.7, 0])
        eixo_x_w = 9.8
        eixo_y_h = 3.8
        step_x   = eixo_x_w / (len(meses) - 1)

        ax_x = Line(orig, orig + RIGHT * eixo_x_w, color=WHITE, stroke_width=2)
        ax_y = Line(orig, orig + UP * (eixo_y_h + 0.15), color=WHITE, stroke_width=2)
        self.play(Create(ax_x), Create(ax_y), run_time=0.9)

        marcas_y = VGroup()
        for v in range(10, 36, 5):
            y = orig[1] + (v - t_min) * eixo_y_h / (t_max - t_min)
            tick = Line(
                np.array([orig[0]-0.12, y, 0]),
                np.array([orig[0],      y, 0]),
                color=WHITE, stroke_width=1.2
            )
            lbl = Text(str(v), color=WHITE, font_size=15).next_to(tick, LEFT, buff=0.07)
            marcas_y.add(tick, lbl)
        self.add(marcas_y)

        lbl_y = Text("Temp. (°C)", color=WHITE, font_size=16).rotate(PI/2)
        lbl_y.move_to(np.array([orig[0]-1.05, orig[1] + eixo_y_h/2, 0]))
        self.add(lbl_y)

        meses_lbl = VGroup()
        coords = []
        for i, (mes, temp) in enumerate(zip(meses, temps)):
            x = orig[0] + i * step_x
            y = orig[1] + (temp - t_min) * eixo_y_h / (t_max - t_min)
            coords.append(np.array([x, y, 0]))
            ml = Text(mes, color=WHITE, font_size=14)
            ml.move_to(np.array([x, orig[1] - 0.28, 0]))
            meses_lbl.add(ml)
        self.add(meses_lbl)

        dot0 = Dot(coords[0], color=GREEN_B, radius=0.09)
        self.play(FadeIn(dot0), run_time=0.3)
        todos = VGroup(dot0)
        for i in range(1, len(coords)):
            seg = Line(coords[i-1], coords[i], color=GREEN_B, stroke_width=2.5)
            dot = Dot(coords[i], color=GREEN_B, radius=0.09)
            self.play(Create(seg), FadeIn(dot), run_time=0.33)
            todos.add(seg, dot)

        self.wait(0.8)

        idx_min = temps.index(min(temps))
        idx_max = temps.index(max(temps))

        c_min = Circle(radius=0.17, color=BLUE,   stroke_width=2.5).move_to(coords[idx_min])
        c_max = Circle(radius=0.17, color=ORANGE, stroke_width=2.5).move_to(coords[idx_max])

        # FIX: lbl_min abaixo do ponto; lbl_max à DIREITA do ponto (Jan fica na borda esq)
        lbl_min = Text(f"Mín: {min(temps)}°C ({meses[idx_min]})",
                       color=BLUE, font_size=20)
        lbl_min.next_to(c_min, DOWN, buff=0.18)

        lbl_max = Text(f"Máx: {max(temps)}°C ({meses[idx_max]})",
                       color=ORANGE, font_size=20)
        # Desloca à direita do círculo e um pouco acima para não sobrepor eixo nem ponto
        lbl_max.next_to(c_max, RIGHT, buff=0.22).shift(UP * 0.25)

        self.play(Create(c_min), FadeIn(lbl_min), run_time=0.8)
        self.play(Create(c_max), FadeIn(lbl_max), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, titulo_graf, ax_x, ax_y,
            marcas_y, lbl_y, meses_lbl, todos,
            c_min, c_max, lbl_min, lbl_max
        )), run_time=1.0)


# =======================================================================
# CENA 5 – PROBLEMA 1: TABELA
# FIX: tabela menor/mais alta + cálculo e resposta em posições fixas
#      sem colidir com a tabela
# =======================================================================
class CenaProblema1(Scene):
    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Problema: Tabela de Dados")

        enunciado = Text(
            "A tabela mostra o número de livros lidos por\n"
            "4 alunos em um semestre. Qual é a diferença\n"
            "entre o aluno que mais leu e o que menos leu?",
            color=WHITE, font_size=25, line_spacing=1.35
        ).move_to(np.array([0, 0.3, 0]))
        self.play(FadeIn(enunciado), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(enunciado), run_time=0.7)

        # Tabela compacta na metade superior da tela
        titulo_tab = Text(
            "Leitura semestral – Turma 9ºA",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.65, 0]))
        self.play(FadeIn(titulo_tab), run_time=0.7)

        headers = ["Aluno", "Livros lidos"]
        dados   = [["Ana","14"],["Bruno","8"],
                   ["Carla","19"],["Daniel","11"]]
        col_w   = [3.0, 3.0]
        row_h   = 0.56
        n_rows  = len(dados) + 1
        n_cols  = 2
        # Topo da tabela logo abaixo do título (y=1.65 - 0.25 = 1.40)
        tab_topo = 1.33

        cells = VGroup()
        texts = VGroup()
        for r in range(n_rows):
            for c in range(n_cols):
                cx = -sum(col_w)/2 + sum(col_w[:c]) + col_w[c]/2
                cy = tab_topo - row_h/2 - r * row_h
                if r == 0:
                    fc, fo, tc = BLUE_E, 0.92, YELLOW
                else:
                    fc  = BLUE_D
                    fo  = 0.30 if r % 2 == 0 else 0.15
                    tc  = WHITE
                cell = Rectangle(
                    width=col_w[c], height=row_h,
                    fill_color=fc, fill_opacity=fo,
                    stroke_color=WHITE, stroke_width=1.5
                ).move_to(np.array([cx, cy, 0]))
                cells.add(cell)
                lbl = Text(
                    headers[c] if r == 0 else dados[r-1][c],
                    color=tc, font_size=21,
                    weight=BOLD if r == 0 else NORMAL
                ).move_to(np.array([cx, cy, 0]))
                texts.add(lbl)

        self.play(FadeIn(VGroup(*cells[:n_cols])),
                  Write(VGroup(*texts[:n_cols])), run_time=0.8)
        for r in range(1, n_rows):
            self.play(
                FadeIn(VGroup(*cells[r*n_cols:(r+1)*n_cols])),
                Write(VGroup(*texts[r*n_cols:(r+1)*n_cols])),
                run_time=0.5
            )
        self.wait(0.8)

        # Destaque: Carla r=3,c=1→idx=7 | Bruno r=2,c=1→idx=5
        box_max = SurroundingRectangle(texts[7], color=ORANGE, buff=0.09)
        box_min = SurroundingRectangle(texts[5], color=BLUE,   buff=0.09)

        # Legendas alinhadas horizontalmente com as linhas da tabela
        # Carla é r=3 → cy = tab_topo - row_h/2 - 3*row_h
        cy_carla = tab_topo - row_h/2 - 3 * row_h
        # Bruno é r=2 → cy = tab_topo - row_h/2 - 2*row_h
        cy_bruno = tab_topo - row_h/2 - 2 * row_h

        lbl_max = Text("Maior: Carla (19)", color=ORANGE, font_size=21)
        lbl_min = Text("Menor: Bruno (8)",  color=BLUE,   font_size=21)
        lbl_max.move_to(np.array([4.5, cy_carla, 0]))
        lbl_min.move_to(np.array([4.5, cy_bruno, 0]))

        self.play(Create(box_max), FadeIn(lbl_max), run_time=0.7)
        self.play(Create(box_min), FadeIn(lbl_min), run_time=0.7)
        self.wait(0.8)

        # Cálculo centralizado abaixo da tabela – sem colisão
        # Última linha da tabela termina em: tab_topo - n_rows*row_h
        # = 1.33 - 5*0.56 = 1.33 - 2.80 = -1.47  → cálculo em -2.0
        calculo = Text("19 − 8 = 11 livros", color=GREEN_B, font_size=36)
        calculo.move_to(np.array([0, Y_CALCULO, 0]))
        box_calc = SurroundingRectangle(
            calculo, color=GREEN_B, buff=0.18, corner_radius=0.10
        )
        self.play(Write(calculo), Create(box_calc), run_time=1.0)

        resposta = Text(
            "Resposta: a diferença é de 11 livros.",
            color=YELLOW, font_size=24
        ).move_to(np.array([0, Y_RESPOSTA, 0]))
        self.play(FadeIn(resposta), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, titulo_tab, cells, texts,
            box_max, box_min, lbl_max, lbl_min,
            calculo, box_calc, resposta
        )), run_time=1.0)


# =======================================================================
# CENA 6 – PROBLEMA 2: GRÁFICO DE SETORES
# FIX: pizza menor + mais para cima, cálculo/resposta fixos abaixo
#      destaque = apenas mudança de stroke do setor original (sem sobreposição)
# =======================================================================
class CenaProblema2(Scene):

    def _setor(self, cx, cy, raio, ang_ini, ang_fim,
               cor, opacidade=0.88, n_pts=60):
        """Setor circular como Polygon (evita bugs de AnnularSector)."""
        pts = [np.array([cx, cy, 0])]
        for k in range(n_pts + 1):
            a = ang_ini + (ang_fim - ang_ini) * k / n_pts
            pts.append(np.array([cx + raio*np.cos(a),
                                  cy + raio*np.sin(a), 0]))
        return Polygon(
            *pts,
            fill_color=cor, fill_opacity=opacidade,
            stroke_color=WHITE, stroke_width=2
        )

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Problema: Gráfico de Setores")

        enunciado = Text(
            "Em uma escola com 400 alunos, o gráfico\n"
            "mostra o meio de transporte usado. Quantos\n"
            "alunos vão a pé para a escola?",
            color=WHITE, font_size=25, line_spacing=1.35
        ).move_to(np.array([0, 0.3, 0]))
        self.play(FadeIn(enunciado), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(enunciado), run_time=0.7)

        titulo_graf = Text(
            "Meio de transporte – 400 alunos",
            color=WHITE, font_size=22
        ).move_to(np.array([0, 1.72, 0]))
        self.play(FadeIn(titulo_graf), run_time=0.7)

        # Pizza: centro à esquerda e mais baixo para não sobrepor o título
        cx, cy = -2.5, -0.35
        raio   = 1.55

        setores_data = [
            ("Ônibus",    40, BLUE_D),
            ("A pé",      25, GREEN_B),
            ("Bicicleta", 20, ORANGE),
            ("Carro",     15, "#9999cc"),
        ]

        # Guardar referências para o destaque posterior
        setores_objs = []
        ang_atual = PI / 2      # começa no topo, sentido horário
        graficos  = VGroup()
        pct_lbls  = VGroup()
        ang_lista = []          # guarda (ang_ini, ang_fim) de cada setor

        for rotulo, pct, cor in setores_data:
            ang_setor = pct / 100 * TAU
            ang_fim   = ang_atual - ang_setor

            setor = self._setor(cx, cy, raio, ang_fim, ang_atual, cor)
            graficos.add(setor)
            setores_objs.append(setor)
            ang_lista.append((ang_fim, ang_atual))

            ang_meio = (ang_atual + ang_fim) / 2
            lx = cx + raio * 0.60 * np.cos(ang_meio)
            ly = cy + raio * 0.60 * np.sin(ang_meio)
            pl = Text(f"{pct}%", color=WHITE, font_size=19, weight=BOLD)
            pl.move_to(np.array([lx, ly, 0]))
            pct_lbls.add(pl)

            self.play(DrawBorderThenFill(setor), run_time=0.75)
            self.play(FadeIn(pl), run_time=0.28)
            ang_atual = ang_fim

        # Legenda à direita da pizza
        leg_x  = 1.5
        leg_y0 = 0.9
        legenda = VGroup()
        for i, (rotulo, pct, cor) in enumerate(setores_data):
            sq = Square(side_length=0.26,
                        fill_color=cor, fill_opacity=0.9, stroke_width=0)
            sq.move_to(np.array([leg_x, leg_y0 - i * 0.55, 0]))
            lt = Text(rotulo, color=WHITE, font_size=20)
            lt.next_to(sq, RIGHT, buff=0.14)
            self.play(FadeIn(sq), Write(lt), run_time=0.40)
            legenda.add(sq, lt)

        self.wait(0.8)

        # FIX: destaque = stroke YELLOW (cor não usada em nenhum setor da pizza)
        # sem criar novo polígono sobreposto
        setor_ape = setores_objs[1]
        self.play(
            setor_ape.animate.set_stroke(color=YELLOW, width=5),
            run_time=0.7
        )

        # Cálculo e resposta em posições fixas abaixo da pizza
        calculo = VGroup(
            Text("Alunos que vão a pé:", color=WHITE, font_size=23),
            Text("25% × 400 = 100 alunos", color=GREEN_B, font_size=30),
        ).arrange(DOWN, buff=0.22)
        calculo.move_to(np.array([0, Y_CALCULO, 0]))

        self.play(FadeIn(calculo[0]), run_time=0.6)
        self.play(Write(calculo[1]), run_time=0.9)
        box_c = SurroundingRectangle(
            calculo[1], color=GREEN_B, buff=0.14, corner_radius=0.10
        )
        self.play(Create(box_c), run_time=0.5)

        resposta = Text(
            "Resposta: 100 alunos vão a pé.",
            color=YELLOW, font_size=24
        ).move_to(np.array([0, Y_RESPOSTA, 0]))
        self.play(FadeIn(resposta), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, titulo_graf, graficos, pct_lbls,
            legenda, calculo, box_c, resposta
        )), run_time=1.0)


# =======================================================================
# CENA 7 – ENCERRAMENTO
# =======================================================================
class Encerramento(Scene):
    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese — Descritor D36")

        descritivo = Text(
            "D36 – Resolver problemas envolvendo informações\n"
            "apresentadas em tabelas e/ou gráficos",
            color=WHITE, font_size=26, line_spacing=1.3
        ).move_to(np.array([0, 1.1, 0]))
        box_desc = SurroundingRectangle(
            descritivo, color=YELLOW, buff=0.18, corner_radius=0.1
        )
        self.play(FadeIn(descritivo), Create(box_desc), run_time=1.2)
        self.wait(0.7)

        mapa_tit = Text(
            "Estratégias para resolver problemas com tabelas e gráficos:",
            color=WHITE, font_size=22
        ).move_to(np.array([0, 0.1, 0]))
        self.play(FadeIn(mapa_tit), run_time=0.8)

        estrategias = VGroup(
            Text("1. Leia o título — ele diz o que está sendo representado",
                 color=WHITE,   font_size=20),
            Text("2. Identifique os eixos ou colunas e suas unidades",
                 color=ORANGE,  font_size=20),
            Text("3. Localize os dados pedidos no enunciado",
                 color=WHITE,   font_size=20),
            Text("4. Compare, some ou subtraia os valores conforme pedido",
                 color=ORANGE,  font_size=20),
            Text("5. Confira se a resposta faz sentido com o contexto",
                 color=GREEN_B, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        estrategias.next_to(mapa_tit, DOWN, buff=0.28)

        dots = VGroup()
        cores_dot = [GREEN_B, ORANGE, GREEN_B, ORANGE, GREEN_B]
        for i, linha in enumerate(estrategias):
            dot = Dot(color=cores_dot[i], radius=0.07).next_to(linha, LEFT, buff=0.14)
            dots.add(dot)
            self.play(FadeIn(dot), FadeIn(linha, shift=RIGHT*0.1), run_time=0.58)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            cab, linha_sep, descritivo, box_desc,
            mapa_tit, estrategias, dots
        )), run_time=1.2)


# =======================================================================
# LOGO – Identidade visual da Prof.ª Emilly Mayre (idêntica ao D14)
# =======================================================================
class LogoEmillyMayre(Scene):
    def construct(self):
        ESCURO_L = "#1a1a2e"
        DOURADO  = "#C8A84B"
        CINZA_L  = "#888899"

        bg = Rectangle(width=16, height=9,
                       fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.add(bg)

        a = 1.9

        def inf_h(t):
            d = 1 + np.sin(t)**2
            return np.array([a*np.cos(t)/d, a*np.sin(t)*np.cos(t)/d, 0])

        def inf_v(t):
            d = 1 + np.sin(t)**2
            return np.array([a*np.sin(t)*np.cos(t)/d, a*np.cos(t)/d, 0])

        logo_h = ParametricFunction(inf_h, t_range=[0, TAU],
                                    color="#3a3a5c", stroke_width=2.5)
        logo_v = ParametricFunction(inf_v, t_range=[0, TAU],
                                    color="#9999bb", stroke_width=2.5)
        logo_h.move_to(UP * 0.5)
        logo_v.move_to(UP * 0.5)

        circ = Circle(radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
                      color=ESCURO_L, stroke_width=0).move_to(UP * 0.5)
        em   = Text("EM", color=WHITE, font_size=22,
                    weight=BOLD).move_to(circ.get_center())

        grp  = VGroup(logo_h, logo_v)
        nome = Text("Emilly Mayre", color=ESCURO_L, font_size=28, weight=BOLD)
        nome.next_to(grp, DOWN, buff=0.55)
        linha = Line(LEFT*1.6, RIGHT*1.6, color=DOURADO, stroke_width=3.5)
        linha.next_to(nome, DOWN, buff=0.16)
        cargo = Text("PROFESSORA DE MATEMÁTICA", color=CINZA_L, font_size=14)
        cargo.next_to(linha, DOWN, buff=0.18)

        self.play(Create(logo_h), run_time=2.0)
        self.wait(0.3)
        self.play(Create(logo_v), run_time=2.0)
        self.wait(0.3)
        self.play(GrowFromCenter(circ), run_time=0.7)
        self.play(Write(em), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(nome, shift=UP*0.15), run_time=0.8)
        self.play(Create(linha), run_time=0.5)
        self.play(FadeIn(cargo), run_time=0.6)
        self.wait(0.4)
        simbolo = VGroup(logo_h, logo_v, circ, em)
        self.play(simbolo.animate.scale(1.06), run_time=0.4)
        self.play(simbolo.animate.scale(1/1.06), run_time=0.35)
        self.wait(3.5)
