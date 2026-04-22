from manim import *
class CoordenadasCartesianas(Scene):
    def construct(self):

        plano = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.25}
        )
        self.add(plano)

        # Ponto a ser identificado
        P = Dot(plano.c2p(3, 4), color=YELLOW, radius=0.12)
        self.add(P)
        self.wait(1)

        # Projeção sobre o eixo x: linha vertical tracejada
        proj_x = DashedLine(
            plano.c2p(3, 4),
            plano.c2p(3, 0),
            color=RED, dash_length=0.15
        )
        label_x = MathTex("3", color=RED).next_to(
            plano.c2p(3, 0), DOWN, buff=0.2)

        # Primeira projeção: eixo x
        self.play(Create(proj_x), run_time=1.5)
        self.play(FadeIn(label_x))
        self.wait(0.5)

        # Projeção sobre o eixo y: linha horizontal tracejada
        proj_y = DashedLine(
            plano.c2p(3, 4),
            plano.c2p(0, 4),
            color=BLUE, dash_length=0.15
        )
        label_y = MathTex("4", color=BLUE).next_to(
            plano.c2p(0, 4), LEFT, buff=0.2)

        # Segunda projeção: eixo y
        self.play(Create(proj_y), run_time=1.5)
        self.play(FadeIn(label_y))
        self.wait(1)

