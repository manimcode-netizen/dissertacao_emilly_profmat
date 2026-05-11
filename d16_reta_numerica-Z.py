from manim import *

class D16RetaNumerica(Scene):
    """
    Descritor: D16 – SAEB 9º Ano
    Conceito: Identificar a localização de números inteiros na reta numérica
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve reconhecer e localizar números inteiros positivos,
              negativos e zero na reta numérica, compreendendo ordem, simetria
              e módulo/valor absoluto.
    """

    def construct(self):
        # --- PALETA DE CORES (consistente em toda a animação) ---
        COR_RETA     = WHITE
        COR_POSITIVO = BLUE
        COR_NEGATIVO = RED
        COR_ZERO     = YELLOW
        COR_DESTAQUE = GREEN

        # ============================================================
        # CENA 1: Título
        # ============================================================
        titulo = Text("D16 – Reta Numérica", color=WHITE, font_size=40)
        subtitulo = Text("Localização de Números Inteiros", color=YELLOW, font_size=28)
        subtitulo.next_to(titulo, DOWN, buff=0.4)

        self.play(Write(titulo), run_time=1.5)
        self.play(FadeIn(subtitulo), run_time=1)
        self.wait(2)
        self.play(FadeOut(titulo), FadeOut(subtitulo))
        self.wait(0.5)

        # ============================================================
        # CENA 2: Construção da reta numérica
        # ============================================================
        label_cena = Text("1. Construindo a reta numérica", color=WHITE, font_size=26)
        label_cena.to_edge(UP, buff=0.3)
        self.play(Write(label_cena), run_time=1)

        # Reta principal
        reta = Line(LEFT * 6.2, RIGHT * 6.2, color=COR_RETA, stroke_width=3)
        seta_dir = Arrow(RIGHT * 5.5, RIGHT * 6.5, color=COR_RETA, buff=0, stroke_width=3)
        seta_esq = Arrow(LEFT * 5.5, LEFT * 6.5, color=COR_RETA, buff=0, stroke_width=3)

        self.play(Create(reta), run_time=1.5)
        self.play(Create(seta_dir), Create(seta_esq), run_time=1)
        self.wait(1)

        # Marcas e rótulos dos inteiros de -5 a 5
        marcas = VGroup()
        rotulos = VGroup()

        for n in range(-5, 6):
            x_pos = n * 1.1
            marca = Line(UP * 0.18, DOWN * 0.18, color=COR_RETA, stroke_width=2)
            marca.move_to(RIGHT * x_pos)
            marcas.add(marca)

            if n == 0:
                cor_label = COR_ZERO
                tamanho = 24
            elif n > 0:
                cor_label = COR_POSITIVO
                tamanho = 22
            else:
                cor_label = COR_NEGATIVO
                tamanho = 22

            rotulo = MathTex(str(n), color=cor_label, font_size=tamanho)
            rotulo.next_to(marca, DOWN, buff=0.25)
            rotulos.add(rotulo)

        self.play(LaggedStart(*[Create(m) for m in marcas], lag_ratio=0.1), run_time=1.5)
        self.play(LaggedStart(*[Write(r) for r in rotulos], lag_ratio=0.1), run_time=1.5)
        self.wait(1.5)

        # Legenda de cores
        leg_neg  = Text("Negativos", color=COR_NEGATIVO, font_size=20)
        leg_zero = Text("Zero",      color=COR_ZERO,     font_size=20)
        leg_pos  = Text("Positivos", color=COR_POSITIVO, font_size=20)
        legenda = VGroup(leg_neg, leg_zero, leg_pos).arrange(RIGHT, buff=0.7)
        legenda.to_edge(DOWN, buff=0.3)

        self.play(FadeIn(legenda), run_time=1)
        self.wait(2)
        self.play(FadeOut(legenda))
        self.wait(0.3)

        # ============================================================
        # CENA 3: Destacar o zero (origem)
        # ============================================================
        novo_label = Text("2. O zero é a origem", color=WHITE, font_size=26)
        novo_label.to_edge(UP, buff=0.3)
        self.play(Transform(label_cena, novo_label), run_time=0.8)

        ponto_zero = Dot(ORIGIN, color=COR_ZERO, radius=0.13)
        texto_zero = Text("Origem (0)", color=COR_ZERO, font_size=22)
        texto_zero.next_to(ponto_zero, UP, buff=0.6)

        seta_zero = Arrow(
            texto_zero.get_bottom() + DOWN * 0.05,
            ponto_zero.get_top()    + UP   * 0.05,
            color=COR_ZERO, buff=0.05, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3
        )

        self.play(Create(ponto_zero), run_time=0.8)
        self.play(Write(texto_zero), Create(seta_zero), run_time=1)
        self.wait(2)
        self.play(FadeOut(texto_zero), FadeOut(seta_zero), FadeOut(ponto_zero))

        # ============================================================
        # CENA 4: Positivos à direita  [AJUSTE 1 — setas e chave mais altas]
        # ============================================================
        novo_label = Text("3. Positivos ficam à direita do zero", color=WHITE, font_size=24)
        novo_label.to_edge(UP, buff=0.3)
        self.play(Transform(label_cena, novo_label), run_time=0.8)

        pontos_pos = VGroup()
        setas_pos  = VGroup()
        textos_pos = VGroup()

        for n in [1, 2, 3, 4, 5]:
            x = n * 1.1
            ponto = Dot(RIGHT * x, color=COR_POSITIVO, radius=0.11)
            pontos_pos.add(ponto)

            # Setas começam mais alto para evitar sobreposição com a chave
            seta = Arrow(
                RIGHT * x + UP * 1.5,
                RIGHT * x + UP * 0.22,
                color=COR_POSITIVO, buff=0, stroke_width=2,
                max_tip_length_to_length_ratio=0.25
            )
            setas_pos.add(seta)

            txt = MathTex(f"+{n}", color=COR_POSITIVO, font_size=22)
            txt.next_to(seta, UP, buff=0.08)
            textos_pos.add(txt)

        self.play(LaggedStart(*[Create(p) for p in pontos_pos], lag_ratio=0.2), run_time=1.5)
        self.play(
            LaggedStart(*[Create(s) for s in setas_pos],  lag_ratio=0.2),
            LaggedStart(*[Write(t)  for t in textos_pos], lag_ratio=0.2),
            run_time=1.5
        )

        # Chave bem acima das setas
        chave_dir     = BraceBetweenPoints(RIGHT * 0.2, RIGHT * 5.7, direction=UP)
        chave_dir.shift(UP * 1.7)
        chave_dir_txt = Text("Inteiros Positivos →", color=COR_POSITIVO, font_size=20)
        chave_dir_txt.next_to(chave_dir, UP, buff=0.15)

        self.play(Create(chave_dir), Write(chave_dir_txt), run_time=1)
        self.wait(2)
        self.play(
            FadeOut(pontos_pos), FadeOut(setas_pos), FadeOut(textos_pos),
            FadeOut(chave_dir),  FadeOut(chave_dir_txt)
        )

        # ============================================================
        # CENA 5: Negativos à esquerda  [AJUSTE 1 — setas e chave mais altas]
        # ============================================================
        novo_label = Text("4. Negativos ficam à esquerda do zero", color=WHITE, font_size=24)
        novo_label.to_edge(UP, buff=0.3)
        self.play(Transform(label_cena, novo_label), run_time=0.8)

        pontos_neg = VGroup()
        setas_neg  = VGroup()
        textos_neg = VGroup()

        for n in [-1, -2, -3, -4, -5]:
            x = n * 1.1
            ponto = Dot(RIGHT * x, color=COR_NEGATIVO, radius=0.11)
            pontos_neg.add(ponto)

            seta = Arrow(
                RIGHT * x + UP * 1.5,
                RIGHT * x + UP * 0.22,
                color=COR_NEGATIVO, buff=0, stroke_width=2,
                max_tip_length_to_length_ratio=0.25
            )
            setas_neg.add(seta)

            txt = MathTex(str(n), color=COR_NEGATIVO, font_size=22)
            txt.next_to(seta, UP, buff=0.08)
            textos_neg.add(txt)

        self.play(LaggedStart(*[Create(p) for p in pontos_neg], lag_ratio=0.2), run_time=1.5)
        self.play(
            LaggedStart(*[Create(s) for s in setas_neg],  lag_ratio=0.2),
            LaggedStart(*[Write(t)  for t in textos_neg], lag_ratio=0.2),
            run_time=1.5
        )

        chave_esq     = BraceBetweenPoints(LEFT * 0.2, LEFT * 5.7, direction=UP)
        chave_esq.shift(UP * 1.7)
        chave_esq_txt = Text("← Inteiros Negativos", color=COR_NEGATIVO, font_size=20)
        chave_esq_txt.next_to(chave_esq, UP, buff=0.15)

        self.play(Create(chave_esq), Write(chave_esq_txt), run_time=1)
        self.wait(2)
        self.play(
            FadeOut(pontos_neg), FadeOut(setas_neg), FadeOut(textos_neg),
            FadeOut(chave_esq),  FadeOut(chave_esq_txt)
        )

        # ============================================================
        # CENA 6: Oposto / Simétrico  [AJUSTES 2 e 3]
        # Duas setas saindo do zero para cada par, substituindo o arco
        # ============================================================
        novo_label = Text("5. Números Opostos (Simétricos)", color=WHITE, font_size=26)
        novo_label.to_edge(UP, buff=0.3)
        self.play(Transform(label_cena, novo_label), run_time=0.8)

        pares       = [(3, -3), (2, -2)]
        cores_pares = [COR_DESTAQUE, ORANGE]

        for (pos, neg), cor in zip(pares, cores_pares):
            xp = pos * 1.1
            xn = neg * 1.1

            dot_p = Dot(RIGHT * xp, color=cor, radius=0.13)
            dot_n = Dot(RIGHT * xn, color=cor, radius=0.13)
            dot_o = Dot(ORIGIN,     color=COR_ZERO, radius=0.13)

            label_p = MathTex(f"+{pos}", color=cor, font_size=24)
            label_p.next_to(dot_p, UP, buff=0.25)
            label_n = MathTex(str(neg), color=cor, font_size=24)
            label_n.next_to(dot_n, UP, buff=0.25)

            # Seta do zero até o positivo
            seta_p = Arrow(
                ORIGIN + RIGHT * 0.15,
                RIGHT * xp - RIGHT * 0.15,
                color=cor, buff=0, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.15
            ).shift(UP * 0.35)

            # Seta do zero até o negativo
            seta_n = Arrow(
                ORIGIN + LEFT * 0.15,
                RIGHT * xn + RIGHT * 0.15,
                color=cor, buff=0, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.15
            ).shift(UP * 0.35)

            dist_txt = Text(f"distância = {pos}  |  distância = {pos}", color=cor, font_size=18)
            dist_txt.next_to(reta, UP, buff=1.1)

            oposto_txt = MathTex(
                f"{neg} \\text{{ e }} +{pos} \\text{{ são opostos}}",
                color=cor, font_size=22
            )
            oposto_txt.next_to(dist_txt, DOWN, buff=0.25)

            self.play(Create(dot_p), Create(dot_n), Create(dot_o), run_time=0.7)
            self.play(Write(label_p), Write(label_n), run_time=0.7)
            self.play(Create(seta_n), Create(seta_p), run_time=1.2)
            self.play(Write(dist_txt), run_time=0.8)
            self.play(Write(oposto_txt), run_time=0.8)
            self.wait(2)
            self.play(
                FadeOut(dot_p), FadeOut(dot_n), FadeOut(dot_o),
                FadeOut(label_p), FadeOut(label_n),
                FadeOut(seta_p), FadeOut(seta_n),
                FadeOut(dist_txt), FadeOut(oposto_txt)
            )

        self.wait(0.3)

        # ============================================================
        # CENA 7: Ordenação  [AJUSTE 4 — quadro lateral com < e >]
        # ============================================================
        novo_label = Text("6. Ordem na reta: menor ← → maior", color=WHITE, font_size=24)
        novo_label.to_edge(UP, buff=0.3)
        self.play(Transform(label_cena, novo_label), run_time=0.8)

        # --- Quadro superior direito com significado dos símbolos ---
        quadro_bg = Rectangle(
            width=3.6, height=1.9,
            fill_color="#1a1a2e", fill_opacity=0.92,
            stroke_color=COR_DESTAQUE, stroke_width=2
        ).to_corner(UR, buff=0.25)

        titulo_quadro = Text("Símbolos", color=COR_DESTAQUE, font_size=20, weight=BOLD)
        titulo_quadro.next_to(quadro_bg.get_top(), DOWN, buff=0.2)

        linha1 = MathTex(r"a < b", color=WHITE, font_size=22)
        desc1  = Text("a é menor que b", color=WHITE, font_size=16)
        linha2 = MathTex(r"a > b", color=WHITE, font_size=22)
        desc2  = Text("a é maior que b", color=WHITE, font_size=16)

        conteudo_quadro = VGroup(linha1, desc1, linha2, desc2)
        conteudo_quadro.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        conteudo_quadro.next_to(titulo_quadro, DOWN, buff=0.18)
        conteudo_quadro.align_to(quadro_bg.get_left() + RIGHT * 0.2, LEFT)

        self.play(
            FadeIn(quadro_bg), Write(titulo_quadro),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[FadeIn(e, shift=RIGHT * 0.2) for e in conteudo_quadro],
                        lag_ratio=0.15),
            run_time=1.2
        )
        self.wait(0.5)

        # --- Comparações na reta ---
        comparacoes = [(-3, 1), (-5, -2)]
        for a, b in comparacoes:
            xa = a * 1.1
            xb = b * 1.1

            dot_a = Dot(RIGHT * xa, color=COR_NEGATIVO, radius=0.13)
            dot_b = Dot(RIGHT * xb, color=COR_POSITIVO, radius=0.13)
            lab_a = MathTex(str(a), color=COR_NEGATIVO, font_size=24)
            lab_a.next_to(dot_a, UP, buff=0.22)
            lab_b = MathTex(str(b), color=COR_POSITIVO, font_size=24)
            lab_b.next_to(dot_b, UP, buff=0.22)

            self.play(Create(dot_a), Create(dot_b), run_time=0.7)
            self.play(Write(lab_a), Write(lab_b), run_time=0.7)

            seta_comp = Arrow(
                RIGHT * xa + UP * 0.85,
                RIGHT * xb + UP * 0.85,
                color=COR_DESTAQUE, buff=0, stroke_width=2.5,
                max_tip_length_to_length_ratio=0.2
            )
            menor_txt = MathTex(f"{a} < {b}", color=COR_DESTAQUE, font_size=26)
            menor_txt.next_to(seta_comp, UP, buff=0.12)

            self.play(Create(seta_comp), run_time=0.8)
            self.play(Write(menor_txt), run_time=0.8)
            self.wait(2)
            self.play(
                FadeOut(dot_a), FadeOut(dot_b),
                FadeOut(lab_a), FadeOut(lab_b),
                FadeOut(seta_comp), FadeOut(menor_txt)
            )

        self.play(FadeOut(quadro_bg), FadeOut(titulo_quadro), FadeOut(conteudo_quadro))
        self.wait(0.3)

        # ============================================================
        # CENA 8: Exemplos – localizar número na reta  [AJUSTE 5]
        # Título sem "SAEB" + 3 exemplos no total
        # ============================================================
        exemplos_config = [
            {
                "pergunta": "Exemplo 1: Qual ponto representa −4?",
                "pontos":   {"A": -4, "B": -2, "C": 0, "D": 2, "E": 5},
                "resposta": "A",
                "valor":    -4,
            },
            {
                "pergunta": "Exemplo 2: Qual ponto representa +3?",
                "pontos":   {"A": -5, "B": -2, "C": 0, "D": 3, "E": 5},
                "resposta": "D",
                "valor":    3,
            },
            {
                "pergunta": "Exemplo 3: Qual ponto representa −2?",
                "pontos":   {"A": -4, "B": -2, "C": 1, "D": 3, "E": 4},
                "resposta": "B",
                "valor":    -2,
            },
        ]

        for cfg in exemplos_config:
            novo_label = Text(cfg["pergunta"], color=WHITE, font_size=24)
            novo_label.to_edge(UP, buff=0.3)
            self.play(Transform(label_cena, novo_label), run_time=0.8)

            grupos = {}
            for letra, valor in cfg["pontos"].items():
                x = valor * 1.1
                ponto = Dot(RIGHT * x, color=WHITE, radius=0.11)
                lab   = Text(letra, color=WHITE, font_size=22)
                lab.next_to(ponto, UP, buff=0.25)
                grupos[letra] = VGroup(ponto, lab)

            self.play(
                LaggedStart(*[Create(g) for g in grupos.values()], lag_ratio=0.2),
                run_time=1.5
            )
            self.wait(1)

            resp_letra = cfg["resposta"]
            resp_valor = cfg["valor"]
            resp_ponto = grupos[resp_letra][0]
            resp_lab   = grupos[resp_letra][1]

            circulo_resp = Circle(radius=0.22, color=COR_DESTAQUE, stroke_width=3)
            circulo_resp.move_to(resp_ponto.get_center())

            sinal = "+" if resp_valor > 0 else ""
            resp_txt = Text(
                f"Resposta: Ponto {resp_letra} = {sinal}{resp_valor} ✓",
                color=COR_DESTAQUE, font_size=22
            )
            resp_txt.to_edge(DOWN, buff=0.5)

            self.play(Create(circulo_resp), run_time=0.8)
            self.play(
                resp_ponto.animate.set_color(COR_DESTAQUE),
                resp_lab.animate.set_color(COR_DESTAQUE),
                run_time=0.8
            )
            self.play(Write(resp_txt), run_time=1)
            self.wait(2.5)

            self.play(
                *[FadeOut(g) for g in grupos.values()],
                FadeOut(circulo_resp), FadeOut(resp_txt)
            )

        self.wait(0.3)

        # ============================================================
        # CENA 9: Módulo / Valor Absoluto  [AJUSTE 6]
        # ============================================================
        novo_label = Text("7. Módulo ou Valor Absoluto", color=WHITE, font_size=26)
        novo_label.to_edge(UP, buff=0.3)
        self.play(Transform(label_cena, novo_label), run_time=0.8)

        # Explicação do conceito
        def_txt = Text(
            "O módulo é a distância do número até o zero.",
            color=WHITE, font_size=22
        )
        def_txt.next_to(novo_label, DOWN, buff=0.35)
        notacao_txt = Text("Notação:  |n|", color=COR_ZERO, font_size=22)
        notacao_txt.next_to(def_txt, DOWN, buff=0.25)

        self.play(Write(def_txt), run_time=1)
        self.play(Write(notacao_txt), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(def_txt), FadeOut(notacao_txt))

        # Exemplos visuais na reta: |−3| e |+3|
        exemplos_mod = [
            (-3, COR_NEGATIVO),
            ( 3, COR_POSITIVO),
        ]

        for valor, cor in exemplos_mod:
            x = valor * 1.1
            dot = Dot(RIGHT * x, color=cor, radius=0.13)
            lab = MathTex(str(valor), color=cor, font_size=24)
            lab.next_to(dot, UP, buff=0.25)

            # Seta do zero até o ponto (mostra a distância)
            if valor > 0:
                seta_mod = Arrow(
                    ORIGIN + RIGHT * 0.15,
                    RIGHT * x - RIGHT * 0.15,
                    color=cor, buff=0, stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.15
                ).shift(UP * 0.45)
            else:
                seta_mod = Arrow(
                    ORIGIN + LEFT * 0.15,
                    RIGHT * x + RIGHT * 0.15,
                    color=cor, buff=0, stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.15
                ).shift(UP * 0.45)

            mod_txt = MathTex(
                f"|{valor}| = {abs(valor)}",
                color=cor, font_size=28
            )
            mod_txt.next_to(seta_mod, UP, buff=0.2)

            self.play(Create(dot), Write(lab), run_time=0.7)
            self.play(Create(seta_mod), run_time=0.8)
            self.play(Write(mod_txt), run_time=0.8)
            self.wait(2)
            self.play(FadeOut(dot), FadeOut(lab), FadeOut(seta_mod), FadeOut(mod_txt))

        # Mostrar que |−3| = |+3| = 3
        conclusao = MathTex(
            r"|-3| = |+3| = 3 \quad \text{(mesma distância ao zero)}",
            color=COR_DESTAQUE, font_size=26
        )
        conclusao.next_to(reta, UP, buff=1.0)
        self.play(Write(conclusao), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(conclusao))
        self.wait(0.3)

        # ============================================================
        # CENA 10: Síntese final
        # ============================================================
        self.play(
            FadeOut(label_cena), FadeOut(reta),
            FadeOut(marcas), FadeOut(rotulos),
            FadeOut(seta_dir), FadeOut(seta_esq)
        )

        sintese_titulo = Text("Resumo – D16", color=YELLOW, font_size=32)
        sintese_titulo.to_edge(UP, buff=0.5)
        self.play(Write(sintese_titulo), run_time=1)

        regras = [
            ("→ O zero é a origem da reta",              COR_ZERO),
            ("→ Positivos ficam à direita do 0",          COR_POSITIVO),
            ("→ Negativos ficam à esquerda do 0",         COR_NEGATIVO),
            ("→ Quanto mais à esquerda, menor o número",  WHITE),
            ("→ Opostos têm a mesma distância ao zero",   COR_DESTAQUE),
            ("→ Módulo |n| = distância até o zero",       ORANGE),
        ]

        grupo_regras = VGroup()
        for texto, cor in regras:
            item = Text(texto, color=cor, font_size=21)
            grupo_regras.add(item)

        grupo_regras.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        grupo_regras.next_to(sintese_titulo, DOWN, buff=0.4)
        grupo_regras.center()

        for item in grupo_regras:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.4)

        self.wait(3)
        self.play(FadeOut(VGroup(sintese_titulo, grupo_regras)))
        self.wait(0.5)


