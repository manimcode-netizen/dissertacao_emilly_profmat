"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D23 – Identificar Frações Equivalentes
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Uso       : Dissertação de Mestrado Profissional em Matemática
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT (coordenadas Manim: centro = 0,0  |  tela: x[-7,7] y[-4,4])
  Faixa SAEB  : y ∈ [3.0, 4.0]   → nunca sobrepor
  Título cena : y = 2.55
  Linha sep   : y = 2.10
  Conteúdo    : y ∈ [-2.7, 1.85]  → régua/blocos aqui
  Cálculo     : y ≈ -2.55
  Resposta    : y = -3.40         → acima da barra do player
=======================================================================
RENDERIZAÇÃO (PowerShell):
  manim -pql d23_fracoes_equivalentes.py Abertura
  manim -pqh d23_fracoes_equivalentes.py Abertura

  foreach ($c in @("Abertura","CenaReguaDeFracoes","CenaEquivalencia",
    "CenaMetodoMDC","CenaMultiplicacaoDivisao","Encerramento","LogoEmillyMayre")) {
      manim -pqh d23_fracoes_equivalentes.py $c }
=======================================================================
"""

from manim import *
import numpy as np

# -----------------------------------------------------------------------
# CONSTANTES DE LAYOUT
# -----------------------------------------------------------------------
Y_FAIXA_CY  =  3.50   # centro da faixa institucional
Y_TITULO    =  2.55   # centro do título da cena
Y_LINHA_SEP =  2.10   # linha separadora amarela
Y_CONTEUDO  =  0.70   # centro geral do conteúdo
Y_CALCULO   = -2.55   # centro do bloco de cálculo
Y_RESPOSTA  = -3.40   # resposta final – acima da barra do player

# -----------------------------------------------------------------------
# PALETA DE CORES (uso consistente em toda a animação)
# -----------------------------------------------------------------------
COR_FAIXA      = BLUE_E       # fundo da faixa SAEB
COR_TITULO     = YELLOW       # títulos e destaques
COR_FRAC_1     = BLUE_D       # cor da fração base (1/2)
COR_FRAC_2     = GREEN_E      # cor de 2/4
COR_FRAC_3     = TEAL_E       # cor de 3/6
COR_FRAC_4     = "#5555aa"    # cor de 4/8
COR_DESTAQUE   = ORANGE       # setas e chamadas de atenção
COR_RESULTADO  = GREEN_B      # resultado/conclusão


# -----------------------------------------------------------------------
# FUNÇÃO AUXILIAR: Cabeçalho padrão (idêntico ao D36)
# -----------------------------------------------------------------------
def cabecalho(scene, texto_titulo):
    """Faixa SAEB + título + linha separadora. Retorna os 4 objetos."""
    faixa = Rectangle(
        width=14.4, height=1.05,
        fill_color=COR_FAIXA, fill_opacity=1, stroke_width=0
    ).move_to(np.array([0, Y_FAIXA_CY, 0]))

    inst = Text(
        "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
        color=WHITE, font_size=22
    ).move_to(faixa.get_center())

    cab = Text(texto_titulo, color=COR_TITULO, font_size=34, weight=BOLD)
    cab.move_to(np.array([0, Y_TITULO, 0]))

    linha_sep = Line(
        np.array([-6.2, Y_LINHA_SEP, 0]),
        np.array([ 6.2, Y_LINHA_SEP, 0]),
        color=COR_TITULO, stroke_width=1.2
    )

    scene.add(faixa, inst)
    scene.play(Write(cab), Create(linha_sep), run_time=1.1)
    scene.wait(0.3)
    return faixa, inst, cab, linha_sep


# -----------------------------------------------------------------------
# FUNÇÃO AUXILIAR: Bloco de fração visual (régua de frações)
# -----------------------------------------------------------------------
def bloco_regua(numerador, denominador, cor_preench, largura_total=10.5,
                altura=0.52, y_pos=0.0):
    """
    Cria uma linha da régua de frações:
    - Retângulo dividido em 'denominador' partes
    - Primeiras 'numerador' partes preenchidas
    - Retorna VGroup com todos os retângulos + rótulo
    """
    parte_w = largura_total / denominador
    blocos = VGroup()
    x_inicio = -largura_total / 2

    for i in range(denominador):
        preenchido = i < numerador
        bloco = Rectangle(
            width=parte_w - 0.03,
            height=altura,
            fill_color=cor_preench if preenchido else "#2a2a3e",
            fill_opacity=0.9 if preenchido else 0.35,
            stroke_color=WHITE,
            stroke_width=1.0
        ).move_to(np.array([x_inicio + parte_w * i + parte_w / 2, y_pos, 0]))
        blocos.add(bloco)

    # Rótulo da fração à direita
    rotulo = MathTex(
        rf"\frac{{{numerador}}}{{{denominador}}}",
        color=cor_preench, font_size=32
    ).move_to(np.array([largura_total / 2 + 0.75, y_pos, 0]))

    return VGroup(blocos, rotulo)


# =======================================================================
# CENA 1 – ABERTURA
# =======================================================================
class Abertura(Scene):
    """
    Conceito: Apresentação do Descritor D23 – Frações Equivalentes
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Contextualizar o que será estudado
    """

    def construct(self):
        # Faixa institucional fixa
        faixa = Rectangle(
            width=14.4, height=1.05,
            fill_color=COR_FAIXA, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        # Título do descritor
        titulo_d23 = Text("Descritor D23", color=COR_TITULO, font_size=52, weight=BOLD)
        titulo_d23.move_to(np.array([0, 1.4, 0]))

        subtitulo = Text(
            "Identificar Frações Equivalentes",
            color=WHITE, font_size=30, line_spacing=1.3
        ).next_to(titulo_d23, DOWN, buff=0.4)

        self.play(Write(titulo_d23), run_time=1.6)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)

        # FadeOut antes dos tópicos (sem sobreposição)
        self.play(FadeOut(VGroup(titulo_d23, subtitulo)), run_time=0.9)
        self.wait(0.2)

        # Linha separadora + tópicos
        linha = Line(
            np.array([-5.5, 1.5, 0]), np.array([5.5, 1.5, 0]),
            color=COR_TITULO, stroke_width=1.5
        )
        self.play(Create(linha), run_time=0.7)

        topicos = VGroup(
            Text("1. O que são frações equivalentes?",       color=WHITE,  font_size=25),
            Text("2. Régua de Frações – visualizando partes iguais", color=WHITE, font_size=25),
            Text("3. Comparando frações equivalentes",        color=WHITE,  font_size=25),
            Text("4. Método: multiplicar ou dividir (MDC)",  color=WHITE,  font_size=25),
            Text("5. Síntese e regra geral",                 color=WHITE,  font_size=25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        topicos.next_to(linha, DOWN, buff=0.30)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        dots_group = VGroup()
        for t in topicos:
            dot = Dot(color=COR_DESTAQUE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots_group.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.55)

        self.wait(2.5)
        self.play(FadeOut(VGroup(linha, topicos, dots_group)), run_time=1.0)


# =======================================================================
# CENA 2 – RÉGUA DE FRAÇÕES (visualização principal)
# =======================================================================
class CenaReguaDeFracoes(Scene):
    """
    Conceito: Régua de Frações mostrando partes equivalentes visualmente
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Perceber que 1/2 = 2/4 = 3/6 = 4/8 pela área preenchida
    """

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Régua de Frações")

        # --- Introdução textual ---
        intro = Text(
            "Observe os retângulos abaixo.\nCada linha representa a mesma quantidade!",
            color=WHITE, font_size=26, line_spacing=1.3
        ).move_to(np.array([0, 0.9, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(1.8)
        self.play(FadeOut(intro), run_time=0.7)
        self.wait(0.2)

        # --- Dados da régua ---
        fracoes = [
            (1, 2,  COR_FRAC_1),
            (2, 4,  COR_FRAC_2),
            (3, 6,  COR_FRAC_3),
            (4, 8,  COR_FRAC_4),
        ]

        # Posições verticais das linhas da régua
        y_posicoes = [1.30, 0.55, -0.20, -0.95]

        linhas_regua = VGroup()
        for i, ((num, den, cor), y) in enumerate(zip(fracoes, y_posicoes)):
            linha_bloco = bloco_regua(num, den, cor,
                                      largura_total=10.0, altura=0.50, y_pos=y)
            linhas_regua.add(linha_bloco)
            self.play(FadeIn(linha_bloco), run_time=0.75)
            self.wait(0.25)

        self.wait(1.0)

        # --- Linha vertical tracejada mostrando que o preenchimento é igual ---
        x_meio_preench = -10.0 / 2 + 10.0 * (1 / 2)   # posição x = fim de 1/2
        linha_ref = DashedLine(
            np.array([x_meio_preench, y_posicoes[0] + 0.35, 0]),
            np.array([x_meio_preench, y_posicoes[-1] - 0.35, 0]),
            color=COR_TITULO, dash_length=0.15, stroke_width=2.5
        )
        self.play(Create(linha_ref), run_time=1.2)

        seta_label = Text(
            "Mesmo preenchimento!",
            color=COR_TITULO, font_size=22, weight=BOLD
        ).move_to(np.array([3.0, (y_posicoes[0] + y_posicoes[-1]) / 2, 0]))
        seta = Arrow(
            seta_label.get_left() + LEFT * 0.1,
            np.array([x_meio_preench + 0.15, (y_posicoes[0] + y_posicoes[-1]) / 2, 0]),
            color=COR_TITULO, buff=0.05, max_tip_length_to_length_ratio=0.2
        )
        self.play(FadeIn(seta_label), Create(seta), run_time=0.9)
        self.wait(2.0)

        # --- Conclusão ---
        conclusao = Text(
            "Todas representam a mesma parte do inteiro!",
            color=COR_RESULTADO, font_size=24, weight=BOLD
        ).move_to(np.array([0, -1.85, 0]))
        box_conc = SurroundingRectangle(
            conclusao, color=COR_RESULTADO, buff=0.14, corner_radius=0.1
        )
        self.play(FadeIn(conclusao), Create(box_conc), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, linhas_regua, linha_ref,
            seta_label, seta, conclusao, box_conc
        )), run_time=1.0)


# =======================================================================
# CENA 3 – COMPARANDO FRAÇÕES EQUIVALENTES (base 1/3)
# FIX: frações de 1/3; altura/espaçamento ajustados sem sobreposição
# =======================================================================
class CenaEquivalencia(Scene):
    """
    Conceito: Frações equivalentes – comparação visual par a par
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Mostrar que 1/3 = 2/6 = 3/9 = 4/12 por justaposição de blocos
    """

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Comparando Frações Equivalentes")

        # --- Instrução logo abaixo da linha sep ---
        inst_txt = Text(
            "Veja que as partes coloridas sempre cobrem a MESMA área:",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(inst_txt), run_time=0.9)
        self.wait(0.5)

        larg  = 4.6
        altura = 0.52

        def bloco_simples(num, den, cor, x_center, y_center):
            parte_w = larg / den
            grupo = VGroup()
            for i in range(den):
                fill = i < num
                b = Rectangle(
                    width=parte_w - 0.04, height=altura,
                    fill_color=cor if fill else "#2a2a3e",
                    fill_opacity=0.9 if fill else 0.3,
                    stroke_color=WHITE, stroke_width=0.9
                ).move_to(np.array([x_center - larg/2 + parte_w*i + parte_w/2, y_center, 0]))
                grupo.add(b)
            # Rótulo posicionado abaixo do bloco com espaço suficiente
            rot = MathTex(rf"\frac{{{num}}}{{{den}}}",
                          color=cor, font_size=28).next_to(grupo, DOWN, buff=0.20)
            return VGroup(grupo, rot)

        # Espaçamento aumentado entre pares para evitar sobreposição dos rótulos
        # Cada par ocupa ~0.52 (altura bloco) + 0.20 (buff) + ~0.50 (fração) ≈ 1.22
        # Espaçamento de 1.35 entre centros garante folga suficiente
        y1, y2, y3 = 0.80, -0.55, -1.90

        # Par 1: 1/3 = 2/6
        b1_esq = bloco_simples(1, 3, COR_FRAC_1, -2.7, y1)
        b1_dir = bloco_simples(2, 6, COR_FRAC_2,  2.7, y1)
        eq1 = MathTex(r"=", color=WHITE, font_size=44).move_to(np.array([0, y1, 0]))
        self.play(FadeIn(b1_esq), run_time=0.7)
        self.play(Write(eq1), FadeIn(b1_dir), run_time=0.7)
        self.wait(0.7)

        # Par 2: 1/3 = 3/9
        b2_esq = bloco_simples(1, 3, COR_FRAC_1, -2.7, y2)
        b2_dir = bloco_simples(3, 9, COR_FRAC_3,  2.7, y2)
        eq2 = MathTex(r"=", color=WHITE, font_size=44).move_to(np.array([0, y2, 0]))
        self.play(FadeIn(b2_esq), run_time=0.7)
        self.play(Write(eq2), FadeIn(b2_dir), run_time=0.7)
        self.wait(0.7)

        # Par 3: 1/3 = 4/12
        b3_esq = bloco_simples(1,  3, COR_FRAC_1, -2.7, y3)
        b3_dir = bloco_simples(4, 12, COR_FRAC_4,  2.7, y3)
        eq3 = MathTex(r"=", color=WHITE, font_size=44).move_to(np.array([0, y3, 0]))
        self.play(FadeIn(b3_esq), run_time=0.7)
        self.play(Write(eq3), FadeIn(b3_dir), run_time=0.7)
        self.wait(0.9)

        # --- Cadeia — y=-3.20, acima da barra do player ---
        cadeia = MathTex(
            r"\frac{1}{3} = \frac{2}{6} = \frac{3}{9} = \frac{4}{12}",
            font_size=30, color=COR_TITULO
        ).move_to(np.array([0, -3.20, 0]))
        box_cad = SurroundingRectangle(cadeia, color=COR_TITULO, buff=0.13, corner_radius=0.1)
        self.play(Write(cadeia), Create(box_cad), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, inst_txt,
            b1_esq, b1_dir, eq1,
            b2_esq, b2_dir, eq2,
            b3_esq, b3_dir, eq3,
            cadeia, box_cad
        )), run_time=1.0)


# =======================================================================
# CENA 4 – MÉTODO DO MDC (multiplicar ou dividir)
# =======================================================================
class CenaMetodoMDC(Scene):
    """
    Conceito: Encontrar frações equivalentes multiplicando/dividindo pelo mesmo número
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Mostrar o procedimento algébrico para gerar equivalentes e simplificar
    """

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(
            self, "Como encontrar frações equivalentes?"
        )

        # ====== PARTE A: Multiplicar numerador e denominador ======
        tit_a = Text(
            "Estratégia 1 — Multiplicar por um mesmo número",
            color=COR_DESTAQUE, font_size=24, weight=BOLD
        ).move_to(np.array([0, 1.68, 0]))
        self.play(FadeIn(tit_a), run_time=0.8)
        self.wait(0.4)

        # Fração base à esquerda, centralizada verticalmente no espaço de conteúdo
        Y_FRAC = -0.10   # altura das frações
        Y_SETA = Y_FRAC + 0.55   # base das setas (acima das frações)
        Y_LABEL = Y_FRAC + 1.30  # rótulos ×2/×3 no topo do arco, longe da seta

        frac_base = MathTex(r"\frac{1}{2}", font_size=56, color=COR_FRAC_1)
        frac_base.move_to(np.array([-4.5, Y_FRAC, 0]))
        self.play(FadeIn(frac_base), run_time=0.6)
        self.wait(0.3)

        # Setas e multiplicações (×2, ×3)
        mult_labels = [
            (r"\times 2", r"\frac{2}{4}", COR_FRAC_2,  0.0),
            (r"\times 3", r"\frac{3}{6}", COR_FRAC_3,  4.5),
        ]

        fracs_geradas = VGroup()
        setas_mult    = VGroup()
        labels_mult   = VGroup()
        iguais_mult   = VGroup()

        x_ant = -4.5
        for lbl, resultado, cor, x_dest in mult_labels:
            x_meio = (x_ant + x_dest) / 2

            # Seta curva partindo da altura Y_SETA
            seta = CurvedArrow(
                np.array([x_ant + 0.50, Y_SETA, 0]),
                np.array([x_dest - 0.50, Y_SETA, 0]),
                angle=-PI / 4, color=COR_DESTAQUE, stroke_width=2.5
            )
            # Rótulo acima do pico do arco — Y_LABEL garante folga da seta
            rotulo = MathTex(lbl, color=COR_DESTAQUE, font_size=28)
            rotulo.move_to(np.array([x_meio, Y_LABEL, 0]))

            frac_dest = MathTex(resultado, font_size=56, color=cor)
            frac_dest.move_to(np.array([x_dest, Y_FRAC, 0]))

            # Sinal de igualdade entre frações
            ig = MathTex(r"=", font_size=46, color=WHITE)
            ig.move_to(np.array([x_meio, Y_FRAC, 0]))

            self.play(Create(seta), FadeIn(rotulo), run_time=0.7)
            self.play(FadeIn(ig), Write(frac_dest), run_time=0.6)
            self.wait(0.4)

            setas_mult.add(seta)
            labels_mult.add(rotulo)
            fracs_geradas.add(frac_dest)
            iguais_mult.add(ig)
            x_ant = x_dest

        # Conclusão parte A
        concl_a = Text(
            "Multiplicamos numerador e denominador pelo MESMO número.",
            color=WHITE, font_size=22
        ).move_to(np.array([0, -1.50, 0]))
        self.play(FadeIn(concl_a), run_time=0.8)
        self.wait(1.8)

        # FadeOut da parte A
        self.play(FadeOut(VGroup(
            tit_a, frac_base, setas_mult, labels_mult,
            fracs_geradas, iguais_mult, concl_a
        )), run_time=0.9)
        self.wait(0.3)

        # ====== PARTE B: Simplificar usando MDC ======
        # Layout reorganizado em coluna clara: fração → MDC → seta → resultado → blocos
        tit_b = Text(
            "Estratégia 2 — Simplificar dividindo pelo MDC",
            color=COR_RESULTADO, font_size=24, weight=BOLD
        ).move_to(np.array([0, 1.68, 0]))
        self.play(FadeIn(tit_b), run_time=0.8)
        self.wait(0.4)

        # Fração 6/8 à esquerda
        frac_grande = MathTex(r"\frac{6}{8}", font_size=60, color=COR_FRAC_4)
        frac_grande.move_to(np.array([-4.0, 0.20, 0]))
        self.play(FadeIn(frac_grande), run_time=0.7)
        self.wait(0.3)

        # MDC centralizado abaixo do título, à esquerda do centro
        mdc_txt = Text("MDC(6, 8) = 2", color=WHITE, font_size=26)
        mdc_txt.move_to(np.array([-0.5, 0.20, 0]))
        self.play(Write(mdc_txt), run_time=0.9)
        self.wait(0.4)

        # Seta de divisão ÷2 — de frac_grande até antes do resultado
        seta_div = CurvedArrow(
            np.array([-3.3, 0.65, 0]),
            np.array([ 2.2, 0.65, 0]),
            angle=-PI / 5, color=COR_RESULTADO, stroke_width=2.5
        )
        rot_div = MathTex(r"\div\ 2", color=COR_RESULTADO, font_size=28)
        rot_div.move_to(np.array([-0.5, 1.25, 0]))
        self.play(Create(seta_div), FadeIn(rot_div), run_time=0.8)
        self.wait(0.3)

        # Resultado 3/4 à direita + sinal de igualdade
        igual_b = MathTex(r"=", font_size=48, color=WHITE)
        igual_b.move_to(np.array([2.8, 0.20, 0]))
        frac_simpl = MathTex(r"\frac{3}{4}", font_size=60, color=COR_RESULTADO)
        frac_simpl.move_to(np.array([4.0, 0.20, 0]))
        self.play(FadeIn(igual_b), Write(frac_simpl), run_time=0.8)
        self.wait(0.5)

        # Verificação visual — blocos bem abaixo, sem colidir com conteúdo acima
        def mini_bloco(num, den, cor, cx, cy):
            larg_m = 3.0
            pw = larg_m / den
            g = VGroup()
            for i in range(den):
                fill = i < num
                b = Rectangle(
                    width=pw - 0.04, height=0.44,
                    fill_color=cor if fill else "#2a2a3e",
                    fill_opacity=0.9 if fill else 0.3,
                    stroke_color=WHITE, stroke_width=0.9
                ).move_to(np.array([cx - larg_m/2 + pw*i + pw/2, cy, 0]))
                g.add(b)
            return g

        blk_68 = mini_bloco(6, 8, COR_FRAC_4,    -4.0, -1.30)
        blk_34 = mini_bloco(3, 4, COR_RESULTADO,   4.0, -1.30)
        eq_blk = MathTex(r"=", font_size=44, color=WHITE).move_to(np.array([0.0, -1.30, 0]))

        self.play(FadeIn(blk_68), run_time=0.6)
        self.play(FadeIn(eq_blk), FadeIn(blk_34), run_time=0.6)
        self.wait(1.0)

        # Conclusão parte B
        concl_b = Text(
            "Dividindo pelo MDC obtemos a fração na forma mais simples!",
            color=COR_TITULO, font_size=22, weight=BOLD
        ).move_to(np.array([0, Y_CALCULO, 0]))
        box_b = SurroundingRectangle(concl_b, color=COR_TITULO, buff=0.14, corner_radius=0.1)
        self.play(FadeIn(concl_b), Create(box_b), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, tit_b,
            frac_grande, mdc_txt, seta_div, rot_div,
            igual_b, frac_simpl, blk_68, blk_34, eq_blk,
            concl_b, box_b
        )), run_time=1.0)


# =======================================================================
# CENA 5 – MULTIPLICAÇÃO E DIVISÃO PARA ENCONTRAR EQUIVALENTES
# =======================================================================
class CenaMultiplicacaoDivisao(Scene):
    """
    Conceito: Encontrar frações equivalentes por multiplicação e por divisão
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Consolidar os dois procedimentos em exemplos numéricos claros
    """

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(
            self, "Multiplicação e Divisão — Frações Equivalentes"
        )

        # ====== EXEMPLO 1: MULTIPLICAÇÃO — 2/5 × 3 = 6/15 ======
        tit_mult = Text(
            "Exemplo 1 — Multiplicação",
            color=COR_DESTAQUE, font_size=26, weight=BOLD
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(tit_mult), run_time=0.7)
        self.wait(0.3)

        # Fração original
        frac_orig_m = MathTex(r"\frac{2}{5}", font_size=64, color=COR_FRAC_1)
        frac_orig_m.move_to(np.array([-3.8, 0.30, 0]))
        self.play(FadeIn(frac_orig_m), run_time=0.6)
        self.wait(0.2)

        # Seta curva com ×3
        seta_m = CurvedArrow(
            np.array([-3.2, 0.75, 0]),
            np.array([ 0.8, 0.75, 0]),
            angle=-PI / 4, color=COR_DESTAQUE, stroke_width=2.5
        )
        rot_m = MathTex(r"\times\ 3", color=COR_DESTAQUE, font_size=30)
        rot_m.move_to(np.array([-1.2, 1.20, 0]))
        self.play(Create(seta_m), FadeIn(rot_m), run_time=0.8)

        # Resultado
        frac_res_m = MathTex(r"\frac{6}{15}", font_size=64, color=COR_FRAC_2)
        frac_res_m.move_to(np.array([1.8, 0.30, 0]))
        igual_m = MathTex(r"=", font_size=50, color=WHITE)
        igual_m.move_to(np.array([0.85, 0.30, 0]))
        self.play(FadeIn(igual_m), Write(frac_res_m), run_time=0.8)
        self.wait(0.4)

        # Explicação passo a passo
        passo_m = VGroup(
            MathTex(r"2 \times 3 = 6", color=WHITE, font_size=26),
            MathTex(r"5 \times 3 = 15", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.20)
        passo_m.move_to(np.array([4.2, 0.30, 0]))
        self.play(FadeIn(passo_m), run_time=0.7)

        concl_m = Text(
            "Multiplicamos numerador e denominador por 3.",
            color=COR_RESULTADO, font_size=21
        ).move_to(np.array([0, -0.75, 0]))
        box_cm = SurroundingRectangle(concl_m, color=COR_RESULTADO, buff=0.12, corner_radius=0.08)
        self.play(FadeIn(concl_m), Create(box_cm), run_time=0.8)
        self.wait(1.8)

        # FadeOut exemplo 1
        self.play(FadeOut(VGroup(
            tit_mult, frac_orig_m, seta_m, rot_m,
            igual_m, frac_res_m, passo_m, concl_m, box_cm
        )), run_time=0.8)
        self.wait(0.3)

        # ====== EXEMPLO 2: DIVISÃO — 12/18 ÷ 6 = 2/3 ======
        tit_div = Text(
            "Exemplo 2 — Divisão (simplificação pelo MDC)",
            color=COR_RESULTADO, font_size=26, weight=BOLD
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(tit_div), run_time=0.7)
        self.wait(0.3)

        # Fração original
        frac_orig_d = MathTex(r"\frac{12}{18}", font_size=64, color=COR_FRAC_4)
        frac_orig_d.move_to(np.array([-3.8, 0.30, 0]))
        self.play(FadeIn(frac_orig_d), run_time=0.6)
        self.wait(0.2)

        # MDC
        mdc_txt = Text("MDC(12, 18) = 6", color=WHITE, font_size=24)
        mdc_txt.move_to(np.array([0.5, -0.90, 0]))
        self.play(Write(mdc_txt), run_time=0.8)
        self.wait(0.4)

        # Seta curva com ÷6
        seta_d = CurvedArrow(
            np.array([-3.2, 0.75, 0]),
            np.array([ 0.8, 0.75, 0]),
            angle=-PI / 4, color=COR_RESULTADO, stroke_width=2.5
        )
        rot_d = MathTex(r"\div\ 6", color=COR_RESULTADO, font_size=30)
        rot_d.move_to(np.array([-1.2, 1.20, 0]))
        self.play(Create(seta_d), FadeIn(rot_d), run_time=0.8)

        # Resultado
        frac_res_d = MathTex(r"\frac{2}{3}", font_size=64, color=COR_RESULTADO)
        frac_res_d.move_to(np.array([1.8, 0.30, 0]))
        igual_d = MathTex(r"=", font_size=50, color=WHITE)
        igual_d.move_to(np.array([0.85, 0.30, 0]))
        self.play(FadeIn(igual_d), Write(frac_res_d), run_time=0.8)
        self.wait(0.4)

        # Explicação passo a passo
        passo_d = VGroup(
            MathTex(r"12 \div 6 = 2", color=WHITE, font_size=26),
            MathTex(r"18 \div 6 = 3", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.20)
        passo_d.move_to(np.array([4.2, 0.30, 0]))
        self.play(FadeIn(passo_d), run_time=0.7)

        concl_d = Text(
            "Dividindo pelo MDC obtemos a forma mais simples!",
            color=COR_TITULO, font_size=21
        ).move_to(np.array([0, -2.10, 0]))
        box_cd = SurroundingRectangle(concl_d, color=COR_TITULO, buff=0.12, corner_radius=0.08)
        self.play(FadeIn(concl_d), Create(box_cd), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep, tit_div,
            frac_orig_d, mdc_txt, seta_d, rot_d,
            igual_d, frac_res_d, passo_d, concl_d, box_cd
        )), run_time=1.0)


# =======================================================================
# CENA 6 – DIVISÃO PARA ENCONTRAR FRAÇÕES EQUIVALENTES
# =======================================================================
class CenaDivisaoEquivalentes(Scene):
    """
    Conceito: Encontrar frações equivalentes dividindo numerador e denominador
              pelo mesmo número (simplificação progressiva)
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Mostrar visualmente que dividir por um mesmo número gera uma
              fração equivalente — espelho direto da cena de multiplicação
    """

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(
            self, "Frações Equivalentes por Divisão"
        )

        # --- Instrução ---
        inst_txt = Text(
            "Dividindo numerador e denominador pelo mesmo número\nobtemos uma fração equivalente!",
            color=WHITE, font_size=24, line_spacing=1.3
        ).move_to(np.array([0, 1.50, 0]))
        self.play(FadeIn(inst_txt), run_time=0.9)
        self.wait(1.2)
        self.play(FadeOut(inst_txt), run_time=0.7)
        self.wait(0.2)

        # ====== CADEIA DE DIVISÃO: 12/18 → 6/9 → 2/3 ======
        # Fração inicial maior, descida para y=0.0 para não sobrepor título
        frac_a = MathTex(r"\frac{12}{18}", font_size=60, color=COR_FRAC_4)
        frac_a.move_to(np.array([-4.5, 0.0, 0]))
        self.play(FadeIn(frac_a), run_time=0.7)
        self.wait(0.4)

        # Dados da cadeia: (rótulo divisão, fração resultado, cor, x destino)
        div_labels = [
            (r"\div\ 2", r"\frac{6}{9}",  COR_FRAC_3,  0.0),
            (r"\div\ 3", r"\frac{2}{3}",  COR_RESULTADO, 4.5),
        ]

        fracs_div  = VGroup()
        setas_div  = VGroup()
        labels_div = VGroup()

        x_ant = -4.5
        y_pos = 0.0  # todas as frações na mesma altura

        for lbl, resultado, cor, x_dest in div_labels:
            x_meio = (x_ant + x_dest) / 2

            # Seta curva acima das frações — apex em y_pos+0.90
            seta = CurvedArrow(
                np.array([x_ant + 0.55, y_pos + 0.50, 0]),
                np.array([x_dest - 0.55, y_pos + 0.50, 0]),
                angle=-PI / 4, color=COR_RESULTADO, stroke_width=2.5
            )
            # Rótulo centralizado no meio da seta, bem acima da ponta
            rotulo = MathTex(lbl, color=COR_RESULTADO, font_size=28)
            rotulo.move_to(np.array([x_meio, y_pos + 1.10, 0]))

            frac_dest = MathTex(resultado, font_size=60, color=cor)
            frac_dest.move_to(np.array([x_dest, y_pos, 0]))

            # Sinal de igualdade entre frações
            ig = MathTex(r"=", font_size=46, color=WHITE)
            ig.move_to(np.array([(x_ant + x_dest) / 2, y_pos, 0]))

            self.play(Create(seta), FadeIn(rotulo), run_time=0.8)
            self.play(FadeIn(ig), Write(frac_dest), run_time=0.7)
            self.wait(0.5)

            setas_div.add(seta)
            labels_div.add(rotulo)
            fracs_div.add(frac_dest, ig)
            x_ant = x_dest

        # --- Verificação visual com blocos ---
        def mini_bloco(num, den, cor, cx, cy):
            larg_m = 3.0
            pw = larg_m / den
            g = VGroup()
            for i in range(den):
                fill = i < num
                b = Rectangle(
                    width=pw - 0.04, height=0.44,
                    fill_color=cor if fill else "#2a2a3e",
                    fill_opacity=0.9 if fill else 0.3,
                    stroke_color=WHITE, stroke_width=0.9
                ).move_to(np.array([cx - larg_m/2 + pw*i + pw/2, cy, 0]))
                g.add(b)
            return g

        blk_a  = mini_bloco(12, 18, COR_FRAC_4,    -4.5, -1.30)
        blk_b  = mini_bloco( 6,  9, COR_FRAC_3,     0.0, -1.30)
        blk_c  = mini_bloco( 2,  3, COR_RESULTADO,  4.5, -1.30)
        eq_ab  = MathTex(r"=", font_size=40, color=WHITE).move_to(np.array([-2.25, -1.30, 0]))
        eq_bc  = MathTex(r"=", font_size=40, color=WHITE).move_to(np.array([ 2.25, -1.30, 0]))

        self.play(FadeIn(blk_a), run_time=0.6)
        self.play(FadeIn(eq_ab), FadeIn(blk_b), run_time=0.6)
        self.play(FadeIn(eq_bc), FadeIn(blk_c), run_time=0.6)
        self.wait(1.0)

        # --- Conclusão ---
        concl = Text(
            "Dividindo pelo mesmo número obtemos frações equivalentes!",
            color=COR_TITULO, font_size=22, weight=BOLD
        ).move_to(np.array([0, Y_CALCULO, 0]))
        box_c = SurroundingRectangle(concl, color=COR_TITULO, buff=0.14, corner_radius=0.1)
        self.play(FadeIn(concl), Create(box_c), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            cab, linha_sep,
            frac_a, fracs_div, setas_div, labels_div,
            blk_a, blk_b, blk_c, eq_ab, eq_bc,
            concl, box_c
        )), run_time=1.0)


# =======================================================================
# CENA 7 – ENCERRAMENTO / SÍNTESE
# =======================================================================
class Encerramento(Scene):
    """
    Conceito: Síntese das estratégias para frações equivalentes
    Nível: Ensino Fundamental – 9º Ano
    Objetivo: Consolidar a regra geral e as estratégias aprendidas
    """

    def construct(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese — Descritor D23")

        descritivo = Text(
            "D23 – Identificar Frações Equivalentes",
            color=WHITE, font_size=26, line_spacing=1.3
        ).move_to(np.array([0, 1.25, 0]))
        box_desc = SurroundingRectangle(
            descritivo, color=COR_TITULO, buff=0.18, corner_radius=0.1
        )
        self.play(FadeIn(descritivo), Create(box_desc), run_time=1.2)
        self.wait(0.7)

        mapa_tit = Text(
            "Como identificar frações equivalentes:",
            color=WHITE, font_size=22
        ).move_to(np.array([0, 0.30, 0]))
        self.play(FadeIn(mapa_tit), run_time=0.8)

        estrategias = VGroup(
            Text("1. Representar como partes de um mesmo inteiro (régua)",
                 color=WHITE,        font_size=20),
            Text("2. Multiplicar numerador e denominador pelo MESMO número",
                 color=COR_DESTAQUE, font_size=20),
            Text("3. Dividir numerador e denominador pelo MDC para simplificar",
                 color=WHITE,        font_size=20),
            Text("4. Verificar: a/b = c/d  ⟺  a×d = b×c  (produtos cruzados)",
                 color=COR_DESTAQUE, font_size=20),
            Text("5. Frações equivalentes representam a mesma quantidade",
                 color=COR_RESULTADO, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        estrategias.next_to(mapa_tit, DOWN, buff=0.28)

        dots = VGroup()
        cores_dot = [COR_RESULTADO, COR_DESTAQUE, COR_RESULTADO, COR_DESTAQUE, COR_RESULTADO]
        for i, linha_txt in enumerate(estrategias):
            dot = Dot(color=cores_dot[i], radius=0.07).next_to(linha_txt, LEFT, buff=0.14)
            dots.add(dot)
            self.play(FadeIn(dot), FadeIn(linha_txt, shift=RIGHT * 0.1), run_time=0.58)

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            cab, linha_sep, descritivo, box_desc,
            mapa_tit, estrategias, dots
        )), run_time=1.2)


# =======================================================================
# LOGO – Identidade visual da Prof.ª Emilly Mayre (idêntica ao D36)
# =======================================================================
class LogoEmillyMayre(Scene):
    """Logo final da professora — idêntico ao arquivo D36."""

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
            return np.array([a * np.cos(t) / d, a * np.sin(t) * np.cos(t) / d, 0])

        def inf_v(t):
            d = 1 + np.sin(t) ** 2
            return np.array([a * np.sin(t) * np.cos(t) / d, a * np.cos(t) / d, 0])

        logo_h = ParametricFunction(inf_h, t_range=[0, TAU],
                                    color="#3a3a5c", stroke_width=2.5)
        logo_v = ParametricFunction(inf_v, t_range=[0, TAU],
                                    color="#9999bb", stroke_width=2.5)
        logo_h.move_to(UP * 0.5)
        logo_v.move_to(UP * 0.5)

        circ = Circle(radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
                      color=ESCURO_L, stroke_width=0).move_to(UP * 0.5)
        em = Text("EM", color=WHITE, font_size=22,
                  weight=BOLD).move_to(circ.get_center())

        grp  = VGroup(logo_h, logo_v)
        nome = Text("Emilly Mayre", color=ESCURO_L, font_size=28, weight=BOLD)
        nome.next_to(grp, DOWN, buff=0.55)
        linha = Line(LEFT * 1.6, RIGHT * 1.6, color=DOURADO, stroke_width=3.5)
        linha.next_to(nome, DOWN, buff=0.16)
        cargo = Text("PROFESSORA DE MATEMÁTICA", color=CINZA_L, font_size=14)
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
