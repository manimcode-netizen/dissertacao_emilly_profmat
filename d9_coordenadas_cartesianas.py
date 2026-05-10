from manim import *

# ================================================================
# D9 – SAEB Matemática 9º Ano
# Conceito : Interpretar informações apresentadas por meio de
#            coordenadas cartesianas.
# Nível    : Ensino Fundamental – 9º Ano
#
# ZONA SEGURA: y entre -2.6 e +2.6 | x entre -6.5 e +6.5
# Paleta: BLUE_C=base | YELLOW=destaque | GREEN_C=fórmula/resultado
#         ORANGE=acento/label | WHITE=texto geral
# ================================================================

COR_BASE     = BLUE_C
COR_DESTAQUE = YELLOW
COR_FORMULA  = GREEN_C
COR_TITULO   = WHITE
COR_ACENTO   = ORANGE
COR_PONTO    = RED

TOPO      =  2.6
CONT_TOPO =  1.9
CONT_BASE = -2.2

# Escala de unidade no plano cartesiano
U = 0.72   # 1 unidade matemática = 0.72 unidades Manim

# Centro do plano deslocado para a esquerda para dar espaço a legendas
CX = -1.8  # centro x do plano na tela


def titulo_cena(texto, cor=COR_TITULO, escala=0.62):
    t = Text(texto, color=cor).scale(escala)
    t.move_to(UP * TOPO)
    return t


def separador():
    return Line(LEFT * 6.5, RIGHT * 6.5,
                color=GREY_D, stroke_width=1.5).move_to(UP * (TOPO - 0.48))


def coord_to_screen(x, y):
    """Converte coordenada matemática para posição na tela."""
    return np.array([CX + x * U, y * U, 0])


def make_axes(x_range=(-5, 5), y_range=(-3, 3)):
    """
    Cria eixos cartesianos com marcações e rótulos.
    Retorna (eixo_x, eixo_y, marcacoes, rotulos)
    """
    # Eixos
    eixo_x = Arrow(
        coord_to_screen(x_range[0] - 0.3, 0),
        coord_to_screen(x_range[1] + 0.3, 0),
        color=COR_TITULO, buff=0, stroke_width=2.0,
        tip_length=0.18,
    )
    eixo_y = Arrow(
        coord_to_screen(0, y_range[0] - 0.3),
        coord_to_screen(0, y_range[1] + 0.3),
        color=COR_TITULO, buff=0, stroke_width=2.0,
        tip_length=0.18,
    )

    # Rótulos dos eixos
    rot_x = MathTex("x", color=COR_TITULO).scale(0.55)
    rot_x.move_to(coord_to_screen(x_range[1] + 0.55, 0))
    rot_y = MathTex("y", color=COR_TITULO).scale(0.55)
    rot_y.move_to(coord_to_screen(0.28, y_range[1] + 0.42))

    # Marcações nos eixos
    marcacoes = VGroup()
    numeros   = VGroup()

    for v in range(x_range[0], x_range[1] + 1):
        if v == 0:
            continue
        tick = Line(
            coord_to_screen(v, -0.12), coord_to_screen(v, 0.12),
            color=GREY_B, stroke_width=1.2,
        )
        marcacoes.add(tick)
        if abs(v) <= 4:   # apenas números visíveis
            num = MathTex(str(v), color=GREY_B).scale(0.38)
            num.move_to(coord_to_screen(v, -0.38))
            numeros.add(num)

    for v in range(y_range[0], y_range[1] + 1):
        if v == 0:
            continue
        tick = Line(
            coord_to_screen(-0.12, v), coord_to_screen(0.12, v),
            color=GREY_B, stroke_width=1.2,
        )
        marcacoes.add(tick)
        if abs(v) <= 2:
            num = MathTex(str(v), color=GREY_B).scale(0.38)
            num.move_to(coord_to_screen(-0.38, v))
            numeros.add(num)

    # Zero na origem
    zero = MathTex("0", color=GREY_B).scale(0.38)
    zero.move_to(coord_to_screen(-0.32, -0.32))
    numeros.add(zero)

    eixos = VGroup(eixo_x, eixo_y, rot_x, rot_y)
    return eixos, marcacoes, numeros


# ══════════════════════════════════════════════════════════════
# CENA 1 – Apresentação do descritor D9
# ══════════════════════════════════════════════════════════════
class C01_Apresentacao(Scene):
    """
    Conceito: Apresentação do descritor D9 – SAEB 9º Ano
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Situar o aluno no contexto do descritor
    """
    def construct(self):
        # Faixa de identificação SAEB
        faixa = Rectangle(width=14.4, height=1.05,
                          fill_color=DARK_BLUE, fill_opacity=0.9,
                          stroke_width=0).move_to(UP * 2.55)
        saeb = Text("SAEB  |  Matemática  |  9º Ano",
                    color=COR_ACENTO).scale(0.52)
        saeb.move_to(faixa.get_center())

        # Código do descritor em destaque
        codigo = Text("D9", color=COR_DESTAQUE).scale(2.4)
        codigo.move_to(UP * 0.85)

        linha = Line(LEFT * 3.0, RIGHT * 3.0,
                     color=COR_BASE, stroke_width=2.5)
        linha.next_to(codigo, DOWN, buff=0.35)

        desc = Text(
            "Interpretar informações apresentadas\n"
            "por meio de coordenadas cartesianas.",
            color=COR_TITULO, line_spacing=1.5,
        ).scale(0.60)
        desc.next_to(linha, DOWN, buff=0.45)

        self.play(FadeIn(faixa), FadeIn(saeb), run_time=0.8)
        self.play(Write(codigo), run_time=1.2)
        self.play(Create(linha), run_time=0.6)
        self.play(Write(desc), run_time=2.0)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 2 – O que são coordenadas cartesianas?
