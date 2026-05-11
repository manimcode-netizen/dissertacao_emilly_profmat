from manim import *
import numpy as np

# =============================================================================
# PALETA DE CORES — definida globalmente, usada consistentemente
# =============================================================================
COR_2D        = BLUE
COR_3D        = ORANGE
COR_DESTAQUE  = YELLOW
COR_PLANIF    = GREEN
COR_FUNDO     = WHITE
COR_LOGO_A    = "#7B2FBE"
COR_LOGO_B    = "#F4A261"


# =============================================================================
# CLASSE 1 — LOGO Emilly Mayre
# =============================================================================
class _LogoEmillyMayre(Scene):  # prefixo _ evita renderização acidental como cena independente
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


# =============================================================================
# CLASSE 2 — CENA COMPLETA — Descritor D2 + Logo no final
# =============================================================================
class DescritorD2Completo(Scene):
    """
    Conceito: Descritor D2 — Figuras 2D, 3D e Planificações
    Nível: Fundamental II (6º ao 9º ano)
    Objetivo: Identificar propriedades comuns e diferenças entre figuras 2D e 3D,
              relacionando-as com suas planificações.
    Autora: Prof.ª Emilly Mayre
    Versão 2: melhorias aplicadas
    Estrutura: Cenas 0–7 (conteúdo) + Cena 8 (logo, via LogoEmillyMayre)
    """

    def construct(self):

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 0 — Título                                         ║
        # ╚══════════════════════════════════════════════════════════╝
        titulo    = Text("Figuras 2D e 3D", color=COR_DESTAQUE, font_size=52)
        subtitulo = Text("e suas Planificações", color=WHITE, font_size=38)
        descritor = Text("Descritor D2 — Matemática", color=GRAY, font_size=26)
        grupo = VGroup(titulo, subtitulo, descritor).arrange(DOWN, buff=0.5)
        self.play(Write(titulo), run_time=1.5)
        self.play(FadeIn(subtitulo, shift=UP * 0.3), run_time=1)
        self.play(FadeIn(descritor, shift=UP * 0.2), run_time=1)
        self.wait(2)
        self.play(FadeOut(grupo))

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 1 — Figuras 2D                                     ║
        # ║  marcações de lados iguais e ângulos retos               ║
        # ╚══════════════════════════════════════════════════════════╝
        tit1 = Text("Figuras Bidimensionais (2D)", color=COR_2D, font_size=36)
        tit1.to_edge(UP, buff=0.4)
        sub1 = Text("Possuem apenas COMPRIMENTO e LARGURA", color=GRAY, font_size=22)
        sub1.next_to(tit1, DOWN, buff=0.15)
        self.play(Write(tit1), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.8)
        self.wait(0.5)

        # --- Quadrado ---
        pos_quad = LEFT * 4.5 + DOWN * 0.6
        L = 1.6   # lado do quadrado
        quadrado = Square(side_length=L, color=COR_2D, fill_color=COR_2D,
                          fill_opacity=0.25, stroke_width=3)
        quadrado.move_to(pos_quad)
        self.play(Create(quadrado), run_time=1.2)

        # Ângulos retos: quadradinhos nos 4 cantos
        ang_size = 0.18
        cantos = [
            pos_quad + LEFT  * (L / 2) + DOWN * (L / 2),   # inferior-esquerdo
            pos_quad + RIGHT * (L / 2) + DOWN * (L / 2),   # inferior-direito
            pos_quad + RIGHT * (L / 2) + UP   * (L / 2),   # superior-direito
            pos_quad + LEFT  * (L / 2) + UP   * (L / 2),   # superior-esquerdo
        ]
        dirs_ang = [
            (RIGHT, UP),
            (LEFT,  UP),
            (LEFT,  DOWN),
            (RIGHT, DOWN),
        ]
        marcas_angulo = VGroup()
        for canto, (dx, dy) in zip(cantos, dirs_ang):
            p0 = canto
            p1 = canto + dx * ang_size
            p2 = canto + dx * ang_size + dy * ang_size
            p3 = canto + dy * ang_size
            sq = Polygon(p0, p1, p2, p3,
                         color=COR_DESTAQUE, stroke_width=2, fill_opacity=0)
            marcas_angulo.add(sq)

        # Lados iguais: traço duplo no meio de cada lado
        tick_size = 0.12
        lados_meios = [
            pos_quad + DOWN  * (L / 2) + RIGHT * 0,
            pos_quad + UP    * (L / 2) + RIGHT * 0,
            pos_quad + LEFT  * (L / 2) + UP    * 0,
            pos_quad + RIGHT * (L / 2) + UP    * 0,
        ]
        perps_tick = [UP, UP, RIGHT, RIGHT]
        marcas_lados = VGroup()
        for meio, perp_t in zip(lados_meios, perps_tick):
            is_up = np.allclose(perp_t, UP)
            ortogonal = RIGHT if is_up else UP
            for offset in [-0.07, 0.07]:
                t1 = meio + perp_t * tick_size + ortogonal * offset
                t2 = meio - perp_t * tick_size + ortogonal * offset
                tick = Line(t1, t2, color=COR_DESTAQUE, stroke_width=2.5)
                marcas_lados.add(tick)

        lq = Text("Quadrado", color=COR_2D, font_size=20)
        lq.next_to(quadrado, DOWN, buff=0.2)
        pq = Text("4 lados iguais\n4 ângulos retos", color=WHITE, font_size=16)
        pq.next_to(lq, DOWN, buff=0.15)

        self.play(Write(lq), run_time=0.7)
        self.play(LaggedStart(*[Create(m) for m in marcas_angulo], lag_ratio=0.15), run_time=1.0)
        self.play(LaggedStart(*[Create(m) for m in marcas_lados],  lag_ratio=0.08), run_time=0.8)
        self.play(FadeIn(pq), run_time=0.6)
        self.wait(0.5)

        # --- Triângulo ---
        triangulo = Triangle(color=COR_2D, fill_color=COR_2D,
                             fill_opacity=0.25, stroke_width=3).scale(1.1)
        triangulo.move_to(DOWN * 0.6)
        lt  = Text("Triângulo", color=COR_2D, font_size=20).next_to(triangulo, DOWN, buff=0.2)
        pt_ = Text("3 lados\n3 vértices", color=WHITE, font_size=16).next_to(lt, DOWN, buff=0.15)
        self.play(Create(triangulo), run_time=1.2)
        self.play(Write(lt), FadeIn(pt_))
        self.wait(0.4)

        # --- Círculo ---
        circulo = Circle(radius=0.8, color=COR_2D, fill_color=COR_2D,
                         fill_opacity=0.25, stroke_width=3)
        circulo.move_to(RIGHT * 4.5 + DOWN * 0.6)
        lc = Text("Círculo", color=COR_2D, font_size=20).next_to(circulo, DOWN, buff=0.2)
        pc = Text("Sem lados retos\nCurva fechada", color=WHITE, font_size=16)
        pc.next_to(lc, DOWN, buff=0.15)
        self.play(Create(circulo), run_time=1.2)
        self.play(Write(lc), FadeIn(pc))
        self.wait(0.7)

        bx1 = RoundedRectangle(corner_radius=0.15, width=8, height=0.75,
                               color=COR_DESTAQUE, fill_color=COR_DESTAQUE,
                               fill_opacity=0.15, stroke_width=2).to_edge(DOWN, buff=0.3)
        tx1 = Text("✦ Figuras 2D: planas, sem volume, apenas ÁREA",
                   color=COR_DESTAQUE, font_size=20).move_to(bx1.get_center())
        self.play(Create(bx1), Write(tx1), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(VGroup(tit1, sub1, quadrado, marcas_angulo, marcas_lados,
                                  lq, pq, triangulo, lt, pt_,
                                  circulo, lc, pc, bx1, tx1)))

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 2 — Figuras 3D                                     ║
        # ╚══════════════════════════════════════════════════════════╝
        tit2 = Text("Figuras Tridimensionais (3D)", color=COR_3D, font_size=36)
        tit2.to_edge(UP, buff=0.4)
        sub2 = Text("Possuem COMPRIMENTO, LARGURA e ALTURA", color=GRAY, font_size=22)
        sub2.next_to(tit2, DOWN, buff=0.15)
        self.play(Write(tit2), run_time=1.2)
        self.play(FadeIn(sub2), run_time=0.8)
        self.wait(0.5)

        # Cubo isométrico
        s = 0.72
        c_cubo = LEFT * 4.5 + DOWN * 0.5
        def pt2(dx, dy): return c_cubo + RIGHT * dx + UP * dy
        v = {
            'FBL': pt2(-s, 0),   'FBR': pt2(0, -s * 0.5),
            'BBR': pt2(s, 0),    'BBL': pt2(0,  s * 0.5),
            'FTL': pt2(-s, s),   'FTR': pt2(0,  s * 0.5),
            'BTR': pt2(s, s),    'BTL': pt2(0,  s * 1.5),
        }
        f_f = Polygon(v['FBL'], v['FBR'], v['FTR'], v['FTL'],
                      color=COR_3D, fill_color=COR_3D, fill_opacity=0.45, stroke_width=2)
        f_r = Polygon(v['FBR'], v['BBR'], v['BTR'], v['FTR'],
                      color=COR_3D, fill_color=COR_3D, fill_opacity=0.25, stroke_width=2)
        f_t = Polygon(v['FTL'], v['FTR'], v['BTR'], v['BTL'],
                      color=COR_3D, fill_color=COR_3D, fill_opacity=0.60, stroke_width=2)
        l_cubo = Text("Cubo\n6 faces / 8 vértices\n12 arestas", color=COR_3D, font_size=17)
        l_cubo.next_to(VGroup(f_f, f_r, f_t), DOWN, buff=0.25)
        self.play(Create(f_f), Create(f_r), Create(f_t), run_time=1.4)
        self.play(Write(l_cubo))
        self.wait(0.5)

        # Pirâmide de Base Quadrada
        cp = ORIGIN + DOWN * 0.5
        apex = cp + UP * 1.7
        bfl = cp + LEFT * 0.9 + DOWN * 0.35
        bfr = cp + RIGHT * 0.9 + DOWN * 0.35
        btd = cp + RIGHT * 0.3 + DOWN * 1.0
        bte = cp + LEFT  * 0.3 + DOWN * 1.0
        p_base = Polygon(bfl, bfr, btd, bte,
                         color=COR_3D, fill_color=COR_3D, fill_opacity=0.30, stroke_width=2)
        p_ff   = Polygon(bfl, bfr, apex,
                         color=COR_3D, fill_color=COR_3D, fill_opacity=0.50, stroke_width=2)
        p_fr   = Polygon(bfr, btd, apex,
                         color=COR_3D, fill_color=COR_3D, fill_opacity=0.25, stroke_width=2)
        l_pir  = Text("Pirâmide de\nBase Quadrada\n5 faces / 5 vértices\n8 arestas",
                      color=COR_3D, font_size=16)
        l_pir.next_to(VGroup(p_base, p_ff, p_fr), DOWN, buff=0.2)
        self.play(Create(p_base), Create(p_ff), Create(p_fr), run_time=1.4)
        self.play(Write(l_pir))
        self.wait(0.5)

        # Cilindro
        cc    = RIGHT * 4.5 + DOWN * 0.5
        r_c, h_c = 0.65, 1.5
        corp_c = Rectangle(width=r_c * 2, height=h_c,
                           color=COR_3D, fill_color=COR_3D, fill_opacity=0.25, stroke_width=2)
        corp_c.move_to(cc)
        top_c = Ellipse(width=r_c * 2, height=r_c * 0.6,
                        color=COR_3D, fill_color=COR_3D, fill_opacity=0.60, stroke_width=2)
        top_c.move_to(cc + UP * (h_c / 2))
        bas_c = Ellipse(width=r_c * 2, height=r_c * 0.6,
                        color=COR_3D, fill_color=COR_3D, fill_opacity=0.35, stroke_width=2)
        bas_c.move_to(cc + DOWN * (h_c / 2))
        l_cil = Text("Cilindro\n2 bases circulares\n1 lateral", color=COR_3D, font_size=17)
        l_cil.next_to(VGroup(corp_c, top_c, bas_c), DOWN, buff=0.3)
        self.play(Create(corp_c), Create(top_c), Create(bas_c), run_time=1.4)
        self.play(Write(l_cil))
        self.wait(0.7)

        bx2 = RoundedRectangle(corner_radius=0.15, width=9, height=0.75,
                               color=COR_DESTAQUE, fill_color=COR_DESTAQUE,
                               fill_opacity=0.15, stroke_width=2).to_edge(DOWN, buff=0.25)
        tx2 = Text("✦ Figuras 3D: possuem VOLUME e ÁREA SUPERFICIAL",
                   color=COR_DESTAQUE, font_size=20).move_to(bx2.get_center())
        self.play(Create(bx2), Write(tx2), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(VGroup(tit2, sub2, f_f, f_r, f_t, l_cubo,
                                  p_base, p_ff, p_fr, l_pir,
                                  corp_c, top_c, bas_c, l_cil, bx2, tx2)))

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 3 — Comparação 2D × 3D                             ║
        # ╚══════════════════════════════════════════════════════════╝
        tit3 = Text("2D × 3D — Semelhanças e Diferenças", color=WHITE, font_size=34)
        tit3.to_edge(UP, buff=0.4)
        self.play(Write(tit3), run_time=1.2)

        linha3 = Line(UP * 2.6, DOWN * 1.5, color=GRAY, stroke_width=1.5)
        self.play(Create(linha3), run_time=0.7)

        cab2d = Text("2D", color=COR_2D, font_size=30).move_to(LEFT * 3.5 + UP * 2.0)
        self.play(Write(cab2d))
        itens2d = VGroup(*[Text(f"• {t}", color=COR_2D, font_size=19) for t in
            ["Plana (sem profundidade)", "Mede-se ÁREA",
             "Tem: lados e vértices", "Ex: quadrado, triângulo"]]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to(LEFT * 3.5 + DOWN * 0.2)
        for it in itens2d:
            self.play(FadeIn(it, shift=RIGHT * 0.2), run_time=0.5)

        cab3d = Text("3D", color=COR_3D, font_size=30).move_to(RIGHT * 3.5 + UP * 2.0)
        self.play(Write(cab3d))
        itens3d = VGroup(*[Text(f"• {t}", color=COR_3D, font_size=19) for t in
            ["Espacial (com profundidade)", "Mede-se ÁREA e VOLUME",
             "Tem: faces, arestas, vértices", "Ex: cubo, pirâmide de base quadrada"]]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to(RIGHT * 3.0 + DOWN * 0.2)
        for it in itens3d:
            self.play(FadeIn(it, shift=LEFT * 0.2), run_time=0.5)

        tr3 = Text("as FACES de um sólido são figuras 2D!",
                   color=COR_DESTAQUE, font_size=22)
        tr3.move_to(DOWN * 2.6)
        seta_esq3 = Arrow(tr3.get_left() + LEFT * 0.1,
                          tr3.get_left() + LEFT * 1.2,
                          color=COR_DESTAQUE, stroke_width=2, buff=0.05,
                          max_tip_length_to_length_ratio=0.3)
        seta_dir3 = Arrow(tr3.get_right() + RIGHT * 0.1,
                          tr3.get_right() + RIGHT * 1.2,
                          color=COR_DESTAQUE, stroke_width=2, buff=0.05,
                          max_tip_length_to_length_ratio=0.3)
        self.play(Write(tr3), run_time=0.9)
        self.play(Create(seta_esq3), Create(seta_dir3), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(VGroup(tit3, linha3, cab2d, itens2d, cab3d,
                                  itens3d, tr3, seta_esq3, seta_dir3)))

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 4 — Planificação do CUBO                           ║
        # ╚══════════════════════════════════════════════════════════╝
        tit4 = Text("Planificação do Cubo", color=COR_3D, font_size=36)
        tit4.to_edge(UP, buff=0.3)
        self.play(Write(tit4), run_time=1)
        ins4 = Text("Observe as 6 faces se 'abrindo'...", color=GRAY, font_size=22)
        ins4.next_to(tit4, DOWN, buff=0.2)
        self.play(FadeIn(ins4))
        self.wait(0.4)

        s4 = 0.65
        cc4 = LEFT * 3.8 + DOWN * 0.5
        def pt4(dx, dy): return cc4 + RIGHT * dx + UP * dy
        v4 = {
            'FBL': pt4(-s4, 0),       'FBR': pt4(0,  -s4 * 0.5),
            'BBR': pt4(s4,  0),       'BBL': pt4(0,   s4 * 0.5),
            'FTL': pt4(-s4, s4),      'FTR': pt4(0,   s4 * 0.5),
            'BTR': pt4(s4,  s4),      'BTL': pt4(0,   s4 * 1.5),
        }
        cf4 = Polygon(v4['FBL'], v4['FBR'], v4['FTR'], v4['FTL'],
                      color=COR_3D, fill_color=COR_3D, fill_opacity=0.45, stroke_width=2)
        cr4 = Polygon(v4['FBR'], v4['BBR'], v4['BTR'], v4['FTR'],
                      color=COR_3D, fill_color=COR_3D, fill_opacity=0.25, stroke_width=2)
        ct4 = Polygon(v4['FTL'], v4['FTR'], v4['BTR'], v4['BTL'],
                      color=COR_3D, fill_color=COR_3D, fill_opacity=0.60, stroke_width=2)
        lc4 = Text("Cubo", color=COR_3D, font_size=20)
        lc4.next_to(VGroup(cf4, cr4, ct4), DOWN, buff=0.3)
        self.play(Create(cf4), Create(cr4), Create(ct4), Write(lc4), run_time=1.2)
        self.wait(0.7)

        L4   = 0.9
        orig4 = RIGHT * 1.5 + DOWN * 0.5
        pos4  = {'cent': ORIGIN, 'top1': UP * L4, 'top2': UP * 2 * L4,
                 'base': DOWN * L4, 'esq': LEFT * L4, 'dir1': RIGHT * L4}
        cores4 = [COR_3D, BLUE_B, BLUE_D, TEAL, BLUE_E, TEAL_D]
        nomes4 = ['cent', 'top1', 'top2', 'base', 'esq', 'dir1']
        faces4 = []
        seta4  = Text("→ planificação", color=COR_PLANIF, font_size=22)
        seta4.move_to(RIGHT * 0.2 + UP * 2.5)
        self.play(Write(seta4), run_time=0.6)
        src4 = [cf4, ct4, cr4, cf4, cr4, ct4]
        for i, nm in enumerate(nomes4):
            face = Square(side_length=L4, color=WHITE,
                          fill_color=cores4[i], fill_opacity=0.55, stroke_width=2)
            face.move_to(orig4 + pos4[nm])
            faces4.append(face)
            self.play(TransformFromCopy(src4[i], face), run_time=0.6)
        self.wait(0.3)

        lf4  = Text("Planificação", color=COR_PLANIF, font_size=24)
        lf4.next_to(VGroup(*faces4), DOWN, buff=0.3)
        cf4_ = Text("6 quadrados = 6 faces do cubo", color=COR_DESTAQUE, font_size=20)
        cf4_.next_to(lf4, DOWN, buff=0.2)
        self.play(Write(lf4), FadeIn(cf4_), run_time=1)

        for face in faces4:
            self.play(face.animate.set_fill(COR_DESTAQUE, opacity=0.8), run_time=0.18)
            self.play(face.animate.set_fill(face.get_fill_color(), opacity=0.55), run_time=0.18)

        sint4 = Text("Abrindo o cubo → 6 faces quadradas!",
                     color=WHITE, font_size=20).to_edge(DOWN, buff=0.3)
        self.play(Write(sint4), run_time=1.2)
        self.wait(2)
        self.play(FadeOut(VGroup(tit4, ins4, cf4, cr4, ct4, lc4, seta4,
                                  *faces4, lf4, cf4_, sint4)))

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 5 — Planificação da PIRÂMIDE                       ║
        # ╚══════════════════════════════════════════════════════════╝
        tit5 = Text("Planificação da Pirâmide de Base Quadrada",
                    color=COR_3D, font_size=32)
        tit5.to_edge(UP, buff=0.3)
        self.play(Write(tit5), run_time=1)
        ins5 = Text("As 4 faces triangulares se abrem ao redor da base...",
                    color=GRAY, font_size=21)
        ins5.next_to(tit5, DOWN, buff=0.2)
        self.play(FadeIn(ins5))
        self.wait(0.4)

        cp5  = LEFT * 3.8 + DOWN * 0.3
        ap5  = cp5 + UP * 1.7
        bf5e = cp5 + LEFT  * 0.9 + DOWN * 0.35
        bf5d = cp5 + RIGHT * 0.9 + DOWN * 0.35
        bt5d = cp5 + RIGHT * 0.3 + DOWN * 1.0
        bt5e = cp5 + LEFT  * 0.3 + DOWN * 1.0
        pb5  = Polygon(bf5e, bf5d, bt5d, bt5e,
                       color=COR_3D, fill_color=COR_3D, fill_opacity=0.30, stroke_width=2)
        pff5 = Polygon(bf5e, bf5d, ap5,
                       color=COR_3D, fill_color=COR_3D, fill_opacity=0.50, stroke_width=2)
        pfr5 = Polygon(bf5d, bt5d, ap5,
                       color=COR_3D, fill_color=COR_3D, fill_opacity=0.25, stroke_width=2)
        lp5  = Text("Pirâmide de\nBase Quadrada", color=COR_3D, font_size=17)
        lp5.next_to(VGroup(pb5, pff5, pfr5), DOWN, buff=0.3)
        self.play(Create(pb5), Create(pff5), Create(pfr5), Write(lp5), run_time=1.2)
        self.wait(0.7)

        L5 = 1.0; alt5 = 1.1
        cx5 = RIGHT * 1.8 + DOWN * 0.3
        bp5_plan = Square(side_length=L5, color=WHITE, fill_color=BLUE_D,
                          fill_opacity=0.55, stroke_width=2)
        bp5_plan.move_to(cx5)

        def perp5(vec): return np.array([-vec[1], vec[0], 0])
        dirs5  = [UP, DOWN, LEFT, RIGHT]
        cores5 = [TEAL, TEAL_B, TEAL_D, GREEN_B]
        tris5  = []
        seta5  = Text("→ planificação", color=COR_PLANIF, font_size=22)
        seta5.move_to(RIGHT * 0.2 + UP * 2.5)
        self.play(Write(seta5), run_time=0.6)
        self.play(TransformFromCopy(pb5, bp5_plan), run_time=0.9)

        for i, d5 in enumerate(dirs5):
            cl5  = cx5 + d5 * L5 * 0.5
            va5  = cx5 + d5 * (L5 * 0.5 + alt5)
            pd5  = perp5(d5)
            v1_5 = cl5 + pd5 * L5 * 0.5
            v2_5 = cl5 - pd5 * L5 * 0.5
            tri5 = Polygon(v1_5, v2_5, va5, color=WHITE,
                           fill_color=cores5[i], fill_opacity=0.55, stroke_width=2)
            tris5.append(tri5)
            self.play(TransformFromCopy(pff5 if i % 2 == 0 else pfr5, tri5), run_time=0.65)

        lf5 = Text("Planificação", color=COR_PLANIF, font_size=24)
        lf5.next_to(VGroup(bp5_plan, *tris5), DOWN, buff=0.35)
        c5  = Text("1 quadrado + 4 triângulos = 5 faces", color=COR_DESTAQUE, font_size=20)
        c5.next_to(lf5, DOWN, buff=0.2)
        self.play(Write(lf5), FadeIn(c5), run_time=1)
        self.wait(1.5)
        sint5 = Text("Abrindo a pirâmide → 1 quadrado + 4 triângulos!",
                     color=WHITE, font_size=20).to_edge(DOWN, buff=0.3)
        self.play(Write(sint5), run_time=1.2)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 6 — Planificação do CILINDRO                       ║
        # ╚══════════════════════════════════════════════════════════╝
        tit6 = Text("Planificação do Cilindro", color=COR_3D, font_size=36)
        tit6.to_edge(UP, buff=0.3)
        self.play(Write(tit6), run_time=1)
        ins6 = Text("A lateral 'desenrola' formando um retângulo...",
                    color=GRAY, font_size=20)
        ins6.next_to(tit6, DOWN, buff=0.2)
        self.play(FadeIn(ins6))
        self.wait(0.5)

        # Cilindro (lado esquerdo)
        cc6  = LEFT * 3.6 + DOWN * 0.1
        r6   = 0.62
        h6   = 1.9
        corp6 = Rectangle(width=r6 * 2, height=h6,
                           color=COR_3D, fill_color=COR_3D, fill_opacity=0.25, stroke_width=2)
        corp6.move_to(cc6)
        top6 = Ellipse(width=r6 * 2, height=r6 * 0.55,
                       color=COR_3D, fill_color=COR_3D, fill_opacity=0.65, stroke_width=2)
        top6.move_to(cc6 + UP * (h6 / 2))
        bas6 = Ellipse(width=r6 * 2, height=r6 * 0.55,
                       color=COR_3D, fill_color=COR_3D, fill_opacity=0.35, stroke_width=2)
        bas6.move_to(cc6 + DOWN * (h6 / 2))
        lc6 = Text("Cilindro", color=COR_3D, font_size=20)
        lc6.next_to(VGroup(corp6, top6, bas6), DOWN, buff=0.25)
        self.play(Create(corp6), Create(top6), Create(bas6), Write(lc6), run_time=1.2)
        self.wait(0.6)

        # Planificação (lado direito)
        esc6 = 0.60
        w6   = 2 * PI * r6 * esc6
        h6p  = h6 * esc6
        r6p  = r6 * esc6
        cx6  = RIGHT * 1.8 + DOWN * 0.0

        ret6 = Rectangle(width=w6, height=h6p, color=WHITE,
                         fill_color=TEAL_D, fill_opacity=0.6, stroke_width=2)
        ret6.move_to(cx6)

        ct6 = Circle(radius=r6p, color=WHITE, fill_color=BLUE_B,
                     fill_opacity=0.75, stroke_width=2)
        ct6.move_to(cx6 + UP * (h6p / 2 + r6p))

        cb6 = Circle(radius=r6p, color=WHITE, fill_color=BLUE_D,
                     fill_opacity=0.75, stroke_width=2)
        cb6.move_to(cx6 + DOWN * (h6p / 2 + r6p))

        seta6     = Arrow(LEFT * 1.2 + DOWN * 0.1, LEFT * 0.05 + DOWN * 0.1,
                          color=COR_PLANIF, stroke_width=3, buff=0.05)
        txt_seta6 = Text("abre", color=COR_PLANIF, font_size=16)
        txt_seta6.next_to(seta6, UP, buff=0.08)

        self.play(Create(seta6), Write(txt_seta6), run_time=0.7)
        self.play(TransformFromCopy(corp6, ret6), run_time=1.0)
        self.play(TransformFromCopy(top6,  ct6),  run_time=0.8)
        self.play(TransformFromCopy(bas6,  cb6),  run_time=0.8)
        self.wait(0.3)

        lr6  = Text("lateral\n(retângulo)", color=WHITE, font_size=14)
        lr6.move_to(ret6.get_center())
        lct6 = Text("topo", color=WHITE, font_size=13).move_to(ct6.get_center())
        lcb6 = Text("base", color=WHITE, font_size=13).move_to(cb6.get_center())
        self.play(Write(lr6), Write(lct6), Write(lcb6), run_time=0.7)

        planif_grupo6 = VGroup(ret6, ct6, cb6)
        leg6 = VGroup(
            Text("Planificação:",              color=COR_PLANIF,  font_size=20),
            Text("2 círculos + 1 retângulo",   color=COR_DESTAQUE, font_size=18),
            Text("= superfície do cilindro",   color=WHITE,        font_size=17),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        leg6.next_to(planif_grupo6, DOWN, buff=0.30)
        self.play(FadeIn(leg6), run_time=0.9)
        self.wait(1.5)

        sint6 = Text("Abrindo o cilindro → 2 círculos + 1 retângulo!",
                     color=WHITE, font_size=20).to_edge(DOWN, buff=0.3)
        self.play(Write(sint6), run_time=1.2)
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 7 — Resumo                                         ║
        # ╚══════════════════════════════════════════════════════════╝
        tit7 = Text("Resumo — Descritor D2", color=COR_DESTAQUE, font_size=36)
        tit7.to_edge(UP, buff=0.4)
        self.play(Write(tit7), run_time=1)
        self.wait(0.3)

        cab7 = VGroup(
            Text("Sólido 3D",    color=WHITE,      font_size=22),
            Text("→",            color=COR_PLANIF, font_size=22),
            Text("Planificação", color=COR_PLANIF, font_size=22),
        ).arrange(RIGHT, buff=1.2).move_to(UP * 1.8)
        self.play(FadeIn(cab7))
        ls7 = Line(LEFT * 5.5, RIGHT * 5.5, color=GRAY, stroke_width=1.5)
        ls7.next_to(cab7, DOWN, buff=0.2)
        self.play(Create(ls7))

        dados7 = [
            ("Cubo",                      "6 quadrados",                COR_3D),
            ("Pirâmide de Base Quadrada", "1 quadrado + 4 triângulos",  COR_3D),
            ("Cilindro",                  "2 círculos + 1 retângulo",   COR_3D),
        ]
        for i, (sol, pla, cor) in enumerate(dados7):
            y  = 0.7 - i * 1.0
            ts = Text(sol, color=cor,       font_size=19).move_to(LEFT  * 3.2 + UP * y)
            ar = Text("→", color=COR_PLANIF, font_size=21).move_to(LEFT  * 0.2 + UP * y)
            tp = Text(pla, color=WHITE,     font_size=19).move_to(RIGHT * 2.8 + UP * y)
            self.play(FadeIn(ts), FadeIn(ar), FadeIn(tp), run_time=0.7)
            self.wait(0.3)

        bx7 = RoundedRectangle(corner_radius=0.2, width=10, height=1.1,
                               color=COR_DESTAQUE, fill_color=COR_DESTAQUE,
                               fill_opacity=0.12, stroke_width=2).to_edge(DOWN, buff=0.4)
        tx7 = Text("Planificação = sólido 3D 'aberto' em figuras 2D!",
                   color=COR_DESTAQUE, font_size=22).move_to(bx7.get_center())
        self.play(Create(bx7), Write(tx7), run_time=1.2)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects])

        # ╔══════════════════════════════════════════════════════════╗
        # ║  CENA 8 — Logo Emilly Mayre                              ║
        # ╚══════════════════════════════════════════════════════════╝
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

