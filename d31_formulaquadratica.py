"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D31 – Equação do 2º Grau
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
  BLUE_D  → equação / objeto principal
  RED_B   → discriminante / operação
  GREEN_B → raízes / resultado / confirmação
  ORANGE  → destaque temporário
  WHITE   → textos explicativos e rótulos gerais
=======================================================================
RENDERIZAÇÃO:
  manim -pql d31_v2.py D31
  manim -pqh d31_v2.py D31
=======================================================================
"""

from manim import *
import numpy as np

# ── Constantes de layout ────────────────────────────────────────────
Y_FAIXA_CY  =  3.50
Y_TITULO    =  2.55
Y_LINHA_SEP =  2.10
Y_CONTEUDO  =  0.50
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
class D31(Scene):
    """
    Classe mestre do Descritor D31.
    Conceito : Equação do 2º Grau — forma geral, discriminante e Bhaskara
    Nível    : Ensino Fundamental – 9º Ano
    Objetivo : Identificar e resolver equações do 2º grau usando Bhaskara
               e interpretar os casos do discriminante.
    """

    def construct(self):
        self._abertura()
        self._fase1_introducao()
        self._fase2_parabola_raizes()
        self._fase3_delta_casos()
        self._fase4_inferencia_exemplo()
        self._fase5_bhaskara()
        self._encerramento()
        self._logo_emilly_mayre()

    # ===================================================================
    # ABERTURA — padrão D29
    # ===================================================================
    def _abertura(self):
        """Contextualização do Descritor D31 – SAEB."""
        faixa = Rectangle(
            width=14.4, height=1.05,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        titulo = Text("Descritor D31", color=YELLOW, font_size=52, weight=BOLD)
        titulo.move_to(np.array([0, 1.4, 0]))
        subtitulo = Text(
            "Equação do 2º Grau",
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
            Text("1. Forma geral da equação do 2º grau",   color=WHITE, font_size=24),
            Text("2. Parábola e raízes no plano",           color=WHITE, font_size=24),
            Text("3. O discriminante — os 3 casos do Δ",   color=WHITE, font_size=24),
            Text("4. Exemplo: calcular Δ e prever raízes",  color=WHITE, font_size=24),
            Text("5. Fórmula Quadrática — resolução",     color=WHITE, font_size=24),
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
    # FASE 1 — Forma geral
    # ===================================================================
    def _fase1_introducao(self):
        """Forma geral ax² + bx + c = 0 e identificação dos coeficientes."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Equação do 2º Grau")

        ctx = Text(
            "Como encontrar os valores de x que satisfazem a equação?",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        # Equação centralizada — cada coeficiente como submobject separado
        forma_geral = MathTex(
            r"a", r"x^2", r"+", r"b", r"x", r"+", r"c", r"=", r"0",
            font_size=56, color=BLUE_D
        ).move_to(np.array([0, 0.4, 0]))
        self.play(Write(forma_geral), run_time=2.5)
        self.wait(1.0)

        # Índices: a=0, b=3, c=6
        idx_a, idx_b, idx_c = 0, 3, 6

        # Centro x de cada letra na equação
        x_a = forma_geral[idx_a].get_center()[0]
        x_b = forma_geral[idx_b].get_center()[0]
        x_c = forma_geral[idx_c].get_center()[0]
        base_y = forma_geral.get_bottom()[1]
        topo_y = forma_geral.get_top()[1]

        # Seta para CIMA do "a" → a ≠ 0
        seta_cima = Arrow(
            np.array([x_a, topo_y + 0.05, 0]),
            np.array([x_a, topo_y + 0.85, 0]),
            color=YELLOW, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )
        label_neq = MathTex(r"a \neq 0", font_size=24, color=YELLOW)
        label_neq.next_to(seta_cima, RIGHT, buff=0.15)
        self.play(GrowArrow(seta_cima), FadeIn(label_neq), run_time=1.0)
        self.wait(0.6)

        # ── Coeficiente a ──────────────────────────────────────────
        lbl_a_color = forma_geral[idx_a].copy().set_color(YELLOW)
        seta_a = Arrow(
            np.array([x_a, base_y - 0.05, 0]),
            np.array([x_a, base_y - 0.80, 0]),
            color=YELLOW, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )
        txt_a = Text("coef. quadrático", font_size=19, color=YELLOW)
        txt_a.move_to(np.array([x_a, base_y - 1.18, 0]))

        self.play(
            forma_geral[idx_a].animate.set_color(YELLOW),
            GrowArrow(seta_a), FadeIn(txt_a), run_time=0.9
        )
        self.wait(1.0)

        # ── Coeficiente b (oculta a) ───────────────────────────────
        self.play(
            FadeOut(seta_a), FadeOut(txt_a),
            forma_geral[idx_a].animate.set_color(BLUE_D),
            run_time=0.5
        )
        seta_b = Arrow(
            np.array([x_b, base_y - 0.05, 0]),
            np.array([x_b, base_y - 0.80, 0]),
            color=RED_B, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )
        txt_b = Text("coef. linear", font_size=19, color=RED_B)
        txt_b.move_to(np.array([x_b, base_y - 1.18, 0]))

        self.play(
            forma_geral[idx_b].animate.set_color(RED_B),
            GrowArrow(seta_b), FadeIn(txt_b), run_time=0.9
        )
        self.wait(1.0)

        # ── Coeficiente c (oculta b) ───────────────────────────────
        self.play(
            FadeOut(seta_b), FadeOut(txt_b),
            forma_geral[idx_b].animate.set_color(BLUE_D),
            run_time=0.5
        )
        seta_c = Arrow(
            np.array([x_c, base_y - 0.05, 0]),
            np.array([x_c, base_y - 0.80, 0]),
            color=GREEN_B, buff=0, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )
        txt_c = Text("termo independente", font_size=19, color=GREEN_B)
        txt_c.move_to(np.array([x_c, base_y - 1.18, 0]))

        self.play(
            forma_geral[idx_c].animate.set_color(GREEN_B),
            GrowArrow(seta_c), FadeIn(txt_c), run_time=0.9
        )
        self.wait(1.8)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            forma_geral, seta_cima, label_neq,
            seta_c, txt_c
        )), run_time=1.2)

    # ===================================================================
    # FASE 2 — Parábola e raízes
    # ===================================================================
    def _fase2_parabola_raizes(self):
        """Parábola no plano cartesiano; raízes como zeros da função."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Parábola e Raízes")

        ctx = Text(
            "As raízes são os valores de x onde a parábola corta o eixo x.",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        axes = Axes(
            x_range=[-1, 4, 1], y_range=[-1.5, 4, 1],
            x_length=6.5, y_length=4.5,
            axis_config={"color": GRAY, "stroke_width": 1.5},
            tips=True,
        )
        x_label = axes.get_x_axis_label(MathTex("x", font_size=26))
        y_label = axes.get_y_axis_label(MathTex("f(x)", font_size=26))
        axes_group = VGroup(axes, x_label, y_label)
        axes_group.move_to(np.array([0, -0.9, 0]))   # descido

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=2)

        def f(x): return x**2 - 3*x + 2

        parabola = axes.plot(f, x_range=[-0.3, 3.3], color=BLUE_D, stroke_width=3)
        label_eq = MathTex(r"f(x)=x^2-3x+2", font_size=32, color=BLUE_D)  # maior
        label_eq.move_to(np.array([3.8, 1.4, 0]))
        box_eq = SurroundingRectangle(label_eq, color=BLUE_D, buff=0.18, corner_radius=0.12)

        self.play(Create(parabola), Write(label_eq), run_time=2.5)
        self.play(Create(box_eq), run_time=0.7)
        self.wait(1)

        dot1 = Dot(axes.c2p(1, 0), color=GREEN_B, radius=0.12)
        dot2 = Dot(axes.c2p(2, 0), color=GREEN_B, radius=0.12)
        lbl1 = MathTex(r"x_1=1", font_size=24, color=GREEN_B).next_to(dot1, DL, buff=0.15)
        lbl2 = MathTex(r"x_2=2", font_size=24, color=GREEN_B).next_to(dot2, DR, buff=0.15)

        self.play(FadeIn(dot1), FadeIn(dot2), run_time=1.2)
        self.play(Write(lbl1), Write(lbl2), run_time=1.5)

        regra = Text("Raízes: onde f(x) = 0", font_size=22, color=GREEN_B)
        regra.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_r = SurroundingRectangle(regra, color=GREEN_B, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(regra), Create(box_r), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            axes_group, parabola, label_eq, box_eq,
            dot1, dot2, lbl1, lbl2, regra, box_r
        )), run_time=1.2)

    # ===================================================================
    # FASE 3 — Os 3 casos do Δ
    # ===================================================================
    def _fase3_delta_casos(self):
        """Discriminante Δ = b² − 4ac e seus três casos."""
        faixa, inst, cab, linha_sep = cabecalho(self, "O Discriminante — Δ")

        ctx = Text(
            "O valor de Δ determina quantas raízes reais a equação possui.",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        def make_axes():
            return Axes(
                x_range=[-2.5, 2.5, 1], y_range=[-1.5, 4, 1],
                x_length=3.6, y_length=3.0,
                axis_config={"color": GRAY, "stroke_width": 1, "include_ticks": False},
                tips=False,
            )

        ax1 = make_axes().shift(LEFT * 4.2 + DOWN * 0.6)
        ax2 = make_axes().shift(ORIGIN   + DOWN * 0.6)
        ax3 = make_axes().shift(RIGHT * 4.2 + DOWN * 0.6)

        p1  = ax1.plot(lambda x: x**2 - 1, x_range=[-1.8, 1.8], color=BLUE_D, stroke_width=2.5)
        d1  = VGroup(
            Dot(ax1.c2p(-1, 0), color=GREEN_B, radius=0.1),
            Dot(ax1.c2p( 1, 0), color=GREEN_B, radius=0.1),
        )
        lbl_d1 = MathTex(r"\Delta > 0", font_size=26, color=GREEN_B).next_to(ax1, UP, buff=0.12)
        desc1  = Text("2 raízes reais", font_size=17, color=GREEN_B).next_to(ax1, DOWN, buff=0.18)

        p2  = ax2.plot(lambda x: x**2, x_range=[-1.8, 1.8], color=BLUE_D, stroke_width=2.5)
        d2  = Dot(ax2.c2p(0, 0), color=YELLOW, radius=0.13)
        lbl_d2 = MathTex(r"\Delta = 0", font_size=26, color=YELLOW).next_to(ax2, UP, buff=0.12)
        desc2  = Text("1 raiz real (dupla)", font_size=17, color=YELLOW).next_to(ax2, DOWN, buff=0.18)

        p3  = ax3.plot(lambda x: x**2 + 0.8, x_range=[-1.8, 1.8], color=BLUE_D, stroke_width=2.5)
        lbl_d3   = MathTex(r"\Delta < 0", font_size=26, color=RED_B).next_to(ax3, UP, buff=0.12)
        desc3    = Text("sem raízes reais", font_size=17, color=RED_B).next_to(ax3, DOWN, buff=0.18)
        sem_raiz = Text("∅", font_size=34, color=RED_B).move_to(ax3.c2p(0, 1.5))

        self.play(Create(ax1), Create(p1), run_time=1.5)
        self.play(FadeIn(d1), Write(lbl_d1), Write(desc1), run_time=1.5)
        self.wait(0.8)

        self.play(Create(ax2), Create(p2), run_time=1.5)
        self.play(FadeIn(d2), Write(lbl_d2), Write(desc2), run_time=1.5)
        self.wait(0.8)

        self.play(Create(ax3), Create(p3), run_time=1.5)
        self.play(FadeIn(sem_raiz), Write(lbl_d3), Write(desc3), run_time=1.5)
        self.wait(2.0)

        regra = MathTex(r"\Delta = b^2 - 4ac", font_size=32, color=RED_B)
        regra.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_r = SurroundingRectangle(regra, color=RED_B, buff=0.14, corner_radius=0.10)
        self.play(Write(regra), Create(box_r), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            ax1, p1, d1, lbl_d1, desc1,
            ax2, p2, d2, lbl_d2, desc2,
            ax3, p3, sem_raiz, lbl_d3, desc3,
            regra, box_r
        )), run_time=1.2)

    # ===================================================================
    # FASE 4 — Exemplo: calcular Δ
    # ===================================================================
    def _fase4_inferencia_exemplo(self):
        """Exemplo concreto: calcular Δ e prever número de raízes."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Exemplo — Calcule Δ")

        eq = MathTex(r"x^2 - 5x + 6 = 0", font_size=44, color=BLUE_D)
        eq.move_to(np.array([0, 1.55, 0]))
        self.play(Write(eq), run_time=2)
        self.wait(1)

        coefs = VGroup(
            MathTex(r"a = 1",  font_size=32, color=YELLOW),
            MathTex(r"b = -5", font_size=32, color=RED_B),
            MathTex(r"c = 6",  font_size=32, color=GREEN_B),
        ).arrange(RIGHT, buff=1.2)
        coefs.move_to(np.array([0, 0.6, 0]))
        self.play(Write(coefs), run_time=2)
        self.wait(1)

        steps = VGroup(
            MathTex(r"\Delta = b^2 - 4ac",                    font_size=34, color=WHITE),
            MathTex(r"\Delta = (-5)^2 - 4 \cdot 1 \cdot 6",  font_size=34, color=WHITE),
            MathTex(r"\Delta = 25 - 24",                       font_size=34, color=WHITE),
            MathTex(r"\Delta = 1 > 0",                         font_size=36, color=GREEN_B),
        ).arrange(DOWN, buff=0.38)
        steps.move_to(np.array([0, -0.9, 0]))

        for s in steps:
            self.play(Write(s), run_time=1.8)
            self.wait(0.6)

        inferencia = Text("→  Δ > 0  ∴  existem 2 raízes reais distintas",
                          font_size=22, color=GREEN_B)
        inferencia.move_to(np.array([0, Y_RESPOSTA, 0]))
        box_inf = SurroundingRectangle(inferencia, color=GREEN_B, buff=0.14, corner_radius=0.10)
        self.play(Write(inferencia), Create(box_inf), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            eq, coefs, steps, inferencia, box_inf
        )), run_time=1.2)

    # ===================================================================
    # FASE 5 — Bhaskara
    # ===================================================================
    def _fase5_bhaskara(self):
        """Fórmula Quadrática aplicada ao exemplo x² − 5x + 6 = 0."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Fórmula Quadrática")

        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{\Delta}}{2a}",
            font_size=52, color=BLUE_D
        ).move_to(np.array([-1.8, 0.6, 0]))   # descido e deslocado à esquerda
        box_f = SurroundingRectangle(formula, color=BLUE_D, buff=0.25, corner_radius=0.18)

        delta_def = MathTex(r"\Delta = b^2 - 4ac", font_size=36, color=RED_B)
        # Quadro rosa ao lado do azul, sem encostar
        delta_def.next_to(box_f, RIGHT, buff=0.55)
        box_d = SurroundingRectangle(delta_def, color=RED_B, buff=0.22, corner_radius=0.14)

        self.play(Write(formula), Create(box_f), run_time=2.5)
        self.play(Write(delta_def), Create(box_d), run_time=1.8)
        self.wait(1.5)

        sep = Line(np.array([-5.5, -0.5, 0]), np.array([5.5, -0.5, 0]), color=GRAY, stroke_width=1)
        self.play(Create(sep), run_time=0.7)

        ex_label = Text("Resolvendo  x² − 5x + 6 = 0  (a=1, b=−5, c=6, Δ=1)",
                        font_size=20, color=GRAY)
        ex_label.move_to(np.array([0, -0.85, 0]))
        self.play(FadeIn(ex_label), run_time=1.0)

        r_steps = VGroup(
            MathTex(r"x = \frac{-(-5) \pm \sqrt{1}}{2 \cdot 1}", font_size=32, color=WHITE),
            MathTex(r"x = \frac{5 \pm 1}{2}", font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=1.5)
        r_steps.next_to(ex_label, DOWN, buff=0.40)
        self.play(Write(r_steps), run_time=2.5)
        self.wait(0.8)

        raizes = VGroup(
            MathTex(r"x_1 = \frac{5+1}{2} = 3", font_size=34, color=GREEN_B),
            MathTex(r"x_2 = \frac{5-1}{2} = 2", font_size=34, color=GREEN_B),
        ).arrange(RIGHT, buff=2.0)
        raizes.next_to(r_steps, DOWN, buff=0.40)

        self.play(Write(raizes[0]), run_time=1.8)
        self.play(Write(raizes[1]), run_time=1.8)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            formula, box_f, delta_def, box_d,
            sep, ex_label, r_steps, raizes
        )), run_time=1.2)

    # ===================================================================
    # ENCERRAMENTO — padrão D29
    # ===================================================================
    def _encerramento(self):
        """Síntese visual do Descritor D31."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese — Descritor D31")

        descritivo = Text(
            "D31 – Resolver equação do 2º grau",
            color=WHITE, font_size=24
        ).move_to(np.array([0, 0.5, 0]))
        box_desc = SurroundingRectangle(
            descritivo, color=YELLOW, buff=0.18, corner_radius=0.10
        )
        self.play(FadeIn(descritivo), Create(box_desc), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(descritivo), FadeOut(box_desc), run_time=0.7)

        form_tit = Text("Resumo:", color=YELLOW, font_size=24, weight=BOLD)
        form_tit.move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(form_tit), run_time=0.6)

        resumo = VGroup(
            Text("Forma geral:  ax² + bx + c = 0  (a ≠ 0)",  color=BLUE_D,  font_size=22),
            Text("Discriminante:  Δ = b² − 4ac",               color=RED_B,   font_size=22),
            Text("Δ > 0  →  2 raízes reais distintas",         color=GREEN_B, font_size=22),
            Text("Δ = 0  →  1 raiz real dupla",                color=YELLOW,  font_size=22),
            Text("Δ < 0  →  sem raízes reais",                 color=RED_B,   font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.27)
        resumo.next_to(form_tit, DOWN, buff=0.30)

        cores_dots = [BLUE_D, RED_B, GREEN_B, YELLOW, RED_B]
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
            return np.array([a * np.cos(t) / d,
                             a * np.sin(t) * np.cos(t) / d, 0])

        def inf_v(t):
            d = 1 + np.sin(t) ** 2
            return np.array([a * np.sin(t) * np.cos(t) / d,
                             a * np.cos(t) / d, 0])

        logo_h = ParametricFunction(
            inf_h, t_range=[0, TAU], color="#3a3a5c", stroke_width=2.5
        ).move_to(UP * 0.5)
        logo_v = ParametricFunction(
            inf_v, t_range=[0, TAU], color="#9999bb", stroke_width=2.5
        ).move_to(UP * 0.5)

        circ = Circle(
            radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
            color=ESCURO_L, stroke_width=0
        ).move_to(UP * 0.5)
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
