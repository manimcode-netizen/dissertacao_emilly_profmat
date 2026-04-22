from manim import *

class InteirosNaReta(Scene):
    def construct(self):

        # Reta numérica de -6 a 6
        reta = NumberLine(
            x_range=[-6, 6, 1],
            length=12,
            include_numbers=True,
            color=GRAY
        )
        self.add(reta)

        # Ponto inicial no zero
        ponto = Dot(reta.n2p(0), color=YELLOW, radius=0.15)
        self.add(ponto)
        self.wait(1)

        # Deslocamento +3: para a direita
        self.play(
            ponto.animate.move_to(reta.n2p(3)),
            run_time=2   # 1 segundo por unidade permite
        )               # acompanhar a contagem de passos
        self.wait(0.5)

        # Deslocamento -5: para a esquerda, cruza o zero
        self.play(
            ponto.animate.move_to(reta.n2p(-2)),
            run_time=3   # mais lento: cruza a fronteira do zero
        )
        self.wait(1)

