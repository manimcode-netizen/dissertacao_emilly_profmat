"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Adição de inteiros na reta numérica — 3 + (−5) = −2
Nível    : Ensino Fundamental
Objetivo : Compreender adição com inteiros negativos visualizando
           o deslocamento na reta, com destaque ao cruzar o zero.
=======================================================================
RENDERIZAÇÃO:
  manim -pql reta_inteiros.py RetaInteiros
  manim -pqh reta_inteiros.py RetaInteiros
=======================================================================
"""

from manim import *
import numpy as np

# ── Paleta semântica ────────────────────────────────────────────────
COR_POSITIVO = BLUE       # números positivos
COR_NEGATIVO = RED        # números negativos
COR_ZERO     = YELLOW     # zero destacado
COR_PONTO    = WHITE      # ponto móvel
COR_SOMA     = GREEN      # resultado final
COR_TEXTO    = WHITE

ESCALA = 1.0  # espaçamento entre unidades na reta


class RetaInteiros(Scene):
    """
    Conceito : Adição de inteiros — 3 + (−5) = −2
    Nível    : Ensino Fundamental
    Objetivo : Visualizar deslocamento positivo e negativo na reta numérica,
               com destaque ao cruzar o zero.
    """

    def construct(self):

        # ── ETAPA 1: Reta numérica ───────────────────────────────────
        reta = NumberLine(
            x_range=[-6, 6, 1],
            length=12,
            include_numbers=False,   # desativa números automáticos
            color=GRAY,
            stroke_width=2,
        )
        reta.shift(DOWN * 0.5)

        # Números coloridos manualmente — sem sobreposição
        nums_pos = VGroup()
        nums_neg = VGroup()
        lbl_zero = MathTex("0", color=COR_ZERO, font_size=24)
        lbl_zero.next_to(reta.n2p(0), DOWN, buff=0.25)

        for i in range(1, 7):
            p = MathTex(str(i),  color=COR_POSITIVO, font_size=24).next_to(reta.n2p(i),  DOWN, buff=0.25)
            n = MathTex(str(-i), color=COR_NEGATIVO,  font_size=24).next_to(reta.n2p(-i), DOWN, buff=0.25)
            nums_pos.add(p)
            nums_neg.add(n)

        # Tick marks
        ticks = VGroup(*[
            Line(reta.n2p(i) + UP*0.1, reta.n2p(i) + DOWN*0.1, stroke_width=2, color=GRAY)
            for i in range(-6, 7)
        ])

        # Seta da reta
        seta_esq = Arrow(reta.n2p(-6), reta.n2p(-6) + LEFT*0.4, buff=0,
                         color=GRAY, stroke_width=2, max_tip_length_to_length_ratio=0.3)
        seta_dir = Arrow(reta.n2p(6),  reta.n2p(6)  + RIGHT*0.4, buff=0,
                         color=GRAY, stroke_width=2, max_tip_length_to_length_ratio=0.3)

        # Marcação do zero na reta
        marca_zero = Dot(reta.n2p(0), color=COR_ZERO, radius=0.07)

        self.play(
            Create(reta), Create(ticks),
            run_time=1.5
        )
        self.play(
            FadeIn(nums_pos), FadeIn(nums_neg), FadeIn(lbl_zero),
            FadeIn(marca_zero),
            run_time=0.8
        )
        self.wait(0.5)

        # ── ETAPA 2: Ponto inicial no zero ───────────────────────────
        ponto = Dot(reta.n2p(0), color=COR_PONTO, radius=0.16)
        self.play(GrowFromCenter(ponto), run_time=0.7)
        self.wait(1.0)

        # ── ETAPA 3: Deslocamento +3 para a direita ──────────────────
        txt_mais3 = MathTex("+3", color=COR_POSITIVO, font_size=42)
        txt_mais3.to_edge(UP, buff=0.5)
        self.play(Write(txt_mais3), run_time=0.8)
        self.wait(0.5)

        # Seta indicando direção → direita
        seta_dir3 = Arrow(
            reta.n2p(0) + UP*0.45,
            reta.n2p(3) + UP*0.45,
            color=COR_POSITIVO, buff=0,
            stroke_width=3, max_tip_length_to_length_ratio=0.12
        )
        lbl_3passos = MathTex("3\\ \\text{passos}", color=COR_POSITIVO, font_size=22)
        lbl_3passos.next_to(seta_dir3, UP, buff=0.12)

        self.play(GrowArrow(seta_dir3), Write(lbl_3passos), run_time=0.8)

        # Mover passo a passo sem contador visível
        for i in range(1, 4):
            self.play(
                ponto.animate.move_to(reta.n2p(i)),
                run_time=0.6
            )

        self.wait(1.5)
        self.play(
            FadeOut(seta_dir3), FadeOut(lbl_3passos),
            FadeOut(txt_mais3),
            run_time=0.5
        )

        # ── ETAPA 4: Deslocamento −5 para a esquerda ─────────────────
        txt_menos5 = MathTex("-5", color=COR_NEGATIVO, font_size=42)
        txt_menos5.to_edge(UP, buff=0.5)
        self.play(Write(txt_menos5), run_time=0.8)
        self.wait(0.5)

        seta_esq5 = Arrow(
            reta.n2p(3) + UP*0.45,
            reta.n2p(-2) + UP*0.45,
            color=COR_NEGATIVO, buff=0,
            stroke_width=3, max_tip_length_to_length_ratio=0.10
        )
        lbl_5passos = MathTex("5\\ \\text{passos}", color=COR_NEGATIVO, font_size=22)
        lbl_5passos.next_to(seta_esq5, UP, buff=0.12)

        self.play(GrowArrow(seta_esq5), Write(lbl_5passos), run_time=0.8)

        pos_atual = 3
        for i in range(1, 6):
            pos_atual -= 1
            self.play(
                ponto.animate.move_to(reta.n2p(pos_atual)),
                run_time=0.55
            )
            # ── Destaque ao cruzar o zero ────────────────────────────
            if pos_atual == 0:
                flash = Flash(reta.n2p(0), color=COR_ZERO, line_length=0.3, num_lines=10)
                marca_flash = Circle(radius=0.28, color=COR_ZERO, stroke_width=3)
                marca_flash.move_to(reta.n2p(0))
                self.play(
                    flash,
                    Create(marca_flash),
                    run_time=0.6
                )
                aviso = Text("Cruzou o zero!", color=COR_ZERO, font_size=24)
                aviso.next_to(reta.n2p(0), DOWN, buff=0.55)
                self.play(Write(aviso), run_time=0.5)
                self.wait(1.0)
                self.play(FadeOut(aviso), FadeOut(marca_flash), run_time=0.4)

        self.wait(1.5)
        self.play(
            FadeOut(seta_esq5), FadeOut(lbl_5passos),
            FadeOut(txt_menos5),
            run_time=0.5
        )

        # ── ETAPA 5: Resultado final ──────────────────────────────────
        resultado = MathTex(
            "3", "+", "(-5)", "=", "-2",
            font_size=48
        )
        resultado[0].set_color(COR_POSITIVO)
        resultado[1].set_color(COR_TEXTO)
        resultado[2].set_color(COR_NEGATIVO)
        resultado[3].set_color(COR_TEXTO)
        resultado[4].set_color(COR_SOMA)
        resultado.to_edge(UP, buff=0.4)

        # Destacar ponto final
        ponto.set_color(COR_SOMA)
        lbl_result = MathTex("-2", color=COR_SOMA, font_size=28)
        lbl_result.next_to(ponto, UP, buff=0.35)

        self.play(Write(resultado), run_time=1.5)
        self.play(GrowFromCenter(lbl_result), run_time=0.6)
        self.wait(3.0)
