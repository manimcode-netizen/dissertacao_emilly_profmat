"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Proporcionalidade direta — razão constante entre grandezas
Nível    : Ensino Fundamental / Médio
=======================================================================
"""

from manim import *
import numpy as np

COR_RETA1   = BLUE
COR_RETA2   = RED
COR_PONTO   = YELLOW
COR_RAZAO   = GREEN
COR_BARRA_X = ORANGE
COR_TEXTO   = WHITE


class Proporcionalidade(Scene):

    def construct(self):
        titulo = Text("Proporcionalidade Direta", color=COR_TEXTO, font_size=34)
        subtit = Text("A razão entre as grandezas é sempre constante",
                      color=COR_RAZAO, font_size=22)
        subtit.next_to(titulo, DOWN, buff=0.3)
        self.play(Write(titulo), run_time=1.2)
        self.play(FadeIn(subtit), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtit)), run_time=0.8)

        self._demonstrar_reta(
            k=3, cor_reta=COR_RETA1,
            pontos_pausa=[(2, 6), (4, 12), (6, 18)],
            titulo_cena="Veículo A  —  3 km por litro",
            label_k="k = 3\\ km/L"
        )

        self._demonstrar_reta(
            k=5, cor_reta=COR_RETA2,
            pontos_pausa=[(2, 10), (4, 20), (6, 30)],
            titulo_cena="Veículo B  —  5 km por litro",
            label_k="k = 5\\ km/L"
        )

        self.wait(2.0)

    def _demonstrar_reta(self, k, cor_reta, pontos_pausa, titulo_cena, label_k):

        # ── Título ───────────────────────────────────────────────────
        tit = Text(titulo_cena, color=cor_reta, font_size=26)
        tit.to_edge(UP, buff=0.2)
        self.play(Write(tit), run_time=0.8)

        # ── Eixos — lado esquerdo ─────────────────────────────────────
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 36, 6],
            x_length=5.0,
            y_length=5.0,
            axis_config={"color": WHITE, "stroke_width": 2,
                         "include_numbers": True, "font_size": 18},
            tips=True
        )
        axes.to_edge(LEFT, buff=0.8).shift(DOWN * 0.5)

        lbl_x = Text("Litros (L)", color=COR_TEXTO, font_size=16)
        lbl_x.next_to(axes.c2p(7, 0), RIGHT, buff=0.05)
        lbl_y = Text("Distância (km)", color=COR_TEXTO, font_size=16)
        lbl_y.next_to(axes.c2p(0, 36), UP, buff=0.05)

        self.play(Create(axes), FadeIn(lbl_x), FadeIn(lbl_y), run_time=1.2)

        # ── Reta ──────────────────────────────────────────────────────
        reta = axes.plot(lambda x: k * x, x_range=[0, 6.9],
                         color=cor_reta, stroke_width=2.5)
        lbl_reta = MathTex(label_k, color=cor_reta, font_size=20)
        lbl_reta.next_to(axes.c2p(6.9, k*6.9), UP, buff=0.15)

        self.play(Create(reta), Write(lbl_reta), run_time=1.2)

        # ── Ponto móvel ───────────────────────────────────────────────
        t = ValueTracker(0.01)

        ponto = always_redraw(lambda: Dot(
            axes.c2p(t.get_value(), k * t.get_value()),
            color=COR_PONTO, radius=0.12
        ))
        self.add(ponto)

        # ── Painel lateral — lado direito ─────────────────────────────
        # Posição base do painel
        painel_x = 3.2   # x do centro do painel
        base_y   = axes.c2p(0, 0)[1]
        BAR_MAX  = 3.2
        BAR_W    = 0.55

        # Linha de base do painel
        base_line = Line(
            np.array([painel_x - 1.0, base_y, 0]),
            np.array([painel_x + 1.0, base_y, 0]),
            color=GRAY, stroke_width=1.5
        )
        self.add(base_line)

        # Labels fixas das barras
        lbl_bx = Text("L", color=COR_BARRA_X, font_size=20)
        lbl_bx.move_to(np.array([painel_x - 0.4, base_y - 0.3, 0]))
        lbl_by = Text("km", color=cor_reta, font_size=20)
        lbl_by.move_to(np.array([painel_x + 0.4, base_y - 0.3, 0]))
        self.add(lbl_bx, lbl_by)

        # Barras dinâmicas
        barra_x = always_redraw(lambda: Rectangle(
            width=BAR_W,
            height=max(t.get_value() / 7 * BAR_MAX, 0.01),
            fill_color=COR_BARRA_X, fill_opacity=0.85, stroke_width=1
        ).move_to(
            np.array([painel_x - 0.4,
                      base_y + max(t.get_value() / 7 * BAR_MAX, 0.01) / 2,
                      0])
        ))

        barra_y = always_redraw(lambda: Rectangle(
            width=BAR_W,
            height=max(k * t.get_value() / (k * 7) * BAR_MAX, 0.01),
            fill_color=cor_reta, fill_opacity=0.85, stroke_width=1
        ).move_to(
            np.array([painel_x + 0.4,
                      base_y + max(k * t.get_value() / (k * 7) * BAR_MAX, 0.01) / 2,
                      0])
        ))

        # Valores numéricos acima das barras
        val_x = always_redraw(lambda: MathTex(
            f"{t.get_value():.1f}\\ L", color=COR_BARRA_X, font_size=20
        ).next_to(barra_x.get_top(), UP, buff=0.1))

        val_y = always_redraw(lambda: MathTex(
            f"{k*t.get_value():.1f}\\ km", color=cor_reta, font_size=20
        ).next_to(barra_y.get_top(), UP, buff=0.1))

        # Razão em tempo real — acima do painel, sempre visível
        razao_pos = np.array([painel_x, base_y + BAR_MAX + 0.85, 0])
        razao_lbl = always_redraw(lambda: MathTex(
            r"\frac{" + f"{k*t.get_value():.1f}" + r"}{" +
            f"{t.get_value():.1f}" + r"} = " + f"{k:.0f}",
            color=COR_RAZAO, font_size=26
        ).move_to(razao_pos))

        self.add(barra_x, barra_y, val_x, val_y, razao_lbl)

        # ── Movimento com pausas ──────────────────────────────────────
        for (px, py) in pontos_pausa:
            self.play(t.animate.set_value(px), run_time=1.8, rate_func=linear)
            self.wait(0.4)

            # Coordenada acima do ponto — lado esquerdo, sem sobrepor reta
            coord = MathTex(f"({px},\\ {py})", color=COR_PONTO, font_size=20)
            coord.next_to(axes.c2p(px, py), UL, buff=0.18)
            self.play(Write(coord), run_time=0.6)
            self.wait(1.5)
            self.play(FadeOut(coord), run_time=0.4)

        self.wait(0.8)
        self.play(FadeOut(VGroup(
            tit, axes, lbl_x, lbl_y, reta, lbl_reta,
            ponto, barra_x, barra_y, val_x, val_y,
            razao_lbl, base_line, lbl_bx, lbl_by
        )), run_time=1.0)
        self.wait(0.3)
