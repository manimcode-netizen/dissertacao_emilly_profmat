"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D35 – Sistema de Equações do 1º Grau
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Uso       : Dissertação de Mestrado Profissional em Matemática
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT (coordenadas Manim: centro=0,0 | tela: x[-7,7] y[-4,4])
  Faixa SAEB  : y ∈ [3.0, 4.0]   → nunca sobrepor
  Título cena : y = 2.55
  Linha sep   : y = 2.10
  Conteúdo    : y ∈ [-2.6, 1.85]
  Resposta    : y = -3.40
=======================================================================
PALETA SEMÂNTICA
  YELLOW  → títulos e cabeçalhos
  BLUE_D  → primeira equação / reta 1
  RED_B   → segunda equação / reta 2
  GREEN_B → solução / ponto de interseção
  ORANGE  → destaque temporário
  WHITE   → textos explicativos e rótulos gerais
=======================================================================
RENDERIZAÇÃO:
  manim -pql d35_v2.py D35
  manim -pqh d35_v2.py D35
=======================================================================
"""

from manim import *
import numpy as np

# ── Constantes de layout ────────────────────────────────────────────
Y_FAIXA_CY  =  3.50
Y_TITULO    =  2.55
Y_LINHA_SEP =  2.10
Y_RESPOSTA  = -3.40


# ── Helper: cabeçalho padrão ────────────────────────────────────────
def cabecalho(scene, texto_titulo):
    """Faixa SAEB fixa + título da cena + linha separadora."""
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
# CLASSE MESTRE — todas as cenas em ordem
# =======================================================================
class D35(Scene):
    """
    Classe mestre do Descritor D35.
    Conceito : Sistema de Equações do 1º Grau
    Nível    : Ensino Fundamental – 9º Ano
    Objetivo : Resolver sistemas de equações e interpretar geometricamente
               os três casos: secantes, coincidentes e paralelas.
    """

    def construct(self):
        self._abertura()
        self._fase1_introducao()
        self._fase2_equacao_vira_reta()
        self._fase3_tres_casos()
        self._fase4_inferencia_exemplo()
        self._fase5_formalizacao()
        self._encerramento()
        self._logo_emilly_mayre()

    # ===================================================================
    # ABERTURA — padrão D29
    # ===================================================================
    def _abertura(self):
        """Contextualização do Descritor D35 – SAEB."""
        faixa = Rectangle(
            width=14.4, height=1.05,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        titulo = Text("Descritor D35", color=YELLOW, font_size=52, weight=BOLD)
        titulo.move_to(np.array([0, 1.4, 0]))
        subtitulo = Text(
            "Sistema de Equações do 1º Grau",
            color=WHITE, font_size=28
        ).next_to(titulo, DOWN, buff=0.45)

        self.play(Write(titulo), run_time=1.6)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtitulo)), run_time=0.9)
        self.wait(0.2)

        linha = Line(
            np.array([-5.5, 1.5, 0]), np.array([5.5, 1.5, 0]),
            color=YELLOW, stroke_width=1.5
        )
        self.play(Create(linha), run_time=0.7)

        topicos = VGroup(
            Text("1. O que é um sistema de equações?",         color=WHITE, font_size=24),
            Text("2. Cada equação define uma reta no plano",   color=WHITE, font_size=24),
            Text("3. Os 3 casos geométricos do sistema",       color=WHITE, font_size=24),
            Text("4. Identificando a solução geometricamente", color=WHITE, font_size=24),
            Text("5. Método de substituição — resolução",      color=WHITE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        topicos.next_to(linha, DOWN, buff=0.28)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        dots = VGroup()
        for t in topicos:
            dot = Dot(color=ORANGE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.48)

        self.wait(2.5)
        self.play(FadeOut(VGroup(faixa, inst, linha, topicos, dots)), run_time=1.0)

    # ===================================================================
    # FASE 1 — O que é um sistema?
    # ===================================================================
    def _fase1_introducao(self):
        """Apresentação do sistema com representação algébrica."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Sistema de Equações")

        ctx = Text(
            "Quais valores de x e y satisfazem as DUAS equações simultaneamente?",
            color=WHITE, font_size=22
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        sistema = MathTex(
            r"\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}",
            font_size=56, color=WHITE
        ).move_to(np.array([0, 0.3, 0]))
        self.play(Write(sistema), run_time=2.5)
        self.wait(1.0)

        eq1_label = MathTex(r"\text{Equação I}", font_size=24, color=BLUE_D)
        eq2_label = MathTex(r"\text{Equação II}", font_size=24, color=RED_B)
        eq1_label.next_to(sistema, RIGHT, buff=0.5).shift(UP * 0.5)
        eq2_label.next_to(sistema, RIGHT, buff=0.5).shift(DOWN * 0.5)

        self.play(FadeIn(eq1_label), FadeIn(eq2_label), run_time=1.0)
        self.wait(1.0)

        regra = Text("Solução: par (x, y) que satisfaz as duas equações ao mesmo tempo.",
                     font_size=21, color=GREEN_B)
        regra.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_r = SurroundingRectangle(regra, color=GREEN_B, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(regra), Create(box_r), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            sistema, eq1_label, eq2_label, regra, box_r
        )), run_time=1.0)

    # ===================================================================
    # FASE 2 — Cada equação define uma reta
    # ===================================================================
    def _fase2_equacao_vira_reta(self):
        """Representação geométrica: cada equação é uma reta no plano."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Equação → Reta no Plano")

        ctx = Text(
            "Cada equação do sistema corresponde a uma reta no plano cartesiano.",
            color=WHITE, font_size=22
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        # Equações algébricas em quadro — esquerda
        eq1 = MathTex(r"x + y = 5", font_size=42, color=BLUE_D)
        eq2 = MathTex(r"x - y = 1", font_size=42, color=RED_B)
        alg = VGroup(eq1, eq2).arrange(DOWN, buff=0.7)
        alg.move_to(np.array([-4.0, 0.0, 0]))
        box_alg = SurroundingRectangle(alg, color=GRAY, buff=0.35, corner_radius=0.14)
        self.play(Write(eq1), run_time=1.5)
        self.play(Write(eq2), run_time=1.5)
        self.play(Create(box_alg), run_time=0.7)
        self.wait(0.5)

        seta = Arrow(LEFT * 0.6, RIGHT * 0.6, color=YELLOW, buff=0, stroke_width=3)
        seta.move_to(np.array([-1.2, 0.0, 0]))
        lbl_seta = Text("representa", font_size=18, color=YELLOW)
        lbl_seta.next_to(seta, UP, buff=0.10)
        self.play(GrowArrow(seta), FadeIn(lbl_seta), run_time=1.0)

        # Plano cartesiano — direita, fonte maior
        axes = Axes(
            x_range=[-1, 6, 1], y_range=[-1, 6, 1],
            x_length=4.0, y_length=4.0,
            axis_config={"color": GRAY, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 22},
            tips=True,
        )
        axes.move_to(np.array([3.4, -0.2, 0]))
        x_lbl = axes.get_x_axis_label(MathTex("x", font_size=28))
        y_lbl = axes.get_y_axis_label(MathTex("y", font_size=28))

        reta1 = axes.plot(lambda x: 5 - x, x_range=[-0.2, 5.2], color=BLUE_D, stroke_width=2.8)
        reta2 = axes.plot(lambda x: x - 1, x_range=[-0.2, 5.2], color=RED_B,  stroke_width=2.8)
        # lbl_r1 à direita da reta azul, sem sobrepor eixo y
        lbl_r1 = MathTex(r"y=5-x", font_size=22, color=BLUE_D)
        lbl_r1.next_to(axes.c2p(2.0, 3.0), RIGHT, buff=0.12)
        lbl_r2 = MathTex(r"y=x-1", font_size=22, color=RED_B).next_to(axes.c2p(4.5, 3.5), RIGHT, buff=0.08)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=1.8)
        self.play(Create(reta1), Write(lbl_r1), run_time=1.5)
        self.play(Create(reta2), Write(lbl_r2), run_time=1.5)

        dot = Dot(axes.c2p(3, 2), color=GREEN_B, radius=0.13)
        # Par ordenado à esquerda do ponto, sem tocar a reta azul
        dot_lbl = MathTex(r"(3,\,2)", font_size=24, color=GREEN_B)
        dot_lbl.next_to(dot, LEFT, buff=0.22)
        self.play(FadeIn(dot), Write(dot_lbl), run_time=1.2)

        regra = Text("O ponto de interseção é a solução do sistema.",
                     font_size=21, color=GREEN_B)
        regra.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_r = SurroundingRectangle(regra, color=GREEN_B, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(regra), Create(box_r), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            alg, box_alg, seta, lbl_seta,
            axes, x_lbl, y_lbl, reta1, reta2,
            lbl_r1, lbl_r2, dot, dot_lbl, regra, box_r
        )), run_time=1.0)

    # ===================================================================
    # FASE 3 — Os 3 casos geométricos
    # ===================================================================
    def _fase3_tres_casos(self):
        """Os três casos: secantes, coincidentes e paralelas."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Os 3 Casos do Sistema")

        ctx = Text(
            "A posição relativa das retas determina o número de soluções.",
            color=WHITE, font_size=22
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        def mini_axes():
            return Axes(
                x_range=[-3, 3, 1], y_range=[-2, 4, 1],
                x_length=3.6, y_length=3.0,
                axis_config={"color": GRAY, "stroke_width": 1, "include_ticks": False},
                tips=False,
            )

        ax1 = mini_axes().shift(LEFT * 4.2 + DOWN * 0.3)
        ax2 = mini_axes().shift(ORIGIN   + DOWN * 0.3)
        ax3 = mini_axes().shift(RIGHT * 4.2 + DOWN * 0.3)

        # Caso 1: secantes
        r1a = ax1.plot(lambda x:  x + 1, x_range=[-2.5, 2.5], color=BLUE_D, stroke_width=2.5)
        r1b = ax1.plot(lambda x: -x + 1, x_range=[-2.5, 2.5], color=RED_B,  stroke_width=2.5)
        pt1 = Dot(ax1.c2p(0, 1), color=GREEN_B, radius=0.12)
        lbl1  = MathTex(r"\text{Retas secantes}", font_size=24, color=GREEN_B).next_to(ax1, UP, buff=0.12)
        desc1 = Text("1 solução", font_size=20, color=GREEN_B).next_to(ax1, DOWN, buff=0.22)

        # Caso 2: coincidentes
        r2a = ax2.plot(lambda x: x + 0.5, x_range=[-2.5, 2.5], color=BLUE_D, stroke_width=4)
        r2b = ax2.plot(lambda x: x + 0.5, x_range=[-2.5, 2.5], color=RED_B,  stroke_width=2, stroke_opacity=0.5)
        lbl2  = MathTex(r"\text{Retas coincidentes}", font_size=24, color=YELLOW).next_to(ax2, UP, buff=0.12)
        desc2 = Text("∞ soluções", font_size=20, color=YELLOW).next_to(ax2, DOWN, buff=0.22)

        # Caso 3: paralelas
        r3a = ax3.plot(lambda x: x + 1.5, x_range=[-2.5, 2.5], color=BLUE_D, stroke_width=2.5)
        r3b = ax3.plot(lambda x: x - 1.5, x_range=[-2.5, 2.5], color=RED_B,  stroke_width=2.5)
        lbl3  = MathTex(r"\text{Retas paralelas}", font_size=24, color=RED_B).next_to(ax3, UP, buff=0.12)
        # desc3 deslocado à direita para não ficar sobre a reta vermelha
        desc3 = Text("sem solução  ∅", font_size=20, color=RED_B)
        desc3.next_to(ax3, DOWN, buff=0.22).shift(RIGHT * 0.6)

        self.play(Create(ax1), Create(r1a), Create(r1b), run_time=1.5)
        self.play(FadeIn(pt1), Write(lbl1), Write(desc1), run_time=1.2)
        self.wait(0.6)

        self.play(Create(ax2), Create(r2a), Create(r2b), run_time=1.5)
        self.play(Write(lbl2), Write(desc2), run_time=1.2)
        self.wait(0.6)

        self.play(Create(ax3), Create(r3a), Create(r3b), run_time=1.5)
        self.play(Write(lbl3), Write(desc3), run_time=1.2)
        self.wait(2.0)

        regra = MathTex(
            r"\text{Secantes} \Rightarrow 1 \text{ sol.} \quad "
            r"\text{Coincidentes} \Rightarrow \infty \quad "
            r"\text{Paralelas} \Rightarrow \emptyset",
            font_size=24, color=YELLOW
        )
        regra.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_r = SurroundingRectangle(regra, color=YELLOW, buff=0.14, corner_radius=0.10)
        self.play(Write(regra), Create(box_r), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            ax1, r1a, r1b, pt1, lbl1, desc1,
            ax2, r2a, r2b, lbl2, desc2,
            ax3, r3a, r3b, lbl3, desc3,
            regra, box_r
        )), run_time=1.2)

    # ===================================================================
    # FASE 4 — Identificando a solução graficamente
    # ===================================================================
    def _fase4_inferencia_exemplo(self):
        """Localizar a solução geometricamente com linhas tracejadas."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Solução — Geometria + Álgebra")

        sistema = MathTex(
            r"\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}",
            font_size=40, color=WHITE
        ).move_to(np.array([-3.8, 0.8, 0]))
        self.play(Write(sistema), run_time=2.0)
        self.wait(0.8)

        iso1 = MathTex(r"y = 5 - x", font_size=30, color=BLUE_D)
        iso2 = MathTex(r"y = x - 1", font_size=30, color=RED_B)
        iso = VGroup(iso1, iso2).arrange(DOWN, buff=0.5)
        iso.next_to(sistema, DOWN, buff=0.5)
        self.play(Write(iso1), run_time=1.2)
        self.play(Write(iso2), run_time=1.2)
        self.wait(0.6)

        axes = Axes(
            x_range=[-0.5, 6, 1], y_range=[-0.5, 6, 1],
            x_length=4.2, y_length=4.2,
            axis_config={"color": GRAY, "stroke_width": 1.5,
                         "include_numbers": True, "font_size": 20},
            tips=True,
        )
        axes.move_to(np.array([3.2, -0.4, 0]))
        x_lbl = axes.get_x_axis_label(MathTex("x", font_size=26))
        y_lbl = axes.get_y_axis_label(MathTex("y", font_size=26))

        reta1 = axes.plot(lambda x: 5 - x, x_range=[0, 5.2], color=BLUE_D, stroke_width=2.8)
        reta2 = axes.plot(lambda x: x - 1, x_range=[0.5, 5.2], color=RED_B, stroke_width=2.8)
        # lbl_r1 à direita da reta azul, mais acima para não sobrepor S
        lbl_r1 = MathTex(r"y=5-x", font_size=22, color=BLUE_D)
        lbl_r1.next_to(axes.c2p(1.2, 3.8), RIGHT, buff=0.12)
        lbl_r2 = MathTex(r"y=x-1", font_size=22, color=RED_B).next_to(axes.c2p(4.5, 3.5), RIGHT, buff=0.08)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), run_time=1.8)
        self.play(Create(reta1), Write(lbl_r1), run_time=1.5)
        self.play(Create(reta2), Write(lbl_r2), run_time=1.5)

        dash_h = DashedLine(axes.c2p(0, 2), axes.c2p(3, 2), color=YELLOW, stroke_width=1.5, dash_length=0.15)
        dash_v = DashedLine(axes.c2p(3, 0), axes.c2p(3, 2), color=YELLOW, stroke_width=1.5, dash_length=0.15)
        self.play(Create(dash_h), Create(dash_v), run_time=1.5)

        dot = Dot(axes.c2p(3, 2), color=GREEN_B, radius=0.14)
        # S=(3,2) bem acima do ponto
        dot_lbl = MathTex(r"S=(3,\,2)", font_size=24, color=GREEN_B)
        dot_lbl.next_to(dot, UP, buff=0.38)
        self.play(FadeIn(dot), Write(dot_lbl), run_time=1.2)

        regra = Text("A solução é o ponto de interseção das retas.", font_size=21, color=GREEN_B)
        regra.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_r = SurroundingRectangle(regra, color=GREEN_B, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(regra), Create(box_r), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            sistema, iso,
            axes, x_lbl, y_lbl, reta1, reta2,
            lbl_r1, lbl_r2, dash_h, dash_v,
            dot, dot_lbl, regra, box_r
        )), run_time=1.2)

    # ===================================================================
    # FASE 5 — Método de substituição
    # ===================================================================
    def _fase5_formalizacao(self):
        """Resolução algébrica pelo método de substituição."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Método de Substituição")

        sistema = MathTex(
            r"\begin{cases} x + y = 5 \quad (I)\\ x - y = 1 \quad (II)\end{cases}",
            font_size=34, color=WHITE
        ).move_to(np.array([-3.4, 1.3, 0]))
        self.play(Write(sistema), run_time=2.0)
        self.wait(0.5)

        sep = Line(np.array([-0.8, 1.8, 0]), np.array([-0.8, -3.0, 0]), color=GRAY, stroke_width=1)
        self.play(Create(sep), run_time=0.5)

        passos = VGroup(
            MathTex(r"\text{De (I):} \quad x = 5 - y",                          font_size=26, color=BLUE_D),
            MathTex(r"\text{Sub. em (II):} \quad (5-y) - y = 1",                font_size=24, color=WHITE),
            MathTex(r"5 - 2y = 1 \;\Rightarrow\; y = 2",                        font_size=26, color=RED_B),
            MathTex(r"x = 5 - 2 = 3",                                            font_size=26, color=BLUE_D),
        ).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        passos.next_to(sistema, DOWN, buff=0.45)
        passos.align_to(sistema, LEFT)

        for p in passos:
            self.play(Write(p), run_time=1.6)
            self.wait(0.5)

        solucao = MathTex(r"S = \{(3,\; 2)\}", font_size=36, color=GREEN_B)
        box_sol = SurroundingRectangle(solucao, color=GREEN_B, buff=0.22, corner_radius=0.15)
        solucao.next_to(passos, DOWN, buff=0.45).align_to(passos, LEFT)
        box_sol = SurroundingRectangle(solucao, color=GREEN_B, buff=0.22, corner_radius=0.15)
        self.play(Write(solucao), Create(box_sol), run_time=1.5)
        self.wait(0.8)

        # Mini gráfico de verificação — direita, menor e mais baixo
        axes = Axes(
            x_range=[-0.5, 5.5, 1], y_range=[-0.5, 5.5, 1],
            x_length=3.8, y_length=3.8,
            axis_config={"color": GRAY, "stroke_width": 1,
                         "include_numbers": True, "font_size": 18},
            tips=True,
        )
        axes.move_to(np.array([3.6, -0.6, 0]))
        reta1 = axes.plot(lambda x: 5 - x, x_range=[0, 5.2], color=BLUE_D, stroke_width=2.5)
        reta2 = axes.plot(lambda x: x - 1, x_range=[0.8, 5.2], color=RED_B,  stroke_width=2.5)
        dot = Dot(axes.c2p(3, 2), color=GREEN_B, radius=0.14)
        dot_lbl = MathTex(r"(3,2)", font_size=22, color=GREEN_B)
        dot_lbl.next_to(dot, UP, buff=0.22)
        verif = Text("Verificação geométrica", font_size=19, color=GRAY).next_to(axes, UP, buff=0.15)

        self.play(Create(axes), Write(verif), run_time=1.2)
        self.play(Create(reta1), Create(reta2), run_time=1.8)
        self.play(FadeIn(dot), Write(dot_lbl), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            sistema, sep, passos, solucao, box_sol,
            axes, reta1, reta2, dot, dot_lbl, verif
        )), run_time=1.2)

    # ===================================================================
    # ENCERRAMENTO — padrão D29
    # ===================================================================
    def _encerramento(self):
        """Síntese visual do Descritor D35."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese — Descritor D35")

        descritivo = Text(
            "D35 – Resolver sistema de equações do 1º grau",
            color=WHITE, font_size=24
        ).move_to(np.array([0, 0.5, 0]))
        box_desc = SurroundingRectangle(descritivo, color=YELLOW, buff=0.18, corner_radius=0.10)
        self.play(FadeIn(descritivo), Create(box_desc), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(descritivo), FadeOut(box_desc), run_time=0.7)

        form_tit = Text("Resumo:", color=YELLOW, font_size=24, weight=BOLD)
        form_tit.move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(form_tit), run_time=0.6)

        resumo = VGroup(
            Text("Sistema: duas equações com duas incógnitas (x e y)",  color=BLUE_D,  font_size=22),
            Text("Geometria: cada equação representa uma reta",          color=WHITE,   font_size=22),
            Text("Retas secantes  →  1 solução",                        color=GREEN_B, font_size=22),
            Text("Retas coincidentes  →  infinitas soluções",           color=YELLOW,  font_size=22),
            Text("Retas paralelas  →  sem solução  ∅",                  color=RED_B,   font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.27)
        resumo.next_to(form_tit, DOWN, buff=0.30)

        cores_dots = [BLUE_D, WHITE, GREEN_B, YELLOW, RED_B]
        dots = VGroup()
        for i, item in enumerate(resumo):
            dot = Dot(color=cores_dots[i], radius=0.07).next_to(item, LEFT, buff=0.14)
            dots.add(dot)
            self.play(FadeIn(dot), FadeIn(item, shift=RIGHT * 0.1), run_time=0.52)

        self.wait(2.0)
        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            form_tit, resumo, dots
        )), run_time=1.2)

    # ===================================================================
    # LOGO — padrão D29
    # ===================================================================
    def _logo_emilly_mayre(self):
        """Identidade visual da Prof.ª Emilly Mayre."""
        ESCURO_L = "#1a1a2e"
        DOURADO  = "#C8A84B"
        CINZA_L  = "#888899"

        bg = Rectangle(
            width=16, height=9,
            fill_color=WHITE, fill_opacity=1, stroke_width=0
        )
        self.add(bg)

        a = 1.9

        def inf_h(t):
            d = 1 + np.sin(t) ** 2
            return np.array([a * np.cos(t) / d, a * np.sin(t) * np.cos(t) / d, 0])

        def inf_v(t):
            d = 1 + np.sin(t) ** 2
            return np.array([a * np.sin(t) * np.cos(t) / d, a * np.cos(t) / d, 0])

        logo_h = ParametricFunction(inf_h, t_range=[0, TAU], color="#3a3a5c", stroke_width=2.5).move_to(UP * 0.5)
        logo_v = ParametricFunction(inf_v, t_range=[0, TAU], color="#9999bb", stroke_width=2.5).move_to(UP * 0.5)

        circ = Circle(radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
                      color=ESCURO_L, stroke_width=0).move_to(UP * 0.5)
        em = Text("EM", color=WHITE, font_size=22, weight=BOLD).move_to(circ.get_center())

        grp  = VGroup(logo_h, logo_v)
        nome = Text("Emilly Mayre", color=ESCURO_L, font_size=28, weight=BOLD)
        nome.next_to(grp, DOWN, buff=0.55)
        linha = Line(LEFT * 1.6, RIGHT * 1.6, color=DOURADO, stroke_width=3.5)
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
        self.play(FadeIn(nome, shift=UP * 0.15), run_time=0.8)
        self.play(Create(linha), run_time=0.5)
        self.play(FadeIn(cargo), run_time=0.6)
        self.wait(0.4)
        simbolo = VGroup(logo_h, logo_v, circ, em)
        self.play(simbolo.animate.scale(1.06), run_time=0.4)
        self.play(simbolo.animate.scale(1 / 1.06), run_time=0.35)
        self.wait(3.5)
