from manim import *

class PadroesSequencias(Scene):
    def construct(self):

        # Primeiro termo: 1 quadrado
        t1 = Square(side_length=0.8,
                    color=BLUE, fill_opacity=0.7)
        t1.move_to(LEFT * 4)

        contador = MathTex("n=1").next_to(t1, DOWN)

        self.play(FadeIn(t1), Write(contador))
        self.wait(1)

        # Segundo termo: 4 quadrados (acréscimo em vermelho)
        t2_base = t1.copy().move_to(LEFT * 1.5)
        t2_novo = VGroup(*[
            Square(side_length=0.8,
                   color=RED, fill_opacity=0.7)
            for _ in range(3)   # 3 quadrados novos
        ]).arrange(RIGHT, buff=0.1)
        t2_novo.next_to(t2_base, RIGHT, buff=0.1)

        contador2 = MathTex("n=2").next_to(
            VGroup(t2_base, t2_novo), DOWN)

        self.play(
            FadeIn(t2_base),
            FadeIn(t2_novo),
            Transform(contador, contador2),
            run_time=1.5
        )
        self.wait(1)

