from manim import *

# ==============================================================================
# SAEB – Descritor D17 (9º Ano)
# Conceito : Identificar a localização de números racionais na reta numérica
# Nível    : Ensino Fundamental – 9º ano
# Objetivo : Ao final o aluno reconhece como localizar frações, decimais e
#            inteiros negativos sobre a reta numérica.
# ==============================================================================

# ── Paleta de cores (fixa em toda a animação) ─────────────────────────────────
COR_RETA       = WHITE          # reta numérica
COR_INTEIRO    = BLUE           # marcas de inteiros
COR_FRACAO     = YELLOW         # frações
COR_DECIMAL    = GREEN          # decimais
COR_NEGATIVO   = RED            # números negativos
COR_DESTAQUE   = ORANGE         # seta / ponto destacado
COR_TEXTO      = WHITE          # rótulos gerais


# ══════════════════════════════════════════════════════════════════════════════
# CENA 1 – Apresentação do tema
# ══════════════════════════════════════════════════════════════════════════════
class Cena1_Titulo(Scene):
    """Introduz o tema e o descritor do SAEB."""

    def construct(self):
        titulo = Text(
            "Números Racionais\nna Reta Numérica",
            color=COR_TEXTO,
            font_size=52,
            line_spacing=1.3,
        ).move_to(ORIGIN)

        descritor = Text(
            "SAEB – D17 | 9.º Ano",
            color=YELLOW,
            font_size=28,
        ).next_to(titulo, DOWN, buff=0.6)

        # Animação sequencial – sem sobreposição
        self.play(Write(titulo), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(descritor, shift=UP * 0.3), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(titulo), FadeOut(descritor), run_time=1)


# ══════════════════════════════════════════════════════════════════════════════
# CENA 2 – A reta numérica e os inteiros
# ══════════════════════════════════════════════════════════════════════════════
class Cena2_RetaInteiros(Scene):
    """Constrói a reta numérica e posiciona os números inteiros."""

    def construct(self):
        # ── Título da cena ──────────────────────────────────────────────────
        titulo = Text("A Reta Numérica", color=COR_TEXTO, font_size=36)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        # ── Construção da reta ──────────────────────────────────────────────
        reta = NumberLine(
            x_range=[-4, 4, 1],
            length=11,
            color=COR_RETA,
            include_tip=True,
            include_numbers=False,   # adicionamos os rótulos manualmente
            tick_size=0.12,
        )
        reta.move_to(ORIGIN)

        self.play(Create(reta), run_time=2)
        self.wait(0.5)

        # ── Rótulos dos inteiros ────────────────────────────────────────────
        rotulos = VGroup()
        for n in range(-4, 5):
            pos = reta.n2p(n)
            label = MathTex(str(n), color=COR_INTEIRO, font_size=30)
            label.next_to(pos, DOWN, buff=0.35)
            rotulos.add(label)

        self.play(LaggedStart(*[Write(r) for r in rotulos], lag_ratio=0.15), run_time=3)
        self.wait(0.8)

        # ── Destaque do zero ────────────────────────────────────────────────
        ponto_zero = Dot(reta.n2p(0), color=COR_DESTAQUE, radius=0.10)
        texto_zero = Text("zero", color=COR_DESTAQUE, font_size=24)
        texto_zero.next_to(ponto_zero, UP, buff=0.4)

        self.play(FadeIn(ponto_zero), Write(texto_zero), run_time=1.5)
        self.wait(1.5)

        # ── Mensagem explicativa ────────────────────────────────────────────
        msg = Text(
            "Os inteiros ficam espaçados\nigualmente na reta.",
            color=COR_TEXTO, font_size=26, line_spacing=1.2
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(titulo), FadeOut(reta), FadeOut(rotulos),
            FadeOut(ponto_zero), FadeOut(texto_zero), FadeOut(msg),
            run_time=1,
        )


