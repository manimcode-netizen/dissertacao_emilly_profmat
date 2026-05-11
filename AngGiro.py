from manim import *
 class AnguloComoGiro(Scene):
    def construct(self):

        # Ponto central e raio fixo de referência
        centro = ORIGIN
        raio_ref = Line(centro, RIGHT * 2.5, color=GRAY)

        # Raio móvel: inicia coincidente com a referência
        raio_mov = Line(centro, RIGHT * 2.5, color=BLUE)

        # Variável rastreada: ângulo atual em graus
        angulo_val = ValueTracker(0)

        # Atualização contínua do raio móvel
        def atualizar_raio(r):
            ang = angulo_val.get_value()
            r.put_start_and_end_on(
                centro,
                centro + 2.5 * np.array([
                    np.cos(np.radians(ang)),
                    np.sin(np.radians(ang)), 0
                ])
            )

        raio_mov.add_updater(atualizar_raio)

        # Rótulo numérico: atualiza junto com a rotação
        rotulo = always_redraw(lambda: DecimalNumber(
            angulo_val.get_value(),
            num_decimal_places=0
        ).next_to(raio_mov.get_end(), UR, buff=0.15))

        self.add(raio_ref, raio_mov, rotulo)
        self.wait(1)

        # Giro de 0 a 90 graus em 3 segundos
        self.play(
            angulo_val.animate.set_value(90),
            run_time=3   # velocidade que permite
        )               # acompanhar a variação numérica
        self.wait(1)
