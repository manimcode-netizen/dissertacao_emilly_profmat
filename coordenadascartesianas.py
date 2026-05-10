"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Coordenadas Cartesianas — par ordenado (x, y)
Nível    : Ensino Fundamental / Médio
Objetivo : Compreender que todo ponto no plano é identificado por
           um par ordenado, via projeção nos eixos x e y.
=======================================================================
RENDERIZAÇÃO:
  manim -pql coord_v2.py CoordenadasCartesianas
  manim -pqh coord_v2.py CoordenadasCartesianas
=======================================================================
"""

from manim import *
import numpy as np

COR_PONTO = YELLOW
COR_X     = RED
COR_Y     = BLUE
COR_TEXTO = WHITE


class CoordenadasCartesianas(Scene):

    def construct(self):
        # ── Título introdutório ──────────────────────────────────────
        titulo = Text("Coordenadas Cartesianas", color=COR_TEXTO, font_size=36)
        subtit = Text("Localizando um ponto no plano", color=COR_PONTO, font_size=24)
        subtit.next_to(titulo, DOWN, buff=0.3)
        grupo_titulo = VGroup(titulo, subtit).move_to(ORIGIN)
        self.play(Write(titulo), run_time=1.2)
        self.play(FadeIn(subtit), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(grupo_titulo), run_time=0.8)
        self.wait(0.3)

        # ── Título fixo no topo ──────────────────────────────────────
        titulo_cena = Text("Coordenadas Cartesianas", color=COR_TEXTO, font_size=26)
        titulo_cena.to_edge(UP, buff=0.15)
        self.play(Write(titulo_cena), run_time=0.8)

        # ── Plano cartesiano descido para não sobrepor título ────────
        plano = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=5.5,
            axis_config={"color": WHITE, "stroke_width": 2},
            background_line_style={
                "stroke_color": GRAY,
                "stroke_opacity": 0.3,
                "stroke_width": 1
            }
        )
        # Descer o plano para não sobrepor o título
        plano.shift(DOWN * 0.6)

        lbl_x = MathTex("x", color=COR_TEXTO, font_size=26).next_to(plano.c2p(5, 0), RIGHT, buff=0.15)
        lbl_y = MathTex("y", color=COR_TEXTO, font_size=26).next_to(plano.c2p(0, 4), UP,    buff=0.15)

        self.play(Create(plano), run_time=1.5)
        self.play(FadeIn(lbl_x), FadeIn(lbl_y))
        self.wait(0.8)

        # ── Demonstração 1: ponto P(3, 4) — quadrante I ─────────────
        self._demonstrar_ponto(plano, px=3, py=4, nome="P")
        self.wait(1.0)

        # ── Demonstração 2: ponto Q(-3, -2) — quadrante III ─────────
        self._demonstrar_ponto(plano, px=-3, py=-2, nome="Q")
        self.wait(2.0)

    def _demonstrar_ponto(self, plano, px, py, nome):
        pos    = plano.c2p(px, py)
        pos_x0 = plano.c2p(px, 0)
        pos_0y = plano.c2p(0, py)

        # 1. Ponto + label (só o nome, sem coordenadas ainda)
        ponto = Dot(pos, color=COR_PONTO, radius=0.12)
        lbl_P = MathTex(nome, color=COR_PONTO, font_size=26)
        lbl_P.next_to(ponto, UR, buff=0.12)
        self.play(GrowFromCenter(ponto), Write(lbl_P), run_time=0.8)
        self.wait(0.8)

        # 2. Linha da malha no y=py (mesma espessura e cor da grade)
        linha_grade = Line(
            plano.c2p(-5, py), plano.c2p(5, py),
            color=GRAY, stroke_width=1, stroke_opacity=0.3
        )
        # Já está na grade — não precisa desenhar separado

        # 3. Projeção vertical → eixo x
        proj_x  = DashedLine(pos, pos_x0, color=COR_X, dash_length=0.15, stroke_width=2.5)
        marca_x = Dot(pos_x0, color=COR_X, radius=0.10)
        dir_x   = DOWN if py > 0 else UP
        lbl_xval = MathTex(str(px), color=COR_X, font_size=24)
        lbl_xval.next_to(pos_x0, dir_x, buff=0.20)

        self.play(Create(proj_x), run_time=1.2)
        self.play(GrowFromCenter(marca_x), Write(lbl_xval), run_time=0.7)
        self.wait(0.6)

        # 4. Projeção horizontal → eixo y
        proj_y  = DashedLine(pos, pos_0y, color=COR_Y, dash_length=0.15, stroke_width=2.5)
        marca_y = Dot(pos_0y, color=COR_Y, radius=0.10)
        dir_y   = LEFT if px > 0 else RIGHT
        lbl_yval = MathTex(str(py), color=COR_Y, font_size=24)
        lbl_yval.next_to(pos_0y, dir_y, buff=0.20)

        self.play(Create(proj_y), run_time=1.2)
        self.play(GrowFromCenter(marca_y), Write(lbl_yval), run_time=0.7)
        self.wait(0.6)

        # 5. Par ordenado ao lado do ponto já marcado (substitui o lbl_P)
        # Posicionado ao lado oposto do quadrante para não sobrepor
        dir_par = UL if px > 0 else UR
        par = MathTex(
            f"{nome}(",
            f"{px}",
            r",\ ",
            f"{py}",
            ")",
            font_size=28
        )
        par[0].set_color(COR_PONTO)
        par[1].set_color(COR_X)
        par[2].set_color(COR_TEXTO)
        par[3].set_color(COR_Y)
        par[4].set_color(COR_PONTO)
        par.next_to(ponto, dir_par, buff=0.35)

        # Substituir o label simples pelo par ordenado
        self.play(ReplacementTransform(lbl_P, par), run_time=1.0)
        self.wait(2.5)

        # 6. Limpar tudo
        self.play(FadeOut(VGroup(
            ponto, par,
            proj_x, marca_x, lbl_xval,
            proj_y, marca_y, lbl_yval,
        )), run_time=1.0)
        self.wait(0.4)