# ══════════════════════════════════════════════════════════════════════════════
# CENA 3 – Frações na reta (½, ¼, ¾)
# ══════════════════════════════════════════════════════════════════════════════
class Cena3_Fracoes(Scene):
    """Mostra como localizar frações entre os inteiros."""

    def construct(self):
        titulo = Text("Frações na Reta Numérica", color=COR_TEXTO, font_size=36)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        # ── Reta entre 0 e 2 ────────────────────────────────────────────────
        reta = NumberLine(
            x_range=[0, 2, 1],
            length=9,
            color=COR_RETA,
            include_tip=True,
            include_numbers=False,
            tick_size=0.12,
        )
        reta.shift(DOWN * 0.5)
        self.play(Create(reta), run_time=1.5)
        self.wait(0.3)

        # Rótulos 0, 1, 2
        for n in [0, 1, 2]:
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=34)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.5)
        self.wait(0.5)

        # ── Subdivisão em meios (tracejadas) ────────────────────────────────
        subtexto = Text(
            "Dividindo cada unidade em 2 partes iguais:",
            color=COR_FRACAO, font_size=26,
        ).to_edge(DOWN, buff=1.2)
        self.play(FadeIn(subtexto), run_time=1)
        self.wait(0.5)

        tracos_meios = VGroup()
        for num in [1, 3]:          # 1/2 e 3/2
            val = num / 2
            tick = Line(
                reta.n2p(val) + UP * 0.15,
                reta.n2p(val) + DOWN * 0.15,
                color=COR_FRACAO, stroke_width=2.5,
            )
            tracos_meios.add(tick)
        self.play(Create(tracos_meios), run_time=1.5)
        self.wait(0.5)

        # ── Marcar ½ ────────────────────────────────────────────────────────
        ponto_meio = Dot(reta.n2p(0.5), color=COR_FRACAO, radius=0.10)
        label_meio = MathTex(r"\frac{1}{2}", color=COR_FRACAO, font_size=36)
        label_meio.next_to(ponto_meio, UP, buff=0.45)

        seta_meio = Arrow(
            label_meio.get_bottom() + DOWN * 0.05,
            ponto_meio.get_top() + UP * 0.05,
            color=COR_FRACAO, buff=0.05, stroke_width=2.5,
        )

        self.play(FadeIn(ponto_meio), run_time=0.8)
        self.play(Write(label_meio), GrowArrow(seta_meio), run_time=1.5)
        self.wait(1.2)

        # ── Marcar ¾ ────────────────────────────────────────────────────────
        subtexto2 = Text(
            "Dividindo em 4 partes iguais:",
            color=COR_FRACAO, font_size=26,
        ).to_edge(DOWN, buff=1.2)

        tracos_quartos = VGroup()
        for num in [1, 3]:           # 1/4 e 3/4
            val = num / 4
            tick = Line(
                reta.n2p(val) + UP * 0.10,
                reta.n2p(val) + DOWN * 0.10,
                color=YELLOW_E, stroke_width=2,
            )
            tracos_quartos.add(tick)

        self.play(FadeOut(subtexto), FadeIn(subtexto2), run_time=1)
        self.play(Create(tracos_quartos), run_time=1.5)
        self.wait(0.5)

        # Marcar 1/4 (acima) e 3/4 (abaixo) — lados alternados para não sobrepor
        ponto_14 = Dot(reta.n2p(0.25), color=COR_FRACAO, radius=0.10)
        label_14 = MathTex(r"\frac{1}{4}", color=COR_FRACAO, font_size=36)
        label_14.next_to(ponto_14, UP, buff=0.45)
        seta_14 = Arrow(
            label_14.get_bottom() + DOWN * 0.05,
            ponto_14.get_top() + UP * 0.05,
            color=COR_FRACAO, buff=0.05, stroke_width=2.5,
        )
        self.play(FadeIn(ponto_14), run_time=0.8)
        self.play(Write(label_14), GrowArrow(seta_14), run_time=1.5)
        self.wait(1)

        ponto_34 = Dot(reta.n2p(0.75), color=COR_FRACAO, radius=0.10)
        label_34 = MathTex(r"\frac{3}{4}", color=COR_FRACAO, font_size=36)
        label_34.next_to(ponto_34, DOWN, buff=0.45)
        seta_34 = Arrow(
            label_34.get_top() + UP * 0.05,
            ponto_34.get_bottom() + DOWN * 0.05,
            color=COR_FRACAO, buff=0.05, stroke_width=2.5,
        )
        self.play(FadeIn(ponto_34), run_time=0.8)
        self.play(Write(label_34), GrowArrow(seta_34), run_time=1.5)
        self.wait(2)

        # ── Mensagem de síntese ──────────────────────────────────────────────
        self.play(FadeOut(subtexto2), run_time=0.5)
        msg_final = Text(
            "Quanto mais dividimos, mais pontos\npodemos localizar na reta.",
            color=COR_TEXTO, font_size=26, line_spacing=1.2,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg_final), run_time=1.5)
        self.wait(2.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


# ══════════════════════════════════════════════════════════════════════════════
# CENA 4 – Decimais na reta
# ══════════════════════════════════════════════════════════════════════════════
class Cena4_Decimais(Scene):
    """Mostra a equivalência decimal-fração e localização de decimais."""

    def construct(self):
        titulo = Text("Decimais na Reta Numérica", color=COR_TEXTO, font_size=36)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        # ── Equivalências antes da reta ─────────────────────────────────────
        equiv = MathTex(
            r"\frac{1}{2} = 0{,}5",
            r"\qquad",
            r"\frac{3}{4} = 0{,}75",
            r"\qquad",
            r"\frac{1}{4} = 0{,}25",
            color=COR_DECIMAL, font_size=36,
        ).shift(UP * 1.5)

        box = SurroundingRectangle(equiv, color=COR_DECIMAL, buff=0.2, corner_radius=0.1)
        self.play(Write(equiv), Create(box), run_time=2)
        self.wait(1.5)

        # ── Reta numérica ────────────────────────────────────────────────────
        reta = NumberLine(
            x_range=[0, 1, 0.25],
            length=9,
            color=COR_RETA,
            include_tip=False,
            include_numbers=False,
            tick_size=0.12,
        )
        reta.shift(DOWN * 0.8)
        self.play(Create(reta), run_time=1.5)

        # Rótulos inteiros 0 e 1
        for n in [0, 1]:
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=34)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.5)
        self.wait(0.5)

        # ── Posicionar 0,25 – 0,5 – 0,75 ────────────────────────────────────
        decimais = [
            (0.25, r"0{,}25", DOWN),
            (0.50, r"0{,}5",  UP  ),
            (0.75, r"0{,}75", DOWN),
        ]

        for val, tex, direcao in decimais:
            ponto = Dot(reta.n2p(val), color=COR_DECIMAL, radius=0.10)
            lbl   = MathTex(tex, color=COR_DECIMAL, font_size=32)
            lbl.next_to(ponto, direcao, buff=0.4)
            seta  = Arrow(
                lbl.get_edge_center(-direcao) + (-direcao) * 0.05,
                ponto.get_edge_center(direcao) + direcao * 0.05,
                color=COR_DECIMAL, buff=0.05, stroke_width=2,
            )
            self.play(FadeIn(ponto), run_time=0.6)
            self.play(Write(lbl), GrowArrow(seta), run_time=1.4)
            self.wait(0.8)

        self.wait(1.5)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


