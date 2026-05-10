"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D29 – Variação Proporcional Direta e Inversa
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Uso       : Dissertação de Mestrado Profissional em Matemática
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT (coordenadas Manim: centro=0,0 | tela: x[-7,7] y[-4,4])
  Faixa SAEB  : y ∈ [3.0, 4.0]   → nunca sobrepor
  Título cena : y = 2.55
  Linha sep   : y = 2.10
  Conteúdo    : y ∈ [-2.6, 1.85]
  Resposta    : y = -3.40
=======================================================================
PALETA SEMÂNTICA
  YELLOW  → títulos e cabeçalhos
  BLUE_D  → grandeza x / proporcional direta
  RED_B   → grandeza y / proporcional inversa
  GREEN_B → resultado, constante k, confirmação
  ORANGE  → destaque temporário, seta de atenção
  WHITE   → textos explicativos e rótulos gerais
=======================================================================
RENDERIZAÇÃO (classe única — ordem garantida):
  manim -pql d29_v2.py D29
  manim -pqh d29_v2.py D29
=======================================================================
"""

from manim import *
import numpy as np

# ── Constantes de layout ────────────────────────────────────────────
Y_FAIXA_CY  =  3.50
Y_TITULO    =  2.55
Y_LINHA_SEP =  2.10
Y_CONTEUDO  =  0.50   # centro vertical do conteúdo principal
Y_RESPOSTA  = -3.40


# ── Helpers globais ─────────────────────────────────────────────────
def cabecalho(scene, texto_titulo):
    """Faixa SAEB fixa + título da cena + linha separadora."""
    faixa = Rectangle(
        width=14.4, height=1.05,
        fill_color=BLUE_E, fill_opacity=1, stroke_width=0
    ).move_to(np.array([0, Y_FAIXA_CY, 0]))
    inst = Text(
        "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
        color=WHITE, font_size=22
    ).move_to(faixa.get_center())
    cab = Text(texto_titulo, color=YELLOW, font_size=36, weight=BOLD)
    cab.move_to(np.array([0, Y_TITULO, 0]))
    linha_sep = Line(
        np.array([-6.2, Y_LINHA_SEP, 0]),
        np.array([ 6.2, Y_LINHA_SEP, 0]),
        color=YELLOW, stroke_width=1.2
    )
    scene.add(faixa, inst)
    scene.play(Write(cab), Create(linha_sep), run_time=1.1)
    scene.wait(0.3)
    return faixa, inst, cab, linha_sep


def barra(altura, cor, largura=0.72):
    """Retângulo vertical alinhado pela base, com preenchimento semântico."""
    b = Rectangle(
        width=largura, height=max(altura, 0.05),
        fill_color=cor, fill_opacity=0.88,
        stroke_color=WHITE, stroke_width=1.2
    )
    return b


# =======================================================================
# CLASSE MESTRE — contém todas as cenas em ordem
# Ordem: Abertura → Direta (barras) → Direta (tabela) →
#        Inversa (barras) → Inversa (tabela) →
#        Formalização → Problema Aplicado → Encerramento → Logo
# =======================================================================
class D29(Scene):
    """
    Classe mestre do Descritor D29.
    Todas as cenas são executadas em sequência dentro de construct(),
    garantindo a ordem correta sem depender de junção de vídeos externos.

    Conceito : Variação Proporcional Direta e Inversa
    Nível    : Ensino Fundamental – 9º Ano
    Objetivo : Distinguir proporcionalidade direta (razão constante)
               de inversa (produto constante) e aplicar em problemas.
    """

    def construct(self):
        self._abertura()
        self._direta_barras()
        self._direta_tabela()
        self._inversa_barras()
        self._inversa_tabela()
        self._formalizacao()
        self._problema_aplicado()
        self._encerramento()
        self._logo_emilly_mayre()

    # ===================================================================
    # CENA 1 – ABERTURA
    # ===================================================================
    def _abertura(self):
        """Contextualização do Descritor D29 – SAEB."""
        faixa = Rectangle(
            width=14.4, height=1.05,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        titulo = Text("Descritor D29", color=YELLOW, font_size=52, weight=BOLD)
        titulo.move_to(np.array([0, 1.4, 0]))
        subtitulo = Text(
            "Variação Proporcional Direta e Inversa",
            color=WHITE, font_size=28
        ).next_to(titulo, DOWN, buff=0.45)

        self.play(Write(titulo), run_time=1.6)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtitulo)), run_time=0.9)
        self.wait(0.2)

        linha = Line(
            np.array([-5.5, 1.5, 0]), np.array([5.5, 1.5, 0]),
            color=YELLOW, stroke_width=1.5
        )
        self.play(Create(linha), run_time=0.7)

        topicos = VGroup(
            Text("1. Proporcionalidade Direta — barras",   color=WHITE, font_size=24),
            Text("2. Proporcionalidade Direta — tabela",   color=WHITE, font_size=24),
            Text("3. Proporcionalidade Inversa — barras",  color=WHITE, font_size=24),
            Text("4. Proporcionalidade Inversa — tabela",  color=WHITE, font_size=24),
            Text("5. Formalização das fórmulas",           color=WHITE, font_size=24),
            Text("6. Problema aplicado (SAEB)",            color=WHITE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        topicos.next_to(linha, DOWN, buff=0.28)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        dots = VGroup()
        for t in topicos:
            dot = Dot(color=ORANGE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.48)

        self.wait(2.5)
        self.play(FadeOut(VGroup(faixa, inst, linha, topicos, dots)), run_time=1.0)

    # ===================================================================
    # CENA 2 – PROPORCIONALIDADE DIRETA: barras visuais
    # ===================================================================
    def _direta_barras(self):
        """
        Conceito : Quando x cresce, y cresce na mesma proporção.
        Visual   : Pares de barras (azul = x, laranja = y) crescendo juntas.
        """
        faixa, inst, cab, linha_sep = cabecalho(self, "Proporcionalidade Direta")

        # Contexto didático
        ctx = Text(
            "Preço unitário fixo: quanto mais unidades, maior o custo total.",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        # Pares (qtd, custo), k = 6
        pares   = [(1, 6), (2, 12), (3, 18), (4, 24)]
        escala  = 0.18          # fator visual de altura
        base_y  = -2.0          # y da linha de base

        grupos = VGroup()
        for x_val, y_val in pares:
            bx = barra(x_val * escala * 3, BLUE_D)
            by = barra(y_val * escala,      ORANGE)

            # Alinhar pela base
            bx.move_to(np.array([0, base_y + bx.height / 2, 0]))
            by.next_to(bx, RIGHT, buff=0.15)
            by.align_to(bx, DOWN)

            lbl_x = MathTex(f"x={x_val}", font_size=22, color=BLUE_D)
            lbl_y = MathTex(f"y={y_val}", font_size=22, color=ORANGE)
            lbl_x.next_to(bx, DOWN, buff=0.12)
            lbl_y.next_to(by, DOWN, buff=0.12)

            grupos.add(VGroup(bx, by, lbl_x, lbl_y))

        grupos.arrange(RIGHT, buff=1.1)
        grupos.move_to(np.array([0, base_y + 0.5, 0]))

        # Linha de base
        base_line = Line(
            grupos.get_left()  + LEFT  * 0.3,
            grupos.get_right() + RIGHT * 0.3,
            color=GRAY_B, stroke_width=2
        ).next_to(grupos, DOWN, buff=0)

        self.play(Create(base_line), run_time=0.8)

        # Barras surgem par a par
        for par in grupos:
            self.play(
                DrawBorderThenFill(par[0]),
                DrawBorderThenFill(par[1]),
                Write(par[2]), Write(par[3]),
                run_time=1.6
            )
            self.wait(0.25)

        # Seta laranja (y) — topo das barras laranjas
        seta_y = Arrow(
            grupos[0][1].get_top() + LEFT  * 0.2,
            grupos[-1][1].get_top() + RIGHT * 0.2,
            color=ORANGE, buff=0.1, stroke_width=3
        )
        # Seta azul (x) — topo das barras azuis (posicionada abaixo da laranja)
        seta_x = Arrow(
            grupos[0][0].get_top() + LEFT  * 0.2,
            grupos[-1][0].get_top() + RIGHT * 0.2,
            color=BLUE_D, buff=0.1, stroke_width=3
        )
        obs = Text(
            "Ambas crescem juntas  →  proporcionalidade direta",
            font_size=22, color=YELLOW
        ).next_to(seta_y, UP, buff=0.18)

        self.play(GrowArrow(seta_x), GrowArrow(seta_y), run_time=1.2)
        self.play(Write(obs), run_time=1.3)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            grupos, base_line, seta_x, seta_y, obs
        )), run_time=1.0)

    # ===================================================================
    # CENA 3 – PROPORCIONALIDADE DIRETA: tabela e razão constante
    # ===================================================================
    def _direta_tabela(self):
        """
        Conceito : y / x = k (constante) — razão sempre igual.
        Visual   : Tabela x | y | y/x com destaque na coluna da razão.
        """
        faixa, inst, cab, linha_sep = cabecalho(self, "Direta — Razão Constante")

        intro = VGroup(
            Text("A razão  ", color=WHITE, font_size=24),
            MathTex(r"\dfrac{y}{x}", font_size=32, color=GREEN_B),
            Text("  é sempre a mesma para todos os pares.", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.08)
        intro.move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(1.8)
        self.play(FadeOut(intro), run_time=0.7)

        # Tabela — cabeçalho com fração y/x; posição descida para -0.8
        dados = [["x", "y", r"\dfrac{y}{x}"],
                 ["1", "6",  "6"],
                 ["2", "12", "6"],
                 ["3", "18", "6"],
                 ["4", "24", "6"]]

        tabela = MathTable(
            dados,
            include_outer_lines=True,
            line_config={"stroke_width": 1.5, "color": GRAY_B},
        ).scale(0.80)
        tabela.move_to(np.array([-2.0, -0.8, 0]))

        self.play(Create(tabela), run_time=2.2)
        self.wait(1.0)

        # Destacar coluna y÷x (linhas 2 a 5, coluna 3)
        celulas_k = VGroup(*[tabela.get_entries((i, 3)) for i in range(2, 6)])
        boxes_k = VGroup(*[
            SurroundingRectangle(c, color=GREEN_B, buff=0.08, stroke_width=2)
            for c in celulas_k
        ])
        self.play(Create(boxes_k), run_time=1.2)
        self.wait(0.5)

        # Fórmula à direita
        formula = VGroup(
            MathTex(r"k = \frac{y}{x} = 6", font_size=44, color=GREEN_B),
            Text("(constante de proporcionalidade)", font_size=20, color=WHITE),
            MathTex(r"\Rightarrow\; y = 6x", font_size=36, color=BLUE_D),
        ).arrange(DOWN, buff=0.35)
        formula.move_to(np.array([3.8, -0.8, 0]))

        for item in formula:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=0.9)
        self.wait(2.5)

        # Regra-chave em caixa amarela — abaixo da fórmula azul
        regra = Text("Direta: dobra x  →  dobra y", color=YELLOW, font_size=22)
        regra.next_to(formula, DOWN, buff=0.45)
        box_r = SurroundingRectangle(regra, color=YELLOW, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(regra), Create(box_r), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            tabela, boxes_k, formula, regra, box_r
        )), run_time=1.0)

    # ===================================================================
    # CENA 4 – PROPORCIONALIDADE INVERSA: barras visuais
    # ===================================================================
    def _inversa_barras(self):
        """
        Conceito : Quando x cresce, y diminui na mesma proporção.
        Visual   : Barras azul (x) cresce enquanto vermelho (y) diminui.
        """
        faixa, inst, cab, linha_sep = cabecalho(self, "Proporcionalidade Inversa")

        ctx = Text(
            "Mesma distância: quanto maior a velocidade, menor o tempo de viagem.",
            color=WHITE, font_size=23
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(ctx), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(ctx), run_time=0.7)

        # Pares (velocidade, tempo), k = 60
        pares  = [(1, 60), (2, 30), (3, 20), (4, 15)]
        base_y = -2.0
        esc_x  = 0.55    # escala barra x
        esc_y  = 0.055   # escala barra y (valor grande, precisa comprimir mais)

        grupos = VGroup()
        for x_val, y_val in pares:
            bx = barra(x_val * esc_x, BLUE_D)
            by = barra(y_val * esc_y, RED_B)

            bx.move_to(np.array([0, base_y + bx.height / 2, 0]))
            by.next_to(bx, RIGHT, buff=0.15)
            by.align_to(bx, DOWN)

            lbl_x = MathTex(f"x={x_val}", font_size=22, color=BLUE_D)
            lbl_y = MathTex(f"y={y_val}", font_size=22, color=RED_B)
            lbl_x.next_to(bx, DOWN, buff=0.12)
            lbl_y.next_to(by, DOWN, buff=0.12)

            grupos.add(VGroup(bx, by, lbl_x, lbl_y))

        grupos.arrange(RIGHT, buff=1.1)
        grupos.move_to(np.array([0, base_y + 0.4, 0]))

        base_line = Line(
            grupos.get_left()  + LEFT  * 0.3,
            grupos.get_right() + RIGHT * 0.3,
            color=GRAY_B, stroke_width=2
        ).next_to(grupos, DOWN, buff=0)

        self.play(Create(base_line), run_time=0.8)
        for par in grupos:
            self.play(
                DrawBorderThenFill(par[0]),
                DrawBorderThenFill(par[1]),
                Write(par[2]), Write(par[3]),
                run_time=1.6
            )
            self.wait(0.25)

        # Setas opostas indicando sentidos contrários
        seta_sobe = Arrow(
            grupos[0][0].get_top() + LEFT  * 0.2,
            grupos[-1][0].get_top() + RIGHT * 0.2,
            color=BLUE_D, buff=0.1, stroke_width=3
        )
        seta_desce = Arrow(
            grupos[0][1].get_top() + LEFT  * 0.2 + UP * 0.3,
            grupos[-1][1].get_top() + RIGHT * 0.2,
            color=RED_B, buff=0.1, stroke_width=3
        )
        obs = Text(
            "x cresce  →  y diminui:  proporcionalidade inversa",
            font_size=22, color=YELLOW
        ).move_to(np.array([0, 1.55, 0]))

        self.play(GrowArrow(seta_sobe), GrowArrow(seta_desce), run_time=1.3)
        self.play(Write(obs), run_time=1.3)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            grupos, base_line, seta_sobe, seta_desce, obs
        )), run_time=1.0)

    # ===================================================================
    # CENA 5 – PROPORCIONALIDADE INVERSA: tabela e produto constante
    # ===================================================================
    def _inversa_tabela(self):
        """
        Conceito : x · y = k (constante) — produto sempre igual.
        Visual   : Tabela x | y | x·y com destaque na coluna do produto.
        """
        faixa, inst, cab, linha_sep = cabecalho(self, "Inversa — Produto Constante")

        intro = Text(
            "O produto x × y é sempre o mesmo para todos os pares.",
            color=WHITE, font_size=24
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(1.8)
        self.play(FadeOut(intro), run_time=0.7)

        dados = [["x", "y", r"x \cdot y"],
                 ["1",  "60", "60"],
                 ["2",  "30", "60"],
                 ["3",  "20", "60"],
                 ["4",  "15", "60"]]

        tabela = MathTable(
            dados,
            include_outer_lines=True,
            line_config={"stroke_width": 1.5, "color": GRAY_B},
        ).scale(0.80)
        tabela.move_to(np.array([-2.0, -0.8, 0]))

        self.play(Create(tabela), run_time=2.2)
        self.wait(1.0)

        celulas_k = VGroup(*[tabela.get_entries((i, 3)) for i in range(2, 6)])
        boxes_k = VGroup(*[
            SurroundingRectangle(c, color=GREEN_B, buff=0.08, stroke_width=2)
            for c in celulas_k
        ])
        self.play(Create(boxes_k), run_time=1.2)
        self.wait(0.5)

        formula = VGroup(
            MathTex(r"k = x \cdot y = 60", font_size=44, color=GREEN_B),
            Text("(constante de proporcionalidade)", font_size=20, color=WHITE),
            MathTex(r"\Rightarrow\; y = \frac{60}{x}", font_size=36, color=RED_B),
        ).arrange(DOWN, buff=0.35)
        formula.move_to(np.array([3.8, -0.8, 0]))

        for item in formula:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=0.9)
        self.wait(2.5)

        regra = Text("Inversa: dobra x  →  y fica na metade", color=YELLOW, font_size=22)
        regra.next_to(formula, DOWN, buff=0.45)
        box_r = SurroundingRectangle(regra, color=YELLOW, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(regra), Create(box_r), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            tabela, boxes_k, formula, regra, box_r
        )), run_time=1.0)

    # ===================================================================
    # CENA 6 – FORMALIZAÇÃO: as duas fórmulas lado a lado
    # ===================================================================
    def _formalizacao(self):
        """
        Conceito : Sistematizar as definições formais de direta e inversa.
        Visual   : Duas caixas lado a lado com fórmulas, condição e interpretação.
        """
        faixa, inst, cab, linha_sep = cabecalho(self, "Formalização")

        # ── Caixa Direta (esquerda) ─────────────────────────────────
        box_dir = RoundedRectangle(
            width=5.8, height=4.0,
            corner_radius=0.30,
            fill_color=BLUE_E, fill_opacity=0.30,
            stroke_color=BLUE_D, stroke_width=2.5
        )
        conteudo_dir = VGroup(
            Text("Proporcional Direta", font_size=24, color=BLUE_D, weight=BOLD),
            MathTex(r"y = k \cdot x", font_size=46, color=BLUE_D),
            MathTex(r"\frac{y}{x} = k \quad (k \neq 0)", font_size=28, color=GREEN_B),
            Text("Dobra x  →  dobra y", font_size=21, color=WHITE),
        ).arrange(DOWN, buff=0.35)
        conteudo_dir.move_to(box_dir.get_center())
        grupo_dir = VGroup(box_dir, conteudo_dir)
        grupo_dir.move_to(np.array([-3.3, -0.3, 0]))

        # ── Caixa Inversa (direita) ──────────────────────────────────
        box_inv = RoundedRectangle(
            width=5.8, height=4.0,
            corner_radius=0.30,
            fill_color="#3d0018", fill_opacity=0.45,
            stroke_color=RED_B, stroke_width=2.5
        )
        conteudo_inv = VGroup(
            Text("Proporcional Inversa", font_size=24, color=RED_B, weight=BOLD),
            MathTex(r"y = \frac{k}{x}", font_size=46, color=RED_B),
            MathTex(r"x \cdot y = k \quad (k \neq 0)", font_size=28, color=GREEN_B),
            Text("Dobra x  →  metade y", font_size=21, color=WHITE),
        ).arrange(DOWN, buff=0.35)
        conteudo_inv.move_to(box_inv.get_center())
        grupo_inv = VGroup(box_inv, conteudo_inv)
        grupo_inv.move_to(np.array([3.3, -0.3, 0]))

        # ── "vs" central ────────────────────────────────────────────
        vs = Text("vs", font_size=32, color=YELLOW, weight=BOLD)
        vs.move_to(np.array([0, -0.3, 0]))

        # Animação sequencial: caixas → conteúdos → vs
        self.play(
            DrawBorderThenFill(box_dir),
            DrawBorderThenFill(box_inv),
            run_time=1.6
        )
        self.play(
            Write(conteudo_dir),
            Write(conteudo_inv),
            run_time=2.5
        )
        self.play(FadeIn(vs, scale=1.3), run_time=0.8)
        self.wait(2.0)

        # Síntese abaixo
        sintese = Text(
            "Direta: razão constante  |  Inversa: produto constante",
            font_size=22, color=YELLOW
        ).move_to(np.array([0, Y_RESPOSTA, 0]))
        box_s = SurroundingRectangle(sintese, color=YELLOW, buff=0.14, corner_radius=0.10)
        self.play(FadeIn(sintese), Create(box_s), run_time=1.0)
        self.wait(3.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            grupo_dir, grupo_inv, vs, sintese, box_s
        )), run_time=1.2)

    # ===================================================================
    # CENA 7 – PROBLEMA APLICADO
    # ===================================================================
    def _problema_aplicado(self):
        """
        Conceito : Aplicar proporcionalidade direta em contexto real.
        Problema : 3 caixas pesam 12 kg. Quantas pesam 40 kg?
        """
        faixa, inst, cab, linha_sep = cabecalho(self, "Problema Aplicado")

        enunciado = Text(
            "3 caixas iguais pesam 12 kg.\n"
            "Quantas caixas são necessárias para ter 40 kg?",
            color=WHITE, font_size=25, line_spacing=1.40
        ).move_to(np.array([0, 0.6, 0]))
        self.play(FadeIn(enunciado), run_time=1.3)
        self.wait(3.0)
        self.play(FadeOut(enunciado), run_time=0.7)

        # Identificação do tipo
        tipo = Text(
            "Mais caixas  →  mais peso   ⟹   Proporcionalidade DIRETA",
            color=BLUE_D, font_size=24
        ).move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(tipo), run_time=1.0)
        self.wait(1.5)

        # Tabela de resolução
        dados = [["Caixas (x)", "Peso (y)", r"\dfrac{y}{x}"],
                 ["3",  "12", "4"],
                 ["?",  "40", "4"]]

        tabela = MathTable(
            dados,
            include_outer_lines=True,
            line_config={"stroke_width": 1.5, "color": GRAY_B},
        ).scale(0.82)
        tabela.move_to(np.array([-2.2, -0.5, 0]))

        self.play(Create(tabela), run_time=2.0)
        self.wait(0.8)

        # Destacar k = 4
        cel_k1 = tabela.get_entries((2, 3))
        cel_k2 = tabela.get_entries((3, 3))
        boxes_k = VGroup(
            SurroundingRectangle(cel_k1, color=GREEN_B, buff=0.08),
            SurroundingRectangle(cel_k2, color=GREEN_B, buff=0.08),
        )
        self.play(Create(boxes_k), run_time=0.9)
        self.wait(0.5)

        # Cálculo passo a passo
        calc = VGroup(
            MathTex(r"k = \frac{12}{3} = 4", font_size=32, color=GREEN_B),
            MathTex(r"x = \frac{40}{k} = \frac{40}{4}", font_size=32, color=BLUE_D),
            MathTex(r"x = 10 \text{ caixas}", font_size=36, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        calc.move_to(np.array([3.5, -0.4, 0]))

        box_calc = SurroundingRectangle(
            calc[2], color=YELLOW, buff=0.14, corner_radius=0.10
        )

        for item in calc:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=1.0)
        self.play(Create(box_calc), run_time=0.6)

        resposta = Text(
            "Resposta: são necessárias 10 caixas.",
            color=YELLOW, font_size=24
        ).move_to(np.array([0, Y_RESPOSTA, 0]))
        self.play(FadeIn(resposta), run_time=0.8)
        self.wait(3.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            tipo, tabela, boxes_k, calc, box_calc, resposta
        )), run_time=1.0)

    # ===================================================================
    # CENA 8 – ENCERRAMENTO
    # ===================================================================
    def _encerramento(self):
        """Síntese visual do Descritor D29."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese — Descritor D29")

        descritivo = Text(
            "D29 – Variação proporcional direta ou inversa entre grandezas",
            color=WHITE, font_size=24
        ).move_to(np.array([0, 0.5, 0]))
        box_desc = SurroundingRectangle(
            descritivo, color=YELLOW, buff=0.18, corner_radius=0.10
        )
        self.play(FadeIn(descritivo), Create(box_desc), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(descritivo), FadeOut(box_desc), run_time=0.7)

        form_tit = Text("Resumo:", color=YELLOW, font_size=24, weight=BOLD)
        form_tit.move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(form_tit), run_time=0.6)

        resumo = VGroup(
            Text("Direta:  y = k · x   (razão y/x = k constante)",   color=BLUE_D,  font_size=22),
            Text("Inversa: y = k / x   (produto x·y = k constante)",  color=RED_B,   font_size=22),
            Text("Direta:  dobra x  →  dobra y",                       color=GREEN_B, font_size=22),
            Text("Inversa: dobra x  →  metade y",                      color=GREEN_B, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.27)
        resumo.next_to(form_tit, DOWN, buff=0.30)

        cores_dots = [BLUE_D, RED_B, GREEN_B, GREEN_B]
        dots = VGroup()
        for i, item in enumerate(resumo):
            dot = Dot(color=cores_dots[i], radius=0.07).next_to(item, LEFT, buff=0.14)
            dots.add(dot)
            self.play(FadeIn(dot), FadeIn(item, shift=RIGHT * 0.1), run_time=0.52)

        self.wait(2.0)
        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            form_tit, resumo, dots
        )), run_time=1.2)

    # ===================================================================
    # CENA 9 – LOGO EMILLY MAYRE
    # ===================================================================
    def _logo_emilly_mayre(self):
        """Identidade visual da Prof.ª Emilly Mayre."""
        ESCURO_L = "#1a1a2e"
        DOURADO  = "#C8A84B"
        CINZA_L  = "#888899"

        bg = Rectangle(
            width=16, height=9,
            fill_color=WHITE, fill_opacity=1, stroke_width=0
        )
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

        logo_h = ParametricFunction(
            inf_h, t_range=[0, TAU], color="#3a3a5c", stroke_width=2.5
        ).move_to(UP * 0.5)
        logo_v = ParametricFunction(
            inf_v, t_range=[0, TAU], color="#9999bb", stroke_width=2.5
        ).move_to(UP * 0.5)

        circ = Circle(
            radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
            color=ESCURO_L, stroke_width=0
        ).move_to(UP * 0.5)
        em = Text("EM", color=WHITE, font_size=22, weight=BOLD).move_to(circ.get_center())

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
