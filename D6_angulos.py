"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D6 – Reconhecer ângulos como mudança de direção
            ou giros, identificando ângulos retos e não retos.
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT (coordenadas Manim: centro=0,0 | tela: x[-7,7] y[-4,4])
  Faixa SAEB  : y ∈ [3.0, 4.0]   → nunca sobrepor
  Título cena : y = 2.55
  Linha sep   : y = 2.10
  Conteúdo    : y ∈ [-2.6, 1.85]
  Resposta    : y = -3.40
=======================================================================
RENDERIZAÇÃO:
  manim -pqh D6_SAEB_Angulos.py D6_SAEB_Angulos
=======================================================================
"""

from manim import *
import numpy as np

# ── PALETA SEMÂNTICA GLOBAL ──────────────────────────────────────────
COR_BASE     = BLUE_C    # raio / segmento de referência
COR_GIRO     = YELLOW    # raio em movimento / ângulo
COR_RETO     = GREEN     # ângulo reto (90°)
COR_NAO_RETO = RED       # ângulos não retos
COR_TEXTO    = WHITE     # texto geral
COR_DESTAQUE = ORANGE    # rótulos de medida / destaques

# ── CONSTANTES DE LAYOUT (idênticas ao D28) ──────────────────────────
Y_FAIXA_CY       =  3.50
Y_TITULO         =  2.55
Y_LINHA_SEP      =  2.10
Y_TOPO_CONTEUDO  =  1.85
Y_BASE_CONTEUDO  = -2.60
Y_RESPOSTA       = -3.40


def faixa_saeb(scene):
    """Faixa SAEB fixa no topo — padrão D28."""
    faixa = Rectangle(
        width=14.4, height=1.05,
        fill_color=BLUE_E, fill_opacity=1, stroke_width=0
    ).move_to(np.array([0, Y_FAIXA_CY, 0]))
    inst = Text(
        "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
        color=WHITE, font_size=22
    ).move_to(faixa.get_center())
    scene.add(faixa, inst)
    return faixa, inst


def cabecalho(scene, texto_titulo):
    """Faixa SAEB + título + linha separadora — padrão D28."""
    faixa, inst = faixa_saeb(scene)
    cab = Text(texto_titulo, color=YELLOW, font_size=34, weight=BOLD)
    cab.move_to(np.array([0, Y_TITULO, 0]))
    linha_sep = Line(
        np.array([-6.2, Y_LINHA_SEP, 0]),
        np.array([ 6.2, Y_LINHA_SEP, 0]),
        color=YELLOW, stroke_width=1.2
    )
    scene.play(Write(cab), Create(linha_sep), run_time=1.1)
    scene.wait(0.3)
    return faixa, inst, cab, linha_sep


# =======================================================================
# CENA MESTRE – encadeia Abertura + 5 cenas + Logo
# =======================================================================
class D6_SAEB_Angulos(Scene):
    """
    Cena principal: encadeia todas as sub-cenas do descritor D6.
    Conceito: D6 – Reconhecer ângulos como mudança de direção
              ou giros, identificando ângulos retos e não retos.
    Nível: Fundamental – 9º Ano (SAEB)
    """

    def construct(self):
        self._abertura()
        self._cena1_introducao()
        self._cena2_giro()
        self._cena3_reto()
        self._cena4_tipos()
        self._cena5_direcao()
        self._cena6_sintese()
        self._logo()

    # ──────────────────────────────────────────────────────────────────
    # ABERTURA – padrão D28
    # ──────────────────────────────────────────────────────────────────
    def _abertura(self):
        faixa, inst = faixa_saeb(self)

        titulo = Text("Descritor D6", color=YELLOW, font_size=52, weight=BOLD)
        titulo.move_to(np.array([0, 1.2, 0]))
        subtitulo = Text(
            "Reconhecer ângulos como mudança de direção ou giros",
            color=WHITE, font_size=24
        ).next_to(titulo, DOWN, buff=0.4)

        self.play(Write(titulo), run_time=1.6)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtitulo)), run_time=0.9)
        self.wait(0.2)

        linha = Line(
            np.array([-5.5, 0.8, 0]), np.array([5.5, 0.8, 0]),
            color=YELLOW, stroke_width=1.5
        )
        self.play(Create(linha), run_time=0.7)

        topicos = VGroup(
            Text("1. O que é um ângulo? (vértice e raios)",  color=WHITE, font_size=22),
            Text("2. Ângulo como giro (rotação de raio)",     color=WHITE, font_size=22),
            Text("3. Ângulo Reto — 90° e o símbolo □",        color=WHITE, font_size=22),
            Text("4. Tipos de ângulos: agudo, obtuso, raso",  color=WHITE, font_size=22),
            Text("5. Ângulo como mudança de direção",          color=WHITE, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        topicos.next_to(linha, DOWN, buff=0.28)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        # Garante que não ultrapasse a borda inferior
        if topicos.get_bottom()[1] < Y_BASE_CONTEUDO:
            topicos.shift(UP * (Y_BASE_CONTEUDO - topicos.get_bottom()[1] + 0.1))

        dots = VGroup()
        for t in topicos:
            dot = Dot(color=ORANGE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.50)

        self.wait(2.0)
        self.play(FadeOut(VGroup(linha, topicos, dots, faixa, inst)), run_time=1.0)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # CENA 1 – Introdução: o que é um ângulo?
    # ──────────────────────────────────────────────────────────────────
    def _cena1_introducao(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "D6 – O que é um Ângulo?")

        # Figura centralizada e mais baixa
        centro = np.array([-0.5, -1.2, 0])
        pA     = centro + RIGHT * 3.2
        pB     = centro + 3.2 * np.array([np.cos(PI/3), np.sin(PI/3), 0])

        # 1) Mostrar vértice V e pontos A, B ANTES das semirretas
        vertice = Dot(centro, color=COR_DESTAQUE, radius=0.10)
        dot_a   = Dot(pA,     color=COR_BASE,     radius=0.08)
        dot_b   = Dot(pB,     color=COR_GIRO,     radius=0.08)

        label_v = Text("V  (vértice)", font_size=20, color=COR_DESTAQUE
                       ).next_to(vertice, DOWN + LEFT * 0.3, buff=0.20)
        label_a = Text("A", font_size=20, color=COR_BASE
                       ).next_to(dot_a, RIGHT, buff=0.14)
        label_b = Text("B", font_size=20, color=COR_GIRO
                       ).next_to(dot_b, RIGHT, buff=0.14)

        self.play(FadeIn(vertice), Write(label_v), run_time=0.8)
        self.play(FadeIn(dot_a), Write(label_a), run_time=0.6)
        self.play(FadeIn(dot_b), Write(label_b), run_time=0.6)
        self.wait(0.6)

        # 2) Traçar semirreta VA (passa por A) e semirreta VB (passa por B)
        raio_a = Arrow(centro, pA, color=COR_BASE, buff=0, stroke_width=4)
        raio_b = Arrow(centro, pB, color=COR_GIRO, buff=0, stroke_width=4)

        # Notação com seta em cima usando MathTex
        label_ra = MathTex(r"\overrightarrow{VA}", font_size=28, color=COR_BASE
                           ).next_to(raio_a, DOWN, buff=0.20)
        label_rb = MathTex(r"\overrightarrow{VB}", font_size=28, color=COR_GIRO
                           ).next_to(raio_b.get_center(), LEFT, buff=0.30)

        self.play(Create(raio_a), Write(label_ra), run_time=1.4)
        self.play(Create(raio_b), Write(label_rb), run_time=1.4)
        self.wait(0.5)

        # 3) Marcar o ângulo AVB
        arc = Arc(radius=0.7, start_angle=0, angle=PI/3,
                  color=COR_DESTAQUE, stroke_width=3
                  ).move_arc_center_to(centro)
        mid_ang = PI / 6
        lbl_ang = MathTex(r"\angle AVB", font_size=30, color=COR_DESTAQUE
                          ).move_to(centro + 1.25 * np.array(
                              [np.cos(mid_ang), np.sin(mid_ang), 0]))

        self.play(Create(arc), Write(lbl_ang), run_time=1.2)
        self.wait(0.8)

        defn = Text(
            "Ângulo = abertura entre duas semirretas com a mesma origem",
            font_size=21, color=COR_TEXTO
        ).move_to(np.array([0, Y_BASE_CONTEUDO + 0.35, 0]))
        self.play(Write(defn), run_time=1.8)
        self.wait(2)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            vertice, label_v, dot_a, label_a, dot_b, label_b,
            raio_a, label_ra, raio_b, label_rb,
            arc, lbl_ang, defn
        )), run_time=1.2)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # CENA 2 – Ângulo como Giro (rotação)
    # ──────────────────────────────────────────────────────────────────
    def _cena2_giro(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Ângulo como Giro")

        cy_circ = -0.5
        circulo = Circle(radius=2.0, color=BLUE_E, stroke_width=1.5)
        circulo.set_fill(BLUE_E, opacity=0.05)
        circulo.move_to(np.array([0, cy_circ, 0]))
        vertice = Dot(np.array([0, cy_circ, 0]),
                      color=COR_DESTAQUE, radius=0.09)

        self.play(Create(circulo), FadeIn(vertice), run_time=1.2)

        raio_fixo = Arrow(
            np.array([0, cy_circ, 0]),
            np.array([2.0, cy_circ, 0]),
            color=COR_BASE, buff=0, stroke_width=5)
        lbl_ini = Text("Posição inicial", font_size=19, color=COR_BASE
                       ).next_to(raio_fixo, DOWN, buff=0.15).shift(LEFT * 1.2)

        self.play(Create(raio_fixo), Write(lbl_ini), run_time=1.2)
        self.wait(0.4)
        self.play(FadeOut(lbl_ini))

        av = ValueTracker(0.01)

        raio_mov = always_redraw(lambda: Arrow(
            np.array([0, cy_circ, 0]),
            np.array([0, cy_circ, 0]) + 2.0 * np.array([
                np.cos(av.get_value()), np.sin(av.get_value()), 0]),
            color=COR_GIRO, buff=0, stroke_width=5))

        arco_giro = always_redraw(lambda: Arc(
            radius=0.65, start_angle=0, angle=av.get_value(),
            color=COR_DESTAQUE, stroke_width=3
        ).move_arc_center_to(np.array([0, cy_circ, 0])))

        def _pos_deg(angle):
            raw = np.array([0, cy_circ, 0]) + 2.5 * np.array([
                np.cos(angle / 2), np.sin(angle / 2), 0])
            raw[1] = min(raw[1], Y_LINHA_SEP - 0.35)
            return raw

        def _graus_str(angle):
            return f"{min(int(round(np.degrees(angle))), 360)}°"

        lbl_deg = always_redraw(lambda: Text(
            _graus_str(av.get_value()),
            font_size=26, color=COR_DESTAQUE
        ).move_to(_pos_deg(av.get_value())))

        self.play(Create(raio_mov), Create(arco_giro),
                  Write(lbl_deg), run_time=0.8)

        instr = Text("O raio gira → o ângulo aumenta",
                     font_size=22, color=COR_TEXTO
                     ).move_to(np.array([0, Y_RESPOSTA + 0.5, 0]))
        self.play(Write(instr), run_time=1.2)

        for val in [PI/4, PI/2, PI, 2*PI - 0.01]:
            self.play(av.animate.set_value(val), run_time=1.8)
            self.wait(0.7)

        self.wait(1)
        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            circulo, vertice, raio_fixo,
            raio_mov, arco_giro, lbl_deg, instr
        )), run_time=1.2)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # CENA 3 – Ângulo Reto (90°)
    # ──────────────────────────────────────────────────────────────────
    def _cena3_reto(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Ângulo Reto  —  90°")

        # Ângulo reto à esquerda; folha à direita — figura mais baixa
        centro = np.array([-2.8, -1.1, 0])

        vertice = Dot(centro, color=COR_RETO, radius=0.09)
        rh = Arrow(centro, centro + RIGHT * 2.8,
                   color=COR_BASE, buff=0, stroke_width=5)
        rv = Arrow(centro, centro + UP * 2.5,
                   color=COR_GIRO, buff=0, stroke_width=5)

        self.play(FadeIn(vertice), run_time=0.5)
        self.play(Create(rh), run_time=1.2)
        self.play(Create(rv), run_time=1.2)
        self.wait(0.4)

        sim = RightAngle(rh, rv, length=0.35,
                         color=COR_RETO, stroke_width=3)
        lbl90 = Text("90°", font_size=32, color=COR_RETO
                     ).move_to(centro + np.array([0.78, 0.78, 0]))

        self.play(Create(sim), run_time=1)
        self.play(Write(lbl90), run_time=0.8)
        self.wait(0.8)

        defn = VGroup(
            Text("O ângulo reto mede exatamente 90°.", font_size=21,
                 color=COR_TEXTO),
            Text("Símbolo: □  (quadradinho no vértice)", font_size=21,
                 color=COR_RETO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22
                  ).move_to(np.array([0, Y_BASE_CONTEUDO + 0.45, 0]))

        self.play(Write(defn[0]), run_time=1.5)
        self.wait(0.3)
        self.play(Write(defn[1]), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(defn), run_time=0.8)

        # Folha à direita, sem sobrepor o ângulo
        folha = Rectangle(width=2.4, height=1.8, color=BLUE_E,
                          stroke_width=2).move_to(np.array([3.2, -1.1, 0]))
        folha.set_fill(BLUE_E, opacity=0.12)
        lbl_f = Text("Canto da folha\n= ângulo reto",
                     font_size=19, color=COR_RETO,
                     line_spacing=1.2).next_to(folha, DOWN, buff=0.22)
        canto = folha.get_corner(UL)
        sq    = Square(side_length=0.22, color=COR_RETO, stroke_width=2
                       ).move_to(canto + RIGHT * 0.11 + DOWN * 0.11)

        self.play(Create(folha), run_time=1.2)
        self.play(Create(sq), Write(lbl_f), run_time=1.2)
        self.wait(2)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            vertice, rh, rv, sim, lbl90,
            folha, sq, lbl_f
        )), run_time=1.2)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # CENA 4 – Tipos de Ângulos
    # ──────────────────────────────────────────────────────────────────
    def _angulo_card(self, graus, titulo, cor, pos):
        """Card de ângulo com label de graus no meio do arco."""
        rad  = np.radians(graus)
        comp = 1.45

        rb = Arrow(ORIGIN, RIGHT * comp, color=COR_BASE,
                   buff=0, stroke_width=3.5)
        rm = Arrow(ORIGIN,
                   comp * np.array([np.cos(rad), np.sin(rad), 0]),
                   color=cor, buff=0, stroke_width=3.5)
        arc = Arc(radius=0.42, start_angle=0, angle=rad,
                  color=cor, stroke_width=2.5)

        marca = (RightAngle(rb, rm, length=0.20, color=cor, stroke_width=2.5)
                 if graus == 90 else VGroup())

        mid = rad / 2
        label_grau = Text(f"{graus}°", font_size=21, color=cor
                          ).move_to(0.70 * np.array([np.cos(mid), np.sin(mid), 0]))
        label_nome = Text(titulo, font_size=17, color=cor, weight=BOLD
                          ).next_to(rb, DOWN, buff=0.42)

        card = VGroup(rb, rm, arc, marca, label_grau, label_nome).move_to(pos)
        return card

    def _cena4_tipos(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Tipos de Ângulos")

        # Tabela de classificação com quadro ao redor
        tabela = VGroup(
            Text("Agudo    0° < α < 90°",   font_size=17, color=RED),
            Text("Reto     α = 90°",          font_size=17, color=COR_RETO),
            Text("Obtuso   90° < α < 180°",  font_size=17, color=ORANGE),
            Text("Raso     α = 180°",         font_size=17, color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20
                  ).move_to(np.array([4.6, 1.0, 0]))

        quadro_tab = SurroundingRectangle(
            tabela, color=YELLOW, stroke_width=1.8,
            fill_color=BLACK, fill_opacity=0.6,
            buff=0.20, corner_radius=0.10
        )

        self.play(FadeIn(quadro_tab), FadeIn(tabela, shift=LEFT), run_time=1.5)
        self.wait(0.8)

        # 4 cards distribuídos mais baixos: y = -1.2
        posicoes = [
            np.array([-4.8, -1.2, 0]),
            np.array([-1.6, -1.2, 0]),
            np.array([ 1.6, -1.2, 0]),
            np.array([ 4.8, -1.2, 0]),
        ]
        dados = [
            (45,  "Agudo",  RED),
            (90,  "Reto",   COR_RETO),
            (120, "Obtuso", ORANGE),
            (180, "Raso",   PURPLE),
        ]

        cards = []
        for (graus, nome, cor), pos in zip(dados, posicoes):
            card = self._angulo_card(graus, nome, cor, pos)
            cards.append(card)
            self.play(Create(card), run_time=1.6)
            self.wait(0.6)

        # Destaque no ângulo reto
        dest = SurroundingRectangle(
            cards[1], color=COR_RETO,
            stroke_width=2.5, buff=0.12, corner_radius=0.1)

        self.play(Create(dest), run_time=1.2)
        self.wait(2)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            tabela, quadro_tab, dest, *cards
        )), run_time=1.2)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # CENA 5 – Mudança de Direção no Plano
    # ──────────────────────────────────────────────────────────────────
    def _cena5_direcao(self):
        faixa, inst, cab, linha_sep = cabecalho(
            self, "Ângulo como Mudança de Direção")

        instrucao = Text(
            "Um pedestre percorre um caminho e muda de direção.",
            font_size=21, color=COR_TEXTO
        ).move_to(np.array([0, Y_TOPO_CONTEUDO - 0.15, 0]))
        self.play(Write(instrucao), run_time=1.5)
        self.wait(0.4)

        # ── EXEMPLO 1: Curva de 90° ───────────────────────────────────
        titulo_ex1 = Text(
            "Exemplo 1 – Curva de 90° (ângulo reto)",
            font_size=19, color=COR_RETO
        ).move_to(np.array([0, Y_TOPO_CONTEUDO - 0.60, 0]))
        self.play(Write(titulo_ex1), run_time=1.2)

        # Figura mais baixa
        pA  = np.array([-5.8, -1.5, 0])
        pB  = np.array([-1.8, -1.5, 0])
        pC  = np.array([-1.8,  0.8, 0])

        trecho1   = Arrow(pA, pB, color=COR_BASE, buff=0, stroke_width=5)
        trecho2   = Arrow(pB, pC, color=COR_GIRO,  buff=0, stroke_width=5)
        # Pontilhado continuando para a direita após pB
        pontilhado1 = DashedLine(pB, pB + RIGHT * 1.8,
                                  color=COR_BASE, stroke_width=2.5,
                                  dash_length=0.15)
        dot_b     = Dot(pB, color=COR_RETO, radius=0.1)
        lbl_curva = Text("Curva aqui!", font_size=17, color=COR_RETO
                         ).next_to(dot_b, DOWN, buff=0.18)

        self.play(Create(trecho1), run_time=1.2)
        self.play(FadeIn(dot_b), Write(lbl_curva), run_time=0.8)
        self.play(Create(pontilhado1), run_time=0.8)
        self.play(Create(trecho2), run_time=1.2)
        self.wait(0.4)

        lin1     = Line(pB, pB + RIGHT * 0.6, color=COR_BASE)
        lin2     = Line(pB, pB + UP   * 0.6, color=COR_GIRO)
        sim_reto = RightAngle(lin1, lin2, length=0.26,
                              color=COR_RETO, stroke_width=2.5)
        lbl_90   = Text("90°", font_size=21, color=COR_RETO
                        ).next_to(sim_reto, RIGHT + UP * 0.3, buff=0.12)

        self.play(Create(sim_reto), Write(lbl_90), run_time=1.2)

        veredicto1 = Text("→ Ângulo RETO ✓", font_size=20,
                          color=COR_RETO, weight=BOLD
                          ).move_to(np.array([3.6, pB[1], 0]))
        self.play(Write(veredicto1), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            titulo_ex1, trecho1, trecho2, pontilhado1,
            dot_b, lbl_curva, lin1, lin2, sim_reto, lbl_90, veredicto1
        )), run_time=1.0)

        # ── EXEMPLO 2: Curva de 45° ───────────────────────────────────
        titulo_ex2 = Text(
            "Exemplo 2 – Curva de 45° (ângulo agudo)",
            font_size=19, color=COR_NAO_RETO
        ).move_to(np.array([0, Y_TOPO_CONTEUDO - 0.60, 0]))
        self.play(Write(titulo_ex2), run_time=1.2)

        pA2   = np.array([-5.8, -1.5, 0])
        pB2   = np.array([-1.8, -1.5, 0])
        ang45 = np.radians(45)
        pC2   = pB2 + 2.3 * np.array([np.cos(ang45), np.sin(ang45), 0])

        trecho1b  = Arrow(pA2, pB2, color=COR_BASE, buff=0, stroke_width=5)
        trecho2b  = Arrow(pB2, pC2, color=COR_NAO_RETO, buff=0, stroke_width=5)
        # Pontilhado continuando para a direita após pB2
        pontilhado2 = DashedLine(pB2, pB2 + RIGHT * 1.8,
                                  color=COR_BASE, stroke_width=2.5,
                                  dash_length=0.15)
        dot_b2    = Dot(pB2, color=COR_DESTAQUE, radius=0.1)

        self.play(Create(trecho1b), run_time=1.2)
        self.play(FadeIn(dot_b2), run_time=0.5)
        self.play(Create(pontilhado2), run_time=0.8)
        self.play(Create(trecho2b), run_time=1.2)
        self.wait(0.4)

        arco45 = Arc(radius=0.55, start_angle=0, angle=ang45,
                     color=COR_NAO_RETO, stroke_width=2.5
                     ).move_arc_center_to(pB2)
        mid45  = ang45 / 2
        lbl_45 = Text("45°", font_size=21, color=COR_NAO_RETO
                      ).move_to(pB2 + 0.95 * np.array(
                          [np.cos(mid45), np.sin(mid45), 0]))

        self.play(Create(arco45), Write(lbl_45), run_time=1.2)

        veredicto2 = Text("→ Ângulo NÃO reto ✗", font_size=20,
                          color=COR_NAO_RETO, weight=BOLD
                          ).move_to(np.array([3.6, pB2[1], 0]))
        self.play(Write(veredicto2), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            titulo_ex2, trecho1b, trecho2b, pontilhado2,
            dot_b2, arco45, lbl_45, veredicto2, instrucao
        )), run_time=1.0)

        self.play(FadeOut(VGroup(faixa, inst, cab, linha_sep)), run_time=0.8)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # CENA 6 – Síntese D6 (cena separada com título próprio)
    # ──────────────────────────────────────────────────────────────────
    def _cena6_sintese(self):
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese – D6 SAEB")

        sintese = VGroup(
            Text("• Ângulo = abertura entre dois raios / giro de direção",
                 font_size=20, color=COR_TEXTO),
            Text("• Ângulo RETO mede 90°  →  marcado com □",
                 font_size=20, color=COR_RETO),
            Text("• Ângulo agudo: 0° < α < 90°  (não reto)",
                 font_size=20, color=COR_NAO_RETO),
            Text("• Ângulo obtuso: 90° < α < 180°  (não reto)",
                 font_size=20, color=ORANGE),
            Text("• Toda mudança de direção forma um ângulo",
                 font_size=20, color=COR_GIRO),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32
                  ).move_to(np.array([0, -0.20, 0]))

        if sintese.get_top()[1] > Y_TOPO_CONTEUDO:
            sintese.shift(DOWN * (sintese.get_top()[1] - Y_TOPO_CONTEUDO + 0.05))
        if sintese.get_bottom()[1] < Y_BASE_CONTEUDO:
            sintese.shift(UP * (Y_BASE_CONTEUDO - sintese.get_bottom()[1] + 0.05))

        for linha in sintese:
            self.play(FadeIn(linha, shift=RIGHT * 0.3), run_time=1.0)
            self.wait(0.3)

        self.wait(2.5)
        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, sintese
        )), run_time=1.5)
        self.wait(0.2)

    # ──────────────────────────────────────────────────────────────────
    # LOGO – Identidade visual Prof.ª Emilly Mayre (padrão D28)
    # ──────────────────────────────────────────────────────────────────
    def _logo(self):
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
                                    color="#3a3a5c", stroke_width=2.5)
        logo_v = ParametricFunction(inf_v, t_range=[0, TAU],
                                    color="#9999bb", stroke_width=2.5)
        logo_h.move_to(UP * 0.5)
        logo_v.move_to(UP * 0.5)

        circ = Circle(radius=0.42, fill_color=ESCURO_L, fill_opacity=1,
                      color=ESCURO_L, stroke_width=0).move_to(UP * 0.5)
        em   = Text("EM", color=WHITE, font_size=22,
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