# ══════════════════════════════════════════════════════════════════════════════
# CENA 5 – Negativos na reta
# ══════════════════════════════════════════════════════════════════════════════
class Cena5_Negativos(Scene):
    """Localiza racionais negativos na reta numérica."""

    def construct(self):
        titulo = Text("Racionais Negativos", color=COR_TEXTO, font_size=36)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        # ── Reta entre −2 e 2 ────────────────────────────────────────────────
        reta = NumberLine(
            x_range=[-2, 2, 1],
            length=10,
            color=COR_RETA,
            include_tip=True,
            include_numbers=False,
            tick_size=0.12,
        )
        reta.shift(DOWN * 0.3)
        self.play(Create(reta), run_time=1.5)

        for n in range(-2, 3):
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=32)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.4)
        self.wait(0.5)

        # ── Simetria: −½ e ½ ────────────────────────────────────────────────
        msg_simetria = Text(
            "Negativos ficam à esquerda do zero,\nsimétricos aos positivos.",
            color=COR_NEGATIVO, font_size=26, line_spacing=1.2,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg_simetria), run_time=1.5)
        self.wait(0.8)

        # Linhas de simetria
        linha_simetria = DashedLine(
            reta.n2p(0) + UP * 1.2,
            reta.n2p(0) + DOWN * 0.6,
            color=GREY, stroke_width=1.5,
        )
        self.play(Create(linha_simetria), run_time=1)
        self.wait(0.5)

        pontos_sim = [
            ( 0.5,  r"\frac{1}{2}",  UP,   COR_FRACAO),
            (-0.5, r"-\frac{1}{2}", DOWN, COR_NEGATIVO),
        ]

        grupo_pontos = VGroup()
        for val, tex, direcao, cor in pontos_sim:
            ponto = Dot(reta.n2p(val), color=cor, radius=0.10)
            lbl   = MathTex(tex, color=cor, font_size=32)
            lbl.next_to(ponto, direcao, buff=0.45)
            self.play(FadeIn(ponto), Write(lbl), run_time=1.2)
            grupo_pontos.add(ponto, lbl)
            self.wait(0.5)

        # Duas linhas saindo do zero — uma ate +1/2, outra ate -1/2
        # mostrando que a distancia ao zero e igual (simetria)
        linha_pos = Line(
            reta.n2p(0), reta.n2p(0.5),
            color=COR_FRACAO, stroke_width=4,
        )
        linha_neg = Line(
            reta.n2p(0), reta.n2p(-0.5),
            color=COR_NEGATIVO, stroke_width=4,
        )
        self.play(Create(linha_pos), Create(linha_neg), run_time=1.8)

        igual_pos = MathTex(r"\tfrac{1}{2}", color=COR_FRACAO, font_size=24)
        igual_pos.next_to(linha_pos.get_center(), UP, buff=0.18)
        igual_neg = MathTex(r"\tfrac{1}{2}", color=COR_NEGATIVO, font_size=24)
        igual_neg.next_to(linha_neg.get_center(), UP, buff=0.18)
        self.play(FadeIn(igual_pos), FadeIn(igual_neg), run_time=1)
        self.wait(2)

        # ── Segundo exemplo: −1,5 ────────────────────────────────────────────
        self.play(FadeOut(msg_simetria), run_time=0.5)
        msg2 = MathTex(
            r"-1{,}5 = -\frac{3}{2} \;\Rightarrow\; \text{entre } -2 \text{ e } -1",
            color=COR_NEGATIVO, font_size=28,
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(msg2), run_time=2)
        self.wait(0.5)

        ponto_neg15 = Dot(reta.n2p(-1.5), color=COR_NEGATIVO, radius=0.12)
        lbl_neg15   = MathTex(r"-1{,}5", color=COR_NEGATIVO, font_size=32)
        lbl_neg15.next_to(ponto_neg15, UP, buff=0.4)

        self.play(FadeIn(ponto_neg15), Write(lbl_neg15), run_time=1.5)
        self.wait(2.5)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


