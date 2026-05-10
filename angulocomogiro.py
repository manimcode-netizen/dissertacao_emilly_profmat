"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Ângulos notáveis — medição e posição do raio giratório
Nível    : Ensino Fundamental / Médio
Objetivo : Associar a posição do raio giratório à medida angular em
           graus, com pausa nos ângulos 30°, 45°, 60°, 90° e 180°.
=======================================================================
RENDERIZAÇÃO:
  manim -pql angulos_notaveis.py AngulosNotaveis
  manim -pqh angulos_notaveis.py AngulosNotaveis
=======================================================================
"""

from manim import *
import numpy as np

# ── Paleta semântica ────────────────────────────────────────────────
COR_REF    = WHITE      # raio de referência fixo
COR_GIRANTE= YELLOW     # raio giratório
COR_ARCO   = BLUE       # arco do ângulo
COR_MEDIDA = GREEN      # medida do ângulo em tempo real
COR_CENTRO = RED        # ponto central
COR_TEXTO  = WHITE

RAIO = 2.5              # comprimento dos raios


class AngulosNotaveis(Scene):
    """
    Conceito : Ângulos notáveis — raio giratório e medida em graus
    Nível    : Ensino Fundamental / Médio
    Objetivo : Associar posição do raio à medida angular, com pausas
               em 30°, 45°, 60°, 90° e 180°.
    """

    def construct(self):

        # ── ETAPA 1: Centro + raio de referência ────────────────────
        centro = Dot(ORIGIN, color=COR_CENTRO, radius=0.10)
        raio_ref = Arrow(
            ORIGIN, RIGHT * RAIO,
            color=COR_REF, buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.10
        )
        lbl_ref = MathTex("0^\\circ", color=COR_REF, font_size=22)
        lbl_ref.next_to(raio_ref.get_end(), RIGHT, buff=0.15)

        self.play(GrowFromCenter(centro), run_time=0.5)
        self.play(GrowArrow(raio_ref), Write(lbl_ref), run_time=1.0)
        self.wait(0.8)

        # ── ETAPA 2: Raio giratório + arco + medida em tempo real ────
        # Usamos ValueTracker para animar o ângulo
        angulo_tracker = ValueTracker(0)

        # Raio giratório — recalculado a cada frame via always_redraw
        raio_girante = always_redraw(lambda: Arrow(
            ORIGIN,
            RAIO * np.array([
                np.cos(angulo_tracker.get_value()),
                np.sin(angulo_tracker.get_value()),
                0
            ]),
            color=COR_GIRANTE, buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.10
        ))

        # Arco colorido crescendo com o ângulo
        arco = always_redraw(lambda: Arc(
            radius=0.9,
            start_angle=0,
            angle=angulo_tracker.get_value(),
            color=COR_ARCO,
            stroke_width=4
        ))

        # Medida em tempo real — sempre no centro da abertura, afastada das retas
        medida = always_redraw(lambda: MathTex(
            f"{int(round(np.degrees(angulo_tracker.get_value())))}^\\circ",
            color=COR_MEDIDA,
            font_size=30
        ).move_to(
            1.3 * np.array([
                np.cos(angulo_tracker.get_value() / 2),
                np.sin(angulo_tracker.get_value() / 2),
                0
            ])
        ))

        self.play(
            FadeIn(raio_girante),
            FadeIn(arco),
            FadeIn(medida),
            run_time=0.5
        )
        self.wait(0.3)

        # ── ETAPA 3: Giro com pausas nos ângulos notáveis ────────────
        angulos_notaveis = [30, 45, 60, 90, 180]
        angulo_atual = 0

        for grau in angulos_notaveis:
            rad = np.radians(grau)
            delta = rad - angulo_atual
            # Velocidade proporcional ao arco percorrido
            tempo = delta / np.radians(45) * 1.5

            self.play(
                angulo_tracker.animate.set_value(rad),
                run_time=max(tempo, 1.0),
                rate_func=linear
            )
            angulo_atual = rad

            # Pausa — sem mostrar destaque separado (a medida já está no arco)
            self.wait(1.5)

        self.wait(0.5)

        # ── ETAPA 4: Composição lateral — ângulos notáveis ───────────
        self.play(
            FadeOut(raio_girante),
            FadeOut(arco),
            FadeOut(medida),
            FadeOut(centro),
            FadeOut(raio_ref),
            FadeOut(lbl_ref),
            run_time=1.0
        )
        self.wait(0.3)

        titulo_comp = Text("Ângulos Notáveis", color=COR_TEXTO, font_size=30)
        titulo_comp.to_edge(UP, buff=0.3)
        self.play(Write(titulo_comp), run_time=0.8)

        # Criar mini-diagrama para cada ângulo notável
        dados = [
            (30,  BLUE),
            (45,  GREEN),
            (60,  YELLOW),
            (90,  ORANGE),
            (180, RED),
        ]

        cards = VGroup()
        for grau, cor in dados:
            rad = np.radians(grau)
            r = 1.5

            c   = Dot(ORIGIN, color=WHITE, radius=0.09)
            ref = Arrow(ORIGIN, RIGHT * r, color=WHITE, buff=0,
                        stroke_width=2.5, max_tip_length_to_length_ratio=0.12)
            gir = Arrow(ORIGIN,
                        r * np.array([np.cos(rad), np.sin(rad), 0]),
                        color=cor, buff=0,
                        stroke_width=3, max_tip_length_to_length_ratio=0.12)
            arc = Arc(radius=0.5, start_angle=0, angle=rad,
                      color=cor, stroke_width=3.5)

            # Label sempre no meio da abertura do ângulo, afastado da reta
            mid_angle = rad / 2
            dist_lbl  = 0.85  # distância do centro ao label
            pos_lbl   = dist_lbl * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
            lbl = MathTex(f"{grau}^\\circ", color=cor, font_size=34)
            lbl.move_to(pos_lbl)

            card = VGroup(c, ref, gir, arc, lbl)
            cards.add(card)

        cards.arrange(RIGHT, buff=0.65)
        cards.move_to(ORIGIN + DOWN * 0.5)

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.55)

        self.wait(3.5)
