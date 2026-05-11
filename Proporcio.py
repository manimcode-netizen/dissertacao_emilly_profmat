from manim import *

class Proporcionalidade(Scene):
    def construct(self):

        eixos = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 12, 2],
            axis_config={"include_numbers": True}
        )
        self.add(eixos)

        # Reta de proporcionalidade: y = 2x
        reta = eixos.plot(
            lambda x: 2 * x,
            x_range=[0, 5],
            color=BLUE
        )
        self.add(reta)

        # Ponto móvel sobre a reta
        t = ValueTracker(0.5)

        ponto = always_redraw(lambda: Dot(
            eixos.c2a(t.get_value(), 2 * t.get_value()),
            color=YELLOW, radius=0.1
        ))

        # Razão exibida em tempo real
        razao = always_redraw(lambda: MathTex(
            r"\frac{y}{x} = \frac{"
            + f"{2 * t.get_value():.1f}"
            + r"}{"
            + f"{t.get_value():.1f}"
            + r"} = 2{,}0"
        ).to_corner(UR).scale(0.7))

        self.add(ponto, razao)
        self.wait(1)

        # Deslocamento do ponto ao longo da reta
        self.play(
            t.animate.set_value(5),
            run_time=5   # lento o suficiente para
        )               # acompanhar a razão constante
        self.wait(1)