# ══════════════════════════════════════════════════════════════
class C02_Introducao(Scene):
    """
    Conceito: Definição do sistema de coordenadas cartesianas
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve compreender que um ponto no plano é
              determinado por um par ordenado (x, y)
    """
    def construct(self):
        tit = titulo_cena("O que são Coordenadas Cartesianas?")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        # Bloco 1 — label "Definição" alinhado à esquerda
        def_lbl = Text("Definição:", color=COR_ACENTO).scale(0.50)
        def_lbl.move_to(LEFT * 4.5 + UP * 1.55)

        # Texto em duas linhas para caber na zona segura
        def_txt = Text(
            "Um sistema que usa dois números para\n"
            "localizar qualquer ponto no plano.",
            color=COR_TITULO, line_spacing=1.4,
        ).scale(0.50)
        def_txt.next_to(def_lbl, DOWN, buff=0.20)
        def_txt.align_to(def_lbl, LEFT)

        self.play(FadeIn(def_lbl), run_time=0.6)
        self.play(Write(def_txt), run_time=1.5)
        self.wait(0.8)

        # Bloco 2 — Par ordenado
        par_lbl = Text("Par ordenado:", color=COR_ACENTO).scale(0.50)
        par_lbl.next_to(def_txt, DOWN, buff=0.42)
        par_lbl.align_to(def_lbl, LEFT)

        par = MathTex(
            r"P = (", r"x", r",\;", r"y", r")",
            color=COR_TITULO,
        ).scale(1.05)
        par[1].set_color(COR_BASE)      # x em azul
        par[3].set_color(COR_DESTAQUE)  # y em amarelo
        par.next_to(par_lbl, DOWN, buff=0.22)
        par.align_to(par_lbl, LEFT)

        self.play(FadeIn(par_lbl), run_time=0.6)
        self.play(Write(par), run_time=1.2)
        self.wait(0.5)

        # Bloco 3 — Legendas x e y
        leg_x = Text("→ abscissa (horizontal)", color=COR_BASE).scale(0.46)
        leg_x.next_to(par, DOWN, buff=0.25)
        leg_x.align_to(par, LEFT)

        leg_y = Text("→ ordenada (vertical)", color=COR_DESTAQUE).scale(0.46)
        leg_y.next_to(leg_x, DOWN, buff=0.18)
        leg_y.align_to(leg_x, LEFT)

        self.play(FadeIn(leg_x), run_time=0.8)
        self.play(FadeIn(leg_y), run_time=0.8)
        self.wait(0.6)

        # Regra essencial — cor verde, centralizada abaixo das legendas
        regra = Text(
            "A ordem importa:  (3, 5) ≠ (5, 3)",
            color=COR_FORMULA,
        ).scale(0.52)
        regra.next_to(leg_y, DOWN, buff=0.42)
        regra.set_x(0)
        caixa_regra = SurroundingRectangle(
            regra, color=COR_FORMULA,
            buff=0.22, corner_radius=0.12, stroke_width=2.2,
        )
        self.play(Write(regra), Create(caixa_regra), run_time=1.3)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)

