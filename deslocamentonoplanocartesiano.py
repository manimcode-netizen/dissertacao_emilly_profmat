"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Deslocamento no plano cartesiano — vetores Norte e Leste
Nível    : Ensino Fundamental / Médio
Objetivo : Compreender deslocamento como variação de posição,
           identificar componentes vertical e horizontal,
           e visualizar a trajetória com rastro e vetor.
=======================================================================
RENDERIZAÇÃO:
  manim -pql deslocamento_plano.py DeslocamentoNoPlano
  manim -pqh deslocamento_plano.py DeslocamentoNoPlano
=======================================================================
"""

from manim import *
import numpy as np

# ── Paleta semântica ────────────────────────────────────────────────
COR_PONTO    = YELLOW   # ponto em movimento
COR_NORTE    = BLUE     # deslocamento vertical (norte)
COR_LESTE    = RED      # deslocamento horizontal (leste)
COR_TEXTO    = WHITE
COR_EIXO     = GRAY


class DeslocamentoNoPlano(Scene):
    """
    Conceito : Deslocamento no plano — norte (+3) e leste (+4)
    Nível    : Ensino Fundamental / Médio
    Objetivo : Visualizar deslocamentos como vetores com rastro e medida,
               partindo de (2,3), movendo +3 norte e +4 leste.
    """

    def construct(self):

        # ── ETAPA 1: Plano cartesiano com eixos numerados ────────────
        plano = NumberPlane(
            x_range=[-1, 8, 1],
            y_range=[-1, 8, 1],
            x_length=8.5,
            y_length=7.0,
            axis_config={
                "color": COR_EIXO,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 20,
            },
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.25,
                "stroke_width": 1,
            }
        )
        plano.shift(DOWN * 0.3 + LEFT * 0.3)

        lbl_x = MathTex("x", color=COR_TEXTO, font_size=24).next_to(plano.c2p(8, 0), RIGHT, buff=0.15)
        lbl_y = MathTex("y", color=COR_TEXTO, font_size=24).next_to(plano.c2p(0, 8), UP,    buff=0.15)

        self.play(Create(plano), run_time=1.5)
        self.play(FadeIn(lbl_x), FadeIn(lbl_y))
        self.wait(0.5)

        # ── ETAPA 2: Ponto inicial em (2, 3) ─────────────────────────
        P0 = plano.c2p(2, 3)
        ponto = Dot(P0, color=COR_PONTO, radius=0.14)

        lbl_P0 = MathTex("(2,\\ 3)", color=COR_PONTO, font_size=22)
        lbl_P0.next_to(ponto, DL, buff=0.18)

        self.play(GrowFromCenter(ponto), Write(lbl_P0), run_time=1.0)
        self.wait(2.0)   # pausa para o estudante registrar a posição inicial

        # ── ETAPA 3: Deslocamento NORTE +3 (vertical) ────────────────
        P1 = plano.c2p(2, 6)

        # Rastro contínuo acompanha o movimento
        rastro_norte = TracedPath(
            ponto.get_center,
            stroke_color=COR_NORTE,
            stroke_width=3
        )
        self.add(rastro_norte)

        self.play(
            ponto.animate.move_to(P1),
            run_time=2.5
        )
        self.remove(rastro_norte)

        # Linha fixa do rastro norte (mantém visível após o movimento)
        linha_norte = Line(P0, P1, color=COR_NORTE, stroke_width=3)
        self.add(linha_norte)

        # Vetor norte sobre o rastro
        vetor_norte = Arrow(
            P0, P1,
            color=COR_NORTE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.12
        )
        medida_norte = MathTex(r"\Delta y = +3", color=COR_NORTE, font_size=24)
        medida_norte.next_to(linha_norte, LEFT, buff=0.20)

        self.play(GrowArrow(vetor_norte), run_time=0.9)
        self.play(Write(medida_norte), run_time=0.8)

        # Label posição intermediária
        lbl_P1 = MathTex("(2,\\ 6)", color=COR_PONTO, font_size=22)
        lbl_P1.next_to(ponto, UL, buff=0.18)
        self.play(Write(lbl_P1), run_time=0.7)
        self.wait(2.0)   # pausa de 2 segundos na posição intermediária

        # ── ETAPA 4: Deslocamento LESTE +4 (horizontal) ──────────────
        P2 = plano.c2p(6, 6)

        rastro_leste = TracedPath(
            ponto.get_center,
            stroke_color=COR_LESTE,
            stroke_width=3
        )
        self.add(rastro_leste)

        self.play(
            ponto.animate.move_to(P2),
            run_time=2.5
        )
        self.remove(rastro_leste)

        # Linha fixa do rastro leste
        linha_leste = Line(P1, P2, color=COR_LESTE, stroke_width=3)
        self.add(linha_leste)

        # Vetor leste
        vetor_leste = Arrow(
            P1, P2,
            color=COR_LESTE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.10
        )
        medida_leste = MathTex(r"\Delta x = +4", color=COR_LESTE, font_size=24)
        medida_leste.next_to(linha_leste, DOWN, buff=0.20)

        self.play(GrowArrow(vetor_leste), run_time=0.9)
        self.play(Write(medida_leste), run_time=0.8)

        # Label posição final
        lbl_P2 = MathTex("(6,\\ 6)", color=COR_PONTO, font_size=22)
        lbl_P2.next_to(ponto, UR, buff=0.18)
        self.play(FadeOut(lbl_P1), Write(lbl_P2), run_time=0.7)

        # ── ETAPA 5: Cena final — tudo visível simultaneamente ───────
        self.wait(3.0)