# ══════════════════════════════════════════════════════════════════════════════
# CENA 6 – Exercício modelo (estilo SAEB)
# ══════════════════════════════════════════════════════════════════════════════
class Cena6_Exercicio(Scene):
    """Resolve um item no formato SAEB: identifica o ponto P na reta."""

    def construct(self):
        titulo = Text("Exercício", color=COR_TEXTO, font_size=36)
        titulo.to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        # ── Enunciado ────────────────────────────────────────────────────────
        enunciado = Text(
            'Qual racional representa o ponto P na reta abaixo?',
            color=COR_TEXTO, font_size=26,
        ).next_to(titulo, DOWN, buff=0.4)
        self.play(FadeIn(enunciado), run_time=1.5)
        self.wait(0.8)

        # ── Reta entre −1 e 2 com subdivisão em quartos ─────────────────────
        reta = NumberLine(
            x_range=[-1, 2, 1],
            length=9,
            color=COR_RETA,
            include_tip=True,
            include_numbers=False,
            tick_size=0.12,
        )
        reta.shift(DOWN * 0.5)
        self.play(Create(reta), run_time=1.5)

        for n in [-1, 0, 1, 2]:
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=32)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.4)

        # Marcas de quartos entre 0 e 1
        for k in [1, 2, 3]:
            val = k / 4
            tick = Line(
                reta.n2p(val) + UP * 0.10,
                reta.n2p(val) + DOWN * 0.10,
                color=GREY_B, stroke_width=2,
            )
            self.play(Create(tick), run_time=0.3)
        self.wait(0.5)

        # Ponto P em 3/4
        ponto_P = Dot(reta.n2p(0.75), color=COR_DESTAQUE, radius=0.13)
        label_P = Text("P", color=COR_DESTAQUE, font_size=32)
        label_P.next_to(ponto_P, UP, buff=0.45)

        self.play(FadeIn(ponto_P), Write(label_P), run_time=1.5)
        self.wait(1)

        # ── Raciocínio guiado ────────────────────────────────────────────────
        paso1 = Text("1. P está entre 0 e 1", color=COR_TEXTO, font_size=26)
        paso1.next_to(reta, DOWN, buff=0.9)
        self.play(Write(paso1), run_time=1.5)
        self.wait(1)

        paso2 = Text("2. A unidade está dividida em 4 partes iguais", color=COR_TEXTO, font_size=26)
        paso2.next_to(paso1, DOWN, buff=0.35)
        self.play(Write(paso2), run_time=1.5)
        self.wait(1)

        paso3 = Text("3. P ocupa a 3.ª marca → P = 3/4", color=COR_TEXTO, font_size=26)
        paso3.next_to(paso2, DOWN, buff=0.35)
        self.play(Write(paso3), run_time=1.5)
        self.wait(1)

        # ── Resposta ─────────────────────────────────────────────────────────
        resposta = MathTex(r"P = \frac{3}{4} = 0{,}75", color=COR_DECIMAL, font_size=42)
        box_resp = SurroundingRectangle(resposta, color=COR_DECIMAL, buff=0.2, corner_radius=0.1)
        resp_grupo = VGroup(resposta, box_resp).to_edge(DOWN, buff=0.4)

        self.play(FadeOut(paso1), FadeOut(paso2), FadeOut(paso3), run_time=0.8)
        self.play(Write(resposta), Create(box_resp), run_time=2)
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