# ══════════════════════════════════════════════════════════════
# CENA 3 – Construção do Plano Cartesiano
# ══════════════════════════════════════════════════════════════
class C03_PlanoCartesiano(Scene):
    """
    Conceito: Construção visual dos eixos do plano cartesiano com destaque
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve reconhecer os eixos x e y e a origem
    """
    def construct(self):
        tit = titulo_cena("O Plano Cartesiano")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        U_local = 0.82
        CX_local = 0.0
        # Plano deslocado para baixo para não colar no separador
        CY_local = -0.30

        def sc(x, y):
            return np.array([CX_local + x * U_local,
                             CY_local + y * U_local, 0])

        # Eixo x e eixo y — criados como objetos separados para poder colorir
        eixo_x = Arrow(sc(-5, 0), sc(5, 0), color=COR_TITULO,
                       buff=0, stroke_width=2.2, tip_length=0.18)
        eixo_y = Arrow(sc(0, -2.5), sc(0, 2.2), color=COR_TITULO,
                       buff=0, stroke_width=2.2, tip_length=0.18)

        rot_x = MathTex("x", color=COR_TITULO).scale(0.60)
        rot_x.move_to(sc(5.35, 0))
        rot_y = MathTex("y", color=COR_TITULO).scale(0.60)
        rot_y.move_to(sc(0.28, 2.45))

        # Marcações e números
        marcacoes = VGroup()
        numeros   = VGroup()
        for v in range(-4, 5):
            if v == 0:
                continue
            tick = Line(sc(v, -0.10), sc(v, 0.10),
                        color=GREY_B, stroke_width=1.2)
            marcacoes.add(tick)
            num = MathTex(str(v), color=GREY_B).scale(0.38)
            num.move_to(sc(v, -0.40))
            numeros.add(num)
        for v in [-2, -1, 1, 2]:
            tick = Line(sc(-0.10, v), sc(0.10, v),
                        color=GREY_B, stroke_width=1.2)
            marcacoes.add(tick)
            num = MathTex(str(v), color=GREY_B).scale(0.38)
            num.move_to(sc(-0.35, v))
            numeros.add(num)
        zero = MathTex("0", color=GREY_B).scale(0.38)
        zero.move_to(sc(-0.32, -0.35))
        numeros.add(zero)

        # Animar eixos sequencialmente
        self.play(Create(eixo_x), run_time=1.2)
        self.wait(0.2)
        self.play(Create(eixo_y), run_time=1.2)
        self.wait(0.2)
        self.play(Write(rot_x), Write(rot_y), run_time=0.8)
        self.play(Create(marcacoes), Write(numeros), run_time=1.0)
        self.wait(0.5)

        # ── Destaque eixo x em azul ──────────────────────────────
        nome_x = Text("Eixo das Abscissas (x)", color=COR_BASE).scale(0.48)
        nome_x.move_to(sc(2.8, -0.82))
        seta_x = Arrow(
            nome_x.get_top() + UP * 0.05,
            sc(2.8, -0.18),
            color=COR_BASE, buff=0.05, stroke_width=1.8, tip_length=0.15,
        )
        # Colorir eixo x em azul com efeito
        self.play(
            eixo_x.animate.set_color(COR_BASE),
            rot_x.animate.set_color(COR_BASE),
            run_time=0.7,
        )
        self.play(FadeIn(nome_x), run_time=0.8)
        self.play(Create(seta_x), run_time=0.6)
        self.wait(0.5)
        # Voltar eixo x ao branco
        self.play(
            eixo_x.animate.set_color(COR_TITULO),
            rot_x.animate.set_color(COR_TITULO),
            run_time=0.5,
        )
        self.wait(0.3)

        # ── Destaque eixo y em amarelo ───────────────────────────
        nome_y = Text("Eixo das Ordenadas (y)", color=COR_DESTAQUE).scale(0.48)
        nome_y.move_to(sc(3.0, 1.6))
        seta_y = Arrow(
            nome_y.get_left() + LEFT * 0.05,
            sc(0.18, 1.6),
            color=COR_DESTAQUE, buff=0.05, stroke_width=1.8, tip_length=0.15,
        )
        # Colorir eixo y em amarelo com efeito
        self.play(
            eixo_y.animate.set_color(COR_DESTAQUE),
            rot_y.animate.set_color(COR_DESTAQUE),
            run_time=0.7,
        )
        self.play(FadeIn(nome_y), run_time=0.8)
        self.play(Create(seta_y), run_time=0.6)
        self.wait(0.5)
        # Voltar eixo y ao branco
        self.play(
            eixo_y.animate.set_color(COR_TITULO),
            rot_y.animate.set_color(COR_TITULO),
            run_time=0.5,
        )
        self.wait(0.3)

        # ── Origem ──────────────────────────────────────────────
        origem_pt = Dot(sc(0, 0), color=COR_ACENTO, radius=0.12)
        origem_lbl = Text("Origem  O(0, 0)", color=COR_ACENTO).scale(0.46)
        # Label à esquerda e abaixo do ponto, longe dos números
        origem_lbl.move_to(sc(-1.8, -0.65))

        self.play(GrowFromCenter(origem_pt), run_time=0.7)
        self.play(FadeIn(origem_lbl), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 4 – Os Quatro Quadrantes
# ══════════════════════════════════════════════════════════════

class C04_Quadrantes(Scene):
    """
    Conceito: Os quatro quadrantes do plano cartesiano e seus sinais
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve identificar o quadrante de um ponto
              a partir do sinal de suas coordenadas e entender
              a numeração no sentido anti-horário
    """
    def construct(self):
        tit = titulo_cena("Os Quatro Quadrantes")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        # Eixos base
        eixos, marcacoes, numeros = make_axes((-4, 4), (-2, 2))
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        COR_Q1 = BLUE
        COR_Q2 = GREEN
        COR_Q3 = ORANGE
        COR_Q4 = RED

        # Cada quadrante: centro exato em coordenadas de grade
        # Q1: x de 0 a 4, y de 0 a 2  → centro (2, 1)
        # Q2: x de -4 a 0, y de 0 a 2 → centro (-2, 1)
        # Q3: x de -4 a 0, y de -2 a 0 → centro (-2, -1)
        # Q4: x de 0 a 4, y de -2 a 0  → centro (2, -1)
        quadrantes = [
            ("1º Quadrante", COR_Q1, "+x, +y",  BLUE,    2.0,  1.0),
            ("2º Quadrante", COR_Q2, "–x, +y",  GREEN,  -2.0,  1.0),
            ("3º Quadrante", COR_Q3, "–x, –y",  ORANGE, -2.0, -1.0),
            ("4º Quadrante", COR_Q4, "+x, –y",  RED,     2.0, -1.0),
        ]

        for nome, cor, sinais, cor_bg, cx, cy in quadrantes:
            # Retângulo cobre exatamente metade do plano visível (4×2 unidades)
            regiao = Rectangle(
                width=4 * U, height=2 * U,
                fill_color=cor_bg,
                fill_opacity=0.18,
                stroke_width=0,
            )
            regiao.move_to(coord_to_screen(cx, cy))

            # Nome posicionado dentro do quadrante, longe do eixo x
            # Para quadrantes superiores (cy > 0): empurra para cima
            # Para quadrantes inferiores (cy < 0): empurra para baixo
            if cy > 0:
                nome_y = cy * 1.55
            else:
                nome_y = cy - 0.35  # ← AJUSTE: desce para longe do eixo x

            nome_txt = Text(nome, color=cor, weight=BOLD).scale(0.46)
            nome_txt.move_to(coord_to_screen(cx, nome_y))

            # Sinais logo abaixo do nome — sempre dentro da região sombreada
            sinal_txt = Text(sinais, color=cor).scale(0.40)
            sinal_txt.next_to(nome_txt, DOWN, buff=0.14)

            self.play(FadeIn(regiao), run_time=0.6)
            self.play(Write(nome_txt), run_time=0.7)
            self.play(FadeIn(sinal_txt), run_time=0.5)
            self.wait(0.4)

        # ── Símbolo anti-horário na origem ───────────────────────
        origem = coord_to_screen(0, 0)

        # Arco começa em 0 (lado direito, 1º quadrante) e gira ~300° no sentido anti-horário
        arco = Arc(
            radius=0.32,
            start_angle=0,          # ← começa no 1º quadrante (ângulo 0 = direita)
            angle=5 * PI / 3,       # ~300° no sentido anti-horário
            color=COR_TITULO,
            stroke_width=2.5,
        )
        arco.move_to(origem)

        # Ponta da seta no ângulo final do arco
        ang_final = 0 + 5 * PI / 3
        tang = np.array([-np.sin(ang_final), np.cos(ang_final), 0])
        ponta_pos = origem + 0.32 * np.array([
            np.cos(ang_final), np.sin(ang_final), 0
        ])
        seta_ponta = Arrow(
            ponta_pos - tang * 0.001,
            ponta_pos + tang * 0.18,
            color=COR_TITULO,
            buff=0,
            stroke_width=2.0,
            tip_length=0.16,
            max_stroke_width_to_length_ratio=10,
        )

        dot_origem = Dot(origem, color=COR_TITULO, radius=0.06)

        # ← AJUSTE: label movido para abaixo do plano cartesiano, fora dos eixos
        lbl_ahc = Text("Sentido anti-horário", color=COR_TITULO).scale(0.32)
        lbl_ahc.move_to(coord_to_screen(0, -2.7))

        self.play(GrowFromCenter(dot_origem), run_time=0.5)
        self.play(Create(arco), run_time=1.0)
        self.play(Create(seta_ponta), run_time=0.5)
        self.play(FadeIn(lbl_ahc), run_time=0.7)
        self.wait(0.5)

        # ── Quadro "Sinais por Quadrante" à direita ──────────────
        dados_resumo = [
            ("1º Q:  (+, +)", COR_Q1),
            ("2º Q:  (–, +)", COR_Q2),
            ("3º Q:  (–, –)", COR_Q3),
            ("4º Q:  (+, –)", COR_Q4),
        ]
        linhas_resumo = VGroup()
        y_lin = 0.78
        for txt, cor_r in dados_resumo:
            t = Text(txt, color=cor_r).scale(0.44)
            t.move_to(RIGHT * 4.8 + UP * y_lin)
            linhas_resumo.add(t)
            y_lin -= 0.52

        titulo_resumo = Text("Sinais por Quadrante", color=COR_ACENTO).scale(0.44)
        titulo_resumo.next_to(linhas_resumo, UP, buff=0.28)
        titulo_resumo.align_to(linhas_resumo, LEFT)

        grp_resumo = VGroup(titulo_resumo, linhas_resumo)
        caixa_resumo = SurroundingRectangle(
            grp_resumo, color=COR_ACENTO,
            buff=0.22, corner_radius=0.14, stroke_width=2.0,
        )

        self.play(FadeIn(titulo_resumo), run_time=0.5)
        for t in linhas_resumo:
            self.play(FadeIn(t), run_time=0.4)
        self.play(Create(caixa_resumo), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)

#
# ══════════════════════════════════════════════════════════════
# CENA 5 – Localizando um Ponto P(3, 2)
# ══════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════
# CENA 5 – Localizando um Ponto P(3, 2)
# ══════════════════════════════════════════════════════════════
class C05_LocalizandoPonto(Scene):
    """
    Conceito: Localização de um ponto no plano cartesiano
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve compreender como plotar um ponto
              a partir de suas coordenadas (x, y)
    """
    def construct(self):
        tit = titulo_cena("Localizando o Ponto  P(3, 2)")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = make_axes((-4, 4), (-2, 2))
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        # ── PASSO 1: mover 3 unidades para a direita ──────────────
        passo1_lbl = Text("Passo 1: mova 3 unidades para a direita (x = 3)",
                          color=COR_BASE).scale(0.46)
        passo1_lbl.move_to(DOWN * 1.90)
        self.play(FadeIn(passo1_lbl), run_time=0.8)

        # Realça o "3" no eixo x
        tick_x3 = Dot(coord_to_screen(3, 0), color=COR_BASE, radius=0.12)
        self.play(GrowFromCenter(tick_x3), run_time=0.7)

        # Reta pontilhada AZUL vertical passando por x=3 (paralela ao eixo y)
        # — permanece na tela até o FadeOut final
        reta_v = DashedLine(coord_to_screen(3, -2), coord_to_screen(3, 2),
                            color=COR_BASE, stroke_width=2.0, dash_length=0.12)
        self.play(Create(reta_v), run_time=1.0)
        self.wait(0.8)

        # ── PASSO 2: subir 2 unidades ──────────────────────────────
        # Passo 1 some do texto, reta azul PERMANECE
        passo2_lbl = Text("Passo 2: suba 2 unidades (y = 2)",
                          color=COR_DESTAQUE).scale(0.46)
        passo2_lbl.move_to(DOWN * 1.90)
        self.play(FadeOut(passo1_lbl), run_time=0.4)
        self.play(FadeIn(passo2_lbl), run_time=0.8)

        # Realça o "2" no eixo y
        tick_y2 = Dot(coord_to_screen(0, 2), color=COR_DESTAQUE, radius=0.10)
        self.play(GrowFromCenter(tick_y2), run_time=0.7)

        # Reta pontilhada AMARELA horizontal passando por y=2 (paralela ao eixo x)
        # — permanece na tela até o FadeOut final
        reta_h = DashedLine(coord_to_screen(-4, 2), coord_to_screen(4, 2),
                            color=COR_DESTAQUE, stroke_width=2.0, dash_length=0.12)
        self.play(Create(reta_h), run_time=1.0)
        self.wait(0.8)

        # ── INTERSEÇÃO: marca o ponto P(3,2) ──────────────────────
        ponto_p = Dot(coord_to_screen(3, 2), color=COR_PONTO, radius=0.13)
        lbl_p = MathTex(r"P(3,\,2)", color=COR_PONTO).scale(0.60)
        lbl_p.next_to(ponto_p, UR, buff=0.15)
        self.play(GrowFromCenter(ponto_p), run_time=0.8)
        self.play(Write(lbl_p), run_time=0.8)
        self.wait(0.5)

        # ── CONCLUSÃO: substitui apenas o texto do passo 2 ────────
        # Retas pontilhadas e ponto PERMANECEM visíveis
        self.play(FadeOut(passo2_lbl), run_time=0.4)
        concl = Text("O ponto P está no 1º Quadrante  (+, +)",
                     color=COR_FORMULA).scale(0.48)
        concl.move_to(DOWN * 2.30)
        caixa_c = SurroundingRectangle(concl, color=COR_FORMULA,
                                       buff=0.18, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(concl), Create(caixa_c), run_time=1.2)
        self.wait(2.5)

        # ── FadeOut final — tudo some junto ───────────────────────
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)
# ══════════════════════════════════════════════════════════════
# CENA 6 – Lendo as Coordenadas de um Ponto Dado
# ══════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════
# CENA 6 – Lendo as Coordenadas de um Ponto Dado
# ══════════════════════════════════════════════════════════════
class C06_LendoCoordenadas(Scene):
    """
    Conceito: Dado um ponto no plano, identificar suas coordenadas
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve projetar o ponto nos eixos para
              determinar a abscissa e a ordenada
    """
    def construct(self):
        tit = titulo_cena("Lendo as Coordenadas de um Ponto")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = make_axes((-4, 4), (-2, 2))
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        # Ponto Q — aparece com label "?"
        qx, qy = -2, -1
        ponto_q = Dot(coord_to_screen(qx, qy), color=COR_PONTO, radius=0.13)
        lbl_q_ini = Text("Q  =  ?", color=COR_PONTO).scale(0.52)
        lbl_q_ini.next_to(ponto_q, DL, buff=0.15)
        self.play(GrowFromCenter(ponto_q), run_time=0.8)
        self.play(Write(lbl_q_ini), run_time=0.7)
        self.wait(0.6)

        # ── PASSO 1: projeção vertical até o eixo x ───────────────
        passo_x = Text("Projete no eixo x  →  abscissa = –2",
                       color=COR_BASE).scale(0.46)
        passo_x.move_to(DOWN * 1.90)
        self.play(FadeIn(passo_x), run_time=0.7)

        # Reta pontilhada AZUL vertical de Q até o eixo x
        proj_h = DashedLine(
            coord_to_screen(qx, qy), coord_to_screen(qx, 0),
            color=COR_BASE, stroke_width=2.2, dash_length=0.12,
        )
        self.play(Create(proj_h), run_time=1.0)

        # Realça o –2 no eixo x com dot azul
        tick_x = Dot(coord_to_screen(qx, 0), color=COR_BASE, radius=0.11)
        self.play(GrowFromCenter(tick_x), run_time=0.6)
        self.wait(0.6)

        # ── PASSO 2: projeção horizontal até o eixo y ─────────────
        passo_y = Text("Projete no eixo y  →  ordenada = –1",
                       color=COR_DESTAQUE).scale(0.46)
        passo_y.move_to(DOWN * 1.90)
        self.play(FadeOut(passo_x), run_time=0.4)
        self.play(FadeIn(passo_y), run_time=0.7)

        # Reta pontilhada AMARELA horizontal de Q até o eixo y
        proj_v = DashedLine(
            coord_to_screen(qx, qy), coord_to_screen(0, qy),
            color=COR_DESTAQUE, stroke_width=2.2, dash_length=0.12,
        )
        self.play(Create(proj_v), run_time=1.0)

        # Realça o –1 no eixo y com dot amarelo
        tick_y = Dot(coord_to_screen(0, qy), color=COR_DESTAQUE, radius=0.11)
        self.play(GrowFromCenter(tick_y), run_time=0.6)
        self.wait(0.6)

        # Revelar coordenadas — substitui "Q = ?"
        self.play(FadeOut(lbl_q_ini), run_time=0.4)
        lbl_q_final = MathTex(r"Q(-2,\,-1)", color=COR_PONTO).scale(0.60)
        lbl_q_final.next_to(ponto_q, DL, buff=0.15)
        self.play(Write(lbl_q_final), run_time=0.9)
        self.wait(0.4)

        # ── CONCLUSÃO: substitui passo_y, sem sobreposição ────────
        self.play(FadeOut(passo_y), run_time=0.4)
        quad = Text("Q está no 3º Quadrante  (–, –)",
                    color=COR_FORMULA).scale(0.48)
        quad.move_to(DOWN * 2.30)
        caixa_q = SurroundingRectangle(quad, color=COR_FORMULA,
                                       buff=0.18, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(quad), Create(caixa_q), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)

