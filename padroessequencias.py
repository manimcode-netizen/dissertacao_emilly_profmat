"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Sequência figural de quadrados — f(n) = n²
Nível    : Ensino Fundamental / Médio
=======================================================================
"""

from manim import *
import numpy as np

COR_BASE    = BLUE_D
COR_NOVO    = YELLOW
COR_TABELA  = GREEN
COR_FORMULA = ORANGE
COR_TEXTO   = WHITE
TAM = 0.55


def grade_nxn(n, cor_base, cor_novo):
    """
    Cria uma grade n×n corretamente alinhada.
    Linha e coluna n-1 (última) são amarelas (novas).
    Restante é azul (base).
    Retorna (grupo_base, grupo_novo, grade_completa).
    """
    grade = VGroup()
    grupo_base = VGroup()
    grupo_novo = VGroup()

    for row in range(n):         # row 0 = baixo
        for col in range(n):     # col 0 = esquerda
            q = Square(
                side_length=TAM,
                fill_color=cor_novo if (row == n-1 or col == n-1) else cor_base,
                fill_opacity=0.85,
                stroke_color=WHITE,
                stroke_width=1.2
            )
            q.move_to(np.array([col * TAM, row * TAM, 0]))
            grade.add(q)
            if row == n-1 or col == n-1:
                grupo_novo.add(q)
            else:
                grupo_base.add(q)

    # Centralizar grade na origem
    grade.move_to(ORIGIN)
    return grupo_base, grupo_novo, grade


class SequenciaQuadrados(Scene):

    def construct(self):

        # ── Título ───────────────────────────────────────────────────
        titulo = Text("Sequência de Quadrados", color=COR_TEXTO, font_size=34)
        subtit = Text("Quantos quadradinhos tem o n-ésimo termo?",
                      color=COR_TABELA, font_size=22)
        subtit.next_to(titulo, DOWN, buff=0.3)
        self.play(Write(titulo), run_time=1.0)
        self.play(FadeIn(subtit), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtit)), run_time=0.7)

        # ── ETAPA 1: Construção dos 4 primeiros termos ───────────────
        tit_cena = Text("Construindo os termos...", color=COR_TEXTO, font_size=26)
        tit_cena.to_edge(UP, buff=0.3)
        self.play(Write(tit_cena), run_time=0.7)

        # Posições horizontais dos 4 termos
        x_pos = [-5.2, -1.9, 1.4, 4.8]
        termos_vgroups = []

        for n in range(1, 5):
            grupo_base, grupo_novo, grade = grade_nxn(n, COR_BASE, COR_NOVO)

            # Posicionar grade
            grade.move_to(np.array([x_pos[n-1], 0.9, 0]))

            # Contador e total
            contador  = MathTex(f"n = {n}", color=COR_TEXTO, font_size=24)
            total_lbl = MathTex(f"{n}^2 = {n*n}", color=COR_NOVO, font_size=22)
            contador.next_to(grade, DOWN, buff=0.25)
            total_lbl.next_to(contador, DOWN, buff=0.12)

            if n == 1:
                self.play(FadeIn(grade), Write(contador), run_time=0.8)
            else:
                self.play(FadeIn(grupo_base), run_time=0.5)
                self.play(FadeIn(grupo_novo), run_time=0.7)
                self.play(Write(contador), run_time=0.4)

            self.play(Write(total_lbl), run_time=0.4)
            self.wait(0.8)

            termos_vgroups.append(VGroup(grade, contador, total_lbl))

        self.wait(1.0)

        # ── ETAPA 2: Tabela n × n² ────────────────────────────────────
        self.play(FadeOut(tit_cena), run_time=0.4)
        self.play(
            *[g.animate.scale(0.75).shift(UP * 1.5) for g in termos_vgroups],
            run_time=1.0
        )

        # Tabela à ESQUERDA
        TX = -3.5  # centro x da tabela
        cab_n  = MathTex("n",   color=COR_TEXTO,  font_size=28).move_to(np.array([TX-0.6, -0.5, 0]))
        cab_n2 = MathTex("n^2", color=COR_TABELA, font_size=28).move_to(np.array([TX+0.6, -0.5, 0]))
        linha_cab = Line(np.array([TX-1.4, -0.8, 0]), np.array([TX+1.4, -0.8, 0]), color=GRAY, stroke_width=1.5)
        col_div   = Line(np.array([TX,     -0.2, 0]), np.array([TX,     -3.1, 0]), color=GRAY, stroke_width=1.5)

        self.play(Write(cab_n), Write(cab_n2), Create(linha_cab), Create(col_div), run_time=0.8)

        celulas = VGroup()
        for i, (nv, n2v) in enumerate([(1,1),(2,4),(3,9),(4,16)]):
            y = -1.15 - i * 0.50
            cn  = MathTex(str(nv),  color=COR_TEXTO,  font_size=24).move_to(np.array([TX-0.6, y, 0]))
            cn2 = MathTex(str(n2v), color=COR_TABELA, font_size=24).move_to(np.array([TX+0.6, y, 0]))
            self.play(Write(cn), Write(cn2), run_time=0.35)
            celulas.add(cn, cn2)

        # Diferenças à direita da tabela
        difs = VGroup()
        for i, d in enumerate(["+3", "+5", "+7"]):
            lbl = MathTex(d, color=ORANGE, font_size=20)
            lbl.move_to(np.array([TX+1.8, -1.62 - i * 0.50, 0]))
            difs.add(lbl)
            self.play(Write(lbl), run_time=0.35)

        self.wait(1.0)

        # ── ETAPA 3: Fórmula geral à DIREITA ─────────────────────────
        formula = MathTex(r"f(n) = n^2", color=COR_FORMULA, font_size=48)
        formula.move_to(np.array([2.8, -1.5, 0]))
        box_f = SurroundingRectangle(formula, color=COR_FORMULA, buff=0.25, corner_radius=0.12)
        self.play(Write(formula), Create(box_f), run_time=1.2)
        self.wait(1.5)

        # ── ETAPA 4: Verificação n = 5 ────────────────────────────────
        self.play(FadeOut(VGroup(
            *termos_vgroups, cab_n, cab_n2, linha_cab,
            col_div, celulas, difs, formula, box_f
        )), run_time=0.8)

        tit_v = Text("Verificação: n = 5", color=COR_TEXTO, font_size=28)
        tit_v.to_edge(UP, buff=0.3)
        self.play(Write(tit_v), run_time=0.7)

        gb5, gn5, grade5 = grade_nxn(5, COR_BASE, COR_NOVO)
        grade5.scale(1.2).move_to(np.array([-2.5, 0.0, 0]))

        self.play(FadeIn(gb5), run_time=0.8)
        self.play(FadeIn(gn5), run_time=0.8)

        verif = MathTex(r"f(5) = 5^2 = 25", color=COR_FORMULA, font_size=38)
        verif.move_to(np.array([2.8, 0.4, 0]))
        conta = MathTex(r"5 \times 5 = 25\ \checkmark", color=COR_TABELA, font_size=30)
        conta.next_to(verif, DOWN, buff=0.4)

        self.play(Write(verif), run_time=1.0)
        self.play(Write(conta), run_time=0.8)
        self.wait(3.0)
