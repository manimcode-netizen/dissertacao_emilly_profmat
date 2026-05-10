"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Porcentagem — invariância sob reescalonamento proporcional
Nível    : Ensino Fundamental / Médio
Objetivo : Compreender que a porcentagem é invariante quando o todo
           muda proporcionalmente: 25/100 = 50/200 = 20/80 = 25%
=======================================================================
RENDERIZAÇÃO:
  manim -pql porcentagem.py Porcentagem
  manim -pqh porcentagem.py Porcentagem
=======================================================================
"""

from manim import *
import numpy as np

# ── Paleta semântica ────────────────────────────────────────────────
COR_BARRA_BASE  = GRAY_D    # partes não destacadas
COR_DESTAQUE    = BLUE      # porção destacada (25%)
COR_RESULTADO   = GREEN     # porcentagem final
COR_TEXTO       = WHITE
COR_TITULO      = YELLOW


class Porcentagem(Scene):
    """
    Conceito : Porcentagem — 25/100 = 50/200 = 20/80 = 25%
    Nível    : Ensino Fundamental / Médio
    Objetivo : Mostrar que a porcentagem é invariante sob reescalonamento.
    """

    def construct(self):

        # ── Título ───────────────────────────────────────────────────
        titulo = Text("O que é Porcentagem?", color=COR_TITULO, font_size=36)
        self.play(Write(titulo), run_time=1.2)
        self.wait(1.0)
        self.play(titulo.animate.scale(0.6).to_edge(UP, buff=0.2), run_time=0.8)

        # ── Situação 1: 25 em 100 ────────────────────────────────────
        self._situacao(
            total=100, destacado=25,
            label_total="25 em 100",
            label_pct="= 25\\%",
            posicao=UP * 1.2
        )

        # ── Situação 2: 50 em 200 ────────────────────────────────────
        self._situacao(
            total=200, destacado=50,
            label_total="50 em 200",
            label_pct="= 25\\%",
            posicao=ORIGIN
        )

        # ── Situação 3: 20 em 80 ─────────────────────────────────────
        self._situacao(
            total=80, destacado=20,
            label_total="20 em 80",
            label_pct="= 25\\%",
            posicao=DOWN * 1.2
        )

        # ── Conclusão ────────────────────────────────────────────────
        concl = MathTex(
            r"\frac{25}{100} = \frac{50}{200} = \frac{20}{80} = 25\%",
            font_size=36, color=COR_RESULTADO
        )
        concl.to_edge(DOWN, buff=0.5)
        box = SurroundingRectangle(concl, color=COR_RESULTADO, buff=0.18, corner_radius=0.10)
        self.play(Write(concl), Create(box), run_time=1.5)
        self.wait(3.5)

    # ── Helper: desenha uma barra e anima a situação ─────────────────
    def _situacao(self, total, destacado, label_total, label_pct, posicao):
        """Cria barra de 'total' partes com 'destacado' em azul."""

        BAR_W   = 9.0
        BAR_H   = 0.48
        n       = total              # número real de células
        cell_w  = BAR_W / n
        proporcao = destacado / total
        n_dest = round(proporcao * n)

        # Construir células
        cells = VGroup()
        for i in range(n):
            cor = COR_DESTAQUE if i < n_dest else COR_BARRA_BASE
            cell = Rectangle(
                width=cell_w - 0.01,
                height=BAR_H,
                fill_color=cor,
                fill_opacity=0.85,
                stroke_width=0.3,
                stroke_color=GRAY
            )
            cell.move_to(LEFT * (BAR_W/2) + RIGHT * (i * cell_w + cell_w/2))
            cells.add(cell)

        barra = VGroup(cells)
        barra.move_to(posicao)

        # Textos
        txt_frac = Text(label_total, color=COR_TEXTO, font_size=24)
        txt_frac.next_to(barra, DOWN, buff=0.15)

        txt_pct = MathTex(label_pct, color=COR_RESULTADO, font_size=28)
        txt_pct.next_to(txt_frac, RIGHT, buff=0.25)

        # Barra cinza primeiro, depois destaque
        cells_base = VGroup(*[c for c in cells if c.get_fill_color() != COR_DESTAQUE])
        cells_dest = VGroup(*cells[:n_dest])

        # Animar: barra base
        self.play(
            *[FadeIn(c, run_time=0.6) for c in cells[n_dest:]],
            run_time=0.8
        )
        # Animar: destaque
        self.play(
            *[FadeIn(c, run_time=0.4) for c in cells[:n_dest]],
            run_time=0.6
        )
        # Textos
        self.play(Write(txt_frac), run_time=0.7)
        self.play(Write(txt_pct),  run_time=0.7)
        self.wait(1.5)
