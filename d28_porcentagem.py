"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D28 – Resolver Problema que Envolva Porcentagem
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
RENDERIZAÇÃO (classe única — sem troca de ordem):
  manim -pql d28_v6.py D28
  manim -pqh d28_v6.py D28
=======================================================================
"""

from manim import *
import numpy as np

# -----------------------------------------------------------------------
# PALETA SEMÂNTICA GLOBAL
# YELLOW  → títulos e cabeçalhos
# BLUE_D  → azul base (partes não destacadas)
# GREEN_B → resultados e confirmações
# ORANGE  → destaque principal (porção em foco)
# WHITE   → textos explicativos
# -----------------------------------------------------------------------

Y_FAIXA_CY  =  3.50
Y_TITULO    =  2.55
Y_LINHA_SEP =  2.10
Y_RESPOSTA  = -3.40


def cabecalho(scene, texto_titulo):
    """Faixa SAEB + título + linha separadora."""
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


def make_setor(cx, cy, r, ang_ini, ang_fim, cor, op=0.88, n=80):
    """Setor circular via Polygon — sem bugs de AnnularSector/Sector."""
    pts = [np.array([cx, cy, 0])]
    for k in range(n + 1):
        a = ang_ini + (ang_fim - ang_ini) * k / n
        pts.append(np.array([cx + r * np.cos(a), cy + r * np.sin(a), 0]))
    return Polygon(*pts, fill_color=cor, fill_opacity=op,
                   stroke_color=WHITE, stroke_width=2)


# =======================================================================
# CLASSE MESTRE — contém todas as cenas em ordem
# Ordem: Abertura → CenaConceito → CenaMetades → CenaQuartos →
#        CenaQuintos → CenaUmPorcento → CenaDesconto → CenaAumento →
#        CenaProblema → Encerramento → LogoEmillyMayre
# =======================================================================
class D28(Scene):
    """
    Classe mestre do Descritor D28.
    Todas as cenas são executadas em sequência dentro de construct(),
    garantindo a ordem correta sem depender da junção de vídeos externos.
    """

    def construct(self):
        self._abertura()
        self._cena_conceito()
        self._cena_metades()
        self._cena_quartos()
        self._cena_quintos()
        self._cena_um_porcento()
        self._cena_desconto()
        self._cena_aumento()
        self._cena_problema()
        self._encerramento()
        self._logo_emilly_mayre()

    # ===================================================================
    # CENA 1 – ABERTURA
    # ===================================================================
    def _abertura(self):
        """Contextualização do Descritor D28 – SAEB."""
        faixa = Rectangle(
            width=14.4, height=1.05,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        titulo = Text("Descritor D28", color=YELLOW, font_size=52, weight=BOLD)
        titulo.move_to(np.array([0, 1.4, 0]))
        subtitulo = Text(
            "Resolver problemas que envolvam porcentagem",
            color=WHITE, font_size=27
        ).next_to(titulo, DOWN, buff=0.4)

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
            Text("1. O todo = 100% (círculo visual)",    color=WHITE, font_size=24),
            Text("2. Metades: 50%",                      color=WHITE, font_size=24),
            Text("3. Quartos: 25% e 75%",                color=WHITE, font_size=24),
            Text("4. Quintos: 20%, 40%, 60%, 80%",       color=WHITE, font_size=24),
            Text("5. Como encontrar 1%",                 color=WHITE, font_size=24),
            Text("6. Desconto e Aumento",                color=WHITE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        topicos.next_to(linha, DOWN, buff=0.28)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        dots = VGroup()
        for t in topicos:
            dot = Dot(color=ORANGE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.50)

        self.wait(2.5)
        self.play(FadeOut(VGroup(faixa, inst, linha, topicos, dots)), run_time=1.0)

    # ===================================================================
    # CENA 2 – O TODO = 100%
    # ===================================================================
    def _cena_conceito(self):
        """Mostrar visualmente que o círculo inteiro = 100%."""
        faixa, inst, cab, linha_sep = cabecalho(self, "O Todo")

        cx, cy, r = 0.0, -0.6, 1.85

        intro = Text(
            'Porcentagem = "por cem".\n100% = o valor inteiro, sem nada faltando.',
            color=ORANGE, font_size=24, line_spacing=1.35
        ).move_to(np.array([0, 0.4, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.2)
        self.play(FadeOut(intro), run_time=0.7)

        circulo = Circle(radius=r, fill_color=BLUE_D, fill_opacity=0.85,
                         stroke_color=WHITE, stroke_width=3)
        circulo.move_to(np.array([cx, cy, 0]))
        lbl_100 = Text("100%", color=YELLOW, font_size=52, weight=BOLD)
        lbl_100.move_to(np.array([cx, cy, 0]))

        self.play(GrowFromCenter(circulo), run_time=1.5)
        self.play(Write(lbl_100), run_time=1.0)
        self.wait(1.5)

        lbl_baixo = Text("O círculo inteiro = 100%", color=WHITE, font_size=24)
        lbl_baixo.next_to(circulo, DOWN, buff=0.25)
        self.play(FadeIn(lbl_baixo), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, circulo, lbl_100, lbl_baixo
        )), run_time=1.0)

    # ===================================================================
    # CENA 3 – METADES: 50%
    # ===================================================================
    def _cena_metades(self):
        """Dividir o círculo ao meio e mostrar que cada parte = 50%."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Dividindo ao Meio")

        cx, cy, r = -1.5, -0.3, 1.8

        intro = Text(
            "Dividindo o círculo ao meio,\ncada parte corresponde a 50%.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.8, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(intro), run_time=0.7)

        circ_base = Circle(radius=r, fill_color=GREY_D, fill_opacity=0.30,
                           stroke_color=WHITE, stroke_width=2)
        circ_base.move_to(np.array([cx, cy, 0]))
        self.play(GrowFromCenter(circ_base), run_time=1.2)

        s1 = make_setor(cx, cy, r, PI / 2, 3 * PI / 2, BLUE_D)
        s2 = make_setor(cx, cy, r, -PI / 2, PI / 2, ORANGE)

        self.play(FadeIn(s1), run_time=1.0)
        self.wait(0.4)
        self.play(FadeIn(s2), run_time=1.0)
        self.wait(0.4)

        linha_div = Line(
            np.array([cx, cy - r, 0]),
            np.array([cx, cy + r, 0]),
            color=WHITE, stroke_width=3
        )
        self.play(Create(linha_div), run_time=0.8)

        lbl1 = Text("50%", color=WHITE, font_size=36, weight=BOLD)
        lbl1.move_to(np.array([cx - r / 2, cy, 0]))
        lbl2 = Text("50%", color=WHITE, font_size=36, weight=BOLD)
        lbl2.move_to(np.array([cx + r / 2, cy, 0]))

        self.play(Write(lbl1), run_time=0.8)
        self.play(Write(lbl2), run_time=0.8)
        self.wait(1.2)

        painel = VGroup(
            Text("2 partes iguais:", color=YELLOW, font_size=24, weight=BOLD),
            Text("cada parte = 50%", color=WHITE, font_size=23),
            Text("50% + 50% = 100%", color=GREEN_B, font_size=23),
            Text("50% = metade do todo", color=ORANGE, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        painel.move_to(np.array([4.0, -0.3, 0]))

        for item in painel:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=0.65)
        self.wait(1.5)

        regra = Text("Encontrar 50% = dividir o todo por 2",
                     color=YELLOW, font_size=22)
        regra.move_to(np.array([-1.5, -2.55, 0]))
        box_regra = SurroundingRectangle(regra, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(regra), Create(box_regra), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, circ_base, s1, s2,
            linha_div, lbl1, lbl2, painel, regra, box_regra
        )), run_time=1.0)

    # ===================================================================
    # CENA 4 – QUARTOS: 25% e 75%
    # ===================================================================
    def _cena_quartos(self):
        """4 partes = 25% cada; 3 partes = 75%."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Quartos")

        cx, cy, r = -1.8, -0.5, 1.9

        intro = Text(
            "Dividindo em 4 partes iguais,\ncada parte corresponde a 25%.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.8, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(intro), run_time=0.7)

        circ_base = Circle(radius=r, fill_color=GREY_D, fill_opacity=0.25,
                           stroke_color=WHITE, stroke_width=2)
        circ_base.move_to(np.array([cx, cy, 0]))
        self.play(GrowFromCenter(circ_base), run_time=1.1)

        cores_q = [BLUE_D, ORANGE, GREEN_B, "#9966cc"]
        setores_q = []
        angs_meio = [PI / 4, -PI / 4, -3 * PI / 4, 3 * PI / 4]
        lbls_q = []

        for i in range(4):
            ang_i = PI / 2 - i * PI / 2
            ang_f = PI / 2 - (i + 1) * PI / 2
            s = make_setor(cx, cy, r, ang_f, ang_i, cores_q[i])
            setores_q.append(s)
            self.play(FadeIn(s), run_time=0.9)

            lx = cx + r * 0.60 * np.cos(angs_meio[i])
            ly = cy + r * 0.60 * np.sin(angs_meio[i])
            lbl = Text("25%", color=WHITE, font_size=26, weight=BOLD)
            lbl.move_to(np.array([lx, ly, 0]))
            self.play(Write(lbl), run_time=0.6)
            lbls_q.append(lbl)
            self.wait(0.3)

        linhas_q = VGroup(
            Line(np.array([cx, cy - r, 0]), np.array([cx, cy + r, 0]),
                 color=WHITE, stroke_width=2.5),
            Line(np.array([cx - r, cy, 0]), np.array([cx + r, cy, 0]),
                 color=WHITE, stroke_width=2.5),
        )
        self.play(Create(linhas_q), run_time=0.8)
        self.wait(1.2)

        painel = VGroup(
            Text("4 partes iguais:", color=YELLOW, font_size=24, weight=BOLD),
            Text("1 parte  = 25%",   color=BLUE_D,  font_size=22),
            Text("2 partes = 50%",   color=ORANGE,  font_size=22),
            Text("3 partes = 75%",   color=GREEN_B, font_size=22),
            Text("4 partes = 100%",  color=WHITE,   font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        painel.move_to(np.array([4.2, -0.5, 0]))

        for item in painel:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=0.65)

        box_painel = SurroundingRectangle(painel, color=WHITE, buff=0.18, corner_radius=0.1)
        self.play(Create(box_painel), run_time=0.6)
        self.wait(1.5)

        self.play(setores_q[3].animate.set_fill(opacity=0.20), run_time=0.8)

        regra = Text("Encontrar 25% = dividir o todo por 4",
                     color=YELLOW, font_size=22)
        regra.move_to(np.array([-1.8, -2.9, 0]))
        box_regra = SurroundingRectangle(regra, color=YELLOW, buff=0.18, corner_radius=0.1)
        self.play(FadeIn(regra), Create(box_regra), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, circ_base,
            *setores_q, *lbls_q, linhas_q,
            painel, box_painel, regra, box_regra
        )), run_time=1.0)

    # ===================================================================
    # CENA 5 – QUINTOS: 20%, 40%, 60%, 80%
    # ===================================================================
    def _cena_quintos(self):
        """5 partes = 20% cada; mostrar múltiplos."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Quintos")

        cx, cy, r = -1.8, -0.5, 1.9

        intro = Text(
            "Dividindo em 5 partes iguais,\ncada parte corresponde a 20%.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.8, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(intro), run_time=0.7)

        circ_base = Circle(radius=r, fill_color=GREY_D, fill_opacity=0.25,
                           stroke_color=WHITE, stroke_width=2)
        circ_base.move_to(np.array([cx, cy, 0]))
        self.play(GrowFromCenter(circ_base), run_time=1.1)

        cores_5 = [BLUE_D, ORANGE, GREEN_B, "#9966cc", RED_B]
        setores_5 = []
        lbls_5 = []
        ang_passo = TAU / 5

        for i in range(5):
            ang_i = PI / 2 - i * ang_passo
            ang_f = PI / 2 - (i + 1) * ang_passo
            s = make_setor(cx, cy, r, ang_f, ang_i, cores_5[i])
            setores_5.append(s)

            ang_meio = (ang_i + ang_f) / 2
            lx = cx + r * 0.62 * np.cos(ang_meio)
            ly = cy + r * 0.62 * np.sin(ang_meio)
            lbl = Text("20%", color=WHITE, font_size=22, weight=BOLD)
            lbl.move_to(np.array([lx, ly, 0]))
            lbls_5.append(lbl)

            self.play(FadeIn(s), run_time=0.85)
            self.play(Write(lbl), run_time=0.55)
            self.wait(0.25)

        linhas_5 = VGroup()
        for i in range(5):
            ang = PI / 2 - i * ang_passo
            linhas_5.add(Line(
                np.array([cx, cy, 0]),
                np.array([cx + r * np.cos(ang), cy + r * np.sin(ang), 0]),
                color=WHITE, stroke_width=2.2
            ))
        self.play(Create(linhas_5), run_time=0.7)
        self.wait(1.0)

        painel = VGroup(
            Text("5 partes iguais:", color=YELLOW, font_size=23, weight=BOLD),
            Text("1 parte  = 20%",  color=cores_5[0], font_size=21),
            Text("2 partes = 40%",  color=cores_5[1], font_size=21),
            Text("3 partes = 60%",  color=cores_5[2], font_size=21),
            Text("4 partes = 80%",  color=cores_5[3], font_size=21),
            Text("5 partes = 100%", color=WHITE,      font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        painel.move_to(np.array([4.2, -0.4, 0]))

        for item in painel:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=0.60)

        box_painel = SurroundingRectangle(painel, color=WHITE, buff=0.18, corner_radius=0.1)
        self.play(Create(box_painel), run_time=0.6)

        regra = Text("Encontrar 20% = dividir o todo por 5",
                     color=YELLOW, font_size=22)
        regra.move_to(np.array([-1.8, -2.9, 0]))
        box_regra = SurroundingRectangle(regra, color=YELLOW, buff=0.18, corner_radius=0.1)
        self.play(FadeIn(regra), Create(box_regra), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, circ_base,
            *setores_5, *lbls_5, linhas_5,
            painel, box_painel, regra, box_regra
        )), run_time=1.0)

    # ===================================================================
    # CENA 6 – COMO ENCONTRAR 1%
    # ===================================================================
    def _cena_um_porcento(self):
        """1% = o todo dividido por 100."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Como Encontrar 1%")

        cx, cy, r = -2.0, -0.5, 2.0

        intro = Text(
            "1% é obtido dividindo o todo por 100.\nÉ a menor fatia do círculo.",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 0.8, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.2)
        self.play(FadeOut(intro), run_time=0.7)

        ang_passo = TAU / 100
        setores_100 = VGroup()
        for i in range(100):
            ang_i = PI / 2 - i * ang_passo
            ang_f = PI / 2 - (i + 1) * ang_passo
            s = make_setor(cx, cy, r, ang_f, ang_i, BLUE_D, op=0.80)
            s.set_stroke(color=WHITE, width=0.8)
            setores_100.add(s)

        self.play(FadeIn(setores_100), run_time=1.5)
        self.wait(0.8)

        setor_1 = make_setor(cx, cy, r, PI / 2 - ang_passo, PI / 2, ORANGE, op=0.97)
        setor_1.set_stroke(color=WHITE, width=0.8)
        self.play(FadeIn(setor_1), run_time=1.0)

        ang_meio = PI / 2 - ang_passo / 2
        px_ext = cx + r * 1.45 * np.cos(ang_meio)
        py_ext = min(cy + r * 1.45 * np.sin(ang_meio), 1.7)
        px_brd = cx + r * 1.02 * np.cos(ang_meio)
        py_brd = cy + r * 1.02 * np.sin(ang_meio)

        seta_1 = Line(
            np.array([px_ext, py_ext, 0]),
            np.array([px_brd, py_brd, 0]),
            color=ORANGE, stroke_width=2.5
        )
        lbl_1pct = Text("1%", color=ORANGE, font_size=28, weight=BOLD)
        lbl_1pct.move_to(np.array([px_ext + 0.4, py_ext, 0]))
        self.play(Create(seta_1), Write(lbl_1pct), run_time=1.0)
        self.wait(1.0)

        painel = VGroup(
            Text("Para encontrar 1%:", color=YELLOW, font_size=23, weight=BOLD),
            Text("divida o valor por 100", color=WHITE, font_size=21),
            Text("Exemplo:", color=WHITE, font_size=21),
            Text("1% de 500 = 500 ÷ 100 = 5", color=GREEN_B, font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        painel.move_to(np.array([4.2, 0.2, 0]))

        for item in painel:
            self.play(FadeIn(item, shift=LEFT * 0.1), run_time=0.55)
        self.wait(0.8)

        msg = Text("Sabendo 1%, multiplique pelo % desejado!",
                   color=ORANGE, font_size=21)
        msg.move_to(np.array([cx, cy - r - 0.52, 0]))
        box_msg = SurroundingRectangle(msg, color=ORANGE, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(msg), Create(box_msg), run_time=0.9)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, setores_100,
            setor_1, seta_1, lbl_1pct, painel, msg, box_msg
        )), run_time=1.0)

    # ===================================================================
    # CENA 7 – DESCONTO PERCENTUAL
    # ===================================================================
    def _cena_desconto(self):
        """Desconto de 15% de forma lenta e didática."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Desconto Percentual")

        enunciado = Text(
            "Uma camiseta custa R$ 80,00.\nDesconto de 15%. Qual o preço final?",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 1.30, 0]))
        self.play(FadeIn(enunciado), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(enunciado), run_time=0.7)

        cx, cy, r = -2.5, -0.5, 1.85
        ang_passo  = TAU / 100

        titulo_circ = Text("R$ 80,00 = 100 partes", color=WHITE, font_size=22)
        titulo_circ.move_to(np.array([-2.5, 1.62, 0]))
        self.play(FadeIn(titulo_circ), run_time=0.7)

        setores_azuis = VGroup()
        for i in range(85):
            ang_i = PI / 2 - i * ang_passo
            ang_f = PI / 2 - (i + 1) * ang_passo
            s = make_setor(cx, cy, r, ang_f, ang_i, BLUE_D, op=0.80)
            s.set_stroke(color=WHITE, width=0.6)
            setores_azuis.add(s)

        setores_desc = VGroup()
        for i in range(85, 100):
            ang_i = PI / 2 - i * ang_passo
            ang_f = PI / 2 - (i + 1) * ang_passo
            s = make_setor(cx, cy, r, ang_f, ang_i, ORANGE, op=0.92)
            s.set_stroke(color=WHITE, width=0.6)
            setores_desc.add(s)

        self.play(FadeIn(setores_azuis), run_time=1.3)
        self.wait(0.5)
        self.play(FadeIn(setores_desc), run_time=1.2)
        self.wait(0.8)

        calc_group = VGroup(
            Text("Desconto:", color=YELLOW, font_size=23, weight=BOLD),
            Text("15% × 80 = 0,15 × 80 = R$ 12,00", color=WHITE, font_size=22),
            Text("Preço final:", color=YELLOW, font_size=23, weight=BOLD),
            Text("80 − 12 = R$ 68,00", color=GREEN_B, font_size=25, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        calc_group.move_to(np.array([3.5, 0.2, 0]))
        box_calc = SurroundingRectangle(
            calc_group[3], color=GREEN_B, buff=0.14, corner_radius=0.10
        )
        self.play(FadeIn(calc_group), run_time=1.0)
        self.play(Create(box_calc), run_time=0.6)

        lbl_85 = Text("85% pago — R$ 68,00", color=GREEN_B, font_size=21)
        lbl_85.next_to(box_calc, DOWN, buff=0.28)
        self.play(FadeIn(lbl_85), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, titulo_circ,
            setores_azuis, setores_desc,
            calc_group, box_calc, lbl_85
        )), run_time=1.0)

    # ===================================================================
    # CENA 8 – AUMENTO PERCENTUAL
    # ===================================================================
    def _cena_aumento(self):
        """Aumento de 12% de forma lenta e didática."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Aumento Percentual")

        enunciado = Text(
            "Um salário de R$ 2.000,00 teve aumento de 12%.\nQual é o novo salário?",
            color=WHITE, font_size=26, line_spacing=1.35
        ).move_to(np.array([0, 1.30, 0]))
        self.play(FadeIn(enunciado), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(enunciado), run_time=0.7)

        cx, cy, r = -2.5, -0.5, 1.85
        ang_passo  = TAU / 100

        titulo_circ = Text("R$ 2.000,00 = 100 partes", color=WHITE, font_size=22)
        titulo_circ.move_to(np.array([cx, 1.62, 0]))
        self.play(FadeIn(titulo_circ), run_time=0.7)

        setores_orig_new = VGroup()
        for i in range(88):
            ang_i = PI / 2 - i * ang_passo
            ang_f = PI / 2 - (i + 1) * ang_passo
            s = make_setor(cx, cy, r, ang_f, ang_i, BLUE_D, op=0.80)
            s.set_stroke(color=WHITE, width=0.6)
            setores_orig_new.add(s)

        setores_aum_new = VGroup()
        for i in range(88, 100):
            ang_i = PI / 2 - i * ang_passo
            ang_f = PI / 2 - (i + 1) * ang_passo
            s = make_setor(cx, cy, r, ang_f, ang_i, GREEN_B, op=0.92)
            s.set_stroke(color=WHITE, width=0.6)
            setores_aum_new.add(s)

        self.play(FadeIn(setores_orig_new), run_time=1.3)
        self.wait(0.5)
        self.play(FadeIn(setores_aum_new), run_time=1.2)
        self.wait(0.8)

        calc_group = VGroup(
            Text("Aumento:", color=YELLOW, font_size=22, weight=BOLD),
            Text("12% × 2.000 = R$ 240,00", color=WHITE, font_size=21),
            Text("Novo salário:", color=YELLOW, font_size=22, weight=BOLD),
            Text("2.000 + 240 = R$ 2.240,00", color=GREEN_B, font_size=23, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        calc_group.move_to(np.array([3.8, 0.2, 0]))
        box_calc = SurroundingRectangle(
            calc_group[3], color=GREEN_B, buff=0.14, corner_radius=0.10
        )
        self.play(FadeIn(calc_group), run_time=1.0)
        self.play(Create(box_calc), run_time=0.6)

        lbl_aum = Text("+12% — R$ 240,00", color=GREEN_B, font_size=20)
        lbl_aum.next_to(box_calc, DOWN, buff=0.22)
        lbl_orig = Text("88% — R$ 2.000,00", color=WHITE, font_size=20)
        lbl_orig.next_to(lbl_aum, DOWN, buff=0.15)
        self.play(FadeIn(lbl_aum), FadeIn(lbl_orig), run_time=0.8)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, titulo_circ,
            setores_orig_new, setores_aum_new,
            calc_group, box_calc, lbl_aum, lbl_orig
        )), run_time=1.0)

    # ===================================================================
    # CENA 9 – PROBLEMA APLICADO
    # ===================================================================
    def _cena_problema(self):
        """Resolver problema completo passo a passo com visual."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Problema Aplicado")

        enunciado = Text(
            "Em uma turma de 40 alunos, 25% foram\n"
            "aprovados na primeira fase.\n"
            "Quantos alunos foram aprovados?",
            color=WHITE, font_size=25, line_spacing=1.38
        ).move_to(np.array([0, 0.5, 0]))
        self.play(FadeIn(enunciado), run_time=1.3)
        self.wait(3.0)
        self.play(FadeOut(enunciado), run_time=0.7)

        cx, cy, r = -2.2, -0.85, 1.85

        titulo_circ = Text("40 alunos = 100%  (4 partes iguais)", color=WHITE, font_size=21)
        titulo_circ.move_to(np.array([-2.2, 1.25, 0]))
        self.play(FadeIn(titulo_circ), run_time=0.7)

        cores_q = [BLUE_D, BLUE_D, BLUE_D, GREEN_B]
        setores_q = VGroup()
        lbls_q    = VGroup()
        angs_meio = [PI / 4, -PI / 4, -3 * PI / 4, 3 * PI / 4]

        for i in range(4):
            ang_i = PI / 2 - i * PI / 2
            ang_f = PI / 2 - (i + 1) * PI / 2
            s = make_setor(cx, cy, r, ang_f, ang_i, cores_q[i])
            s.set_stroke(color=WHITE, width=2)
            setores_q.add(s)
            self.play(FadeIn(s), run_time=0.8)

            lx = cx + r * 0.60 * np.cos(angs_meio[i])
            ly = cy + r * 0.60 * np.sin(angs_meio[i])
            lbl = Text("25%", color=WHITE, font_size=24, weight=BOLD)
            lbl.move_to(np.array([lx, ly, 0]))
            lbls_q.add(lbl)
            self.play(Write(lbl), run_time=0.5)

        linha_v = Line(np.array([cx, cy - r, 0]), np.array([cx, cy + r, 0]),
                       color=WHITE, stroke_width=2.5)
        linha_h = Line(np.array([cx - r, cy, 0]), np.array([cx + r, cy, 0]),
                       color=WHITE, stroke_width=2.5)
        self.play(Create(linha_v), Create(linha_h), run_time=0.7)
        self.wait(0.8)

        calc = VGroup(
            Text("25% de 40:", color=YELLOW, font_size=23, weight=BOLD),
            Text("40 ÷ 4 = 10 alunos", color=WHITE, font_size=22),
            Text("1 quarto = 10 aprovados!", color=GREEN_B, font_size=24, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        calc.move_to(np.array([3.8, -0.2, 0]))
        box_c = SurroundingRectangle(
            calc[2], color=GREEN_B, buff=0.14, corner_radius=0.10
        )
        self.play(FadeIn(calc), run_time=1.0)
        self.play(Create(box_c), run_time=0.6)

        resposta = Text(
            "Resposta: 10 alunos foram aprovados.",
            color=YELLOW, font_size=24
        ).move_to(np.array([0, Y_RESPOSTA, 0]))
        self.play(FadeIn(resposta), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, titulo_circ,
            setores_q, lbls_q, linha_v, linha_h,
            calc, box_c, resposta
        )), run_time=1.0)

    # ===================================================================
    # CENA 10 – ENCERRAMENTO
    # ===================================================================
    def _encerramento(self):
        """Síntese do Descritor D28."""
        faixa, inst, cab, linha_sep = cabecalho(self, "Síntese — Descritor D28")

        descritivo = Text(
            "D28 – Resolver problemas que envolvam porcentagem",
            color=WHITE, font_size=25
        ).move_to(np.array([0, 0.5, 0]))
        box_desc = SurroundingRectangle(
            descritivo, color=YELLOW, buff=0.18, corner_radius=0.1
        )
        self.play(FadeIn(descritivo), Create(box_desc), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(descritivo), FadeOut(box_desc), run_time=0.7)

        form_tit = Text("Resumo:", color=YELLOW, font_size=24, weight=BOLD)
        form_tit.move_to(np.array([0, 1.55, 0]))
        self.play(FadeIn(form_tit), run_time=0.6)

        resumo = VGroup(
            Text("½ do todo  = 50%  (dividir por 2)",  color=BLUE_B,  font_size=22),
            Text("¼ do todo  = 25%  (dividir por 4)",  color=ORANGE,  font_size=22),
            Text("⅕ do todo  = 20%  (dividir por 5)",  color=GREEN_B, font_size=22),
            Text("1% = todo ÷ 100",                    color=WHITE,   font_size=22),
            Text("Desconto: V × (1 − %)",               color=ORANGE,  font_size=22),
            Text("Aumento:  V × (1 + %)",               color=GREEN_B, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        resumo.next_to(form_tit, DOWN, buff=0.30)

        dots = VGroup()
        cores = [BLUE_B, ORANGE, GREEN_B, WHITE, ORANGE, GREEN_B]
        for i, item in enumerate(resumo):
            dot = Dot(color=cores[i], radius=0.07).next_to(item, LEFT, buff=0.14)
            dots.add(dot)
            self.play(FadeIn(dot), FadeIn(item, shift=RIGHT * 0.1), run_time=0.55)

        self.wait(1.8)
        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep, form_tit, resumo, dots
        )), run_time=1.2)

    # ===================================================================
    # CENA 11 – LOGO EMILLY MAYRE
    # ===================================================================
    def _logo_emilly_mayre(self):
        """Identidade visual da Prof.ª Emilly Mayre."""
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
