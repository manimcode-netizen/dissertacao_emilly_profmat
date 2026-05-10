"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Transformação Homotética e Figuras Semelhantes
Descritor : D7 — SAEB / Matemática / 9º Ano / Ensino Fundamental
Autora    : Prof.ª Emilly Mayre
Fundamento: Phillips, Norris e Macnab (2010)
=======================================================================
LAYOUT SEGURO (sobreposições eliminadas):
  Faixa SAEB  : y ∈ [3.14, 4.00]  → nunca sobrepor
  Título cena : y = 2.65
  Linha sep   : y = 2.20
  Conteúdo    : y ∈ [-2.40, 1.85]
  Rodapé texto: y = -2.85          → margem de segurança
=======================================================================
RENDERIZAÇÃO:
  manim -pqh d7_homotetia.py DescritorD7Completo
=======================================================================
"""

from manim import *
import numpy as np

# -----------------------------------------------------------------------
# CONSTANTES DE LAYOUT
# -----------------------------------------------------------------------
Y_FAIXA_CY  =  3.57
Y_TITULO    =  2.65
Y_LINHA_SEP =  2.20
Y_RODAPE    = -2.85

# -----------------------------------------------------------------------
# PALETA GLOBAL
# COR_ORIGINAL  = BLUE_C  → figura original
# COR_AMPLIADA  = YELLOW  → figura ampliada
# COR_REDUZIDA  = GREEN   → figura reduzida
# COR_DESTAQUE  = RED     → centro de homotetia / ângulos
# COR_TEXTO     = WHITE   → texto geral
# -----------------------------------------------------------------------
COR_ORIGINAL = BLUE_C
COR_AMPLIADA = YELLOW
COR_REDUZIDA = GREEN_C
COR_DESTAQUE = RED
COR_TEXTO    = WHITE


# =======================================================================
# CENA ÚNICA — DescritorD7Completo
# =======================================================================
class DescritorD7Completo(Scene):
    """
    Conceito : D7 — Reconhecer que as imagens de uma figura construída
               por uma transformação homotética são semelhantes,
               identificando propriedades e/ou medidas que se modificam
               ou não se alteram.
    Nível    : Ensino Fundamental II — 9º Ano
    Objetivo : Compreender o que é homotetia, identificar o centro,
               razão de homotetia, e reconhecer semelhança de figuras.
    Autora   : Prof.ª Emilly Mayre
    """

    def construct(self):
        self._cena_abertura()
        self._cena_o_que_e_homotetia()
        self._cena_ampliacao()
        self._cena_reducao()
        self._cena_propriedades()
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

        cab = Text(texto_titulo, color=COR_AMPLIADA, font_size=32, weight=BOLD)
        cab.move_to(np.array([0, Y_TITULO, 0]))

        linha_sep = Line(
            np.array([-6.2, Y_LINHA_SEP, 0]),
            np.array([ 6.2, Y_LINHA_SEP, 0]),
            color=COR_AMPLIADA, stroke_width=1.2
        )

        self.add(faixa, inst)
        self.play(Write(cab), Create(linha_sep), run_time=1.1)
        self.wait(0.3)
        return faixa, inst, cab, linha_sep

    # ==================================================================
    # HELPER — triângulo escalado a partir de vértices base
    # ==================================================================
    def _triangulo(self, vertices, cor, fill_op=0.25, stroke=3):
        return Polygon(*vertices,
                       color=cor,
                       fill_color=cor,
                       fill_opacity=fill_op,
                       stroke_width=stroke)

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
            "Transformação Homotética\ne Figuras Semelhantes",
            color=COR_AMPLIADA, font_size=44, weight=BOLD, line_spacing=1.2
        ).move_to(np.array([0, 0.8, 0]))

        subtitulo = Text(
            "D7 — Como ampliar ou reduzir uma figura mantendo a forma?",
            color=COR_TEXTO, font_size=22
        ).next_to(titulo, DOWN, buff=0.45)

        self.play(Write(titulo), run_time=1.8)
        self.wait(0.2)
        self.play(FadeIn(subtitulo, shift=UP * 0.12), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(VGroup(titulo, subtitulo)), run_time=0.9)
        self.wait(0.2)

        # --- Prévia visual: 3 triângulos LADO A LADO, bem separados ---
        # Posições horizontais: esquerda, centro, direita
        pos_orig = np.array([-4.2,  1.9, 0])
        pos_amp  = np.array([ 0.0,  1.9, 0])
        pos_red  = np.array([ 4.2,  1.9, 0])

        # Triângulo original (tamanho médio)
        v_o = [np.array([-0.55, -0.45, 0]),
               np.array([ 0.55, -0.45, 0]),
               np.array([ 0.0,   0.55, 0])]
        tri_orig = self._triangulo(v_o, COR_ORIGINAL, fill_op=0.35)
        tri_orig.move_to(pos_orig)

        # Triângulo ampliado (maior)
        v_a = [np.array([-1.0, -0.80, 0]),
               np.array([ 1.0, -0.80, 0]),
               np.array([ 0.0,  1.00, 0])]
        tri_amp = self._triangulo(v_a, COR_AMPLIADA, fill_op=0.20)
        tri_amp.move_to(pos_amp)

        # Triângulo reduzido (menor)
        v_r = [np.array([-0.32, -0.28, 0]),
               np.array([ 0.32, -0.28, 0]),
               np.array([ 0.0,   0.34, 0])]
        tri_red = self._triangulo(v_r, COR_REDUZIDA, fill_op=0.45)
        tri_red.move_to(pos_red)

        # Labels posicionados logo abaixo de cada triângulo
        lbl_orig = Text("original",     color=COR_ORIGINAL, font_size=22, weight=BOLD)
        lbl_amp  = Text("ampliada\n(k > 1)", color=COR_AMPLIADA, font_size=22, weight=BOLD, line_spacing=1.1)
        lbl_red  = Text("reduzida\n(0 < k < 1)", color=COR_REDUZIDA, font_size=22, weight=BOLD, line_spacing=1.1)

        lbl_orig.next_to(tri_orig, DOWN, buff=0.35)
        lbl_amp .next_to(tri_amp,  DOWN, buff=0.35)
        lbl_red .next_to(tri_red,  DOWN, buff=0.35)

        box_orig = SurroundingRectangle(lbl_orig, color=COR_ORIGINAL,  fill_color=BLACK, fill_opacity=0.6, buff=0.18, corner_radius=0.10)
        box_amp  = SurroundingRectangle(lbl_amp,  color=COR_AMPLIADA,  fill_color=BLACK, fill_opacity=0.6, buff=0.18, corner_radius=0.10)
        box_red  = SurroundingRectangle(lbl_red,  color=COR_REDUZIDA,  fill_color=BLACK, fill_opacity=0.6, buff=0.18, corner_radius=0.10)

        self.play(Create(tri_orig), run_time=0.9)
        self.play(FadeIn(box_orig), Write(lbl_orig), run_time=0.6)
        self.play(Create(tri_amp),  run_time=1.0)
        self.play(FadeIn(box_amp),  Write(lbl_amp),  run_time=0.6)
        self.play(Create(tri_red),  run_time=0.8)
        self.play(FadeIn(box_red),  Write(lbl_red),  run_time=0.6)
        self.wait(1.5)

        # Lista de tópicos (abaixo das figuras, dentro de um quadro)
        topicos = VGroup(
            Text("1. O que é homotetia e centro de homotetia",   color=WHITE, font_size=20),
            Text("2. Homotetia de ampliação  (k > 1)",           color=WHITE, font_size=20),
            Text("3. Homotetia de redução  (0 < k < 1)",         color=WHITE, font_size=20),
            Text("4. Propriedades: o que muda e o que não muda", color=WHITE, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        topicos.move_to(np.array([0, -2.55, 0]))

        dots_group = VGroup()
        for t in topicos:
            dot = Dot(color=COR_DESTAQUE, radius=0.08).next_to(t, LEFT, buff=0.18)
            dots_group.add(dot)

        box_topicos = SurroundingRectangle(
            VGroup(topicos, dots_group), color=COR_AMPLIADA,
            fill_color=BLUE_E, fill_opacity=0.25, buff=0.22, corner_radius=0.12
        )
        self.play(FadeIn(box_topicos), run_time=0.5)
        for dot, t in zip(dots_group, topicos):
            self.play(FadeIn(dot), Write(t), run_time=0.45)

        self.wait(2.0)
        self.play(FadeOut(VGroup(
            faixa, inst, box_topicos, topicos, dots_group,
            tri_orig, tri_amp, tri_red,
            lbl_orig, lbl_amp, lbl_red,
            box_orig, box_amp, box_red
        )), run_time=1.0)
        self.wait(0.2)

    # ==================================================================
    # CENA 1 — O QUE É HOMOTETIA
    # ==================================================================
    def _cena_o_que_e_homotetia(self):
        faixa, inst, cab, linha_sep = self._cabecalho("O que é Homotetia?")

        # Definição textual curta
        definicao = Text(
            "Homotetia é uma transformação geométrica que\n"
            "amplia ou reduz uma figura a partir de um ponto fixo\n"
            "chamado  Centro de Homotetia  (H).",
            color=COR_TEXTO, font_size=23, line_spacing=1.35
        ).move_to(np.array([0, 0.5, 0]))
        self.play(FadeIn(definicao), run_time=1.4)
        self.wait(2.5)
        self.play(FadeOut(definicao), run_time=0.8)
        self.wait(0.2)

        # --- Ilustração: centro H, ponto A, imagem A' --- DESCIDA para evitar sobreposição
        centro_h = np.array([-3.5, -1.6, 0])
        ponto_a  = np.array([ 0.2,  0.1, 0])
        razao    = 2.0
        ponto_a_linha = centro_h + razao * (ponto_a - centro_h)

        dot_h = Dot(centro_h, color=COR_DESTAQUE, radius=0.18)
        lbl_h = Text("H", color=COR_DESTAQUE, font_size=26, weight=BOLD).next_to(dot_h, DOWN, buff=0.15)

        dot_a = Dot(ponto_a, color=COR_ORIGINAL, radius=0.16)
        # Calcular direção perpendicular à reta para posicionar A abaixo dela
        _dir = (ponto_a - centro_h) / np.linalg.norm(ponto_a - centro_h)
        _perp_down = np.array([-_dir[1], _dir[0], 0])  # perpendicular
        # Colocar A abaixo e levemente à direita do tick, como o H
        lbl_a = Text("A", color=COR_ORIGINAL, font_size=24, weight=BOLD)
        lbl_a.move_to(ponto_a - 0.55 * _perp_down + RIGHT * 0.15)

        dot_al = Dot(ponto_a_linha, color=COR_AMPLIADA, radius=0.16)
        lbl_al = Text("A'", color=COR_AMPLIADA, font_size=24, weight=BOLD).next_to(dot_al, RIGHT, buff=0.15)

        # Reta de homotetia H→A→A'
        reta_homot = Line(
            centro_h - 0.3 * (ponto_a - centro_h) / np.linalg.norm(ponto_a - centro_h),
            ponto_a_linha + 0.3 * (ponto_a - centro_h) / np.linalg.norm(ponto_a - centro_h),
            color=GRAY, stroke_width=1.5, stroke_opacity=0.7
        )

        self.play(GrowFromCenter(dot_h), Write(lbl_h), run_time=1.0)
        self.wait(0.4)
        self.play(Create(reta_homot), run_time=0.9)
        self.play(GrowFromCenter(dot_a), Write(lbl_a), run_time=0.8)
        self.wait(0.4)

        # Seta H→A
        seta_ha = Arrow(centro_h, ponto_a, color=COR_ORIGINAL, buff=0.18, stroke_width=4,
                        max_tip_length_to_length_ratio=0.15)
        # Seta H→A'
        seta_hal = Arrow(centro_h, ponto_a_linha, color=COR_AMPLIADA, buff=0.18, stroke_width=4,
                         max_tip_length_to_length_ratio=0.15)

        narr1 = Text(
            "A reta parte do centro H e passa por A.",
            color=COR_TEXTO, font_size=21
        ).move_to(np.array([0, Y_RODAPE, 0]))
        self.play(GrowArrow(seta_ha), Write(narr1), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(narr1), run_time=0.5)

        narr2 = Text(
            "A imagem A' está na mesma reta, a uma distância\n"
            "k × HA do centro  (aqui k = 2).",
            color=COR_TEXTO, font_size=21, line_spacing=1.3
        ).move_to(np.array([0, Y_RODAPE - 0.3, 0]))
        self.play(GrowArrow(seta_hal), GrowFromCenter(dot_al), Write(lbl_al),
                  Write(narr2), run_time=1.4)
        self.wait(2.0)

        # Segmentos diagonais com labels, alinhados com a reta H→A→A'
        dir_unit = (ponto_a - centro_h) / np.linalg.norm(ponto_a - centro_h)
        perp = np.array([-dir_unit[1], dir_unit[0], 0])  # perpendicular

        # Segmento HA — paralelo à reta, deslocado levemente abaixo
        offset_ha = -0.35 * perp
        p_ha_ini = centro_h + offset_ha
        p_ha_fim = ponto_a  + offset_ha
        seg_ha = Line(p_ha_ini, p_ha_fim, color=COR_ORIGINAL, stroke_width=2.5)
        tick_ha_a = Line(p_ha_ini - 0.1*perp, p_ha_ini + 0.1*perp, color=COR_ORIGINAL, stroke_width=2)
        tick_ha_b = Line(p_ha_fim - 0.1*perp, p_ha_fim + 0.1*perp, color=COR_ORIGINAL, stroke_width=2)
        mid_ha = (p_ha_ini + p_ha_fim) / 2
        t_ha = Text("HA", color=COR_ORIGINAL, font_size=20).move_to(mid_ha - 0.35*perp)

        # Segmento HA' — paralelo à reta, deslocado acima
        offset_hal = 0.35 * perp
        p_hal_ini = centro_h   + offset_hal
        p_hal_fim = ponto_a_linha + offset_hal
        seg_hal = Line(p_hal_ini, p_hal_fim, color=COR_AMPLIADA, stroke_width=2.5)
        tick_hal_a = Line(p_hal_ini - 0.1*perp, p_hal_ini + 0.1*perp, color=COR_AMPLIADA, stroke_width=2)
        tick_hal_b = Line(p_hal_fim - 0.1*perp, p_hal_fim + 0.1*perp, color=COR_AMPLIADA, stroke_width=2)
        mid_hal = (p_hal_ini + p_hal_fim) / 2
        t_hal = Text("HA' = 2·HA", color=COR_AMPLIADA, font_size=20).move_to(mid_hal + 0.38*perp + LEFT * 0.5)

        self.play(FadeOut(narr2), run_time=0.5)
        self.play(
            Create(seg_ha), Create(tick_ha_a), Create(tick_ha_b), Write(t_ha), run_time=0.9
        )
        self.play(
            Create(seg_hal), Create(tick_hal_a), Create(tick_hal_b), Write(t_hal), run_time=0.9
        )
        self.wait(2.5)

        razao_lbl = Text(
            "Razão de homotetia:  k = HA' ÷ HA",
            color=COR_AMPLIADA, font_size=24, weight=BOLD
        ).move_to(np.array([0, Y_RODAPE, 0]))
        self.play(Write(razao_lbl), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            faixa, inst, cab, linha_sep,
            dot_h, lbl_h, dot_a, lbl_a, dot_al, lbl_al,
            reta_homot, seta_ha, seta_hal,
            seg_ha, tick_ha_a, tick_ha_b, t_ha,
            seg_hal, tick_hal_a, tick_hal_b, t_hal,
            razao_lbl
        )), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 2 — HOMOTETIA DE AMPLIAÇÃO (k = 2)
    # ==================================================================
    def _cena_ampliacao(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Homotetia de Ampliação  (k = 2)")

        # Layout seguro: H à esquerda baixo, triângulo original pequeno
        # centrado no meio-esquerda, imagem ampliada à direita — tudo em y ∈ [-3.0, 1.8]
        centro_h = np.array([-6.2, -3.5, 0])
        k = 2.0

        # Triângulo original BEM PEQUENO para a imagem ampliada caber na tela
        v_orig_rel = [np.array([ 0.0,  0.6, 0]),
                      np.array([ 0.45, -0.3, 0]),
                      np.array([-0.45, -0.3, 0])]
        offset_orig = np.array([-3.5, -1.8, 0])
        v_orig = [v + offset_orig for v in v_orig_rel]

        # Imagem ampliada via homotetia
        v_imag = [centro_h + k * (v - centro_h) for v in v_orig]

        tri_orig = self._triangulo(v_orig, COR_ORIGINAL, fill_op=0.35, stroke=3)
        tri_imag = self._triangulo(v_imag, COR_AMPLIADA, fill_op=0.20, stroke=3)

        dot_h = Dot(centro_h, color=COR_DESTAQUE, radius=0.20)
        lbl_h = Text("H", color=COR_DESTAQUE, font_size=26, weight=BOLD).next_to(dot_h, UP, buff=0.12)

        # Labels dos vértices
        lbl_v  = []
        lbl_vi = []
        nomes = ["A", "B", "C"]
        dirs_orig = [UP, DR, DL]
        dirs_imag = [UP, DR, DL]
        for v, vi, n, d_o, d_i in zip(v_orig, v_imag, nomes, dirs_orig, dirs_imag):
            dv  = Dot(v,  color=COR_ORIGINAL, radius=0.11)
            dvi = Dot(vi, color=COR_AMPLIADA,  radius=0.11)
            lv  = Text(n,     color=COR_ORIGINAL, font_size=20, weight=BOLD).next_to(dv,  d_o, buff=0.10)
            lvi = Text(n+"'", color=COR_AMPLIADA,  font_size=20, weight=BOLD).next_to(dvi, d_i, buff=0.10)
            lbl_v.append(VGroup(dv, lv))
            lbl_vi.append(VGroup(dvi, lvi))

        # Quadro intro — canto inferior esquerdo
        intro_txt = Text(
            "Quando k > 1,\na imagem é MAIOR.",
            color=COR_TEXTO, font_size=21, line_spacing=1.2
        )
        intro_txt.move_to(np.array([0.0, -2.8, 0]))
        box_intro = SurroundingRectangle(intro_txt, color=COR_AMPLIADA,
                                         fill_color=BLACK, fill_opacity=0.7,
                                         buff=0.20, corner_radius=0.12)

        self.play(GrowFromCenter(dot_h), Write(lbl_h), run_time=0.9)
        self.wait(0.3)
        self.play(Create(tri_orig), run_time=1.2)
        for g in lbl_v:
            self.play(GrowFromCenter(g[0]), Write(g[1]), run_time=0.4)
        self.play(FadeIn(box_intro), Write(intro_txt), run_time=0.9)
        self.wait(0.8)

        # Retas de homotetia
        retas = VGroup()
        for v, vi in zip(v_orig, v_imag):
            dir_v = vi - centro_h
            dir_v_n = dir_v / np.linalg.norm(dir_v)
            reta = Line(
                centro_h + dir_v_n * 0.22,
                vi + dir_v_n * 0.18,
                color=GRAY, stroke_width=1.2, stroke_opacity=0.6
            )
            retas.add(reta)
        self.play(Create(retas), run_time=1.2)
        self.wait(0.5)

        # Quadro narrativo — canto inferior direito
        self.play(FadeOut(box_intro), FadeOut(intro_txt), run_time=0.4)
        narr_txt = Text(
            "A imagem A'B'C' é construída\nmultiplicando cada distância\nao centro H por k = 2.",
            color=COR_TEXTO, font_size=20, line_spacing=1.25
        )
        narr_txt.move_to(np.array([3.5, -2.2, 0]))
        box_narr = SurroundingRectangle(narr_txt, color=COR_ORIGINAL,
                                        fill_color=BLACK, fill_opacity=0.7,
                                        buff=0.20, corner_radius=0.12)
        self.play(Create(tri_imag), FadeIn(box_narr), Write(narr_txt), run_time=1.5)
        for g in lbl_vi:
            self.play(GrowFromCenter(g[0]), Write(g[1]), run_time=0.35)
        self.wait(2.0)

        # Segmentos comparando lados — alinhados com lado A→B de cada triângulo
        self.play(FadeOut(box_narr), FadeOut(narr_txt), run_time=0.5)
        v_a, v_b   = v_orig[0], v_orig[1]
        vi_a, vi_b = v_imag[0], v_imag[1]

        dir_ab   = (v_b  - v_a)  / np.linalg.norm(v_b  - v_a)
        perp_ab  = np.array([-dir_ab[1],  dir_ab[0],  0])
        dir_iab  = (vi_b - vi_a) / np.linalg.norm(vi_b - vi_a)
        perp_iab = np.array([-dir_iab[1], dir_iab[0], 0])

        off_o = 0.28 * perp_ab
        seg_o_ini = v_a  + off_o; seg_o_fim = v_b  + off_o
        seg_o  = Line(seg_o_ini, seg_o_fim, color=COR_ORIGINAL, stroke_width=2.5)
        tick_oa = Line(seg_o_ini - 0.08*perp_ab, seg_o_ini + 0.08*perp_ab, color=COR_ORIGINAL, stroke_width=2)
        tick_ob = Line(seg_o_fim - 0.08*perp_ab, seg_o_fim + 0.08*perp_ab, color=COR_ORIGINAL, stroke_width=2)
        t_brace_o = Text("lado = 1", color=COR_ORIGINAL, font_size=19).move_to((seg_o_ini+seg_o_fim)/2 + 0.55*perp_ab)

        off_i = 0.30 * perp_iab
        seg_i_ini = vi_a + off_i; seg_i_fim = vi_b + off_i
        seg_i  = Line(seg_i_ini, seg_i_fim, color=COR_AMPLIADA, stroke_width=2.5)
        tick_ia = Line(seg_i_ini - 0.08*perp_iab, seg_i_ini + 0.08*perp_iab, color=COR_AMPLIADA, stroke_width=2)
        tick_ib = Line(seg_i_fim - 0.08*perp_iab, seg_i_fim + 0.08*perp_iab, color=COR_AMPLIADA, stroke_width=2)
        t_brace_i = Text("lado = 2", color=COR_AMPLIADA, font_size=19).move_to((seg_i_ini+seg_i_fim)/2 + 0.55*perp_iab)

        self.play(Create(seg_o), Create(tick_oa), Create(tick_ob), Write(t_brace_o), run_time=0.9)
        self.play(Create(seg_i), Create(tick_ia), Create(tick_ib), Write(t_brace_i), run_time=0.9)
        self.wait(0.5)

        conc_txt = Text(
            "Lados dobraram (k=2),\nângulos iguais!\n→ Figuras SEMELHANTES.",
            color=COR_AMPLIADA, font_size=21, weight=BOLD, line_spacing=1.2
        )
        conc_txt.move_to(np.array([3.5, -2.2, 0]))
        box_conc = SurroundingRectangle(conc_txt, color=COR_AMPLIADA,
                                        fill_color=BLACK, fill_opacity=0.75,
                                        buff=0.20, corner_radius=0.12)
        self.play(FadeIn(box_conc), Write(conc_txt), run_time=1.3)
        self.wait(3.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 3 — HOMOTETIA DE REDUÇÃO (k = 0.5)
    # ==================================================================
    def _cena_reducao(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Homotetia de Redução  (k = 0,5)")

        # Centro H à esquerda, triângulo original à direita (bem separados)
        centro_h = np.array([-5.5, -1.8, 0])
        k = 0.5

        # Triângulo original — posicionado à direita, médio porte
        v_orig_rel = [np.array([ 0.0,  1.6, 0]),
                      np.array([ 1.4, -0.9, 0]),
                      np.array([-1.4, -0.9, 0])]
        offset_orig = np.array([2.2, -0.2, 0])
        v_orig = [v + offset_orig for v in v_orig_rel]

        # Imagem reduzida: cada vértice mais perto de H por fator k=0.5
        v_imag = [centro_h + k * (v - centro_h) for v in v_orig]
        # v_imag fica entre H e v_orig — deveria estar à esquerda de v_orig sem sobrepor

        tri_orig = self._triangulo(v_orig, COR_ORIGINAL, fill_op=0.25, stroke=3)
        tri_imag = self._triangulo(v_imag, COR_REDUZIDA, fill_op=0.45, stroke=3)

        dot_h = Dot(centro_h, color=COR_DESTAQUE, radius=0.20)
        lbl_h = Text("H", color=COR_DESTAQUE, font_size=26, weight=BOLD).next_to(dot_h, UP, buff=0.12)

        lbl_v  = []
        lbl_vi = []
        nomes = ["A", "B", "C"]
        dirs_o = [UP, RIGHT, LEFT]
        dirs_i = [UP, RIGHT, LEFT]
        for v, vi, n, d_o, d_i in zip(v_orig, v_imag, nomes, dirs_o, dirs_i):
            dv  = Dot(v,  color=COR_ORIGINAL, radius=0.11)
            dvi = Dot(vi, color=COR_REDUZIDA,  radius=0.11)
            lv  = Text(n,     color=COR_ORIGINAL, font_size=20, weight=BOLD).next_to(dv,  d_o, buff=0.10)
            lvi = Text(n+"'", color=COR_REDUZIDA,  font_size=20, weight=BOLD).next_to(dvi, d_i, buff=0.10)
            lbl_v.append(VGroup(dv, lv))
            lbl_vi.append(VGroup(dvi, lvi))

        # Quadro de intro — canto inferior direito
        intro_txt = Text(
            "Quando 0 < k < 1,\na imagem é MENOR.",
            color=COR_TEXTO, font_size=21, line_spacing=1.2
        )
        intro_txt.move_to(np.array([5.0, -2.0, 0]))
        box_intro = SurroundingRectangle(intro_txt, color=COR_REDUZIDA,
                                         fill_color=BLACK, fill_opacity=0.7,
                                         buff=0.20, corner_radius=0.12)

        self.play(GrowFromCenter(dot_h), Write(lbl_h), run_time=0.9)
        self.play(Create(tri_orig), run_time=1.2)
        for g in lbl_v:
            self.play(GrowFromCenter(g[0]), Write(g[1]), run_time=0.38)
        self.play(FadeIn(box_intro), Write(intro_txt), run_time=0.9)
        self.wait(0.8)

        # Retas de homotetia H → imagem (k=0.5 → imagem entre H e original)
        retas = VGroup()
        for v, vi in zip(v_orig, v_imag):
            dir_v = v - centro_h
            dir_v_n = dir_v / np.linalg.norm(dir_v)
            reta = Line(
                centro_h + dir_v_n * 0.22,
                v + dir_v_n * 0.14,
                color=GRAY, stroke_width=1.2, stroke_opacity=0.6
            )
            retas.add(reta)
        self.play(Create(retas), run_time=1.1)

        # Cria triângulo imagem
        self.play(FadeOut(box_intro), FadeOut(intro_txt), run_time=0.4)
        narr_txt = Text(
            "A imagem A'B'C' tem cada\ndistância ao centro H\nmultiplicada por k = 0,5.",
            color=COR_TEXTO, font_size=20, line_spacing=1.25
        )
        narr_txt.move_to(np.array([4.2, -2.2, 0]))
        box_narr = SurroundingRectangle(narr_txt, color=COR_ORIGINAL,
                                        fill_color=BLACK, fill_opacity=0.7,
                                        buff=0.20, corner_radius=0.12)
        self.play(Create(tri_imag), FadeIn(box_narr), Write(narr_txt), run_time=1.5)
        for g in lbl_vi:
            self.play(GrowFromCenter(g[0]), Write(g[1]), run_time=0.35)
        self.wait(2.0)
        self.play(FadeOut(box_narr), FadeOut(narr_txt), run_time=0.5)

        # Braces comparando bases — ambos embaixo, mesmo padrão
        v_b1, v_b2   = v_orig[1], v_orig[2]
        vi_b1, vi_b2 = v_imag[1], v_imag[2]
        brace_orig = BraceBetweenPoints(v_b2, v_b1, direction=DOWN, color=COR_ORIGINAL)
        t_orig = Text("base = 2", color=COR_ORIGINAL, font_size=19).next_to(brace_orig, DOWN, buff=0.12)
        brace_imag = BraceBetweenPoints(vi_b2, vi_b1, direction=DOWN, color=COR_REDUZIDA)
        t_imag = Text("base = 1", color=COR_REDUZIDA, font_size=19).next_to(brace_imag, DOWN, buff=0.12)

        self.play(Create(brace_orig), Write(t_orig), run_time=0.9)
        self.play(Create(brace_imag), Write(t_imag), run_time=0.9)
        self.wait(0.5)

        conc_txt = Text(
            "Lados reduzidos à metade,\nângulos iguais!\n→ Figuras SEMELHANTES.",
            color=COR_REDUZIDA, font_size=21, weight=BOLD, line_spacing=1.2
        )
        conc_txt.move_to(np.array([2.5, -3.0, 0]))
        box_conc = SurroundingRectangle(conc_txt, color=COR_REDUZIDA,
                                        fill_color=BLACK, fill_opacity=0.75,
                                        buff=0.20, corner_radius=0.12)
        self.play(FadeIn(box_conc), Write(conc_txt), run_time=1.3)
        self.wait(3.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 4 — PROPRIEDADES (O QUE MUDA / O QUE NÃO MUDA)
    # ==================================================================
    def _cena_propriedades(self):
        faixa, inst, cab, linha_sep = self._cabecalho("Propriedades da Homotetia")

        # --- Título da tabela ---
        titulo_tabela = Text(
            "Na homotetia, o que se modifica e o que não se altera?",
            color=COR_TEXTO, font_size=22
        ).move_to(np.array([0, 1.70, 0]))
        self.play(Write(titulo_tabela), run_time=1.0)
        self.wait(0.5)

        # --- Dois painéis lado a lado ---
        # Painel ESQUERDO: O que NÃO muda
        rect_nao = Rectangle(width=5.8, height=3.2, color=COR_REDUZIDA,
                             fill_color=DARK_GRAY, fill_opacity=0.7, stroke_width=2)
        rect_nao.move_to(np.array([-3.2, -0.5, 0]))

        titulo_nao = Text("✓  NÃO se altera", color=COR_REDUZIDA, font_size=22, weight=BOLD)
        titulo_nao.next_to(rect_nao, UP, buff=0.12)

        itens_nao = VGroup(
            Text("• Forma da figura",         color=WHITE, font_size=20),
            Text("• Ângulos internos",         color=WHITE, font_size=20),
            Text("• Proporcionalidade dos\n  lados correspondentes", color=WHITE, font_size=20, line_spacing=1.1),
            Text("• Paralelismo dos lados",    color=WHITE, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        itens_nao.move_to(rect_nao.get_center())

        # Painel DIREITO: O que MUDA
        rect_sim = Rectangle(width=5.8, height=3.2, color=COR_AMPLIADA,
                             fill_color=DARK_GRAY, fill_opacity=0.7, stroke_width=2)
        rect_sim.move_to(np.array([ 3.2, -0.5, 0]))

        titulo_sim = Text("✗  SE MODIFICA", color=COR_AMPLIADA, font_size=22, weight=BOLD)
        titulo_sim.next_to(rect_sim, UP, buff=0.12)

        itens_sim = VGroup(
            Text("• Comprimento dos lados",    color=WHITE, font_size=20),
            Text("• Área (muda por k²)",        color=WHITE, font_size=20),
            Text("• Perímetro (muda por k)",    color=WHITE, font_size=20),
            Text("• Tamanho geral da figura",  color=WHITE, font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        itens_sim.move_to(rect_sim.get_center())

        self.play(Create(rect_nao), Create(rect_sim), run_time=1.2)
        self.play(Write(titulo_nao), Write(titulo_sim), run_time=0.9)
        self.wait(0.3)

        for item_n, item_s in zip(itens_nao, itens_sim):
            self.play(FadeIn(item_n, shift=RIGHT * 0.12),
                      FadeIn(item_s, shift=LEFT  * 0.12), run_time=0.70)
            self.wait(0.35)

        self.wait(1.5)

        # --- Destaque: figuras semelhantes ---
        conc = Text(
            "Figuras obtidas por homotetia são SEMELHANTES:\n"
            "mesma forma, tamanhos proporcionais.",
            color=COR_AMPLIADA, font_size=22, weight=BOLD, line_spacing=1.3
        ).move_to(np.array([0, Y_RODAPE - 0.2, 0]))
        box_conc = SurroundingRectangle(conc, color=COR_AMPLIADA,
                                        fill_color=BLACK, fill_opacity=0.75,
                                        buff=0.20, corner_radius=0.15)
        self.play(FadeIn(box_conc), Write(conc), run_time=1.4)
        self.wait(3.0)

        self.play(FadeOut(*self.mobjects), run_time=1.0)
        self.wait(0.3)

    # ==================================================================
    # CENA 5 — SÍNTESE FINAL
    # ==================================================================
    def _cena_sintese(self):
        faixa, inst, cab, linha_sep = self._cabecalho("O que aprendemos?")

        conceitos = [
            ("Homotetia",
             "Transf. que amplia/reduz a partir do centro H com razão k.",
             COR_ORIGINAL),
            ("Ampliação  (k > 1)",
             "A imagem é maior; lados × k, área × k².",
             COR_AMPLIADA),
            ("Redução  (0 < k < 1)",
             "A imagem é menor; lados × k, área × k².",
             COR_REDUZIDA),
            ("Semelhança",
             "Figuras homotéticas têm mesma forma e ângulos iguais.",
             COR_DESTAQUE),
        ]

        cards = VGroup()
        for titulo_c, descricao_c, cor_c in conceitos:
            num_bg = Circle(radius=0.20, fill_color=cor_c, fill_opacity=1, stroke_width=0)
            t_titulo = Text(titulo_c,    color=cor_c,     font_size=20, weight=BOLD)
            t_desc   = Text(descricao_c, color=COR_TEXTO, font_size=17)
            linha_card = Line(LEFT * 0.01, RIGHT * 0.01, color=cor_c, stroke_width=1.5)
            bloco = VGroup(t_titulo, linha_card, t_desc).arrange(DOWN, buff=0.10, aligned_edge=LEFT)
            card  = VGroup(num_bg, bloco).arrange(RIGHT, buff=0.25)
            cards.add(card)

        cards.arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        cards.move_to(np.array([0, 0.0, 0]))

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.15), run_time=0.75)
            self.wait(0.4)

        self.wait(1.5)

        fechamento = Text(
            "Reconhecer homotetia é essencial para entender semelhança!",
            color=COR_AMPLIADA, font_size=22, weight=BOLD
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
