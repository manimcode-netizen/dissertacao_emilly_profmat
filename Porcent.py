from manim import *

class Porcentagem(Scene):
    def construct(self):

        # Barra do todo: 100 unidades
        barra_total = Rectangle(
            width=8, height=1,
            color=GRAY, fill_opacity=0.3
        ).shift(UP)

        # Destaque: 25 partes de 100
        barra_parte = Rectangle(
            width=2, height=1,      # 25% de largura 8 = 2
            color=BLUE, fill_opacity=0.7
        ).align_to(barra_total, LEFT).shift(UP)

        rotulo = MathTex(
            r"25 \text{ em } 100 = 25\%"
        ).next_to(barra_total, DOWN)

        self.add(barra_total, barra_parte, rotulo)
        self.wait(2)

        # Transformação: novo todo de 200 unidades
        # A barra cresce; a parte também cresce
        # proporcionalmente
        self.play(
            barra_total.animate.set_width(8),   # mantém
            barra_parte.animate.set_width(2),   # 25% = 2/8
            Transform(
                rotulo,
                MathTex(
                    r"50 \text{ em } 200 = 25\%"
                ).next_to(barra_total, DOWN)
            ),
            run_time=2
        )
        self.wait(2)

