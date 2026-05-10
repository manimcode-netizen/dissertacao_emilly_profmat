from manim import *

# ================================================================
# D32 – SAEB Matemática 9º Ano  (versão final)
# Conceito : Identificar a expressão algébrica que expressa
#            uma regularidade observada em sequências de
#            números ou figuras (padrões).
# Nível    : Ensino Fundamental – 9º Ano
#
# ZONA SEGURA: y entre -2.6 e +2.6 | x entre -6.5 e +6.5
# Notação matemática: SEMPRE MathTex para potências e subscritos
# ================================================================

COR_BASE     = BLUE_C
COR_DESTAQUE = YELLOW
COR_FORMULA  = GREEN_C
COR_TITULO   = WHITE
COR_ACENTO   = ORANGE

TOPO = 2.6
BASE = -2.6
CONT_TOPO = 1.9   # topo da área de conteúdo (abaixo do sep)
CONT_BASE = -2.2  # base da área de conteúdo (acima da margem)


def titulo_cena(texto, cor=COR_TITULO, escala=0.62):
    t = Text(texto, color=cor).scale(escala)
    t.move_to(UP * TOPO)
    return t


def separador():
    return Line(LEFT * 6.5, RIGHT * 6.5,
                color=GREY_D, stroke_width=1.5).move_to(UP * (TOPO - 0.48))


def tabela_3col(dados_triplos, cab_labels, ancora_y, ancora_x,
                col_w=2.2, row_h=0.55, scene=None):
    """
    Monta tabela de 3 colunas com cabeçalho e linhas de dados.
    dados_triplos: lista de (val1, val2, val3_mobject)
    cab_labels: [str, str, str]
    Retorna lista de VGroup (cab, linha1, linha2, ...)
    """
    grupos = []

    def pos(col, row):
        return np.array([
            ancora_x + col_w * col + col_w / 2,
            ancora_y - row_h * row - row_h / 2,
            0,
        ])

    # Cabeçalho
    cab = VGroup()
    for j, lab in enumerate(cab_labels):
        r = Rectangle(width=col_w, height=row_h,
                      fill_color=DARK_BLUE, fill_opacity=0.85,
                      color=COR_ACENTO, stroke_width=1.8)
        r.move_to(pos(j, 0))
        t = Text(lab, color=COR_ACENTO).scale(0.44)
        t.move_to(r.get_center())
        cab.add(r, t)
    grupos.append(cab)

    cores_col = [COR_BASE, COR_FORMULA, COR_DESTAQUE]
    for i, triplo in enumerate(dados_triplos):
        lg = VGroup()
        for j, (val, fc) in enumerate(zip(triplo, cores_col)):
            r = Rectangle(width=col_w, height=row_h,
                          fill_color=fc, fill_opacity=0.10,
                          color=fc, stroke_width=1.0)
            r.move_to(pos(j, i + 1))
            if isinstance(val, str):
                t = Text(val, color=COR_TITULO).scale(0.50)
            else:
                t = val  # já é um Mobject (MathTex)
                t.scale(0.55)
            t.move_to(r.get_center())
            lg.add(r, t)
        grupos.append(lg)

    return grupos, pos