# ══════════════════════════════════════════════════════════════
# CENA 7 – Múltiplos Pontos: leitura e interpretação
# ══════════════════════════════════════════════════════════════
class C07_MultiplosPontos(Scene):
    """
    Conceito: Leitura e interpretação de múltiplos pontos no plano
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve identificar as coordenadas de vários
              pontos e reconhecer suas posições relativas
    """
    def construct(self):
        tit = titulo_cena("Identificando Múltiplos Pontos")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = make_axes((-4, 4), (-2, 2))
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        pontos_dados = [
            ("A",  2,  1,  COR_BASE,     UR),
            ("B", -3,  2,  COR_DESTAQUE, UL),
            ("C", -2, -1,  COR_ACENTO,   DL),
            ("D",  3, -2,  COR_FORMULA,  DR),
        ]

        # Tabela à direita — guardamos os elementos para o SurroundingRectangle
        tab_titulo = Text("Ponto   (x,  y)", color=COR_TITULO).scale(0.46)
        tab_titulo.move_to(RIGHT * 4.6 + UP * 1.65)
        linha_tab = Line(RIGHT * 3.8, RIGHT * 5.5,
                         color=GREY_D, stroke_width=1.0)
        linha_tab.next_to(tab_titulo, DOWN, buff=0.12)
        self.play(FadeIn(tab_titulo), Create(linha_tab), run_time=0.6)

        linhas_resumo = VGroup()
        y_tab = 1.15
        for nome, px, py, cor, dire in pontos_dados:
            # Plota o ponto
            pt = Dot(coord_to_screen(px, py), color=cor, radius=0.12)
            self.play(GrowFromCenter(pt), run_time=0.8)
            self.wait(0.6)

            # Label do ponto no plano
            lbl = MathTex(f"{nome}({px},{py})", color=cor).scale(0.50)
            lbl.next_to(pt, dire, buff=0.18)
            self.play(Write(lbl), run_time=1.0)
            self.wait(0.5)

            # Linha na tabela
            linha_txt = Text(f"  {nome}      ({px:+d}, {py:+d})",
                             color=cor).scale(0.42)
            linha_txt.move_to(RIGHT * 4.6 + UP * y_tab)
            linhas_resumo.add(linha_txt)
            self.play(FadeIn(linha_txt), run_time=0.8)
            self.wait(0.6)

            y_tab -= 0.48

        # Quadro ao redor do título + linhas da tabela
        grp_tabela = VGroup(tab_titulo, linhas_resumo)
        caixa_tab = SurroundingRectangle(
            grp_tabela, color=COR_ACENTO,
            buff=0.22, corner_radius=0.14, stroke_width=2.0,
        )
        self.play(Create(caixa_tab), run_time=0.8)
        self.wait(0.5)

        # Observação final
        obs = Text(
            "Cada ponto é único: troca de x e y muda o ponto!",
            color=COR_DESTAQUE,
        ).scale(0.46)
        obs.move_to(DOWN * 2.30)
        self.play(Write(obs), run_time=1.3)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)
    

