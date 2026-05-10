from manim import *

# ================================================================
# D5 – SAEB Matemática 9º Ano
# Conceito : Reconhecer a conservação ou modificação de medidas
#            dos lados, do perímetro e da área em ampliação e/ou
#            redução de figuras poligonais usando malhas quadriculadas.
# Nível    : Ensino Fundamental – 9º Ano
#
# ZONA SEGURA DE CONTEÚDO: y ∈ [-2.8, +2.8] | x ∈ [-6.2, +6.2]
#
# Paleta fixa:
#   COR_TITULO   = WHITE    textos gerais
#   COR_ORIGINAL = BLUE_C   figura original
#   COR_AMPLIADA = YELLOW   figura ampliada
#   COR_REDUZIDA = RED      figura reduzida
#   COR_ACENTO   = ORANGE   perímetro / destaques
#   COR_FORMULA  = GREEN_C  área / conclusões
# ================================================================

COR_TITULO   = WHITE
COR_ORIGINAL = BLUE_C
COR_AMPLIADA = YELLOW
COR_REDUZIDA = RED
COR_ACENTO   = ORANGE
COR_FORMULA  = GREEN_C

Y_TITULO = 2.8
Y_SEP    = 2.35
Y_TOPO   = 1.85
Y_RODAPE = -2.50
CELL     = 0.55


def tit(texto):
    t = Text(texto, color=COR_TITULO).scale(0.60)
    t.move_to(UP * Y_TITULO)
    return t


def sep():
    return Line(LEFT * 6.2, RIGHT * 6.2,
                color=GREY_D, stroke_width=1.5).move_to(UP * Y_SEP)


def malha(cols, rows, cx=0.0, cy=0.0, cor=GREY_C, op=0.35):
    g = VGroup()
    w  = cols * CELL
    h  = rows * CELL
    ox = cx - w / 2
    oy = cy - h / 2
    for i in range(cols + 1):
        x = ox + i * CELL
        g.add(Line([x, oy, 0], [x, oy + h, 0],
                   color=cor, stroke_width=0.9, stroke_opacity=op))
    for j in range(rows + 1):
        y = oy + j * CELL
        g.add(Line([ox, y, 0], [ox + w, y, 0],
                   color=cor, stroke_width=0.9, stroke_opacity=op))
    return g


def retangulo(cols, rows, cx=0.0, cy=0.0, cor=COR_ORIGINAL, op=0.30):
    w = cols * CELL
    h = rows * CELL
    r = Rectangle(width=w, height=h,
                  fill_color=cor, fill_opacity=op,
                  stroke_color=cor, stroke_width=2.5)
    r.move_to([cx, cy, 0])
    return r


def malha_e_figura(fig_cols, fig_rows, ox=0.0, oy=0.0, margem=1,
                   cor_fig=COR_ORIGINAL, op_fig=0.35,
                   cor_malha=GREY_C, op_malha=0.35):
    """
    Cria malha e figura perfeitamente alinhadas.
    ox, oy = canto inferior esquerdo da malha.
    A figura começa 'margem' células dentro da malha em cada lado.
    Retorna (malha_vgroup, figura, cx_fig, cy_fig).
    """
    m_cols = fig_cols + 2 * margem
    m_rows = fig_rows + 2 * margem
    cx_m = ox + m_cols * CELL / 2
    cy_m = oy + m_rows * CELL / 2
    m = malha(m_cols, m_rows, cx=cx_m, cy=cy_m,
              cor=cor_malha, op=op_malha)
    fig_ox = ox + margem * CELL
    fig_oy = oy + margem * CELL
    cx_fig = fig_ox + fig_cols * CELL / 2
    cy_fig = fig_oy + fig_rows * CELL / 2
    fig = retangulo(fig_cols, fig_rows, cx=cx_fig, cy=cy_fig,
                    cor=cor_fig, op=op_fig)
    return m, fig, cx_fig, cy_fig