# ══════════════════════════════════════════════════════════════
# CENA 1 – Apresentação do descritor D32
# ══════════════════════════════════════════════════════════════
class C01_Apresentacao(Scene):
    def construct(self):
        faixa = Rectangle(width=14.4, height=1.05,
                          fill_color=DARK_BLUE, fill_opacity=0.9,
                          stroke_width=0).move_to(UP * 2.55)

        saeb = Text("SAEB  |  Matemática  |  9º Ano",
                    color=COR_ACENTO).scale(0.52)
        saeb.move_to(faixa.get_center())

        codigo = Text("D32", color=COR_DESTAQUE).scale(2.4)
        codigo.move_to(UP * 0.85)

        linha = Line(LEFT * 3.0, RIGHT * 3.0,
                     color=COR_BASE, stroke_width=2.5)
        linha.next_to(codigo, DOWN, buff=0.35)

        desc = Text(
            "Identificar a expressão algébrica que\n"
            "expressa uma regularidade observada\n"
            "em sequências de números ou figuras.",
            color=COR_TITULO, line_spacing=1.5,
        ).scale(0.58)
        desc.next_to(linha, DOWN, buff=0.45)

        self.play(FadeIn(faixa), FadeIn(saeb), run_time=0.8)
        self.play(Write(codigo), run_time=1.2)
        self.play(Create(linha), run_time=0.6)
        self.play(Write(desc), run_time=2.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 2 – O que é um Padrão?
# ══════════════════════════════════════════════════════════════
class C02_OQueEPadrao(Scene):
    """
    Conceito: O que é um Padrão? (figuras quadradas crescentes)
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve perceber que figuras quadradas crescem segundo n²
    """
    def construct(self):
        tit = titulo_cena("O que é um Padrão?")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        TAM = 0.34
        grupos = VGroup()
        for n in range(1, 5):
            grade = VGroup()
            for r in range(n):
                for c in range(n):
                    sq = Square(side_length=TAM, color=COR_BASE,
                                fill_color=COR_BASE, fill_opacity=0.5,
                                stroke_width=1.5)
                    sq.move_to(RIGHT * c * TAM + DOWN * r * TAM)
                    grade.add(sq)
            grade.move_to(ORIGIN)

            rot_n = Text(f"n = {n}", color=COR_DESTAQUE).scale(0.50)
            # Usar MathTex para n²
            rot_qt = MathTex(f"{n*n}", color=COR_FORMULA).scale(0.55)
            rot_label = Text("quad.", color=COR_FORMULA).scale(0.42)
            rot_linha = VGroup(rot_qt, rot_label).arrange(RIGHT, buff=0.08)

            bloco = VGroup(grade, rot_n, rot_linha)
            bloco.arrange(DOWN, buff=0.25)
            grupos.add(bloco)

        grupos.arrange(RIGHT, buff=0.7)
        # Círculos centralizados na metade superior da zona segura
        grupos.move_to(UP * 0.35)

        pergunta = Text(
            "Quantos quadradinhos tem a figura de posição n?",
            color=COR_TITULO,
        ).scale(0.52)
        # Margem de segurança: CONT_BASE + 0.1 em vez de - 0.1
        pergunta.move_to(UP * (CONT_BASE + 0.1))

        for bloco in grupos:
            self.play(FadeIn(bloco), run_time=0.9)
            self.wait(0.35)

        self.play(Write(pergunta), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 3 – Tabela com 3 colunas: Figura | Quadradinhos | Padrão
# ══════════════════════════════════════════════════════════════
class C03_TabelaQuadratica(Scene):
    """
    Conceito: Tabela com padrão quadrático (n, n², nº de quadradinhos)
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve identificar o padrão n² organizando dados em tabela
    """
    def construct(self):
        tit = titulo_cena("Organizando em Tabela")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        COL_W  = 2.55
        ROW_H  = 0.54
        # 6 linhas (cab + 5 dados): altura total = 6 × 0.54 = 3.24
        # ancora_y tal que fundo = ancora_y - 6×0.54 >= CONT_BASE
        # ancora_y >= -2.2 + 3.24 = 1.04  → usamos CONT_TOPO = 1.9
        ancora_y = CONT_TOPO
        ancora_x = -3 * COL_W / 2   # 3 colunas centradas

        dados = [
            ("1", "1",  MathTex(r"1^2", color=COR_DESTAQUE)),
            ("2", "4",  MathTex(r"2^2", color=COR_DESTAQUE)),
            ("3", "9",  MathTex(r"3^2", color=COR_DESTAQUE)),
            ("4", "16", MathTex(r"4^2", color=COR_DESTAQUE)),
            ("5", "25", MathTex(r"5^2", color=COR_DESTAQUE)),
        ]

        cab_labels = ["Figura (n)", "Quadradinhos", "Padrão"]
        grupos, pos = tabela_3col(dados, cab_labels,
                                  ancora_y, ancora_x,
                                  col_w=COL_W, row_h=ROW_H)

        # Anima cabeçalho
        self.play(FadeIn(grupos[0]), run_time=0.8)
        self.wait(0.2)

        # Anima cada linha
        for lg in grupos[1:]:
            self.play(FadeIn(lg), run_time=0.55)
            self.wait(0.2)

        # Rodapé: observação
        # fundo tabela: ancora_y - 6×ROW_H = 1.9 - 3.24 = -1.34  (seguro)
        obs = VGroup(
            Text("Padrão observado: quantidade = ", color=COR_TITULO).scale(0.50),
            MathTex(r"n^2", color=COR_DESTAQUE).scale(0.75),
        ).arrange(RIGHT, buff=0.1)
        obs.move_to(UP * (CONT_BASE + 0.3))

        self.play(Write(obs), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 4 – Construindo a Expressão Algébrica (padrão n²)
# Correção: label e conteúdo em linhas separadas, sem sobreposição
# ══════════════════════════════════════════════════════════════
class C04_ExpressaoQuadratica(Scene):
    """
    Conceito: Construção passo a passo da expressão algébrica n²
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve compreender como observar → traduzir → simplificar → generalizar
    """
    def construct(self):
        tit = titulo_cena("Construindo a Expressão Algébrica")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        passos = [
            ("Passo 1 – Observar",
             Text("Cada figura n tem n linhas × n colunas de quadradinhos.",
                  color=COR_TITULO).scale(0.50)),
            ("Passo 2 – Traduzir",
             MathTex(r"\text{Quantidade} = n \times n",
                     color=COR_TITULO).scale(0.80)),
            ("Passo 3 – Simplificar",
             MathTex(r"\text{Quantidade} = n^2",
                     color=COR_DESTAQUE).scale(0.82)),
            ("Passo 4 – Fórmula Geral",
             MathTex(r"a_n = n^2",
                     color=COR_FORMULA).scale(0.90)),
        ]

        # y_tops: posições dos labels de cada passo
        y_tops = [1.70, 0.94, 0.06, -1.05]
        objetos_form = []

        for (label, conteudo), y_top in zip(passos, y_tops):
            lbl = Text(label, color=COR_ACENTO).scale(0.44)
            lbl.move_to(UP * y_top)
            lbl.align_to(LEFT * 6.0, LEFT)

            # Passo 4: buff maior para afastar o quadro verde do label
            buff = 0.35 if label.startswith("Passo 4") else 0.08
            conteudo.next_to(lbl, DOWN, buff=buff)
            conteudo.align_to(LEFT * 4.5, LEFT)

            self.play(FadeIn(lbl), run_time=0.5)
            self.play(Write(conteudo), run_time=1.0)
            self.wait(0.6)
            objetos_form.append(conteudo)

        # Caixa ao redor da fórmula final
        caixa = SurroundingRectangle(
            objetos_form[-1], color=COR_FORMULA,
            buff=0.22, corner_radius=0.14, stroke_width=2.5)
        self.play(Create(caixa), run_time=0.9)
        self.wait(0.8)

        # Verificação abaixo da caixa, centralizada na tela
        verif = VGroup(
            Text("Verificação: n = 6  →  ", color=COR_ACENTO).scale(0.50),
            MathTex(r"6^2 = 36", color=COR_ACENTO).scale(0.65),
            Text("quadradinhos  ✓", color=COR_ACENTO).scale(0.50),
        ).arrange(RIGHT, buff=0.1)
        verif.next_to(caixa, DOWN, buff=0.18)
        verif.set_x(0)

        self.play(Write(verif), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 5a – Sequência Linear: círculos + setas arqueadas
# ══════════════════════════════════════════════════════════════
class C05a_LinearCirculos(Scene):
    """
    Conceito: Sequência linear 3, 5, 7, 9, 11 com diferença constante +2
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve identificar diferença constante como marca do padrão linear
    """
    def construct(self):
        tit = titulo_cena("Sequência Linear:  3, 5, 7, 9, 11, ...")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        numeros = [3, 5, 7, 9, 11]
        RAIO    = 0.50
        pos_x   = [-4.4, -2.2, 0.0, 2.2, 4.4]
        # Círculos mais para baixo (não colam no título)
        CY      = 0.4

        circulos = VGroup()
        nums_txt = VGroup()
        pos_txt  = VGroup()

        for i, (val, px) in enumerate(zip(numeros, pos_x)):
            circ = Circle(radius=RAIO, color=COR_BASE,
                          fill_color=COR_BASE, fill_opacity=0.35,
                          stroke_width=2.5).move_to(RIGHT * px + UP * CY)
            n_t = Text(str(val), color=COR_TITULO).scale(0.75)
            n_t.move_to(circ.get_center())
            p_t = MathTex(f"n={i+1}", color=COR_DESTAQUE).scale(0.50)
            p_t.next_to(circ, DOWN, buff=0.20)
            circulos.add(circ)
            nums_txt.add(n_t)
            pos_txt.add(p_t)

        for c, n, p in zip(circulos, nums_txt, pos_txt):
            self.play(FadeIn(c), Write(n), Write(p), run_time=0.65)
            self.wait(0.2)

        self.wait(0.4)

        # Setas ARQUEADAS entre círculos consecutivos
        setas_arq = VGroup()
        dif_lbl   = VGroup()
        for i in range(4):
            xa = np.array([pos_x[i],   CY + RAIO + 0.05, 0])
            xb = np.array([pos_x[i+1], CY + RAIO + 0.05, 0])
            seta = CurvedArrow(xa, xb, angle=-TAU/6,
                               color=COR_DESTAQUE, stroke_width=2.2,
                               tip_length=0.18)
            lbl = Text("+2", color=COR_DESTAQUE).scale(0.44)
            lbl.move_to(UP * (CY + RAIO + 0.55)
                        + RIGHT * (pos_x[i] + pos_x[i+1]) / 2)
            setas_arq.add(seta)
            dif_lbl.add(lbl)

        self.play(Create(setas_arq), Write(dif_lbl), run_time=1.3)
        self.wait(0.8)

        obs = Text(
            "A diferença entre termos consecutivos é sempre 2.",
            color=COR_DESTAQUE,
        ).scale(0.52)
        obs.move_to(UP * (CONT_BASE + 0.5))
        self.play(Write(obs), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 5b – Tabela e fórmula da Sequência Linear
# ══════════════════════════════════════════════════════════════
class C05b_LinearTabela(Scene):
    """
    Conceito: Derivação da fórmula linear a_n = 2n+1 via tabela
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve aprender a derivar a fórmula geral a partir dos dados da tabela
    """
    def construct(self):
        tit = titulo_cena("Encontrando a Fórmula da Sequência Linear")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        # --- Tabela 3 colunas à esquerda ---
        COL_W   = 2.2
        ROW_H   = 0.52
        anc_y   = CONT_TOPO
        anc_x   = -5.8   # começar bem à esquerda

        dados = [
            ("1", "3",  MathTex(r"2(1)+1", color=COR_DESTAQUE)),
            ("2", "5",  MathTex(r"2(2)+1", color=COR_DESTAQUE)),
            ("3", "7",  MathTex(r"2(3)+1", color=COR_DESTAQUE)),
            ("4", "9",  MathTex(r"2(4)+1", color=COR_DESTAQUE)),
            ("5", "11", MathTex(r"2(5)+1", color=COR_DESTAQUE)),
        ]
        cab_labels = ["n", "Valor", "Padrão"]
        grupos, pos = tabela_3col(dados, cab_labels,
                                  anc_y, anc_x,
                                  col_w=COL_W, row_h=ROW_H)

        self.play(FadeIn(grupos[0]), run_time=0.7)
        for lg in grupos[1:]:
            self.play(FadeIn(lg), run_time=0.45)
            self.wait(0.15)

        # --- Derivação à direita ---
        # posição x de início da derivação
        dx = anc_x + 3 * COL_W + 0.6   # = -5.8 + 6.6 + 0.6 = 1.4

        passos = [
            ("Diferença constante = 2", UP * 1.55),
            ("Coeficiente de n é 2",    UP * 0.80),
        ]
        for txt, pos_v in passos:
            t = Text(txt, color=COR_TITULO).scale(0.50)
            t.move_to(RIGHT * 3.5 + pos_v)
            self.play(Write(t), run_time=0.9)
            self.wait(0.5)

        p2 = MathTex(r"a_n = 2n + \;?", color=COR_TITULO).scale(0.80)
        p2.move_to(RIGHT * 3.5 + UP * 0.05)
        self.play(Write(p2), run_time=1.0)
        self.wait(0.5)

        p3 = Text("Para n=1:  2×1+? = 3  →  ? = 1",
                  color=COR_TITULO).scale(0.48)
        p3.move_to(RIGHT * 3.5 + UP * (-0.65))
        self.play(Write(p3), run_time=1.0)
        self.wait(0.5)

        formula = MathTex(r"a_n = 2n + 1", color=COR_FORMULA).scale(1.05)
        formula.move_to(RIGHT * 3.5 + UP * (-1.4))
        caixa = SurroundingRectangle(formula, color=COR_FORMULA,
                                     buff=0.22, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Write(formula), Create(caixa), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 6 – Construindo a Fórmula Linear passo a passo
# ══════════════════════════════════════════════════════════════
class C06_ExpressaoLinear(Scene):
    """
    Conceito: Construção passo a passo da fórmula linear a_n = 2n+1
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve consolidar o método de encontrar a constante usando n=1
    """
    def construct(self):
        # Título com MathTex inline — usar VGroup
        tit2 = Text("Construindo a Fórmula:", color=COR_TITULO).scale(0.62)
        tit_form = MathTex(r"a_n = 2n + 1", color=COR_FORMULA).scale(0.70)
        tit_grp = VGroup(tit2, tit_form).arrange(RIGHT, buff=0.3)
        tit_grp.move_to(UP * TOPO)
        sep = separador()
        # Separar animações para não sobrecarregar a percepção visual
        self.play(Write(tit_grp), run_time=1.0)
        self.play(Create(sep), run_time=0.6)
        self.wait(0.3)

        passos = [
            ("Passo 1 – Diferença constante",
             MathTex(r"5-3=2,\quad 7-5=2,\quad 9-7=2 \quad\Rightarrow\quad \Delta = 2",
                     color=COR_DESTAQUE).scale(0.60)),
            ("Passo 2 – Coeficiente de n",
             MathTex(r"a_n = 2n + \;?", color=COR_TITULO).scale(0.80)),
            ("Passo 3 – Encontrar a constante",
             MathTex(r"n=1:\; 2(1)+?=3 \;\Rightarrow\; ?=1",
                     color=COR_TITULO).scale(0.68)),
            ("Passo 4 – Fórmula Geral",
             MathTex(r"a_n = 2n + 1", color=COR_FORMULA).scale(0.90)),
        ]

        # y_tops: posições dos labels de cada passo
        y_tops = [1.65, 0.83, -0.05, -1.05]
        form_final = None

        for (label, conteudo), y_top in zip(passos, y_tops):
            lbl = Text(label, color=COR_ACENTO).scale(0.44)
            lbl.move_to(UP * y_top)
            lbl.align_to(LEFT * 6.0, LEFT)

            # Passo 4: buff maior para afastar o quadro verde do label
            buff = 0.35 if label.startswith("Passo 4") else 0.08
            conteudo.next_to(lbl, DOWN, buff=buff)
            conteudo.align_to(LEFT * 5.0, LEFT)

            self.play(FadeIn(lbl), run_time=0.5)
            self.play(Write(conteudo), run_time=1.0)
            self.wait(0.6)
            if label.startswith("Passo 4"):
                form_final = conteudo

        caixa = SurroundingRectangle(form_final, color=COR_FORMULA,
                                     buff=0.22, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Create(caixa), run_time=0.8)
        self.wait(0.7)

        # Verificação abaixo da caixa, centralizada na tela
        verif = VGroup(
            Text("Verificação: n=10  →  ", color=COR_ACENTO).scale(0.50),
            MathTex(r"2(10)+1 = 21", color=COR_ACENTO).scale(0.65),
            Text("  ✓", color=COR_ACENTO).scale(0.50),
        ).arrange(RIGHT, buff=0.08)
        verif.next_to(caixa, DOWN, buff=0.18)
        verif.set_x(0)

        self.play(Write(verif), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 7a – Padrão Triangular: figuras de pontos + setas arqueadas
# ══════════════════════════════════════════════════════════════
class C07a_TriangularFiguras(Scene):
    """
    Conceito: Padrão triangular 1, 3, 6, 10 com diferenças crescentes
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve perceber que diferenças crescentes indicam padrão não linear
    """
    def construct(self):
        tit = titulo_cena("Padrão Triangular:  1, 3, 6, 10, ...")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        RAIO_PT = 0.17
        dados   = [(1, 1), (2, 3), (3, 6), (4, 10)]
        pos_x   = [-4.8, -1.6, 1.6, 4.8]
        # Baixar CY para que as setas arqueadas passem bem acima das figuras
        CY      = 0.0

        blocos = VGroup()
        for (n, total), px in zip(dados, pos_x):
            pontos = VGroup()
            for i in range(1, n + 1):
                offset_x = -(i - 1) * RAIO_PT * 2.6 / 2
                for j in range(i):
                    pt = Circle(radius=RAIO_PT, color=COR_BASE,
                                fill_color=COR_BASE, fill_opacity=0.85,
                                stroke_width=0)
                    pt.move_to(RIGHT * (offset_x + j * RAIO_PT * 2.6)
                               + DOWN * (i - 1) * RAIO_PT * 2.4)
                    pontos.add(pt)

            rot_n  = MathTex(f"n={n}", color=COR_DESTAQUE).scale(0.52)
            rot_qt = MathTex(str(total), color=COR_FORMULA).scale(0.60)
            bloco  = VGroup(pontos, rot_n, rot_qt)
            bloco.arrange(DOWN, buff=0.28)
            bloco.move_to(RIGHT * px + UP * CY)
            blocos.add(bloco)

        for b in blocos:
            self.play(FadeIn(b), run_time=0.85)
            self.wait(0.3)

        self.wait(0.4)

        # Setas arqueadas com diferenças +2, +3, +4
        # topo_y elevado para garantir que as setas fiquem acima das figuras
        difs_val = ["+2", "+3", "+4"]
        setas_arq = VGroup()
        dif_lbl   = VGroup()
        topo_y = CY + 1.10   # setas passam alto, sem sobrepor as figuras

        for i in range(3):
            xa = np.array([pos_x[i],   topo_y + 0.10, 0])
            xb = np.array([pos_x[i+1], topo_y + 0.10, 0])
            seta = CurvedArrow(xa, xb, angle=-TAU / 6,
                               color=COR_DESTAQUE, stroke_width=2.2,
                               tip_length=0.18)
            lbl = Text(difs_val[i], color=COR_DESTAQUE).scale(0.46)
            lbl.move_to(UP * (topo_y + 0.85)
                        + RIGHT * (pos_x[i] + pos_x[i+1]) / 2)
            setas_arq.add(seta)
            dif_lbl.add(lbl)

        self.play(Create(setas_arq), Write(dif_lbl), run_time=1.3)
        self.wait(0.8)

        obs = Text(
            "As diferenças crescem de 1 em 1 → padrão não linear!",
            color=COR_DESTAQUE,
        ).scale(0.50)
        obs.move_to(UP * (CONT_BASE + 0.5))
        self.play(Write(obs), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 7b – Tabela e fórmula do Padrão Triangular
# ══════════════════════════════════════════════════════════════
class C07b_TriangularTabela(Scene):
    """
    Conceito: Fórmula do padrão triangular a_n = n(n+1)/2
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve reconhecer a fórmula triangular e verificá-la com valores
    """
    def construct(self):
        tit = titulo_cena("Fórmula do Padrão Triangular")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        # ROW_H=0.60 para que a tabela caiba e a verificação não sobreponha
        COL_W = 2.3
        ROW_H = 0.60
        anc_y = CONT_TOPO
        anc_x = -5.8

        dados = [
            ("1", "1",  MathTex(r"\frac{1 \cdot 2}{2}", color=COR_DESTAQUE)),
            ("2", "3",  MathTex(r"\frac{2 \cdot 3}{2}", color=COR_DESTAQUE)),
            ("3", "6",  MathTex(r"\frac{3 \cdot 4}{2}", color=COR_DESTAQUE)),
            ("4", "10", MathTex(r"\frac{4 \cdot 5}{2}", color=COR_DESTAQUE)),
            ("5", "15", MathTex(r"\frac{5 \cdot 6}{2}", color=COR_DESTAQUE)),
        ]
        cab_labels = ["n", "Quantidade", "Padrão"]
        grupos, _ = tabela_3col(dados, cab_labels,
                                anc_y, anc_x,
                                col_w=COL_W, row_h=ROW_H)

        self.play(FadeIn(grupos[0]), run_time=0.7)
        for lg in grupos[1:]:
            self.play(FadeIn(lg), run_time=0.45)
            self.wait(0.15)

        # Fórmula geral à direita com buff maior para não encostar no label
        label_form = Text("Fórmula Geral:", color=COR_ACENTO).scale(0.50)
        formula = MathTex(r"a_n = \dfrac{n\,(n+1)}{2}",
                          color=COR_FORMULA).scale(0.95)
        grp_form = VGroup(label_form, formula).arrange(DOWN, buff=0.45)
        grp_form.move_to(RIGHT * 3.6 + UP * (-0.3))

        caixa = SurroundingRectangle(formula, color=COR_FORMULA,
                                     buff=0.25, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Write(label_form), run_time=0.8)
        self.play(Write(formula), Create(caixa), run_time=1.3)
        self.wait(0.8)

        # Verificação posicionada abaixo da última linha da tabela
        verif = VGroup(
            Text("Verificação: n=5  →  ", color=COR_ACENTO).scale(0.49),
            MathTex(r"\frac{5 \cdot 6}{2} = 15", color=COR_ACENTO).scale(0.65),
            Text("  ✓", color=COR_ACENTO).scale(0.49),
        ).arrange(RIGHT, buff=0.08)
        verif.next_to(grupos[-1], DOWN, buff=0.20)

        self.play(Write(verif), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 8 – Resumo: os três padrões lado a lado
# ══════════════════════════════════════════════════════════════
class C08_Comparativo(Scene):
    """
    Conceito: Resumo comparativo dos três padrões estudados
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve consolidar a diferença entre padrão quadrático, linear e triangular
    """
    def construct(self):
        tit = titulo_cena("Resumo dos Padrões Estudados")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        padroes = [
            ("1. Quadrático",  "1, 4, 9, 16, 25, ...",
             MathTex(r"a_n = n^2",               color=COR_FORMULA).scale(0.75),
             COR_BASE,      1.4),
            ("2. Linear",      "3, 5, 7, 9, 11, ...",
             MathTex(r"a_n = 2n + 1",            color=COR_FORMULA).scale(0.75),
             COR_DESTAQUE,  0.0),
            ("3. Triangular",  "1, 3, 6, 10, 15, ...",
             MathTex(r"a_n = \dfrac{n(n+1)}{2}", color=COR_FORMULA).scale(0.72),
             COR_FORMULA,  -1.2),
        ]

        boxes = []
        for nome, seq, form, cor, y in padroes:
            nome_t = Text(nome, color=cor).scale(0.56)
            nome_t.move_to(LEFT * 4.2 + UP * y)

            seq_t = Text(seq, color=COR_TITULO).scale(0.50)
            seq_t.move_to(LEFT * 1.0 + UP * y)

            form.move_to(RIGHT * 3.5 + UP * y)
            box = SurroundingRectangle(form, color=cor, buff=0.18,
                                       corner_radius=0.10, stroke_width=1.8)
            boxes.append(box)

            self.play(FadeIn(nome_t), run_time=0.55)
            self.play(Write(seq_t), run_time=0.75)
            self.play(Write(form), Create(box), run_time=0.90)
            self.wait(0.65)

        final = Text(
            "Toda sequência com padrão tem uma expressão algébrica!",
            color=COR_ACENTO,
        ).scale(0.50)
        # Frase abaixo da caixa triangular, centralizada na tela
        final.next_to(boxes[-1], DOWN, buff=0.30)
        final.set_x(0)
        self.play(Write(final), run_time=1.3)
        self.wait(3.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)


# ══════════════════════════════════════════════════════════════
# CENA 9 – Estratégia para o D32
# ══════════════════════════════════════════════════════════════
class C09_Estrategia(Scene):
    """
    Conceito: Estratégia de resolução para questões do D32
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: O aluno deve saber aplicar os 5 passos para identificar e verificar a expressão algébrica
    """
    def construct(self):
        tit = titulo_cena("Estratégia para o D32")
        sep = separador()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        passos = [
            ("1", "Observe a sequência e organize em tabela (n, valor)."),
            ("2", "Calcule as diferenças entre termos consecutivos."),
            ("3", "Diferença fixa → padrão linear  |  cresce → quadrático."),
            ("4", "Monte a fórmula geral e use n=1 para encontrar a constante."),
            ("5", "Verifique com n=2 e n=3 antes de marcar a resposta!"),
        ]

        # 5 passos × 0.82 = 4.10 unidades
        # y vai de 1.75 até 1.75 - 4×0.82 = -1.53  (seguro)
        y_ini = 1.75
        dy    = 0.82

        for i, (num, texto) in enumerate(passos):
            y = y_ini - i * dy

            bolinha = Circle(radius=0.26, color=COR_ACENTO,
                             fill_color=COR_ACENTO, fill_opacity=0.90,
                             stroke_width=0)
            bolinha.move_to(LEFT * 5.8 + UP * y)

            num_t = Text(num, color=BLACK).scale(0.50)
            num_t.move_to(bolinha.get_center())

            passo_t = Text(texto, color=COR_TITULO).scale(0.48)
            passo_t.next_to(bolinha, RIGHT, buff=0.30)
            passo_t.align_to(bolinha, UP)

            self.play(FadeIn(bolinha), FadeIn(num_t), run_time=0.35)
            self.play(Write(passo_t), run_time=0.85)
            self.wait(0.45)

        # Frase de fechamento: bem abaixo do passo 5
        # y passo 5 = 1.75 - 4×0.82 = -1.53 → fundo ≈ -1.8
        # conclusão em CONT_BASE + 0.20 = -2.0  (afastado, sem sobreposição)
        conclusao = Text(
            "A expressão algébrica é a linguagem matemática do padrão!",
            color=COR_DESTAQUE,
        ).scale(0.51)
        conclusao.move_to(UP * (CONT_BASE + 0.20))

        self.play(Write(conclusao), run_time=1.3)
        self.wait(3.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(0.3)


# ══════════════════════════════════════════════════════════════
# CENA MESTRE – une todas as cenas em sequência
# ══════════════════════════════════════════════════════════════
class D32_Final(Scene):
    """
    Animação completa D32 – SAEB Matemática 9º Ano.

    Cenas:
      1  Apresentação do descritor
      2  O que é um Padrão? (figuras quadradas)
      3  Tabela 3 colunas: padrão quadrático
      4  Construindo a expressão algébrica n²
      5a Sequência Linear: círculos + setas arqueadas
      5b Tabela + derivação da fórmula linear
      6  Construindo a fórmula a_n = 2n+1 (passo a passo)
      7a Padrão Triangular: figuras + setas arqueadas
      7b Tabela + fórmula triangular
      8  Resumo comparativo dos 3 padrões
      9  Estratégia para o D32
    """

    def _limpar(self):
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)

    def _tit(self, texto, cor=COR_TITULO, escala=0.62):
        t = Text(texto, color=cor).scale(escala)
        t.move_to(UP * TOPO)
        return t

    def _tit_com_formula(self, texto, formula_tex):
        t = Text(texto, color=COR_TITULO).scale(0.62)
        f = MathTex(formula_tex, color=COR_FORMULA).scale(0.70)
        grp = VGroup(t, f).arrange(RIGHT, buff=0.3)
        grp.move_to(UP * TOPO)
        return grp

    def _sep(self):
        return separador()

    def _tabela(self, dados, cab_labels, col_w=2.2, row_h=0.54,
                anc_y=None, anc_x=None):
        if anc_y is None: anc_y = CONT_TOPO
        if anc_x is None: anc_x = -len(cab_labels) * col_w / 2
        return tabela_3col(dados, cab_labels,
                           anc_y, anc_x,
                           col_w=col_w, row_h=row_h)

    # ----------------------------------------------------------
    def _cena1(self):
        faixa = Rectangle(width=14.4, height=1.05,
                          fill_color=DARK_BLUE, fill_opacity=0.9,
                          stroke_width=0).move_to(UP * 2.55)
        saeb = Text("SAEB  |  Matemática  |  9º Ano",
                    color=COR_ACENTO).scale(0.52)
        saeb.move_to(faixa.get_center())
        codigo = Text("D32", color=COR_DESTAQUE).scale(2.4)
        codigo.move_to(UP * 0.85)
        linha = Line(LEFT * 3.0, RIGHT * 3.0,
                     color=COR_BASE, stroke_width=2.5)
        linha.next_to(codigo, DOWN, buff=0.35)
        desc = Text(
            "Identificar a expressão algébrica que\n"
            "expressa uma regularidade observada\n"
            "em sequências de números ou figuras.",
            color=COR_TITULO, line_spacing=1.5,
        ).scale(0.58)
        desc.next_to(linha, DOWN, buff=0.45)
        self.play(FadeIn(faixa), FadeIn(saeb), run_time=0.8)
        self.play(Write(codigo), run_time=1.2)
        self.play(Create(linha), run_time=0.6)
        self.play(Write(desc), run_time=2.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena2(self):
        tit = self._tit("O que é um Padrão?")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        TAM = 0.34
        grupos = VGroup()
        for n in range(1, 5):
            grade = VGroup()
            for r in range(n):
                for c in range(n):
                    sq = Square(side_length=TAM, color=COR_BASE,
                                fill_color=COR_BASE, fill_opacity=0.5,
                                stroke_width=1.5)
                    sq.move_to(RIGHT * c * TAM + DOWN * r * TAM)
                    grade.add(sq)
            grade.move_to(ORIGIN)
            rot_n  = Text(f"n = {n}", color=COR_DESTAQUE).scale(0.50)
            rot_qt = MathTex(f"{n*n}", color=COR_FORMULA).scale(0.55)
            rot_l  = Text("quad.", color=COR_FORMULA).scale(0.42)
            rot_linha = VGroup(rot_qt, rot_l).arrange(RIGHT, buff=0.08)
            bloco = VGroup(grade, rot_n, rot_linha)
            bloco.arrange(DOWN, buff=0.25)
            grupos.add(bloco)

        grupos.arrange(RIGHT, buff=0.7)
        grupos.move_to(UP * 0.35)

        pergunta = Text(
            "Quantos quadradinhos tem a figura de posição n?",
            color=COR_TITULO,
        ).scale(0.52)
        # Margem de segurança: CONT_BASE + 0.1 em vez de - 0.1
        pergunta.move_to(UP * (CONT_BASE + 0.1))

        for bloco in grupos:
            self.play(FadeIn(bloco), run_time=0.9)
            self.wait(0.35)
        self.play(Write(pergunta), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena3(self):
        tit = self._tit("Organizando em Tabela")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        COL_W = 2.55
        ROW_H = 0.54
        dados = [
            ("1", "1",  MathTex(r"1^2", color=COR_DESTAQUE)),
            ("2", "4",  MathTex(r"2^2", color=COR_DESTAQUE)),
            ("3", "9",  MathTex(r"3^2", color=COR_DESTAQUE)),
            ("4", "16", MathTex(r"4^2", color=COR_DESTAQUE)),
            ("5", "25", MathTex(r"5^2", color=COR_DESTAQUE)),
        ]
        cab_labels = ["Figura (n)", "Quadradinhos", "Padrão"]
        grupos, _ = self._tabela(dados, cab_labels,
                                  col_w=COL_W, row_h=ROW_H,
                                  anc_y=CONT_TOPO,
                                  anc_x=-3*COL_W/2)

        self.play(FadeIn(grupos[0]), run_time=0.8)
        for lg in grupos[1:]:
            self.play(FadeIn(lg), run_time=0.55)
            self.wait(0.2)

        obs = VGroup(
            Text("Padrão observado: quantidade = ", color=COR_TITULO).scale(0.50),
            MathTex(r"n^2", color=COR_DESTAQUE).scale(0.75),
        ).arrange(RIGHT, buff=0.1)
        obs.move_to(UP * (CONT_BASE + 0.3))
        self.play(Write(obs), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena4(self):
        tit = self._tit("Construindo a Expressão Algébrica")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        passos = [
            ("Passo 1 – Observar",
             Text("Cada figura n tem n linhas × n colunas de quadradinhos.",
                  color=COR_TITULO).scale(0.50)),
            ("Passo 2 – Traduzir",
             MathTex(r"\text{Quantidade} = n \times n",
                     color=COR_TITULO).scale(0.80)),
            ("Passo 3 – Simplificar",
             MathTex(r"\text{Quantidade} = n^2",
                     color=COR_DESTAQUE).scale(0.82)),
            ("Passo 4 – Fórmula Geral",
             MathTex(r"a_n = n^2", color=COR_FORMULA).scale(0.90)),
        ]
        # y_tops: gap calculado para que fundo do Passo3 não toque label do Passo4
        y_tops = [1.70, 0.94, 0.06, -1.05]
        form_final = None

        for (label, conteudo), y_top in zip(passos, y_tops):
            lbl = Text(label, color=COR_ACENTO).scale(0.44)
            lbl.move_to(UP * y_top).align_to(LEFT * 6.0, LEFT)
            conteudo.next_to(lbl, DOWN, buff=0.08)
            conteudo.align_to(LEFT * 4.5, LEFT)
            self.play(FadeIn(lbl), run_time=0.5)
            self.play(Write(conteudo), run_time=1.0)
            self.wait(0.6)
            if label.startswith("Passo 4"):
                form_final = conteudo

        caixa = SurroundingRectangle(form_final, color=COR_FORMULA,
                                     buff=0.22, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Create(caixa), run_time=0.9)
        self.wait(0.8)

        # Verificação abaixo da caixa, centralizada na tela
        verif = VGroup(
            Text("Verificação: n = 6  →  ", color=COR_ACENTO).scale(0.50),
            MathTex(r"6^2 = 36", color=COR_ACENTO).scale(0.65),
            Text("  quadradinhos  ✓", color=COR_ACENTO).scale(0.50),
        ).arrange(RIGHT, buff=0.08)
        verif.next_to(caixa, DOWN, buff=0.18)
        verif.set_x(0)
        self.play(Write(verif), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena5a(self):
        tit = self._tit("Sequência Linear:  3, 5, 7, 9, 11, ...")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        numeros = [3, 5, 7, 9, 11]
        RAIO = 0.50
        pos_x = [-4.4, -2.2, 0.0, 2.2, 4.4]
        CY = 0.4

        circulos = VGroup(); nums_txt = VGroup(); pos_txt = VGroup()
        for i, (val, px) in enumerate(zip(numeros, pos_x)):
            circ = Circle(radius=RAIO, color=COR_BASE,
                          fill_color=COR_BASE, fill_opacity=0.35,
                          stroke_width=2.5).move_to(RIGHT * px + UP * CY)
            n_t = Text(str(val), color=COR_TITULO).scale(0.75)
            n_t.move_to(circ.get_center())
            p_t = MathTex(f"n={i+1}", color=COR_DESTAQUE).scale(0.50)
            p_t.next_to(circ, DOWN, buff=0.20)
            circulos.add(circ); nums_txt.add(n_t); pos_txt.add(p_t)

        for c, n, p in zip(circulos, nums_txt, pos_txt):
            self.play(FadeIn(c), Write(n), Write(p), run_time=0.65)
            self.wait(0.2)
        self.wait(0.4)

        setas_arq = VGroup(); dif_lbl = VGroup()
        for i in range(4):
            xa = np.array([pos_x[i],   CY + RAIO + 0.05, 0])
            xb = np.array([pos_x[i+1], CY + RAIO + 0.05, 0])
            seta = CurvedArrow(xa, xb, angle=-TAU/6,
                               color=COR_DESTAQUE, stroke_width=2.2,
                               tip_length=0.18)
            lbl = Text("+2", color=COR_DESTAQUE).scale(0.44)
            lbl.move_to(UP*(CY+RAIO+0.55) + RIGHT*(pos_x[i]+pos_x[i+1])/2)
            setas_arq.add(seta); dif_lbl.add(lbl)

        self.play(Create(setas_arq), Write(dif_lbl), run_time=1.3)
        self.wait(0.8)

        obs = Text("A diferença entre termos consecutivos é sempre 2.",
                   color=COR_DESTAQUE).scale(0.52)
        obs.move_to(UP * (CONT_BASE + 0.5))
        self.play(Write(obs), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena5b(self):
        tit = self._tit("Encontrando a Fórmula da Sequência Linear")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        COL_W = 2.2; ROW_H = 0.52
        dados = [
            ("1", "3",  MathTex(r"2(1)+1", color=COR_DESTAQUE)),
            ("2", "5",  MathTex(r"2(2)+1", color=COR_DESTAQUE)),
            ("3", "7",  MathTex(r"2(3)+1", color=COR_DESTAQUE)),
            ("4", "9",  MathTex(r"2(4)+1", color=COR_DESTAQUE)),
            ("5", "11", MathTex(r"2(5)+1", color=COR_DESTAQUE)),
        ]
        cab_labels = ["n", "Valor", "Padrão"]
        grupos, _ = tabela_3col(dados, cab_labels,
                                CONT_TOPO, -5.8,
                                col_w=COL_W, row_h=ROW_H)

        self.play(FadeIn(grupos[0]), run_time=0.7)
        for lg in grupos[1:]:
            self.play(FadeIn(lg), run_time=0.45)
            self.wait(0.15)

        for txt, dy in [("Diferença constante = 2", 1.55),
                        ("Coeficiente de n é 2",    0.80)]:
            t = Text(txt, color=COR_TITULO).scale(0.50)
            t.move_to(RIGHT * 3.5 + UP * dy)
            self.play(Write(t), run_time=0.9); self.wait(0.4)

        p2 = MathTex(r"a_n = 2n + \;?", color=COR_TITULO).scale(0.80)
        p2.move_to(RIGHT * 3.5 + UP * 0.05)
        self.play(Write(p2), run_time=1.0); self.wait(0.4)

        p3 = Text("Para n=1:  2×1+? = 3  →  ? = 1",
                  color=COR_TITULO).scale(0.48)
        p3.move_to(RIGHT * 3.5 + UP * (-0.65))
        self.play(Write(p3), run_time=1.0); self.wait(0.4)

        formula = MathTex(r"a_n = 2n + 1", color=COR_FORMULA).scale(1.05)
        formula.move_to(RIGHT * 3.5 + UP * (-1.4))
        caixa = SurroundingRectangle(formula, color=COR_FORMULA,
                                     buff=0.22, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Write(formula), Create(caixa), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena6(self):
        tit_grp = self._tit_com_formula("Construindo a Fórmula:",
                                        r"a_n = 2n + 1")
        sep = self._sep()
        # Separar animações para não sobrecarregar a percepção visual
        self.play(Write(tit_grp), run_time=1.0)
        self.play(Create(sep), run_time=0.6)
        self.wait(0.3)

        passos = [
            ("Passo 1 – Diferença constante",
             MathTex(r"5-3=2,\quad 7-5=2,\quad 9-7=2 \;\Rightarrow\; \Delta=2",
                     color=COR_DESTAQUE).scale(0.60)),
            ("Passo 2 – Coeficiente de n",
             MathTex(r"a_n = 2n + \;?", color=COR_TITULO).scale(0.80)),
            ("Passo 3 – Encontrar a constante",
             MathTex(r"n=1:\; 2(1)+?=3 \;\Rightarrow\; ?=1",
                     color=COR_TITULO).scale(0.68)),
            ("Passo 4 – Fórmula Geral",
             MathTex(r"a_n = 2n + 1", color=COR_FORMULA).scale(0.90)),
        ]
        # y_tops: gap calculado para que fundo do Passo3 não toque label do Passo4
        y_tops = [1.65, 0.83, -0.05, -1.05]
        form_final = None

        for (label, conteudo), y_top in zip(passos, y_tops):
            lbl = Text(label, color=COR_ACENTO).scale(0.44)
            lbl.move_to(UP * y_top).align_to(LEFT * 6.0, LEFT)
            conteudo.next_to(lbl, DOWN, buff=0.08)
            conteudo.align_to(LEFT * 5.0, LEFT)
            self.play(FadeIn(lbl), run_time=0.5)
            self.play(Write(conteudo), run_time=1.0)
            self.wait(0.6)
            if label.startswith("Passo 4"):
                form_final = conteudo

        caixa = SurroundingRectangle(form_final, color=COR_FORMULA,
                                     buff=0.22, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Create(caixa), run_time=0.8)
        self.wait(0.7)

        # Verificação abaixo da caixa, centralizada na tela
        verif = VGroup(
            Text("Verificação: n=10  →  ", color=COR_ACENTO).scale(0.50),
            MathTex(r"2(10)+1 = 21", color=COR_ACENTO).scale(0.65),
            Text("  ✓", color=COR_ACENTO).scale(0.50),
        ).arrange(RIGHT, buff=0.08)
        verif.next_to(caixa, DOWN, buff=0.18)
        verif.set_x(0)
        self.play(Write(verif), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena7a(self):
        tit = self._tit("Padrão Triangular:  1, 3, 6, 10, ...")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        RAIO_PT = 0.17
        dados = [(1,1),(2,3),(3,6),(4,10)]
        pos_x = [-4.8,-1.6,1.6,4.8]
        # Baixar CY para que as setas arqueadas passem bem acima das figuras
        CY = 0.0

        blocos = VGroup()
        for (n, total), px in zip(dados, pos_x):
            pontos = VGroup()
            for i in range(1, n+1):
                offset_x = -(i-1)*RAIO_PT*2.6/2
                for j in range(i):
                    pt = Circle(radius=RAIO_PT, color=COR_BASE,
                                fill_color=COR_BASE, fill_opacity=0.85,
                                stroke_width=0)
                    pt.move_to(RIGHT*(offset_x+j*RAIO_PT*2.6)
                               + DOWN*(i-1)*RAIO_PT*2.4)
                    pontos.add(pt)
            rot_n  = MathTex(f"n={n}", color=COR_DESTAQUE).scale(0.52)
            rot_qt = MathTex(str(total), color=COR_FORMULA).scale(0.60)
            bloco  = VGroup(pontos, rot_n, rot_qt)
            bloco.arrange(DOWN, buff=0.28)
            bloco.move_to(RIGHT*px + UP*CY)
            blocos.add(bloco)

        for b in blocos:
            self.play(FadeIn(b), run_time=0.85); self.wait(0.3)
        self.wait(0.4)

        difs_val = ["+2", "+3", "+4"]
        setas_arq = VGroup(); dif_lbl = VGroup()
        # topo_y elevado para garantir que as setas fiquem acima das figuras
        topo_y = CY + 1.10
        for i in range(3):
            xa = np.array([pos_x[i],   topo_y+0.10, 0])
            xb = np.array([pos_x[i+1], topo_y+0.10, 0])
            seta = CurvedArrow(xa, xb, angle=-TAU/6,
                               color=COR_DESTAQUE, stroke_width=2.2,
                               tip_length=0.18)
            lbl = Text(difs_val[i], color=COR_DESTAQUE).scale(0.46)
            lbl.move_to(UP*(topo_y+0.85)+RIGHT*(pos_x[i]+pos_x[i+1])/2)
            setas_arq.add(seta); dif_lbl.add(lbl)

        self.play(Create(setas_arq), Write(dif_lbl), run_time=1.3)
        self.wait(0.8)

        obs = Text("As diferenças crescem de 1 em 1 → padrão não linear!",
                   color=COR_DESTAQUE).scale(0.50)
        obs.move_to(UP * (CONT_BASE + 0.5))
        self.play(Write(obs), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena7b(self):
        tit = self._tit("Fórmula do Padrão Triangular")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        # ROW_H=0.60 para que a tabela caiba e a verificação não sobreponha
        COL_W = 2.3; ROW_H = 0.60
        dados = [
            ("1", "1",  MathTex(r"\frac{1\cdot2}{2}", color=COR_DESTAQUE)),
            ("2", "3",  MathTex(r"\frac{2\cdot3}{2}", color=COR_DESTAQUE)),
            ("3", "6",  MathTex(r"\frac{3\cdot4}{2}", color=COR_DESTAQUE)),
            ("4", "10", MathTex(r"\frac{4\cdot5}{2}", color=COR_DESTAQUE)),
            ("5", "15", MathTex(r"\frac{5\cdot6}{2}", color=COR_DESTAQUE)),
        ]
        cab_labels = ["n", "Quantidade", "Padrão"]
        grupos, _ = tabela_3col(dados, cab_labels,
                                CONT_TOPO, -5.8,
                                col_w=COL_W, row_h=ROW_H)

        self.play(FadeIn(grupos[0]), run_time=0.7)
        for lg in grupos[1:]:
            self.play(FadeIn(lg), run_time=0.45); self.wait(0.15)

        label_form = Text("Fórmula Geral:", color=COR_ACENTO).scale(0.50)
        formula = MathTex(r"a_n = \dfrac{n\,(n+1)}{2}",
                          color=COR_FORMULA).scale(0.95)
        grp_form = VGroup(label_form, formula).arrange(DOWN, buff=0.45)
        # Fórmula geral com buff maior para não encostar no label
        grp_form.move_to(RIGHT * 3.6 + UP * (-0.3))
        caixa = SurroundingRectangle(formula, color=COR_FORMULA,
                                     buff=0.25, corner_radius=0.14,
                                     stroke_width=2.5)
        self.play(Write(label_form), run_time=0.8)
        self.play(Write(formula), Create(caixa), run_time=1.3)
        self.wait(0.8)

        # Verificação posicionada abaixo da última linha da tabela
        verif = VGroup(
            Text("Verificação: n=5  →  ", color=COR_ACENTO).scale(0.49),
            MathTex(r"\frac{5\cdot6}{2}=15", color=COR_ACENTO).scale(0.65),
            Text("  ✓", color=COR_ACENTO).scale(0.49),
        ).arrange(RIGHT, buff=0.08)
        verif.next_to(grupos[-1], DOWN, buff=0.20)
        self.play(Write(verif), run_time=1.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena8(self):
        tit = self._tit("Resumo dos Padrões Estudados")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        padroes = [
            ("1. Quadrático",  "1, 4, 9, 16, 25, ...",
             MathTex(r"a_n = n^2", color=COR_FORMULA).scale(0.75),
             COR_BASE,     1.4),
            ("2. Linear",      "3, 5, 7, 9, 11, ...",
             MathTex(r"a_n = 2n+1", color=COR_FORMULA).scale(0.75),
             COR_DESTAQUE, 0.0),
            ("3. Triangular",  "1, 3, 6, 10, 15, ...",
             MathTex(r"a_n = \dfrac{n(n+1)}{2}", color=COR_FORMULA).scale(0.72),
             COR_FORMULA, -1.2),
        ]
        boxes = []
        for nome, seq, form, cor, y in padroes:
            nome_t = Text(nome, color=cor).scale(0.56)
            nome_t.move_to(LEFT * 4.2 + UP * y)
            seq_t = Text(seq, color=COR_TITULO).scale(0.50)
            seq_t.move_to(LEFT * 1.0 + UP * y)
            form.move_to(RIGHT * 3.5 + UP * y)
            box = SurroundingRectangle(form, color=cor, buff=0.18,
                                       corner_radius=0.10, stroke_width=1.8)
            boxes.append(box)
            self.play(FadeIn(nome_t), run_time=0.55)
            self.play(Write(seq_t), run_time=0.75)
            self.play(Write(form), Create(box), run_time=0.90)
            self.wait(0.65)

        final = Text("Toda sequência com padrão tem uma expressão algébrica!",
                     color=COR_ACENTO).scale(0.50)
        # Frase abaixo da caixa triangular, centralizada na tela
        final.next_to(boxes[-1], DOWN, buff=0.30)
        final.set_x(0)
        self.play(Write(final), run_time=1.3)
        self.wait(3.0)
        self._limpar()

    # ----------------------------------------------------------
    def _cena9(self):
        tit = self._tit("Estratégia para o D32")
        sep = self._sep()
        self.play(Write(tit), Create(sep), run_time=1.0)
        self.wait(0.3)

        passos = [
            ("1", "Observe a sequência e organize em tabela (n, valor)."),
            ("2", "Calcule as diferenças entre termos consecutivos."),
            ("3", "Diferença fixa → padrão linear  |  cresce → quadrático."),
            ("4", "Monte a fórmula geral e use n=1 para encontrar a constante."),
            ("5", "Verifique com n=2 e n=3 antes de marcar a resposta!"),
        ]
        y_ini = 1.75
        dy    = 0.82

        for i, (num, texto) in enumerate(passos):
            y = y_ini - i * dy
            bolinha = Circle(radius=0.26, color=COR_ACENTO,
                             fill_color=COR_ACENTO, fill_opacity=0.90,
                             stroke_width=0)
            bolinha.move_to(LEFT * 5.8 + UP * y)
            num_t = Text(num, color=BLACK).scale(0.50)
            num_t.move_to(bolinha.get_center())
            passo_t = Text(texto, color=COR_TITULO).scale(0.48)
            passo_t.next_to(bolinha, RIGHT, buff=0.30)
            passo_t.align_to(bolinha, UP)
            self.play(FadeIn(bolinha), FadeIn(num_t), run_time=0.35)
            self.play(Write(passo_t), run_time=0.85)
            self.wait(0.45)

        # Passo 5 termina em y ≈ -1.53; conclusão em -2.0 (afastada)
        conclusao = Text(
            "A expressão algébrica é a linguagem matemática do padrão!",
            color=COR_DESTAQUE,
        ).scale(0.51)
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
        self._cena5a()
        self._cena5b()
        self._cena6()
        self._cena7a()
        self._cena7b()
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
