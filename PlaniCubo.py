from manim import *
class PlanificacaoCubo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES,
                                    theta=-45*DEGREES)

        # Face base: quadrado no plano horizontal
        base = Square(side_length=2, color=BLUE,
                      fill_opacity=0.6)
        base.set_fill(BLUE)

        # Face lateral: dobra 90 graus em torno da aresta inferior
        lateral = Square(side_length=2, color=RED,
                         fill_opacity=0.6)
        lateral.next_to(base, DOWN, buff=0)

        self.add(base, lateral)
        self.wait(1)

        # Animação do dobramento: rotação em torno da aresta comum
        self.play(
            Rotate(
                lateral,
                angle=PI/2,            # dobramento de 90 graus
                axis=RIGHT,            # eixo: aresta de articulação
                about_point=base.get_bottom(),
                run_time=2             # velocidade controlada
            )
        )
        self.wait(1)
 