# ══════════════════════════════════════════════════════════════════════════════
# CENA 7 – Síntese final
# ══════════════════════════════════════════════════════════════════════════════
class Cena7_Sintese(Scene):
    """Resume os passos para localizar racionais na reta."""

    def construct(self):
        titulo = Text("Como localizar racionais na reta:", color=COR_TEXTO, font_size=34)
        titulo.to_edge(UP, buff=0.5)
        self.play(Write(titulo), run_time=1.5)
        self.wait(0.5)

        passos = [
            ("1.", "Identifique os inteiros vizinhos ao número."),
            ("2.", "Descubra em quantas partes iguais a unidade está dividida."),
            ("3.", "Conte as marcas a partir do inteiro inferior."),
            ("4.", "Converta fração ↔ decimal para confirmar a posição."),
        ]

        grupo = VGroup()
        for num, texto in passos:
            numero = Text(num, color=COR_DESTAQUE, font_size=28)
            corpo  = Text(texto, color=COR_TEXTO,    font_size=26)
            corpo.next_to(numero, RIGHT, buff=0.25)
            linha = VGroup(numero, corpo)
            grupo.add(linha)

        grupo.arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        grupo.next_to(titulo, DOWN, buff=0.6)

        for linha in grupo:
            self.play(FadeIn(linha, shift=RIGHT * 0.3), run_time=1.2)
            self.wait(0.8)

        self.wait(1.5)

        fechamento = Text(
            "Todo número racional tem um lugar\nexato na reta numérica!",
            color=YELLOW, font_size=30, line_spacing=1.2,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(fechamento), run_time=2)
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)