# ══════════════════════════════════════════════════════════════
# CENA 8 – Pontos sobre os Eixos e na Origem
# ══════════════════════════════════════════════════════════════
class C08_PontosNosEixos(Scene):
    """
    Conceito: Pontos situados nos eixos ou na origem têm coordenada nula
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve reconhecer que y=0 indica ponto no eixo x,
              x=0 indica ponto no eixo y, e (0,0) é a origem
    """
    def construct(self):
        tit = titulo_cena("Pontos sobre os Eixos")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        # Eixos
        eixos, marcacoes, numeros = make_axes((-4, 4), (-2, 2))
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        casos = [
            # (x, y, label, cor, direção, observação)
            (3,  0, "E(3, 0)",  COR_BASE,     UP,
             "y = 0  →  ponto no eixo x"),
            (0,  2, "F(0, 2)",  COR_DESTAQUE, RIGHT,
             "x = 0  →  ponto no eixo y"),
            (0,  0, "O(0, 0)",  COR_ACENTO,   UR,
             "x = 0 e y = 0  →  Origem"),
        ]

        obs_y = 1.55
        for cx, cy, lbl_str, cor, dire, obs_str in casos:
            pt = Dot(coord_to_screen(cx, cy), color=cor, radius=0.13)
            lbl = MathTex(lbl_str, color=cor).scale(0.55)
            lbl.next_to(pt, dire, buff=0.15)

            obs = Text(obs_str, color=cor).scale(0.46)
            obs.move_to(RIGHT * 3.8 + UP * obs_y)

            self.play(GrowFromCenter(pt), run_time=0.7)
            self.play(Write(lbl), FadeIn(obs), run_time=0.9)
            self.wait(0.8)
            obs_y -= 0.72

        # Regra geral
        regra = Text(
            "Se x = 0 ou y = 0, o ponto está sobre um eixo.",
            color=COR_FORMULA,
        ).scale(0.48)
        regra.move_to(DOWN * 2.30)
        caixa_r = SurroundingRectangle(regra, color=COR_FORMULA,
                                       buff=0.18, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(regra), Create(caixa_r), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 9 – Estratégia para o D9
# ══════════════════════════════════════════════════════════════
class C09_Estrategia(Scene):
    """
    Conceito: Estratégia de resolução para questões do D9
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve saber identificar e interpretar
              coordenadas em qualquer situação do SAEB
    """
    def construct(self):
        tit = titulo_cena("Estratégia para o D9")
        sep = separador()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        passos = [
            ("1", "Identifique os eixos x (horizontal) e y (vertical)."),
            ("2", "Leia a abscissa: conte unidades à direita (+) ou esquerda (–)."),
            ("3", "Leia a ordenada: conte unidades para cima (+) ou baixo (–)."),
            ("4", "Escreva o par ordenado na forma  (x, y)."),
            ("5", "Verifique o quadrante pelo sinal de cada coordenada."),
        ]

        y_ini = 1.70
        dy    = 0.82

        for i, (num, texto) in enumerate(passos):
            y = y_ini - i * dy

            bolinha = Circle(radius=0.26, color=COR_ACENTO,
                             fill_color=COR_ACENTO, fill_opacity=0.90,
                             stroke_width=0)
            bolinha.move_to(LEFT * 5.8 + UP * y)

            num_t = Text(num, color=BLACK).scale(0.50)
            num_t.move_to(bolinha.get_center())

            passo_t = Text(texto, color=COR_TITULO).scale(0.47)
            passo_t.next_to(bolinha, RIGHT, buff=0.30)
            passo_t.align_to(bolinha, UP)

            self.play(FadeIn(bolinha), FadeIn(num_t), run_time=0.35)
            self.play(Write(passo_t), run_time=0.90)
            self.wait(0.45)

        conclusao = Text(
            "Coordenadas cartesianas são a linguagem da localização!",
            color=COR_DESTAQUE,
        ).scale(0.50)
        conclusao.move_to(UP * (CONT_BASE + 0.20))
        self.play(Write(conclusao), run_time=1.3)
        self.wait(3.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA MESTRE – une todas as cenas em sequência
# ══════════════════════════════════════════════════════════════
class D9_Final(Scene):
    """
    Animação completa D9 – SAEB Matemática 9º Ano.

    Cenas:
      1  Apresentação do descritor
      2  O que são coordenadas cartesianas?
      3  Construção do plano cartesiano
      4  Os quatro quadrantes
      5  Localizando um ponto P(3, 2)
      6  Lendo coordenadas de um ponto dado
      7  Múltiplos pontos: leitura e interpretação
      8  Pontos sobre os eixos e na origem
      9  Estratégia para o D9
    """

    def _limpar(self):
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)

    def _tit(self, texto, cor=COR_TITULO):
        t = Text(texto, color=cor).scale(0.62)
        t.move_to(UP * TOPO)
        return t

    def _sep(self):
        return separador()

    def _eixos(self, xr=(-4, 4), yr=(-2, 2)):
        return make_axes(xr, yr)

    # ----------------------------------------------------------
    def _cena1(self):
        faixa = Rectangle(width=14.4, height=1.05,
                          fill_color=DARK_BLUE, fill_opacity=0.9,
                          stroke_width=0).move_to(UP * 2.55)
        saeb = Text("SAEB  |  Matemática  |  9º Ano",
                    color=COR_ACENTO).scale(0.52)
        saeb.move_to(faixa.get_center())
        codigo = Text("D9", color=COR_DESTAQUE).scale(2.4)
        codigo.move_to(UP * 0.85)
        linha = Line(LEFT * 3.0, RIGHT * 3.0,
                     color=COR_BASE, stroke_width=2.5)
        linha.next_to(codigo, DOWN, buff=0.35)
        desc = Text(
            "Interpretar informações apresentadas\n"
            "por meio de coordenadas cartesianas.",
            color=COR_TITULO, line_spacing=1.5,
        ).scale(0.60)
        desc.next_to(linha, DOWN, buff=0.45)
        self.play(FadeIn(faixa), FadeIn(saeb), run_time=0.8)
        self.play(Write(codigo), run_time=1.2)
        self.play(Create(linha), run_time=0.6)
        self.play(Write(desc), run_time=2.0)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena2(self):
        tit = self._tit("O que são Coordenadas Cartesianas?")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        def_lbl = Text("Definição:", color=COR_ACENTO).scale(0.50)
        def_lbl.move_to(LEFT * 4.5 + UP * 1.5)
        def_txt = Text(
            "Um sistema que usa dois números para\n"
            "localizar qualquer ponto no plano.",
            color=COR_TITULO, line_spacing=1.4,
        ).scale(0.52)
        def_txt.next_to(def_lbl, DOWN, buff=0.18)
        def_txt.align_to(def_lbl, LEFT)
        self.play(FadeIn(def_lbl), run_time=0.6)
        self.play(Write(def_txt), run_time=1.5)
        self.wait(0.8)

        par_lbl = Text("Par ordenado:", color=COR_ACENTO).scale(0.50)
        par_lbl.move_to(LEFT * 4.5 + UP * 0.3)
        par = MathTex(r"P = (", r"x", r",\;", r"y", r")",
                      color=COR_TITULO).scale(1.10)
        par[1].set_color(COR_BASE)
        par[3].set_color(COR_DESTAQUE)
        par.next_to(par_lbl, DOWN, buff=0.22)
        par.align_to(par_lbl, LEFT)
        self.play(FadeIn(par_lbl), run_time=0.6)
        self.play(Write(par), run_time=1.2)
        self.wait(0.6)

        leg_x = Text("→ abscissa (horizontal)", color=COR_BASE).scale(0.46)
        leg_x.next_to(par, DOWN, buff=0.22)
        leg_x.align_to(par, LEFT)
        leg_y = Text("→ ordenada (vertical)", color=COR_DESTAQUE).scale(0.46)
        leg_y.next_to(leg_x, DOWN, buff=0.16)
        leg_y.align_to(leg_x, LEFT)
        self.play(FadeIn(leg_x), run_time=0.8)
        self.play(FadeIn(leg_y), run_time=0.8)
        self.wait(0.6)

        regra = Text("A ordem importa:  (3, 5) ≠ (5, 3)",
                     color=COR_DESTAQUE).scale(0.52)
        regra.move_to(UP * (CONT_BASE + 0.35))
        caixa_regra = SurroundingRectangle(regra, color=COR_DESTAQUE,
                                           buff=0.20, corner_radius=0.12,
                                           stroke_width=2.0)
        self.play(Write(regra), Create(caixa_regra), run_time=1.3)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena3(self):
        tit = self._tit("O Plano Cartesiano")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = self._eixos()
        self.play(Create(eixos[0]), run_time=1.2)
        self.wait(0.3)
        self.play(Create(eixos[1]), run_time=1.2)
        self.wait(0.3)
        self.play(Write(eixos[2]), Write(eixos[3]), run_time=0.8)
        self.play(Create(marcacoes), Write(numeros), run_time=1.0)
        self.wait(0.5)

        nome_x = Text("Eixo das Abscissas (x)", color=COR_BASE).scale(0.44)
        nome_x.move_to(coord_to_screen(2.5, -0.70))
        seta_x = Arrow(nome_x.get_top() + UP * 0.05,
                       coord_to_screen(2.5, -0.15),
                       color=COR_BASE, buff=0.05,
                       stroke_width=1.8, tip_length=0.15)
        self.play(FadeIn(nome_x), run_time=0.8)
        self.play(Create(seta_x), run_time=0.6)
        self.wait(0.5)

        nome_y = Text("Eixo das Ordenadas (y)", color=COR_DESTAQUE).scale(0.44)
        nome_y.move_to(coord_to_screen(2.2, 1.6))
        seta_y = Arrow(nome_y.get_left() + LEFT * 0.05,
                       coord_to_screen(0.15, 1.5),
                       color=COR_DESTAQUE, buff=0.05,
                       stroke_width=1.8, tip_length=0.15)
        self.play(FadeIn(nome_y), run_time=0.8)
        self.play(Create(seta_y), run_time=0.6)
        self.wait(0.5)

        origem_pt = Dot(coord_to_screen(0, 0), color=COR_ACENTO, radius=0.10)
        origem_lbl = Text("Origem O(0,0)", color=COR_ACENTO).scale(0.44)
        origem_lbl.move_to(coord_to_screen(-0.5, -0.60))
        self.play(GrowFromCenter(origem_pt), run_time=0.7)
        self.play(FadeIn(origem_lbl), run_time=0.8)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena4(self):
        tit = self._tit("Os Quatro Quadrantes")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = self._eixos()
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        quadrantes = [
            ("I",   BLUE,   "+x, +y", "#1a3a5c",  1.8,  1.0),
            ("II",  GREEN,  "–x, +y", "#1a3a2a", -1.8,  1.0),
            ("III", ORANGE, "–x, –y", "#3a2a1a", -1.8, -1.0),
            ("IV",  RED,    "+x, –y", "#3a1a1a",  1.8, -1.0),
        ]
        for nome, cor, sinais, cor_bg, qx, qy in quadrantes:
            sx = 1 if qx > 0 else -1
            sy = 1 if qy > 0 else -1
            regiao = Rectangle(width=4*U, height=2*U,
                               fill_color=cor_bg, fill_opacity=0.55,
                               stroke_width=0)
            regiao.move_to(coord_to_screen(sx*2, sy*1))
            num_romano = Text(nome, color=cor, weight=BOLD).scale(0.62)
            num_romano.move_to(coord_to_screen(sx*2.9, sy*1.55))
            sinal_txt = Text(sinais, color=cor).scale(0.42)
            sinal_txt.move_to(coord_to_screen(sx*2.9, sy*1.08))
            self.play(FadeIn(regiao), run_time=0.6)
            self.play(Write(num_romano), FadeIn(sinal_txt), run_time=0.8)
            self.wait(0.5)

        resumo_lbl = Text("Resumo:", color=COR_ACENTO).scale(0.48)
        resumo_lbl.move_to(RIGHT * 4.8 + UP * 1.5)
        linhas = [("I","+, +",BLUE),("II","–, +",GREEN_C),
                  ("III","–, –",ORANGE),("IV","+, –",RED)]
        y_lin = 1.05
        for q, sinais_r, cor_r in linhas:
            t = Text(f"Q{q}:  ({sinais_r})", color=cor_r).scale(0.44)
            t.move_to(RIGHT * 4.8 + UP * y_lin)
            self.play(FadeIn(t), run_time=0.4)
            y_lin -= 0.52
        self.play(FadeIn(resumo_lbl), run_time=0.5)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena5(self):
        tit = self._tit("Localizando o Ponto  P(3, 2)")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = self._eixos()
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        # ← AJUSTE: labels posicionados abaixo do plano para evitar sobreposição
        passo1_lbl = Text("Passo 1: mova 3 unidades para a direita (x = 3)",
                          color=COR_BASE).scale(0.46)
        passo1_lbl.move_to(coord_to_screen(0, -2.72))
        self.play(FadeIn(passo1_lbl), run_time=0.8)

        linha_h = DashedLine(coord_to_screen(0, 0), coord_to_screen(3, 0),
                             color=COR_BASE, stroke_width=2.5, dash_length=0.12)
        self.play(Create(linha_h), run_time=1.2)
        tick_x3 = Dot(coord_to_screen(3, 0), color=COR_BASE, radius=0.10)
        lbl_x3 = MathTex("3", color=COR_BASE).scale(0.52)
        lbl_x3.move_to(coord_to_screen(3, -0.48))
        self.play(GrowFromCenter(tick_x3), Write(lbl_x3), run_time=0.7)
        self.wait(0.8)

        # ← AJUSTE: passo 2 logo abaixo do passo 1, fora da área dos eixos
        passo2_lbl = Text("Passo 2: suba 2 unidades (y = 2)",
                          color=COR_DESTAQUE).scale(0.46)
        passo2_lbl.move_to(coord_to_screen(0, -3.22))
        self.play(FadeIn(passo2_lbl), run_time=0.8)

        linha_v = DashedLine(coord_to_screen(3, 0), coord_to_screen(3, 2),
                             color=COR_DESTAQUE, stroke_width=2.5, dash_length=0.12)
        self.play(Create(linha_v), run_time=1.0)
        tick_y2 = Dot(coord_to_screen(0, 2), color=COR_DESTAQUE, radius=0.08)
        lbl_y2 = MathTex("2", color=COR_DESTAQUE).scale(0.52)
        lbl_y2.move_to(coord_to_screen(-0.42, 2))
        self.play(GrowFromCenter(tick_y2), Write(lbl_y2), run_time=0.7)
        self.wait(0.5)

        ponto_p = Dot(coord_to_screen(3, 2), color=COR_PONTO, radius=0.13)
        lbl_p = MathTex(r"P(3,\,2)", color=COR_PONTO).scale(0.60)
        lbl_p.next_to(ponto_p, UR, buff=0.15)
        self.play(GrowFromCenter(ponto_p), run_time=0.8)
        self.play(Write(lbl_p), run_time=0.8)
        self.wait(0.5)

        concl = Text("O ponto P está no 1º Quadrante  (+, +)",
                     color=COR_FORMULA).scale(0.48)
        concl.move_to(UP * (CONT_BASE + 0.28))
        caixa_c = SurroundingRectangle(concl, color=COR_FORMULA,
                                       buff=0.18, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(concl), Create(caixa_c), run_time=1.2)
        self.wait(2.5)
        self._limpar()

        # ----------------------------------------------------------

    def _cena6(self):
        tit = self._tit("Lendo as Coordenadas de um Ponto")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = self._eixos()
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        qx, qy = -2, -1
        ponto_q = Dot(coord_to_screen(qx, qy), color=COR_PONTO, radius=0.13)
        lbl_q_ini = Text("Q  =  ?", color=COR_PONTO).scale(0.52)
        lbl_q_ini.next_to(ponto_q, UR, buff=0.15)
        self.play(GrowFromCenter(ponto_q), run_time=0.8)
        self.play(Write(lbl_q_ini), run_time=0.7)
        self.wait(0.6)

        proj_h = DashedLine(coord_to_screen(qx, qy), coord_to_screen(qx, 0),
                            color=COR_BASE, stroke_width=2.2, dash_length=0.12)
        lbl_proj_x = MathTex(str(qx), color=COR_BASE).scale(0.58)
        lbl_proj_x.move_to(coord_to_screen(qx, -0.45))
        # ← AJUSTE: labels abaixo do plano para evitar sobreposição
        passo_x = Text("Projete no eixo x  →  abscissa = –2",
                       color=COR_BASE).scale(0.46)
        passo_x.move_to(coord_to_screen(0, -2.72))
        self.play(FadeIn(passo_x), run_time=0.7)
        self.play(Create(proj_h), run_time=1.0)
        self.play(Write(lbl_proj_x), run_time=0.6)
        self.wait(0.6)

        proj_v = DashedLine(coord_to_screen(qx, qy), coord_to_screen(0, qy),
                            color=COR_DESTAQUE, stroke_width=2.2, dash_length=0.12)
        lbl_proj_y = MathTex(str(qy), color=COR_DESTAQUE).scale(0.58)
        lbl_proj_y.move_to(coord_to_screen(-0.42, qy))
        # ← AJUSTE: passo_y logo abaixo do passo_x, fora da área dos eixos
        passo_y = Text("Projete no eixo y  →  ordenada = –1",
                       color=COR_DESTAQUE).scale(0.46)
        passo_y.move_to(coord_to_screen(0, -3.22))
        self.play(FadeIn(passo_y), run_time=0.7)
        self.play(Create(proj_v), run_time=1.0)
        self.play(Write(lbl_proj_y), run_time=0.6)
        self.wait(0.6)

        self.play(FadeOut(lbl_q_ini), run_time=0.4)
        lbl_q_final = MathTex(r"Q(-2,\,-1)", color=COR_PONTO).scale(0.62)
        lbl_q_final.next_to(ponto_q, UR, buff=0.15)
        self.play(Write(lbl_q_final), run_time=0.9)
        self.wait(0.4)

        quad = Text("Q está no 3º Quadrante  (–, –)",
                    color=COR_FORMULA).scale(0.48)
        quad.move_to(UP * (CONT_BASE + 0.28))
        caixa_q = SurroundingRectangle(quad, color=COR_FORMULA,
                                       buff=0.18, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(quad), Create(caixa_q), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena7(self):
        tit = self._tit("Identificando Múltiplos Pontos")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = self._eixos()
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        pontos_dados = [
            ("A",  2,  1, COR_BASE,     UR),
            ("B", -3,  2, COR_DESTAQUE, UL),
            ("C", -2, -1, COR_ACENTO,   DL),
            ("D",  3, -2, COR_FORMULA,  DR),
        ]
        tab_titulo = Text("Ponto   (x,  y)", color=COR_TITULO).scale(0.46)
        tab_titulo.move_to(RIGHT * 4.6 + UP * 1.65)
        linha_tab = Line(RIGHT * 3.8, RIGHT * 5.5,
                         color=GREY_D, stroke_width=1.0)
        linha_tab.next_to(tab_titulo, DOWN, buff=0.12)
        self.play(FadeIn(tab_titulo), Create(linha_tab), run_time=0.6)

        y_tab = 1.15
        for nome, px, py, cor, dire in pontos_dados:
            pt = Dot(coord_to_screen(px, py), color=cor, radius=0.12)
            lbl = MathTex(f"{nome}({px},{py})", color=cor).scale(0.50)
            lbl.next_to(pt, dire, buff=0.12)
            linha_txt = Text(f"  {nome}      ({px:+d}, {py:+d})",
                             color=cor).scale(0.42)
            linha_txt.move_to(RIGHT * 4.6 + UP * y_tab)
            self.play(GrowFromCenter(pt), run_time=0.6)
            self.play(Write(lbl), FadeIn(linha_txt), run_time=0.7)
            self.wait(0.4)
            y_tab -= 0.48

        obs = Text("Cada ponto é único: troca de x e y muda o ponto!",
                   color=COR_DESTAQUE).scale(0.48)
        obs.move_to(UP * (CONT_BASE + 0.28))
        self.play(Write(obs), run_time=1.3)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena8(self):
        tit = self._tit("Pontos sobre os Eixos")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        eixos, marcacoes, numeros = self._eixos()
        self.play(Create(eixos), Create(marcacoes), Write(numeros), run_time=1.2)
        self.wait(0.3)

        casos = [
            (3,  0, "E(3, 0)",  COR_BASE,     UP,
             "y = 0  →  ponto no eixo x"),
            (0,  2, "F(0, 2)",  COR_DESTAQUE, RIGHT,
             "x = 0  →  ponto no eixo y"),
            (0,  0, "O(0, 0)",  COR_ACENTO,   UR,
             "x = 0 e y = 0  →  Origem"),
        ]
        obs_y = 1.55
        for cx, cy, lbl_str, cor, dire, obs_str in casos:
            pt = Dot(coord_to_screen(cx, cy), color=cor, radius=0.13)
            lbl = MathTex(lbl_str, color=cor).scale(0.55)
            lbl.next_to(pt, dire, buff=0.15)
            obs = Text(obs_str, color=cor).scale(0.46)
            obs.move_to(RIGHT * 3.8 + UP * obs_y)
            self.play(GrowFromCenter(pt), run_time=0.7)
            self.play(Write(lbl), FadeIn(obs), run_time=0.9)
            self.wait(0.8)
            obs_y -= 0.72

        regra = Text("Se x = 0 ou y = 0, o ponto está sobre um eixo.",
                     color=COR_FORMULA).scale(0.48)
        regra.move_to(UP * (CONT_BASE + 0.28))
        caixa_r = SurroundingRectangle(regra, color=COR_FORMULA,
                                       buff=0.18, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(regra), Create(caixa_r), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena9(self):
        tit = self._tit("Estratégia para o D9")
        sep = self._sep()
        self.play(Write(tit), run_time=1.0)
        self.play(Create(sep), run_time=0.5)
        self.wait(0.3)

        passos = [
            ("1", "Identifique os eixos x (horizontal) e y (vertical)."),
            ("2", "Leia a abscissa: conte unidades à direita (+) ou esquerda (–)."),
            ("3", "Leia a ordenada: conte unidades para cima (+) ou baixo (–)."),
            ("4", "Escreva o par ordenado na forma  (x, y)."),
            ("5", "Verifique o quadrante pelo sinal de cada coordenada."),
        ]
        y_ini = 1.70
        dy    = 0.82
        for i, (num, texto) in enumerate(passos):
            y = y_ini - i * dy
            bolinha = Circle(radius=0.26, color=COR_ACENTO,
                             fill_color=COR_ACENTO, fill_opacity=0.90,
                             stroke_width=0)
            bolinha.move_to(LEFT * 5.8 + UP * y)
            num_t = Text(num, color=BLACK).scale(0.50)
            num_t.move_to(bolinha.get_center())
            passo_t = Text(texto, color=COR_TITULO).scale(0.47)
            passo_t.next_to(bolinha, RIGHT, buff=0.30)
            passo_t.align_to(bolinha, UP)
            self.play(FadeIn(bolinha), FadeIn(num_t), run_time=0.35)
            self.play(Write(passo_t), run_time=0.90)
            self.wait(0.45)

        conclusao = Text(
            "Coordenadas cartesianas são a linguagem da localização!",
            color=COR_DESTAQUE,
        ).scale(0.50)
        conclusao.move_to(UP * (CONT_BASE + 0.20))
        self.play(Write(conclusao), run_time=1.3)
        self.wait(3.0)
        self._limpar()

    # ----------------------------------------------------------
    def construct(self):
        self._cena1()
        self._cena2()
        self._cena3()
        self._cena4()
        self._cena5()
        self._cena6()
        self._cena7()
        self._cena8()
        self._cena9()


# ══════════════════════════════════════════════════════════════
# LOGO – Identidade visual da Prof.ª Emilly Mayre
# ══════════════════════════════════════════════════════════════
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

        bg_logo = Rectangle(width=16, height=9,
                            fill_color=WHITE, fill_opacity=1, stroke_width=0)
        self.add(bg_logo)

        a_inf = 1.9

        def inf_horiz(t):
            d = 1 + np.sin(t)**2
            return np.array([a_inf * np.cos(t) / d,
                             a_inf * np.sin(t) * np.cos(t) / d, 0])

        def inf_vert(t):
            d = 1 + np.sin(t)**2
            return np.array([a_inf * np.sin(t) * np.cos(t) / d,
                             a_inf * np.cos(t) / d, 0])

        logo_inf_h = ParametricFunction(
            inf_horiz, t_range=[0, TAU],
            color="#3a3a5c", stroke_width=2.5,
        ).move_to(ORIGIN + UP * 0.5)

        logo_inf_v = ParametricFunction(
            inf_vert, t_range=[0, TAU],
            color="#9999bb", stroke_width=2.5,
        ).move_to(ORIGIN + UP * 0.5)

        grupo_logo = VGroup(logo_inf_h, logo_inf_v)

        logo_circ = Circle(
            radius=0.42,
            fill_color=ESCURO_L, fill_opacity=1,
            color=ESCURO_L, stroke_width=0,
        ).move_to(ORIGIN + UP * 0.5)

        logo_em = Text("EM", color=WHITE, font_size=22, weight=BOLD)
        logo_em.move_to(logo_circ.get_center())

        logo_nome = Text("Emilly Mayre", color=ESCURO_L,
                         font_size=28, weight=BOLD)
        logo_nome.next_to(grupo_logo, DOWN, buff=0.55)

        logo_linha = Line(LEFT * 1.6, RIGHT * 1.6,
                          color=DOURADO, stroke_width=3.5)
        logo_linha.next_to(logo_nome, DOWN, buff=0.16)

        logo_cargo = Text("PROFESSORA DE MATEMÁTICA",
                          color=CINZA_L, font_size=14)
        logo_cargo.next_to(logo_linha, DOWN, buff=0.18)

        self.play(Create(logo_inf_h), run_time=2.0)
        self.wait(0.3)
        self.play(Create(logo_inf_v), run_time=2.0)
        self.wait(0.3)
        self.play(GrowFromCenter(logo_circ), run_time=0.7)
        self.play(Write(logo_em), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(logo_nome, shift=UP * 0.15), run_time=0.8)
        self.play(Create(logo_linha), run_time=0.5)
        self.play(FadeIn(logo_cargo), run_time=0.6)
        self.wait(0.4)
        logo_simbolo = VGroup(logo_inf_h, logo_inf_v, logo_circ, logo_em)
        self.play(logo_simbolo.animate.scale(1.06), run_time=0.4)
        self.play(logo_simbolo.animate.scale(1 / 1.06), run_time=0.35)
        self.wait(3.5)
