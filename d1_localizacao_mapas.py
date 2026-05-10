"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Localização e Movimentação em Mapas
Descritor : D1 — SAEB / Matemática / 6º ao 8º Ano
Autora    : Prof.ª Emilly Mayre
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT SEGURO (sobreposições eliminadas):
  Faixa SAEB  : y ∈ [3.0 , 4.0]   → nunca sobrepor
  Título cena : y = 2.55
  Linha sep   : y = 2.10
  Conteúdo    : y ∈ [-2.40, 1.85]
  Rodapé texto: y = -2.85          → margem de segurança acima do corte
=======================================================================
RENDERIZAÇÃO:
  manim -pqh localizacao_mapas.py DescritorD1Completo
=======================================================================
"""

from manim import *
import numpy as np

# -----------------------------------------------------------------------
# CONSTANTES DE LAYOUT
# Tela Manim: x ∈ [-7.1, 7.1]  y ∈ [-4.0, 4.0]
# Faixa SAEB (altura 0.85) centrada em y=3.57 → ocupa y ∈ [3.14, 4.00]
# Título em y=2.65 fica claramente abaixo da faixa, sem sobreposição
# -----------------------------------------------------------------------
Y_FAIXA_CY  =  3.57   # centro da faixa — encostada no topo visível
Y_TITULO    =  2.65   # título em amarelo, abaixo da faixa
Y_LINHA_SEP =  2.20   # linha separadora
Y_RODAPE    = -2.85   # rodapé seguro para narrações/sínteses

# -----------------------------------------------------------------------
# PALETA GLOBAL
# -----------------------------------------------------------------------
COR_GRADE    = BLUE_C
COR_LOCAL    = YELLOW
COR_TRAJETO  = GREEN
COR_DESTAQUE = RED
COR_TEXTO    = WHITE


# =======================================================================
# CENA ÚNICA — DescritorD1Completo
# =======================================================================
class DescritorD1Completo(Scene):
    """
    Conceito : D1 — Identificar a localização/movimentação de objeto
               em mapas, croquis e outras representações gráficas.
    Nível    : Ensino Fundamental II — 6º ao 8º Ano
    Objetivo : Apresentar grade de referência, rosa dos ventos,
               coordenadas e trajetória em sequência didática única.
    Autora   : Prof.ª Emilly Mayre
    """

    BLOCO_W = 2.2
    BLOCO_H = 1.3
    POS_ESCOLA     = np.array([-3.8,  1.0, 0])
    POS_PRACA      = np.array([ 0.0, -0.9, 0])
    POS_BIBLIOTECA = np.array([ 3.8,  1.0, 0])

    def construct(self):
        self._cena_abertura()
        self._cena_grade()
        self._cena_rosa()
        self._cena_coordenadas()
        self._cena_movimentacao()
        self._cena_sintese()
        self._cena_logo()

    # ==================================================================
    # HELPER — cabeçalho SAEB
    # ==================================================================
    def _cabecalho(self, texto_titulo):
        faixa = Rectangle(
            width=14.4, height=0.86,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))

        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=19
        ).move_to(faixa.get_center())

        cab = Text(texto_titulo, color=COR_LOCAL, font_size=34, weight=BOLD)
        cab.move_to(np.array([0, Y_TITULO, 0]))

        linha_sep = Line(
            np.array([-6.2, Y_LINHA_SEP, 0]),
            np.array([ 6.2, Y_LINHA_SEP, 0]),
            color=COR_LOCAL, stroke_width=1.2
        )

        self.add(faixa, inst)
        self.play(Write(cab), Create(linha_sep), run_time=1.1)
        self.wait(0.3)
        return faixa, inst, cab, linha_sep

    # ==================================================================
    # CENA 0 — ABERTURA
    # ==================================================================
    def _cena_abertura(self):
        faixa = Rectangle(
            width=14.4, height=0.86,
            fill_color=BLUE_E, fill_opacity=1, stroke_width=0
        ).move_to(np.array([0, Y_FAIXA_CY, 0]))
        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=19
        ).move_to(faixa.get_center())
        self.add(faixa, inst)

        titulo = Text(
            "Localização e Movimentação\nem Mapas",
            color=COR_LOCAL, font_size=46, weight=BOLD, line_spacing=1.2
        ).move_to(np.array([0, 0.8, 0]))

        subtitulo = Text(
            "Como nos localizamos e descrevemos trajetos?",
            color=WHITE, font_size=26
        ).next_to(titulo, DOWN, buff=0.45)

        self.play(Write(titulo), run_time=1.8)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtitulo)), run_time=0.9)
        self.wait(0.2)

        linha = Line(
            np.array([-5.5, 1.60, 0]), np.array([5.5, 1.60, 0]),
            color=COR_LOCAL, stroke_width=1.5
        )
        self.play(Create(linha), run_time=0.7)

        topicos = VGroup(
            Text("1. Grade de referência em mapas",           color=WHITE, font_size=24),
            Text("2. Rosa dos Ventos — pontos cardeais",      color=WHITE, font_size=24),
            Text("3. Localização por coordenadas (col, lin)", color=WHITE, font_size=24),
            Text("4. Movimentação e trajetória no mapa",      color=WHITE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        topicos.next_to(linha, DOWN, buff=0.35)
        topicos.move_to(np.array([0, topicos.get_center()[1], 0]))

        dots_group = VGroup()
        for t in topicos:
            dot = Dot(color=COR_DESTAQUE, radius=0.08).next_to(t, LEFT, buff=0.20)
            dots_group.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.55)

        self.wait(2.5)
        self.play(FadeOut(VGroup(faixa, inst, linha, topicos, dots_group)), run_time=1.0)
        self.wait(0.2)

    # ==================================================================
    # CENA 1 — GRADE DE REFERÊNCIA
    # ==================================================================
    def _cena_grade(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Grade de Referência")

        intro = Text(
            "Mapas usam uma grade para que qualquer\nponto seja localizado com precisão.",
            color=WHITE, font_size=25, line_spacing=1.35
        ).move_to(np.array([0, 0.2, 0]))
        self.play(FadeIn(intro), run_time=1.1)
        self.wait(2.0)
        self.play(FadeOut(intro), run_time=0.7)
        self.wait(0.2)

        largura, altura = 9.5, 3.6
        n_cols, n_rows  = 7, 5
        passo_x = largura / n_cols
        passo_y = altura  / n_rows
        y_base  = -0.65

        grade = VGroup()
        for i in range(n_rows + 1):
            y = y_base - altura / 2 + i * passo_y
            l = Line(LEFT * (largura / 2), RIGHT * (largura / 2),
                     color=COR_GRADE, stroke_width=1.5).set_y(y)
            grade.add(l)
        for j in range(n_cols + 1):
            x = -largura / 2 + j * passo_x
            l = Line(
                np.array([x, y_base - altura / 2, 0]),
                np.array([x, y_base + altura / 2, 0]),
                color=COR_GRADE, stroke_width=1.5
            )
            grade.add(l)

        # Texto da grade no rodapé seguro (sem sobrepor grade nem cabeçalho)
        texto_grade = Text(
            "A grade divide o mapa em células de referência",
            color=COR_GRADE, font_size=21
        ).move_to(np.array([0, Y_RODAPE, 0]))

        self.play(Create(grade), run_time=2.5)
        self.play(Write(texto_grade), run_time=1.2)
        self.wait(1.2)

        # Ponto "Você está aqui" — dentro da grade
        # Grade ocupa x ∈ [-4.75, 4.75]; label fica em x=6.0, fora da grade
        pos_ponto = RIGHT * 1.4 + DOWN * 0.6
        ponto_voce = Dot(pos_ponto, color=COR_LOCAL, radius=0.18)

        label_voce = Text("Você está aqui!", color=COR_LOCAL, font_size=21)
        label_voce.move_to(np.array([5.8, pos_ponto[1], 0]))

        # Seta da borda esquerda do label até o ponto (coordenadas fixas)
        seta_voce = Arrow(
            start=np.array([4.80, pos_ponto[1], 0]),
            end=pos_ponto + RIGHT * 0.22,
            color=COR_DESTAQUE, buff=0, stroke_width=4
        )

        self.play(GrowFromCenter(ponto_voce), run_time=1.0)
        self.play(GrowArrow(seta_voce), Write(label_voce), run_time=1.2)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            grade, texto_grade,
            ponto_voce, seta_voce, label_voce
        )), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 2 — ROSA DOS VENTOS
    # ==================================================================
    def _cena_rosa(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Rosa dos Ventos")

        # Centro bem abaixo do cabeçalho para o título não sobrepor a faixa
        centro = np.array([0, -0.90, 0])
        raio_seta = 1.65

        anel  = Circle(radius=2.0, color=COR_GRADE, stroke_width=2).move_to(centro)
        miolo = Dot(centro, color=COR_LOCAL, radius=0.18)
        self.play(Create(anel), GrowFromCenter(miolo), run_time=1.5)
        self.wait(0.5)

        cardeais = [
            ("N", UP,    COR_DESTAQUE),
            ("S", DOWN,  COR_GRADE),
            ("L", RIGHT, COR_GRADE),
            ("O", LEFT,  COR_GRADE),
        ]

        grupo_cardeais = VGroup()

        for letra, direcao, cor in cardeais:
            seta = Arrow(
                start=centro,
                end=centro + direcao * raio_seta,
                color=cor, buff=0, stroke_width=6,
                max_tip_length_to_length_ratio=0.15
            )
            label = Text(letra, color=cor, font_size=34, weight=BOLD)
            label.move_to(centro + direcao * (raio_seta + 0.38))

            grupo_cardeais.add(seta, label)
            self.play(GrowArrow(seta), Write(label), run_time=0.9)
            self.wait(0.4)

        # Colaterais — traços curtos sem textos que ultrapassem a tela
        dirs_col  = [UR, DR, DL, UL]
        nomes_col = ["NE", "SE", "SO", "NO"]
        grupo_col = VGroup()

        for direcao, nome in zip(dirs_col, nomes_col):
            dn = direcao / np.linalg.norm(direcao)
            traco = Line(
                centro + dn * 1.35,
                centro + dn * 1.75,
                color=GRAY, stroke_width=2
            )
            lbl = Text(nome, color=GRAY, font_size=17)
            lbl.move_to(centro + dn * 2.05)
            grupo_col.add(traco, lbl)

        self.play(Create(grupo_col), run_time=1.2)
        self.wait(0.8)

        sintese = Text(
            "Os pontos cardeais orientam qualquer mapa ou croqui.",
            color=COR_LOCAL, font_size=22
        ).move_to(np.array([0, Y_RODAPE - 0.45, 0]))
        self.play(Write(sintese), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            anel, miolo,
            grupo_cardeais,
            grupo_col, sintese
        )), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 3 — LOCALIZAÇÃO POR COORDENADAS
    # ==================================================================
    def _cena_coordenadas(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Localização por Coordenadas")

        n_col, n_lin = 6, 4
        passo = 0.95
        ox = -(n_col * passo) / 2
        oy = -(n_lin * passo) / 2 - 0.55

        orig = np.array([ox, oy, 0])

        eixo_x = Arrow(orig, orig + RIGHT * (n_col * passo + 0.5),
                       color=COR_GRADE, buff=0, stroke_width=3)
        eixo_y = Arrow(orig, orig + UP * (n_lin * passo + 0.5),
                       color=COR_GRADE, buff=0, stroke_width=3)

        lbl_x = Text("Colunas →", color=COR_GRADE, font_size=19)
        lbl_x.next_to(eixo_x.get_end(), RIGHT, buff=0.08)
        lbl_y = Text("Linhas ↑", color=COR_GRADE, font_size=19)
        lbl_y.next_to(eixo_y.get_end(), UP, buff=0.08)

        self.play(GrowArrow(eixo_x), GrowArrow(eixo_y), run_time=1.2)
        self.play(Write(lbl_x), Write(lbl_y), run_time=0.8)
        self.wait(0.4)

        grade = VGroup()
        nums  = VGroup()

        for c in range(1, n_col + 1):
            xc = ox + c * passo
            l = DashedLine(
                np.array([xc, oy, 0]),
                np.array([xc, oy + n_lin * passo, 0]),
                color=COR_GRADE, stroke_width=1, dash_length=0.12
            )
            grade.add(l)
            n = Text(str(c), color=COR_GRADE, font_size=17)
            n.move_to(np.array([xc, oy - 0.30, 0]))
            nums.add(n)

        for r in range(1, n_lin + 1):
            yr = oy + r * passo
            l = DashedLine(
                np.array([ox, yr, 0]),
                np.array([ox + n_col * passo, yr, 0]),
                color=COR_GRADE, stroke_width=1, dash_length=0.12
            )
            grade.add(l)
            n = Text(str(r), color=COR_GRADE, font_size=17)
            n.move_to(np.array([ox - 0.30, yr, 0]))
            nums.add(n)

        self.play(Create(grade), run_time=1.2)
        self.play(FadeIn(nums), run_time=0.8)
        self.wait(0.5)

        col_alvo, lin_alvo = 4, 3
        pos_estrela = np.array([ox + col_alvo * passo,
                                oy + lin_alvo * passo, 0])
        estrela = Star(n=5, outer_radius=0.24, color=COR_LOCAL, fill_opacity=1)
        estrela.move_to(pos_estrela)
        self.play(GrowFromCenter(estrela), run_time=1.0)
        self.wait(0.4)

        instrucao = Text(
            "Passo 1\nEncontre a COLUNA",
            color=COR_TEXTO, font_size=21
        ).move_to(np.array([5.0, 1.20, 0]))
        self.play(Write(instrucao), run_time=0.9)
        self.wait(0.5)

        guia_col = DashedLine(
            np.array([ox + col_alvo * passo, oy, 0]),
            pos_estrela,
            color=COR_TRAJETO, stroke_width=4
        )
        lbl_col = Text(f"Coluna {col_alvo}", color=COR_TRAJETO,
                       font_size=21, weight=BOLD)
        lbl_col.move_to(np.array([ox + col_alvo * passo, oy - 0.75, 0]))

        self.play(Create(guia_col), Write(lbl_col), run_time=1.2)
        self.wait(0.8)

        instrucao2 = Text(
            "Passo 2\nEncontre a LINHA",
            color=COR_TEXTO, font_size=21
        ).move_to(np.array([5.0, 1.20, 0]))
        self.play(FadeOut(instrucao), Write(instrucao2), run_time=0.9)
        self.wait(0.5)

        guia_lin = DashedLine(
            np.array([ox, oy + lin_alvo * passo, 0]),
            pos_estrela,
            color=COR_DESTAQUE, stroke_width=4
        )
        # Rótulo da linha deslocado para não sobrepor numeração do eixo
        lbl_lin = Text(f"Linha {lin_alvo}", color=COR_DESTAQUE,
                       font_size=21, weight=BOLD)
        lbl_lin.move_to(np.array([ox - 1.05, oy + lin_alvo * passo, 0]))

        self.play(Create(guia_lin), Write(lbl_lin), run_time=1.2)
        self.wait(0.8)

        resultado = Text(
            f"Localização: (Coluna {col_alvo}, Linha {lin_alvo})",
            color=COR_LOCAL, font_size=21, weight=BOLD
        ).move_to(np.array([0, oy - 1.10, 0]))
        self.play(FadeOut(instrucao2), Write(resultado), run_time=1.2)
        self.play(Indicate(estrela, scale_factor=1.8, color=COR_LOCAL), run_time=1.0)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            eixo_x, eixo_y, lbl_x, lbl_y,
            grade, nums, estrela,
            guia_col, lbl_col, guia_lin, lbl_lin,
            resultado
        )), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 4 — MOVIMENTAÇÃO
    # ==================================================================
    def _cena_movimentacao(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Movimentação em Mapas")

        blocos     = self._criar_blocos()
        nomes_ruas = self._criar_ruas()
        labels_ref = self._criar_referencias()
        rosa       = self._criar_rosa()   # canto inferior direito

        self.play(Create(blocos), run_time=1.8)
        self.wait(0.4)
        self.play(FadeIn(nomes_ruas), run_time=0.9)
        self.play(FadeIn(labels_ref, shift=UP * 0.1), run_time=0.9)
        self.wait(0.4)
        self.play(Create(rosa), run_time=1.2)
        self.wait(0.4)

        instrucao_mapa = Text(
            "Observe o mapa antes de iniciar o trajeto.",
            color=COR_TEXTO, font_size=20
        ).move_to(np.array([0, Y_RODAPE, 0]))
        self.play(Write(instrucao_mapa), run_time=0.9)
        self.wait(1.8)
        self.play(FadeOut(instrucao_mapa), run_time=0.6)

        personagem = Dot(self.POS_ESCOLA, color=COR_LOCAL, radius=0.22)
        label_ana  = Text("Ana", color=COR_LOCAL, font_size=20, weight=BOLD)
        label_ana.next_to(personagem, UP, buff=0.14)
        self.play(GrowFromCenter(personagem), FadeIn(label_ana, shift=UP * 0.1), run_time=1.0)
        self.wait(0.8)

        # --- TRECHO 1: Escola → Praça em diagonal SUDESTE ---
        narr1 = Text(
            "Trecho 1 — Ana sai da Escola rumo ao Sudeste até a Praça",
            color=COR_TEXTO, font_size=19
        ).move_to(np.array([0, Y_RODAPE, 0]))
        self.play(Write(narr1), run_time=1.2)
        self.wait(1.0)

        seta_se_rosa = self._rosa_setas["SE"]
        self.play(
            seta_se_rosa.animate.set_color(COR_DESTAQUE).set_stroke(width=6),
            run_time=0.8
        )
        self.wait(0.4)

        dir_se = np.array([1, -1, 0]) / np.sqrt(2)
        seta_dir1 = self._seta_direcional_diag(self.POS_ESCOLA, dir_se)
        self.play(GrowArrow(seta_dir1), run_time=0.8)

        trajeto1 = VMobject(color=COR_TRAJETO, stroke_width=5)
        trajeto1.set_points_as_corners([self.POS_ESCOLA, self.POS_ESCOLA])
        self.add(trajeto1)

        p_ini1 = self.POS_ESCOLA.copy()
        p_fim1 = self.POS_PRACA.copy()

        self.play(
            personagem.animate.move_to(p_fim1),
            UpdateFromAlphaFunc(
                trajeto1,
                lambda m, a: m.set_points_as_corners(
                    [p_ini1, interpolate(p_ini1, p_fim1, a)]
                )
            ),
            run_time=2.5
        )

        label_ana.next_to(personagem, UP, buff=0.14)
        self.play(FadeOut(seta_dir1), run_time=0.5)
        self.wait(1.0)

        self.play(
            seta_se_rosa.animate.set_color(GRAY).set_stroke(width=2),
            FadeOut(narr1),
            run_time=0.8
        )
        self.wait(0.3)

        # --- TRECHO 2: Praça → Biblioteca em diagonal NORDESTE ---
        narr2 = Text(
            "Trecho 2 — Depois segue ao Nordeste até a Biblioteca",
            color=COR_TEXTO, font_size=19
        ).move_to(np.array([0, Y_RODAPE, 0]))
        self.play(Write(narr2), run_time=1.2)
        self.wait(1.0)

        seta_ne_rosa = self._rosa_setas["NE"]
        self.play(
            seta_ne_rosa.animate.set_color(COR_DESTAQUE).set_stroke(width=6),
            run_time=0.8
        )
        self.wait(0.4)

        dir_ne = np.array([1, 1, 0]) / np.sqrt(2)
        seta_dir2 = self._seta_direcional_diag(self.POS_PRACA, dir_ne)
        self.play(GrowArrow(seta_dir2), run_time=0.8)

        trajeto2 = VMobject(color=COR_TRAJETO, stroke_width=5)
        trajeto2.set_points_as_corners([self.POS_PRACA, self.POS_PRACA])
        self.add(trajeto2)

        p_ini2 = self.POS_PRACA.copy()
        p_fim2 = self.POS_BIBLIOTECA.copy()

        self.play(
            personagem.animate.move_to(p_fim2),
            UpdateFromAlphaFunc(
                trajeto2,
                lambda m, a: m.set_points_as_corners(
                    [p_ini2, interpolate(p_ini2, p_fim2, a)]
                )
            ),
            run_time=2.5
        )

        label_ana.next_to(personagem, UP, buff=0.14)
        self.play(FadeOut(seta_dir2), run_time=0.5)

        chegada = Text("Chegou!", color=COR_TRAJETO, font_size=24, weight=BOLD)
        chegada.next_to(personagem, UP, buff=0.40)
        self.play(
            Write(chegada),
            Indicate(personagem, scale_factor=2.0, color=COR_LOCAL),
            run_time=1.0
        )
        self.wait(1.2)

        self.play(
            seta_ne_rosa.animate.set_color(GRAY).set_stroke(width=2),
            FadeOut(narr2),
            run_time=0.8
        )
        self.wait(0.3)

        # --- SÍNTESE ---
        self.play(FadeOut(chegada), run_time=0.5)

        t1  = Text("Trecho 1:", color=COR_TEXTO,   font_size=19, weight=BOLD)
        t1v = Text("Escola → Praça  |  direção: Sudeste",
                   color=COR_TRAJETO, font_size=19)
        t2  = Text("Trecho 2:", color=COR_TEXTO,   font_size=19, weight=BOLD)
        t2v = Text("Praça → Biblioteca  |  direção: Nordeste",
                   color=COR_TRAJETO, font_size=19)

        painel = VGroup(
            VGroup(t1, t1v).arrange(RIGHT, buff=0.3),
            VGroup(t2, t2v).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)

        fundo_painel = SurroundingRectangle(
            painel, color=COR_GRADE, fill_color=BLACK,
            fill_opacity=0.80, buff=0.28, corner_radius=0.15
        )
        painel_grupo = VGroup(fundo_painel, painel)
        painel_grupo.move_to(np.array([0, -2.55, 0]))

        self.play(FadeIn(fundo_painel), run_time=0.6)
        self.play(Write(t1), FadeIn(t1v), run_time=0.9)
        self.play(Write(t2), FadeIn(t2v), run_time=0.9)
        self.wait(1.5)

        regra = Text(
            "Trajetória = partida + direção + chegada",
            color=COR_LOCAL, font_size=20, weight=BOLD
        ).move_to(np.array([0, Y_RODAPE, 0]))

        self.play(FadeOut(painel_grupo), run_time=0.6)
        self.play(Write(regra), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 5 — SÍNTESE FINAL
    # ==================================================================
    def _cena_sintese(self):
        """Síntese dos 4 conceitos antes da logo."""
        faixa, inst, cab, linha_sep = self._cabecalho("O que aprendemos?")

        conceitos = [
            ("Grade de Referência",       "Divide o mapa em células para localizar pontos.",       COR_GRADE),
            ("Rosa dos Ventos",           "Indica os pontos cardeais: N, S, L e O.",               COR_DESTAQUE),
            ("Coordenadas (col, lin)",    "Permitem identificar qualquer posição no mapa.",         COR_LOCAL),
            ("Movimentação e Trajetória", "Descrevemos o caminho usando direção e pontos cardeais.", COR_TRAJETO),
        ]

        cards = VGroup()
        for titulo_c, descricao_c, cor_c in conceitos:
            num_bg = Circle(radius=0.22, fill_color=cor_c, fill_opacity=1,
                            stroke_width=0)
            t_titulo = Text(titulo_c,    color=cor_c,      font_size=20, weight=BOLD)
            t_desc   = Text(descricao_c, color=COR_TEXTO,  font_size=17)
            linha_card = Line(LEFT * 0.01, RIGHT * 0.01, color=cor_c, stroke_width=1.5)
            bloco = VGroup(t_titulo, linha_card, t_desc).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
            card  = VGroup(num_bg, bloco).arrange(RIGHT, buff=0.25)
            cards.add(card)

        cards.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        cards.move_to(np.array([0, 0.0, 0]))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.15), run_time=0.75)
            self.wait(0.5)

        self.wait(1.5)

        fechamento = Text(
            "Localizar e movimentar em mapas é uma habilidade essencial!",
            color=COR_LOCAL, font_size=22, weight=BOLD
        ).move_to(np.array([0, Y_RODAPE, 0]))
        self.play(Write(fechamento), run_time=1.4)
        self.wait(2.5)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 6 — LOGO EMILLY MAYRE
    # ==================================================================
    def _cena_logo(self):
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

    # ==================================================================
    # HELPERS — Cena 4 (Movimentação)
    # ==================================================================

    def _criar_blocos(self):
        posicoes = [
            self.POS_ESCOLA,
            np.array([-3.8, -0.9, 0]),
            np.array([ 0.0,  1.0, 0]),
            self.POS_PRACA,
            self.POS_BIBLIOTECA,
            np.array([ 3.8, -0.9, 0]),
        ]
        blocos = VGroup()
        for pos in posicoes:
            r = Rectangle(
                width=self.BLOCO_W, height=self.BLOCO_H,
                color=COR_GRADE,
                fill_color=BLUE_E, fill_opacity=0.2,
                stroke_width=2
            ).move_to(pos)
            blocos.add(r)
        return blocos

    def _criar_ruas(self):
        rua_h = Text("Rua das Flores", color=GRAY, font_size=14)
        rua_h.move_to(np.array([-1.9, 0.10, 0]))
        rua_v = Text("Av. Central", color=GRAY, font_size=14)
        rua_v.move_to(np.array([ 1.9, 0.10, 0]))
        return VGroup(rua_h, rua_v)

    def _criar_referencias(self):
        refs = VGroup()
        pontos = [
            (self.POS_ESCOLA,     "Escola"),
            (self.POS_PRACA,      "Praça"),
            (self.POS_BIBLIOTECA, "Biblioteca"),
        ]
        for pos, nome in pontos:
            lbl = Text(nome, color=COR_GRADE, font_size=17, weight=BOLD)
            lbl.move_to(pos)
            refs.add(lbl)
        return refs

    def _criar_rosa(self):
        """Rosa dos ventos no canto inferior direito — com cardeais e colaterais."""
        centro_rosa = np.array([5.8, -3.00, 0])
        comprimento = 0.52

        fundo = Circle(
            radius=0.92, color=GRAY,
            fill_color=BLACK, fill_opacity=0.70, stroke_width=1.5
        ).move_to(centro_rosa)

        rosa = VGroup(fundo)
        self._rosa_setas = {}

        # Pontos cardeais
        config_cardeais = [
            ("N", UP,    COR_DESTAQUE, True,  BOLD),
            ("S", DOWN,  GRAY,         False, NORMAL),
            ("L", RIGHT, GRAY,         False, NORMAL),
            ("O", LEFT,  GRAY,         False, NORMAL),
        ]
        for letra, direcao, cor, grossa, peso in config_cardeais:
            espessura = 5 if grossa else 2
            seta = Arrow(
                start=centro_rosa,
                end=centro_rosa + direcao * comprimento,
                color=cor, buff=0, stroke_width=espessura,
                max_tip_length_to_length_ratio=0.30
            )
            lbl = Text(letra, color=cor, font_size=13, weight=peso)
            lbl.move_to(centro_rosa + direcao * (comprimento + 0.20))
            rosa.add(seta, lbl)
            self._rosa_setas[letra] = seta

        # Pontos colaterais — traços e rótulos
        dirs_col  = [UR, DR, DL, UL]
        nomes_col = ["NE", "SE", "SO", "NO"]
        for direcao, nome in zip(dirs_col, nomes_col):
            dn = direcao / np.linalg.norm(direcao)
            traco = Line(
                centro_rosa + dn * 0.36,
                centro_rosa + dn * comprimento,
                color=GRAY, stroke_width=1.5
            )
            lbl_col = Text(nome, color=GRAY, font_size=10)
            lbl_col.move_to(centro_rosa + dn * (comprimento + 0.18))
            rosa.add(traco, lbl_col)
            # Guardar seta colateral como Line animável
            seta_col = Arrow(
                start=centro_rosa,
                end=centro_rosa + dn * comprimento,
                color=GRAY, buff=0, stroke_width=2,
                max_tip_length_to_length_ratio=0.30
            )
            rosa.add(seta_col)
            self._rosa_setas[nome] = seta_col

        titulo_rosa = Text("Rosa dos Ventos", color=GRAY, font_size=9)
        titulo_rosa.next_to(fundo, DOWN, buff=0.05)
        rosa.add(titulo_rosa)

        return rosa

    def _seta_direcional(self, posicao: np.ndarray, direcao: np.ndarray) -> Arrow:
        inicio = posicao + direcao * 0.3 + UP * 0.7
        fim    = posicao + direcao * 0.9 + UP * 0.7
        return Arrow(
            start=inicio, end=fim,
            color=COR_DESTAQUE, buff=0,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.35
        )

    def _seta_direcional_diag(self, posicao: np.ndarray, direcao: np.ndarray) -> Arrow:
        """Seta indicativa de direção diagonal (colateral)."""
        inicio = posicao + direcao * 0.4
        fim    = posicao + direcao * 1.0
        return Arrow(
            start=inicio, end=fim,
            color=COR_DESTAQUE, buff=0,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.35
        )