# ══════════════════════════════════════════════════════════════════════════════
# CENA COMPLETA – une todas as cenas em sequência (copiar cada construct)
# ══════════════════════════════════════════════════════════════════════════════
class D17_RetaNumerica(Scene):
    """
    Animação completa do Descritor SAEB D17 – 9.º Ano.
    Executa todas as cenas em ordem, sem sobreposição.

    Renderização recomendada (arquivo único, todas as cenas):
        manim -pqh saeb_d17_reta_numerica.py D17_RetaNumerica

    Para renderizar cada cena individualmente:
        manim -pqh saeb_d17_reta_numerica.py Cena1_Titulo
        manim -pqh saeb_d17_reta_numerica.py Cena2_RetaInteiros
        ... etc.
    """

    def _limpa(self):
        """Remove todos os objetos da tela com FadeOut."""
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)

    # ── Cena 1 ──────────────────────────────────────────────────────────────
    def _cena1(self):
        titulo = Text(
            "Números Racionais\nna Reta Numérica",
            color=COR_TEXTO, font_size=52, line_spacing=1.3,
        ).move_to(ORIGIN)
        descritor = Text(
            "SAEB – D17 | 9.º Ano", color=YELLOW, font_size=28,
        ).next_to(titulo, DOWN, buff=0.6)

        self.play(Write(titulo), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(descritor, shift=UP * 0.3), run_time=1.5)
        self.wait(2)
        self._limpa()

    # ── Cena 2 ──────────────────────────────────────────────────────────────
    def _cena2(self):
        titulo = Text("A Reta Numérica", color=COR_TEXTO, font_size=36).to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5); self.wait(0.4)

        reta = NumberLine(
            x_range=[-4, 4, 1], length=11, color=COR_RETA,
            include_tip=True, include_numbers=False, tick_size=0.12,
        ).move_to(ORIGIN)
        self.play(Create(reta), run_time=2); self.wait(0.4)

        rotulos = VGroup()
        for n in range(-4, 5):
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=30)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            rotulos.add(lbl)
        self.play(LaggedStart(*[Write(r) for r in rotulos], lag_ratio=0.15), run_time=3)
        self.wait(0.8)

        ponto_zero = Dot(reta.n2p(0), color=COR_DESTAQUE, radius=0.10)
        texto_zero = Text("zero", color=COR_DESTAQUE, font_size=24)
        texto_zero.next_to(ponto_zero, UP, buff=0.4)
        self.play(FadeIn(ponto_zero), Write(texto_zero), run_time=1.5); self.wait(1.2)

        msg = Text(
            "Os inteiros ficam espaçados igualmente na reta.",
            color=COR_TEXTO, font_size=26,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg), run_time=1.5); self.wait(2)
        self._limpa()

    # ── Cena 3 ──────────────────────────────────────────────────────────────
    def _cena3(self):
        titulo = Text("Frações na Reta Numérica", color=COR_TEXTO, font_size=36).to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5); self.wait(0.4)

        reta = NumberLine(
            x_range=[0, 2, 1], length=9, color=COR_RETA,
            include_tip=True, include_numbers=False, tick_size=0.12,
        ).shift(DOWN * 0.5)
        self.play(Create(reta), run_time=1.5); self.wait(0.3)

        for n in [0, 1, 2]:
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=34)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.5)
        self.wait(0.5)

        subtexto = Text(
            "Dividindo cada unidade em 2 partes iguais:",
            color=COR_FRACAO, font_size=26,
        ).to_edge(DOWN, buff=1.2)
        self.play(FadeIn(subtexto), run_time=1); self.wait(0.5)

        tracos_meios = VGroup(*[
            Line(reta.n2p(n/2) + UP*0.15, reta.n2p(n/2) + DOWN*0.15,
                 color=COR_FRACAO, stroke_width=2.5)
            for n in [1, 3]
        ])
        self.play(Create(tracos_meios), run_time=1.5); self.wait(0.5)

        ponto_meio = Dot(reta.n2p(0.5), color=COR_FRACAO, radius=0.10)
        label_meio = MathTex(r"\frac{1}{2}", color=COR_FRACAO, font_size=36)
        label_meio.next_to(ponto_meio, UP, buff=0.45)
        seta_meio = Arrow(
            label_meio.get_bottom() + DOWN*0.05, ponto_meio.get_top() + UP*0.05,
            color=COR_FRACAO, buff=0.05, stroke_width=2.5,
        )
        self.play(FadeIn(ponto_meio), run_time=0.8)
        self.play(Write(label_meio), GrowArrow(seta_meio), run_time=1.5); self.wait(1.2)

        subtexto2 = Text(
            "Dividindo em 4 partes iguais:",
            color=COR_FRACAO, font_size=26,
        ).to_edge(DOWN, buff=1.2)
        self.play(FadeOut(subtexto), FadeIn(subtexto2), run_time=1)

        tracos_quartos = VGroup(*[
            Line(reta.n2p(n/4) + UP*0.10, reta.n2p(n/4) + DOWN*0.10,
                 color=YELLOW_E, stroke_width=2)
            for n in [1, 3]
        ])
        self.play(Create(tracos_quartos), run_time=1.5); self.wait(0.5)

        ponto_14 = Dot(reta.n2p(0.25), color=COR_FRACAO, radius=0.10)
        label_14 = MathTex(r"\frac{1}{4}", color=COR_FRACAO, font_size=36)
        label_14.next_to(ponto_14, UP, buff=0.45)
        seta_14 = Arrow(
            label_14.get_bottom() + DOWN*0.05, ponto_14.get_top() + UP*0.05,
            color=COR_FRACAO, buff=0.05, stroke_width=2.5,
        )
        self.play(FadeIn(ponto_14), run_time=0.8)
        self.play(Write(label_14), GrowArrow(seta_14), run_time=1.5); self.wait(1)

        ponto_34 = Dot(reta.n2p(0.75), color=COR_FRACAO, radius=0.10)
        label_34 = MathTex(r"\frac{3}{4}", color=COR_FRACAO, font_size=36)
        label_34.next_to(ponto_34, DOWN, buff=0.45)
        seta_34 = Arrow(
            label_34.get_top() + UP*0.05, ponto_34.get_bottom() + DOWN*0.05,
            color=COR_FRACAO, buff=0.05, stroke_width=2.5,
        )
        self.play(FadeIn(ponto_34), run_time=0.8)
        self.play(Write(label_34), GrowArrow(seta_34), run_time=1.5); self.wait(2)

        self.play(FadeOut(subtexto2), run_time=0.5)
        msg_final = Text(
            "Quanto mais dividimos, mais pontos\npodemos localizar na reta.",
            color=COR_TEXTO, font_size=26, line_spacing=1.2,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg_final), run_time=1.5); self.wait(2.5)
        self._limpa()

    # ── Cena 4 ──────────────────────────────────────────────────────────────
    def _cena4(self):
        titulo = Text("Decimais na Reta Numérica", color=COR_TEXTO, font_size=36).to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5); self.wait(0.5)

        equiv = MathTex(
            r"\frac{1}{2} = 0{,}5", r"\qquad",
            r"\frac{3}{4} = 0{,}75", r"\qquad",
            r"\frac{1}{4} = 0{,}25",
            color=COR_DECIMAL, font_size=36,
        ).shift(UP * 1.5)
        box = SurroundingRectangle(equiv, color=COR_DECIMAL, buff=0.2, corner_radius=0.1)
        self.play(Write(equiv), Create(box), run_time=2); self.wait(1.5)

        reta = NumberLine(
            x_range=[0, 1, 0.25], length=9, color=COR_RETA,
            include_tip=False, include_numbers=False, tick_size=0.12,
        ).shift(DOWN * 0.8)
        self.play(Create(reta), run_time=1.5)

        for n in [0, 1]:
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=34)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.5)
        self.wait(0.5)

        for val, tex, direcao in [
            (0.25, r"0{,}25", DOWN),
            (0.50, r"0{,}5",  UP  ),
            (0.75, r"0{,}75", DOWN),
        ]:
            ponto = Dot(reta.n2p(val), color=COR_DECIMAL, radius=0.10)
            lbl   = MathTex(tex, color=COR_DECIMAL, font_size=32)
            lbl.next_to(ponto, direcao, buff=0.4)
            seta  = Arrow(
                lbl.get_edge_center(-direcao) + (-direcao)*0.05,
                ponto.get_edge_center(direcao) + direcao*0.05,
                color=COR_DECIMAL, buff=0.05, stroke_width=2,
            )
            self.play(FadeIn(ponto), run_time=0.6)
            self.play(Write(lbl), GrowArrow(seta), run_time=1.4); self.wait(0.8)

        self.wait(1.5)
        self._limpa()

    # ── Cena 5 ──────────────────────────────────────────────────────────────
    def _cena5(self):
        titulo = Text("Racionais Negativos", color=COR_TEXTO, font_size=36).to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5); self.wait(0.5)

        reta = NumberLine(
            x_range=[-2, 2, 1], length=10, color=COR_RETA,
            include_tip=True, include_numbers=False, tick_size=0.12,
        ).shift(DOWN * 0.3)
        self.play(Create(reta), run_time=1.5)

        for n in range(-2, 3):
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=32)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.4)
        self.wait(0.5)

        msg = Text(
            "Negativos ficam à esquerda do zero,\nsimétricos aos positivos.",
            color=COR_NEGATIVO, font_size=26, line_spacing=1.2,
        ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg), run_time=1.5); self.wait(0.8)

        linha_simetria = DashedLine(
            reta.n2p(0) + UP*1.2, reta.n2p(0) + DOWN*0.6,
            color=GREY, stroke_width=1.5,
        )
        self.play(Create(linha_simetria), run_time=1); self.wait(0.5)

        for val, tex, direcao, cor in [
            ( 0.5,  r"\frac{1}{2}",  UP,   COR_FRACAO),
            (-0.5, r"-\frac{1}{2}", DOWN, COR_NEGATIVO),
        ]:
            ponto = Dot(reta.n2p(val), color=cor, radius=0.10)
            lbl   = MathTex(tex, color=cor, font_size=32)
            lbl.next_to(ponto, direcao, buff=0.45)
            self.play(FadeIn(ponto), Write(lbl), run_time=1.2); self.wait(0.5)

        # Duas linhas saindo do zero: uma ate +1/2 (amarelo) e outra ate -1/2 (vermelho)
        # mostrando visualmente que as distancias ao zero sao iguais
        linha_pos = Line(
            reta.n2p(0), reta.n2p(0.5),
            color=COR_FRACAO, stroke_width=4,
        )
        linha_neg = Line(
            reta.n2p(0), reta.n2p(-0.5),
            color=COR_NEGATIVO, stroke_width=4,
        )
        self.play(Create(linha_pos), Create(linha_neg), run_time=1.8)

        # Marcas de distancia igual acima de cada segmento
        igual_pos = MathTex(r"\tfrac{1}{2}", color=COR_FRACAO, font_size=24)
        igual_pos.next_to(linha_pos.get_center(), UP, buff=0.18)
        igual_neg = MathTex(r"\tfrac{1}{2}", color=COR_NEGATIVO, font_size=24)
        igual_neg.next_to(linha_neg.get_center(), UP, buff=0.18)
        self.play(FadeIn(igual_pos), FadeIn(igual_neg), run_time=1)
        self.wait(1.5)

        self.play(FadeOut(msg), run_time=0.5)
        msg2 = MathTex(
            r"-1{,}5 = -\frac{3}{2} \;\Rightarrow\; \text{entre } -2 \text{ e } -1",
            color=COR_NEGATIVO, font_size=28,
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(msg2), run_time=2); self.wait(0.5)

        ponto_neg15 = Dot(reta.n2p(-1.5), color=COR_NEGATIVO, radius=0.12)
        lbl_neg15   = MathTex(r"-1{,}5", color=COR_NEGATIVO, font_size=32)
        lbl_neg15.next_to(ponto_neg15, UP, buff=0.4)
        self.play(FadeIn(ponto_neg15), Write(lbl_neg15), run_time=1.5); self.wait(2.5)
        self._limpa()

    # ── Cena 6 ──────────────────────────────────────────────────────────────
    def _cena6(self):
        titulo = Text("Exercício", color=COR_TEXTO, font_size=36).to_edge(UP, buff=0.4)
        self.play(Write(titulo), run_time=1.5); self.wait(0.5)

        enunciado = Text(
            "Qual racional representa o ponto P na reta abaixo?",
            color=COR_TEXTO, font_size=26,
        ).next_to(titulo, DOWN, buff=0.4)
        self.play(FadeIn(enunciado), run_time=1.5); self.wait(0.8)

        reta = NumberLine(
            x_range=[-1, 2, 1], length=9, color=COR_RETA,
            include_tip=True, include_numbers=False, tick_size=0.12,
        ).shift(DOWN * 0.5)
        self.play(Create(reta), run_time=1.5)

        for n in [-1, 0, 1, 2]:
            lbl = MathTex(str(n), color=COR_INTEIRO, font_size=32)
            lbl.next_to(reta.n2p(n), DOWN, buff=0.35)
            self.play(Write(lbl), run_time=0.4)

        for k in [1, 2, 3]:
            tick = Line(
                reta.n2p(k/4) + UP*0.10, reta.n2p(k/4) + DOWN*0.10,
                color=GREY_B, stroke_width=2,
            )
            self.play(Create(tick), run_time=0.3)
        self.wait(0.5)

        ponto_P = Dot(reta.n2p(0.75), color=COR_DESTAQUE, radius=0.13)
        label_P = Text("P", color=COR_DESTAQUE, font_size=32)
        label_P.next_to(ponto_P, UP, buff=0.45)
        self.play(FadeIn(ponto_P), Write(label_P), run_time=1.5); self.wait(1)

        passos = [
            "1. P está entre 0 e 1",
            "2. A unidade está dividida em 4 partes iguais",
            "3. P ocupa a 3.ª marca → P = 3/4",
        ]
        objs_passos = []
        ancora = reta
        for texto in passos:
            obj = Text(texto, color=COR_TEXTO, font_size=26)
            if not objs_passos:
                obj.next_to(ancora, DOWN, buff=0.9)
            else:
                obj.next_to(objs_passos[-1], DOWN, buff=0.35)
            objs_passos.append(obj)
            self.play(Write(obj), run_time=1.5); self.wait(1)

        resposta = MathTex(r"P = \frac{3}{4} = 0{,}75", color=COR_DECIMAL, font_size=42)
        box_resp = SurroundingRectangle(resposta, color=COR_DECIMAL, buff=0.2, corner_radius=0.1)
        VGroup(resposta, box_resp).to_edge(DOWN, buff=0.4)
        self.play(*[FadeOut(o) for o in objs_passos], run_time=0.8)
        self.play(Write(resposta), Create(box_resp), run_time=2); self.wait(3)
        self._limpa()

    # ── Cena 7 ──────────────────────────────────────────────────────────────
    def _cena7(self):
        titulo = Text("Como localizar racionais na reta:", color=COR_TEXTO, font_size=34)
        titulo.to_edge(UP, buff=0.5)
        self.play(Write(titulo), run_time=1.5); self.wait(0.5)

        passos = [
            ("1.", "Identifique os inteiros vizinhos ao número."),
            ("2.", "Descubra em quantas partes iguais a unidade está dividida."),
            ("3.", "Conte as marcas a partir do inteiro inferior."),
            ("4.", "Converta fração ↔ decimal para confirmar a posição."),
        ]
        grupo = VGroup()
        for num, texto in passos:
            numero = Text(num, color=COR_DESTAQUE, font_size=28)
            corpo  = Text(texto, color=COR_TEXTO,  font_size=26)
            corpo.next_to(numero, RIGHT, buff=0.25)
            grupo.add(VGroup(numero, corpo))
        grupo.arrange(DOWN, aligned_edge=LEFT, buff=0.55).next_to(titulo, DOWN, buff=0.6)

        for linha in grupo:
            self.play(FadeIn(linha, shift=RIGHT*0.3), run_time=1.2); self.wait(0.8)

        self.wait(1.5)
        fechamento = Text(
            "Todo número racional tem um lugar\nexato na reta numérica!",
            color=YELLOW, font_size=30, line_spacing=1.2,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(fechamento), run_time=2); self.wait(3)
        self._limpa()

    # ── construct principal ──────────────────────────────────────────────────
    def construct(self):
        self._cena1()
        self._cena2()
        self._cena3()
        self._cena4()
        self._cena5()
        self._cena6()
        self._cena7()