# ============================================================
# CENA LOGO – Prof.ª Emilly Mayre  [AJUSTE 7]
# ============================================================
class LogoEmillyMayre(Scene):
    """
    Conceito: Animação da Logo da Prof.ª Emilly Mayre
    Objetivo: Exibir a identidade visual da professora com dois infinitos
              cruzados, círculo EM, nome e cargo.
    Fundo: BRANCO · Dois infinitos cruzados · EM no centro
    Traço DOURADO em negrito abaixo do nome.
    """

    def construct(self):
        ESCURO_L = "#1a1a2e"
        DOURADO  = "#C8A84B"
        CINZA_L  = "#888899"

        # Fundo branco
        bg_logo = Rectangle(width=16, height=9,
                            fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.add(bg_logo)

        # ── Dois infinitos (lemniscata de Bernoulli) ──────────────
        a_inf = 1.9

        def inf_horiz(t):
            d = 1 + np.sin(t)**2
            return np.array([a_inf * np.cos(t) / d,
                             a_inf * np.sin(t) * np.cos(t) / d, 0])

        def inf_vert(t):
            d = 1 + np.sin(t)**2
            return np.array([a_inf * np.sin(t) * np.cos(t) / d,
                             a_inf * np.cos(t) / d, 0])

        # Infinito horizontal — cinza escuro
        logo_inf_h = ParametricFunction(
            inf_horiz, t_range=[0, TAU],
            color="#3a3a5c", stroke_width=2.5,
        ).move_to(ORIGIN + UP * 0.5)

        # Infinito vertical — cinza médio
        logo_inf_v = ParametricFunction(
            inf_vert, t_range=[0, TAU],
            color="#9999bb", stroke_width=2.5,
        ).move_to(ORIGIN + UP * 0.5)

        grupo_logo = VGroup(logo_inf_h, logo_inf_v)

        # ── Círculo central EM ────────────────────────────────────
        logo_circ = Circle(
            radius=0.42,
            fill_color=ESCURO_L, fill_opacity=1,
            color=ESCURO_L, stroke_width=0,
        ).move_to(ORIGIN + UP * 0.5)

        logo_em = Text("EM", color=WHITE, font_size=22, weight=BOLD)
        logo_em.move_to(logo_circ.get_center())

        # ── Textos ────────────────────────────────────────────────
        logo_nome = Text("Emilly Mayre", color=ESCURO_L,
                         font_size=28, weight=BOLD)
        logo_nome.next_to(grupo_logo, DOWN, buff=0.55)

        # Traço DOURADO e GROSSO (negrito)
        logo_linha = Line(LEFT * 1.6, RIGHT * 1.6,
                          color=DOURADO, stroke_width=3.5)
        logo_linha.next_to(logo_nome, DOWN, buff=0.16)

        logo_cargo = Text("PROFESSORA DE MATEMÁTICA",
                          color=CINZA_L, font_size=14)
        logo_cargo.next_to(logo_linha, DOWN, buff=0.18)

        # ── Animação ──────────────────────────────────────────────
        # 1) Infinito horizontal
        self.play(Create(logo_inf_h), run_time=2.0)
        self.wait(0.3)
        # 2) Infinito vertical
        self.play(Create(logo_inf_v), run_time=2.0)
        self.wait(0.3)
        # 3) Círculo EM
        self.play(GrowFromCenter(logo_circ), run_time=0.7)
        self.play(Write(logo_em), run_time=0.5)
        self.wait(0.3)
        # 4) Nome, traço dourado, cargo
        self.play(FadeIn(logo_nome, shift=UP * 0.15), run_time=0.8)
        self.play(Create(logo_linha), run_time=0.5)
        self.play(FadeIn(logo_cargo), run_time=0.6)
        self.wait(0.4)
        # 5) Pulso suave
        logo_simbolo = VGroup(logo_inf_h, logo_inf_v, logo_circ, logo_em)
        self.play(logo_simbolo.animate.scale(1.06), run_time=0.4)
        self.play(logo_simbolo.animate.scale(1 / 1.06), run_time=0.35)
        self.wait(3.5)