# ══════════════════════════════════════════════════════════════
class D5_Final(Scene):
    """
    Conceito: Ampliação e redução de figuras poligonais em malha
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Reconhecer como lados, perímetro e área mudam
              ao ampliar ou reduzir uma figura na malha quadriculada.
    Cenas:
      1  Apresentação do D5
      2  Figura original — lados, perímetro e área com cálculos
      3  Ampliação fator 2 — evidencia perímetro dobra e área quadruplica
      4  Redução fator ½ — mesma lógica
      5  Tabela comparativa + fórmula geral
      6  Ângulos conservados
      7  Estratégia para o D5
    """

    def _limpar(self):
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.7)
        self.wait(0.2)

    # ----------------------------------------------------------
    def _cena1(self):
        """Apresentação do descritor D5 com texto balanceado."""
        faixa = Rectangle(width=14.4, height=1.0,
                          fill_color=DARK_BLUE, fill_opacity=0.9,
                          stroke_width=0).move_to(UP * 2.8)
        rotulo = Text("SAEB  |  Matemática  |  9º Ano",
                      color=COR_ACENTO).scale(0.50)
        rotulo.move_to(faixa.get_center())

        codigo = Text("D5", color=COR_AMPLIADA).scale(2.2)
        codigo.move_to(UP * 0.95)

        linha = Line(LEFT * 3.0, RIGHT * 3.0,
                     color=COR_ORIGINAL, stroke_width=2.0)
        linha.next_to(codigo, DOWN, buff=0.30)

        # Texto com quebras manuais equilibradas — efeito justificado
        desc = Text(
            "Reconhecer a conservação ou modificação de medidas\n"
            "dos lados, do perímetro e da área em ampliação e/ou\n"
            "redução de figuras poligonais usando malhas quadriculadas.",
            color=COR_TITULO, line_spacing=1.45,
        ).scale(0.52)
        desc.next_to(linha, DOWN, buff=0.38)

        self.play(FadeIn(faixa), FadeIn(rotulo), run_time=0.8)
        self.play(Write(codigo), run_time=1.0)
        self.play(Create(linha), run_time=0.5)
        self.play(Write(desc), run_time=2.2)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena2(self):
        """Figura original com setas de largura/altura e cálculos explícitos."""
        titulo = tit("A Figura Original na Malha")
        separador = sep()
        self.play(Write(titulo), run_time=1.0)
        self.play(Create(separador), run_time=0.5)
        self.wait(0.3)

        # Malha e figura alinhadas — ox,oy = canto inf-esq da malha
        # malha 6×5 (4+1 margem cada lado), figura 4×3 no centro
        m, fig, cx_fig, cy_fig = malha_e_figura(
            4, 3, ox=-5.0, oy=-1.10, margem=1,
            cor_fig=COR_ORIGINAL, op_fig=0.35)
        self.play(Create(m), run_time=1.0)
        self.wait(0.2)
        self.play(Create(fig), run_time=1.0)
        self.wait(0.4)

        lbl = Text("Figura Original", color=COR_ORIGINAL, weight=BOLD).scale(0.46)
        lbl.next_to(fig, UP, buff=0.22)
        self.play(FadeIn(lbl), run_time=0.6)
        self.wait(0.4)

        # Setas dimensionais usando cx_fig/cy_fig calculados
        larg_w = 4 * CELL
        alt_h  = 3 * CELL

        seta_larg = DoubleArrow(
            [cx_fig - larg_w / 2, cy_fig - alt_h / 2 - 0.32, 0],
            [cx_fig + larg_w / 2, cy_fig - alt_h / 2 - 0.32, 0],
            color=COR_AMPLIADA, buff=0,
            stroke_width=2.0, tip_length=0.16,
        )
        lbl_larg = Text("4 un", color=COR_AMPLIADA).scale(0.40)
        lbl_larg.next_to(seta_larg, DOWN, buff=0.10)
        self.play(Create(seta_larg), FadeIn(lbl_larg), run_time=0.8)
        self.wait(0.3)

        # Seta dupla de ALTURA — vertical, à esquerda da figura
        seta_alt = DoubleArrow(
            [cx_fig - larg_w / 2 - 0.32, cy_fig - alt_h / 2, 0],
            [cx_fig - larg_w / 2 - 0.32, cy_fig + alt_h / 2, 0],
            color=COR_REDUZIDA, buff=0,
            stroke_width=2.0, tip_length=0.16,
        )
        lbl_alt = Text("3 un", color=COR_REDUZIDA).scale(0.40)
        lbl_alt.next_to(seta_alt, LEFT, buff=0.10)
        self.play(Create(seta_alt), FadeIn(lbl_alt), run_time=0.8)
        self.wait(0.4)

        # Informações lado direito — empilhadas sem sobreposição
        x_info = 3.4
        y_cur  = Y_TOPO

        i1 = Text("Largura = 4 unidades", color=COR_AMPLIADA).scale(0.44)
        i1.move_to([x_info, y_cur, 0])
        self.play(FadeIn(i1), run_time=0.6)
        self.wait(0.2)
        y_cur -= 0.58

        i2 = Text("Altura   = 3 unidades", color=COR_REDUZIDA).scale(0.44)
        i2.move_to([x_info, y_cur, 0])
        self.play(FadeIn(i2), run_time=0.6)
        self.wait(0.3)
        y_cur -= 0.72

        # Cálculo do perímetro
        p_tit = Text("Perímetro:", color=COR_ACENTO, weight=BOLD).scale(0.44)
        p_tit.move_to([x_info, y_cur, 0])
        self.play(FadeIn(p_tit), run_time=0.5)
        y_cur -= 0.50

        p_calc = Text("4 + 3 + 4 + 3 = 14 unidades", color=COR_ACENTO).scale(0.42)
        p_calc.move_to([x_info, y_cur, 0])
        self.play(FadeIn(p_calc), run_time=0.7)
        self.wait(0.3)
        y_cur -= 0.72

        # Cálculo da área
        a_tit = Text("Área:", color=COR_FORMULA, weight=BOLD).scale(0.44)
        a_tit.move_to([x_info, y_cur, 0])
        self.play(FadeIn(a_tit), run_time=0.5)
        y_cur -= 0.50

        a_calc = Text("4 × 3 = 12 unidades²", color=COR_FORMULA).scale(0.42)
        a_calc.move_to([x_info, y_cur, 0])
        self.play(FadeIn(a_calc), run_time=0.7)
        self.wait(0.3)

        grp = VGroup(i1, i2, p_tit, p_calc, a_tit, a_calc)
        caixa = SurroundingRectangle(grp, color=COR_ORIGINAL,
                                     buff=0.22, corner_radius=0.12,
                                     stroke_width=2.0)
        self.play(Create(caixa), run_time=0.7)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena3(self):
        """Ampliação ×2: encaixa 4 originais dentro da ampliada para evidenciar área."""
        titulo = tit("Ampliação  –  Fator 2")
        separador = sep()
        self.play(Write(titulo), run_time=1.0)
        self.play(Create(separador), run_time=0.5)
        self.wait(0.3)

        # ── Coordenadas base calculadas a partir do canto inferior esquerdo ──
        # Estratégia: definir ox_o/oy_o (canto inf-esq da malha original) e
        # ox_a/oy_a (canto inf-esq da malha ampliada) explicitamente,
        # garantindo que CELL bate pixel a pixel em ambas.

        # ETAPA 1 — Original 4×3 e ampliada 8×6 lado a lado
        # Todas criadas com malha_e_figura para alinhamento perfeito
        m_o, fig_o, cx_o, cy_o = malha_e_figura(
            4, 3, ox=-6.0, oy=-0.65, margem=1,
            cor_fig=COR_ORIGINAL, op_fig=0.35)
        self.play(Create(m_o), run_time=0.8)
        self.play(Create(fig_o), run_time=0.9)
        lbl_o = Text("Original  4×3", color=COR_ORIGINAL).scale(0.42)
        lbl_o.next_to(fig_o, DOWN, buff=0.18)
        self.play(FadeIn(lbl_o), run_time=0.5)
        self.wait(0.5)

        seta = Arrow([-2.0, cy_o, 0], [-0.9, cy_o, 0],
                     color=COR_AMPLIADA, buff=0,
                     stroke_width=2.5, tip_length=0.20)
        f_lbl = Text("× 2", color=COR_AMPLIADA).scale(0.52)
        f_lbl.next_to(seta, UP, buff=0.10)
        self.play(Create(seta), FadeIn(f_lbl), run_time=0.8)
        self.wait(0.3)

        m_a2, fig_a2, cx_a2, cy_a2 = malha_e_figura(
            8, 6, ox=-0.6, oy=-1.65, margem=0,
            cor_fig=COR_AMPLIADA, op_fig=0.22)
        self.play(Create(m_a2), run_time=0.8)
        self.play(Create(fig_a2), run_time=1.2)
        lbl_a2 = Text("Ampliada  8×6", color=COR_AMPLIADA).scale(0.42)
        lbl_a2.next_to(fig_a2, DOWN, buff=0.18)
        self.play(FadeIn(lbl_a2), run_time=0.5)
        self.wait(0.8)

        # ── ETAPA 2: Fade out original/seta; centraliza a ampliada ──────────
        self.play(
            FadeOut(m_o), FadeOut(fig_o), FadeOut(lbl_o),
            FadeOut(seta), FadeOut(f_lbl),
            FadeOut(m_a2), FadeOut(fig_a2), FadeOut(lbl_a2),
            run_time=0.7,
        )
        self.wait(0.2)

        # Recria ampliada na metade ESQUERDA — malha x=[-5.50, 0.00], y=[-2.10, 2.30]
        # Toda a zona x > 0.30 fica LIVRE para textos
        m_a, fig_a, cx_fig, cy_fig = malha_e_figura(
            8, 6, ox=-5.50, oy=-2.10, margem=1,
            cor_fig=COR_AMPLIADA, op_fig=0.22)
        lbl_a = Text("Ampliada  8×6", color=COR_AMPLIADA).scale(0.42)
        lbl_a.next_to(fig_a, UP, buff=0.18)   # acima da figura — sem conflito

        self.play(Create(m_a), run_time=0.8)
        self.play(Create(fig_a), run_time=1.0)
        self.play(FadeIn(lbl_a), run_time=0.5)
        self.wait(0.4)

        # ── ETAPA 3: msg à DIREITA (x > 0.30, fora da malha) ────────────────
        msg_q = Text("Quantas vezes a\noriginal cabe\nna ampliada?",
                     color=COR_TITULO, line_spacing=1.3).scale(0.48)
        msg_q.move_to([3.5, 0.0, 0])
        self.play(FadeIn(msg_q), run_time=0.7)
        self.wait(0.4)

        fig_ox = -5.50 + 1 * CELL
        fig_oy = -2.10 + 1 * CELL
        w4 = 4 * CELL
        h3 = 3 * CELL

        posicoes = [
            (fig_ox + w4 / 2,       fig_oy + h3 + h3 / 2),
            (fig_ox + w4 + w4 / 2,  fig_oy + h3 + h3 / 2),
            (fig_ox + w4 / 2,       fig_oy + h3 / 2),
            (fig_ox + w4 + w4 / 2,  fig_oy + h3 / 2),
        ]
        cores_mini = [BLUE_C, BLUE_B, TEAL_C, TEAL_D]

        for i, ((px, py), cor_m) in enumerate(zip(posicoes, cores_mini)):
            mini = retangulo(4, 3, cx=px, cy=py, cor=cor_m, op=0.50)
            num_lbl = Text(str(i + 1), color=WHITE, weight=BOLD).scale(0.52)
            num_lbl.move_to([px, py, 0])
            self.play(FadeIn(mini), run_time=0.55)
            self.play(FadeIn(num_lbl), run_time=0.35)
            self.wait(0.25)

        self.play(FadeOut(msg_q), FadeOut(lbl_a), run_time=0.3)
        msg4 = Text("Cabe exatamente\n4 vezes!\n→  Área × 4",
                    color=COR_FORMULA, weight=BOLD, line_spacing=1.3).scale(0.50)
        msg4.move_to([3.5, 0.0, 0])
        caixa4 = SurroundingRectangle(msg4, color=COR_FORMULA,
                                      buff=0.18, corner_radius=0.10,
                                      stroke_width=2.0)
        self.play(Write(msg4), Create(caixa4), run_time=1.0)
        self.wait(1.5)

        # ── ETAPA 4: Cálculos à DIREITA — x_d=3.5, x > 0.30 sem malha ───────
        self.play(FadeOut(msg4), FadeOut(caixa4), run_time=0.4)

        x_d = 3.5
        y_cur = Y_TOPO   # 1.85

        p_orig = Text("Perímetro original:", color=COR_TITULO, weight=BOLD).scale(0.44)
        p_orig.move_to([x_d, y_cur, 0])
        self.play(FadeIn(p_orig), run_time=0.5)
        y_cur -= 0.52

        p_c1 = Text("4+3+4+3 = 14 un", color=COR_ORIGINAL).scale(0.42)
        p_c1.move_to([x_d, y_cur, 0])
        self.play(FadeIn(p_c1), run_time=0.5)
        y_cur -= 0.60

        p_amp_lbl = Text("Perímetro ampliado:", color=COR_TITULO, weight=BOLD).scale(0.44)
        p_amp_lbl.move_to([x_d, y_cur, 0])
        self.play(FadeIn(p_amp_lbl), run_time=0.5)
        y_cur -= 0.52

        p_c2 = Text("8+6+8+6 = 28 un", color=COR_AMPLIADA).scale(0.42)
        p_c2.move_to([x_d, y_cur, 0])
        self.play(FadeIn(p_c2), run_time=0.5)
        y_cur -= 0.60

        p_concl = Text("28 ÷ 14 = 2  →  dobrou!", color=COR_ACENTO, weight=BOLD).scale(0.44)
        p_concl.move_to([x_d, y_cur, 0])
        caixa_p = SurroundingRectangle(p_concl, color=COR_ACENTO,
                                       buff=0.16, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(p_concl), Create(caixa_p), run_time=0.9)
        y_cur -= 1.00
        self.wait(0.5)

        a_concl = Text("4×3=12  →  8×6=48\n48÷12 = 4  →  quadruplicou!",
                       color=COR_FORMULA, weight=BOLD,
                       line_spacing=1.3).scale(0.44)
        a_concl.move_to([x_d, y_cur, 0])
        caixa_a = SurroundingRectangle(a_concl, color=COR_FORMULA,
                                       buff=0.16, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(a_concl), Create(caixa_a), run_time=1.0)
        self.wait(3.0)
        self._limpar()

    # ----------------------------------------------------------
    def _cena4(self):
        """Redução ×½: lados caem à metade, área cai a ¼ — cálculos em duas colunas abaixo."""
        titulo = tit("Redução  –  Fator  ½")
        separador = sep()
        self.play(Write(titulo), run_time=1.0)
        self.play(Create(separador), run_time=0.5)
        self.wait(0.3)

        # ── Figuras alinhadas com malha_e_figura ──────────────────
        m_o, fig_o, cx_o, cy_o = malha_e_figura(
            4, 3, ox=-5.8, oy=-0.55, margem=1,
            cor_fig=COR_ORIGINAL, op_fig=0.35)
        self.play(Create(m_o), run_time=0.8)
        self.play(Create(fig_o), run_time=0.9)
        lbl_o = Text("Original  4×3", color=COR_ORIGINAL).scale(0.42)
        lbl_o.next_to(fig_o, DOWN, buff=0.18)
        self.play(FadeIn(lbl_o), run_time=0.5)
        self.wait(0.5)

        seta = Arrow([-1.6, cy_o, 0], [-0.4, cy_o, 0],
                     color=COR_REDUZIDA, buff=0,
                     stroke_width=2.5, tip_length=0.20)
        f_lbl = Text("÷ 2", color=COR_REDUZIDA).scale(0.52)
        f_lbl.next_to(seta, UP, buff=0.10)
        self.play(Create(seta), FadeIn(f_lbl), run_time=0.8)
        self.wait(0.3)

        # Reduzida: 2×1,5 — usamos 2×2 células mas altura real é 1.5
        # Para alinhar: malha 4×3 com figura 2×2 dentro (margem 1)
        m_r, fig_r, cx_r, cy_r = malha_e_figura(
            2, 2, ox=-0.1, oy=-0.55, margem=1,
            cor_fig=COR_REDUZIDA, op_fig=0.30)
        self.play(Create(m_r), run_time=0.7)
        self.play(Create(fig_r), run_time=0.8)
        lbl_r = Text("Reduzida  2×1,5", color=COR_REDUZIDA).scale(0.42)
        lbl_r.next_to(fig_r, DOWN, buff=0.18)
        self.play(FadeIn(lbl_r), run_time=0.5)
        self.wait(0.6)

        # ── Cálculos em DUAS COLUNAS abaixo das figuras ───────────
        # Coluna esquerda — PERÍMETRO
        p_tit = Text("PERÍMETRO", color=COR_ACENTO, weight=BOLD).scale(0.46)
        p_tit.move_to([-3.2, -1.45, 0])
        self.play(FadeIn(p_tit), run_time=0.5)

        p1 = Text("Original:   4+3+4+3 = 14 un", color=COR_ORIGINAL).scale(0.42)
        p1.next_to(p_tit, DOWN, buff=0.22)
        self.play(FadeIn(p1), run_time=0.5)

        p2 = Text("Reduzida:  2+1,5+2+1,5 = 7 un", color=COR_REDUZIDA).scale(0.42)
        p2.next_to(p1, DOWN, buff=0.18)
        self.play(FadeIn(p2), run_time=0.5)

        p3 = Text("7 ÷ 14 = ½  →  caiu à metade!", color=COR_ACENTO, weight=BOLD).scale(0.44)
        p3.next_to(p2, DOWN, buff=0.22)
        caixa_p = SurroundingRectangle(p3, color=COR_ACENTO,
                                       buff=0.16, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(p3), Create(caixa_p), run_time=0.9)
        self.wait(0.4)

        # Coluna direita — ÁREA
        a_tit = Text("ÁREA", color=COR_FORMULA, weight=BOLD).scale(0.46)
        a_tit.move_to([3.2, -1.45, 0])
        self.play(FadeIn(a_tit), run_time=0.5)

        a1 = Text("Original:   4×3 = 12 un²", color=COR_ORIGINAL).scale(0.42)
        a1.next_to(a_tit, DOWN, buff=0.22)
        self.play(FadeIn(a1), run_time=0.5)

        a2 = Text("Reduzida:  2×1,5 = 3 un²", color=COR_REDUZIDA).scale(0.42)
        a2.next_to(a1, DOWN, buff=0.18)
        self.play(FadeIn(a2), run_time=0.5)

        a3 = Text("3 ÷ 12 = ¼  →  caiu a um quarto!", color=COR_FORMULA, weight=BOLD).scale(0.44)
        a3.next_to(a2, DOWN, buff=0.22)
        caixa_a = SurroundingRectangle(a3, color=COR_FORMULA,
                                       buff=0.16, corner_radius=0.10,
                                       stroke_width=2.0)
        self.play(Write(a3), Create(caixa_a), run_time=0.9)
        self.wait(3.0)
        self._limpar()

    # ----------------------------------------------------------
    def _cena5(self):
        """Tabela comparativa e fórmula geral com fator k."""
        titulo = tit("Comparando as Medidas")
        separador = sep()
        self.play(Write(titulo), run_time=1.0)
        self.play(Create(separador), run_time=0.5)
        self.wait(0.3)

        xs    = [-5.0, -1.6, 1.2, 4.0]
        y_cab = Y_TOPO

        cabecalhos = [
            ("Figura",    COR_TITULO),
            ("Lados",     COR_TITULO),
            ("Perímetro", COR_ACENTO),
            ("Área",      COR_FORMULA),
        ]
        for (txt, cor), x in zip(cabecalhos, xs):
            t = Text(txt, color=cor, weight=BOLD).scale(0.46)
            t.move_to([x, y_cab, 0])
            self.play(FadeIn(t), run_time=0.25)
        self.wait(0.2)

        y_linha = y_cab - 0.40
        linha_h = Line([-6.0, y_linha, 0], [5.5, y_linha, 0],
                       color=GREY_D, stroke_width=1.2)
        self.play(Create(linha_h), run_time=0.4)
        self.wait(0.2)

        dados = [
            ("Original", COR_ORIGINAL, "4 e 3",   "14 un",  "12 un²"),
            ("Ampliada", COR_AMPLIADA, "8 e 6",   "28 un",  "48 un²"),
            ("Reduzida", COR_REDUZIDA, "2 e 1,5", "7 un",   "3 un²"),
        ]

        y_lin = y_linha - 0.58
        for nome, cor, lados, perim, area in dados:
            for val, x in zip([nome, lados, perim, area], xs):
                t = Text(val, color=cor).scale(0.44)
                t.move_to([x, y_lin, 0])
                self.play(FadeIn(t), run_time=0.25)
            self.wait(0.5)
            y_lin -= 0.65

        linha_b = Line([-6.0, y_lin + 0.30, 0], [5.5, y_lin + 0.30, 0],
                       color=GREY_D, stroke_width=1.2)
        self.play(Create(linha_b), run_time=0.4)
        self.wait(0.3)

        formula = Text(
            "Fator k:   lados × k   |   perímetro × k   |   área × k²",
            color=COR_FORMULA,
        ).scale(0.46)
        formula.move_to([0.0, Y_RODAPE, 0])
        caixa_f = SurroundingRectangle(formula, color=COR_FORMULA,
                                       buff=0.20, corner_radius=0.12,
                                       stroke_width=2.0)
        self.play(Write(formula), run_time=1.0)
        self.play(Create(caixa_f), run_time=0.6)
        self.wait(3.0)
        self._limpar()

    # ----------------------------------------------------------
    def _cena6(self):
        """Ângulos internos conservados — triângulo original e ampliado."""
        titulo = tit("Os Ângulos São Conservados!")
        separador = sep()
        self.play(Write(titulo), run_time=1.0)
        self.play(Create(separador), run_time=0.5)
        self.wait(0.3)

        # Triângulo original — esquerda
        Ao = np.array([-5.0, -0.8, 0])
        Bo = np.array([-5.0,  0.8, 0])
        Co = np.array([-3.4, -0.8, 0])
        tri_o = Polygon(Ao, Bo, Co,
                        fill_color=COR_ORIGINAL, fill_opacity=0.30,
                        stroke_color=COR_ORIGINAL, stroke_width=2.5)
        lbl_o = Text("Original", color=COR_ORIGINAL).scale(0.44)
        lbl_o.move_to([-4.3, -1.35, 0])
        self.play(Create(tri_o), run_time=1.0)
        self.play(FadeIn(lbl_o), run_time=0.5)
        self.wait(0.4)

        sq_o = Square(side_length=0.20, stroke_color=COR_ORIGINAL,
                      stroke_width=1.8, fill_opacity=0)
        sq_o.move_to(Ao + np.array([0.10, 0.10, 0]))
        self.play(Create(sq_o), run_time=0.5)
        self.wait(0.3)

        # Seta central
        seta = Arrow([-2.6, 0.0, 0], [-1.4, 0.0, 0],
                     color=COR_AMPLIADA, buff=0,
                     stroke_width=2.5, tip_length=0.20)
        f_lbl = Text("× 2", color=COR_AMPLIADA).scale(0.50)
        f_lbl.next_to(seta, UP, buff=0.10)
        self.play(Create(seta), FadeIn(f_lbl), run_time=0.7)
        self.wait(0.3)

        # Triângulo ampliado — direita
        Aa = np.array([-0.8, -1.4, 0])
        Ba = np.array([-0.8,  1.4, 0])
        Ca = np.array([ 2.4, -1.4, 0])
        tri_a = Polygon(Aa, Ba, Ca,
                        fill_color=COR_AMPLIADA, fill_opacity=0.22,
                        stroke_color=COR_AMPLIADA, stroke_width=2.5)
        lbl_a = Text("Ampliada (×2)", color=COR_AMPLIADA).scale(0.44)
        lbl_a.move_to([0.8, -2.00, 0])
        self.play(Create(tri_a), run_time=1.2)
        self.play(FadeIn(lbl_a), run_time=0.5)
        self.wait(0.4)

        sq_a = Square(side_length=0.20, stroke_color=COR_AMPLIADA,
                      stroke_width=1.8, fill_opacity=0)
        sq_a.move_to(Aa + np.array([0.10, 0.10, 0]))
        self.play(Create(sq_a), run_time=0.5)
        self.wait(0.5)

        # Destaque dos ângulos com arcos coloridos
        arco_o = Arc(radius=0.35, start_angle=0, angle=PI/2,
                     color=COR_FORMULA, stroke_width=2.5)
        arco_o.move_to(Ao + np.array([0.18, 0.18, 0]))

        arco_a = Arc(radius=0.35, start_angle=0, angle=PI/2,
                     color=COR_FORMULA, stroke_width=2.5)
        arco_a.move_to(Aa + np.array([0.18, 0.18, 0]))

        lbl_90o = Text("90°", color=COR_FORMULA).scale(0.38)
        lbl_90o.move_to(Ao + np.array([0.55, 0.30, 0]))
        lbl_90a = Text("90°", color=COR_FORMULA).scale(0.38)
        lbl_90a.move_to(Aa + np.array([0.55, 0.30, 0]))

        self.play(Create(arco_o), FadeIn(lbl_90o), run_time=0.7)
        self.play(Create(arco_a), FadeIn(lbl_90a), run_time=0.7)
        self.wait(0.5)

        # Anotação à direita
        nota = Text("Mesmos ângulos!\nFiguras semelhantes.",
                    color=COR_TITULO, line_spacing=1.3).scale(0.46)
        nota.move_to([4.5, 0.60, 0])
        self.play(FadeIn(nota), run_time=0.7)
        self.wait(0.4)

        msg = Text("Ângulos internos NÃO mudam na ampliação/redução.",
                   color=COR_FORMULA).scale(0.46)
        msg.move_to([0.0, Y_RODAPE - 0.30, 0])
        caixa_m = SurroundingRectangle(msg, color=COR_FORMULA,
                                       buff=0.20, corner_radius=0.12,
                                       stroke_width=2.0)
        self.play(Write(msg), run_time=1.0)
        self.play(Create(caixa_m), run_time=0.6)
        self.wait(2.5)
        self._limpar()

    # ----------------------------------------------------------
    def _cena7(self):
        """Estratégia passo a passo para resolver questões do D5."""
        titulo = tit("Estratégia para o D5")
        separador = sep()
        self.play(Write(titulo), run_time=1.0)
        self.play(Create(separador), run_time=0.5)
        self.wait(0.3)

        passos = [
            ("1", "Conte os lados da figura na malha original."),
            ("2", "Identifique o fator de escala  k."),
            ("3", "Novos lados  =  lados originais  × k."),
            ("4", "Novo perímetro  =  perímetro original  × k."),
            ("5", "Nova área  =  área original  × k²."),
            ("6", "Ângulos internos: sempre conservados!"),
        ]

        y_ini = 1.55
        dy    = 0.68

        for i, (num, texto) in enumerate(passos):
            y = y_ini - i * dy
            bolinha = Circle(radius=0.24, color=COR_ACENTO,
                             fill_color=COR_ACENTO, fill_opacity=0.90,
                             stroke_width=0)
            bolinha.move_to([-5.6, y, 0])
            num_t = Text(num, color=BLACK).scale(0.46)
            num_t.move_to(bolinha.get_center())
            passo_t = Text(texto, color=COR_TITULO).scale(0.44)
            passo_t.next_to(bolinha, RIGHT, buff=0.26)
            passo_t.align_to(bolinha, UP)
            self.play(FadeIn(bolinha), FadeIn(num_t), run_time=0.30)
            self.play(Write(passo_t), run_time=0.80)
            self.wait(0.35)

        conclusao = Text(
            "Ampliação e redução mudam o tamanho, mas não a forma!",
            color=COR_AMPLIADA, weight=BOLD,
        ).scale(0.48)
        conclusao.move_to([0.0, Y_RODAPE, 0])
        caixa_c = SurroundingRectangle(conclusao, color=COR_AMPLIADA,
                                       buff=0.20, corner_radius=0.12,
                                       stroke_width=2.0)
        self.play(Write(conclusao), Create(caixa_c), run_time=1.2)
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


# ══════════════════════════════════════════════════════════════
# LOGO – Identidade visual da Prof.ª Emilly Mayre
# ══════════════════════════════════════════════════════════════
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