# ══════════════════════════════════════════════════════════════════════════════
# LOGO – Identidade visual da professora
# ══════════════════════════════════════════════════════════════════════════════
class LogoEmillyMayre(Scene):
    """Objetivo: Exibir a identidade visual da professora."""
    def construct(self):
        ESCURO_L = "#1a1a2e"
        DOURADO  = "#C8A84B"
        CINZA_L  = "#888899"

        bg = Rectangle(width=16, height=9,
                       fill_color=WHITE, fill_opacity=1, stroke_width=0)
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

        logo_h = ParametricFunction(inf_h, t_range=[0, TAU],
                                    color="#3a3a5c",
                                    stroke_width=2.5).move_to(UP * 0.5)
        logo_v = ParametricFunction(inf_v, t_range=[0, TAU],
                                    color="#9999bb",
                                    stroke_width=2.5).move_to(UP * 0.5)
        circ = Circle(radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
                      color=ESCURO_L, stroke_width=0).move_to(UP * 0.5)
        em = Text("EM", color=WHITE, font_size=22,
                  weight=BOLD).move_to(circ.get_center())
        grp = VGroup(logo_h, logo_v)
        nome = Text("Emilly Mayre", color=ESCURO_L,
                    font_size=28, weight=BOLD)
        nome.next_to(grp, DOWN, buff=0.55)
        linha = Line(LEFT * 1.6, RIGHT * 1.6,
                     color=DOURADO, stroke_width=3.5)
        linha.next_to(nome, DOWN, buff=0.16)
        cargo = Text("PROFESSORA DE MATEMÁTICA",
                     color=CINZA_L, font_size=14)
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
