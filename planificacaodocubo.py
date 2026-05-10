"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Conceito : Planificação do Cubo — dobramento das faces no espaço
Nível    : Ensino Fundamental / Médio
Objetivo : Mostrar como a planificação em cruz se transforma num cubo
           pelo dobramento progressivo das faces, com câmera rotacionando
           para revelar a dimensão emergente.
Paleta   : BLUE, RED, GREEN, YELLOW, ORANGE, WHITE (padrão skill)
=======================================================================
RENDERIZAÇÃO:
  manim -pql planificacao_cubo.py PlanificacaoCubo
  manim -pqh planificacao_cubo.py PlanificacaoCubo
=======================================================================
"""

from manim import *
import numpy as np

# ── Paleta semântica (padrão skill: máx 5 cores) ───────────────────
COR_BASE   = BLUE      # face base (chão)
COR_FRENTE = RED       # face frontal
COR_ESQ    = ORANGE    # face esquerda
COR_DIR    = ORANGE    # face direita
COR_TOPO   = GREEN     # face traseira (sobe junto com tampa)
COR_TAMPA  = YELLOW    # face superior — fecha por último
COR_TEXTO  = WHITE


class PlanificacaoCubo(ThreeDScene):
    """
    Conceito : Planificação do cubo em cruz → dobramento → cubo completo
    Nível    : Ensino Fundamental II / Médio
    Objetivo : Compreender a relação entre planificação plana e sólido 3D,
               rastreando cada face pela sua cor durante o dobramento.
    """

    S = 1.6  # lado de cada face

    def construct(self):
        s = self.S

        # ── ETAPA 1: câmera top-down, planificação em cruz ───────────
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        titulo = Text("Planificação do Cubo", color=COR_TEXTO, font_size=34)
        titulo.to_edge(UP)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo), run_time=1.2)
        self.wait(0.4)

        # Layout da cruz (sem sobreposição):
        #        [tampa]       y = +2s
        #        [topo]        y = +s
        #  [esq] [base] [dir]  y =  0
        #        [frente]      y = -s

        face_base   = self._face(COR_BASE)
        face_frente = self._face(COR_FRENTE)
        face_esq    = self._face(COR_ESQ)
        face_dir    = self._face(COR_DIR)
        face_topo   = self._face(COR_TOPO)
        face_tampa  = self._face(COR_TAMPA)

        face_base  .move_to(np.array([ 0,    0,   0]))
        face_frente.move_to(np.array([ 0,   -s,   0]))
        face_esq   .move_to(np.array([-s,    0,   0]))
        face_dir   .move_to(np.array([ s,    0,   0]))
        face_topo  .move_to(np.array([ 0,    s,   0]))
        face_tampa .move_to(np.array([ 0,   2*s,  0]))

        grupo_plan = VGroup(face_base, face_frente, face_esq,
                            face_dir, face_topo, face_tampa)
        grupo_plan.move_to(ORIGIN + DOWN * 0.3)

        # Mostrar faces sequencialmente
        for f in [face_base, face_topo, face_tampa,
                  face_esq, face_dir, face_frente]:
            self.play(DrawBorderThenFill(f), run_time=0.6)
        self.wait(2.0)

        # ── ETAPA 2: rotacionar câmera revelando 3D ──────────────────
        self.play(FadeOut(titulo), run_time=0.4)
        txt = Text("As faces se dobram...", color=COR_TEXTO, font_size=28)
        txt.to_edge(UP)
        self.add_fixed_in_frame_mobjects(txt)
        self.play(Write(txt), run_time=0.8)
        self.move_camera(phi=55 * DEGREES, theta=-55 * DEGREES, run_time=2.5)
        self.wait(0.8)

        # ── ETAPA 3: dobramento das faces ────────────────────────────
        # Todos os about_points calculados ANTES de qualquer rotação

        # Ponto da aresta inferior da base → face FRENTE sobe
        pt_frente = face_base.get_bottom().copy()

        # Ponto da aresta superior da base → topo+tampa sobem JUNTOS
        pt_topo = face_base.get_top().copy()

        # Aresta esquerda → face ESQ sobe
        pt_esq = face_base.get_left().copy()

        # Aresta direita → face DIR sobe
        pt_dir = face_base.get_right().copy()

        # Face FRENTE sobe
        self.play(
            Rotate(face_frente, angle=PI/2,
                   axis=RIGHT,
                   about_point=pt_frente),
            run_time=1.8
        )
        self.wait(0.5)

        # face TOPO e face TAMPA sobem JUNTAS (VGroup mantém conexão)
        grupo_topo_tampa = VGroup(face_topo, face_tampa)
        self.play(
            Rotate(grupo_topo_tampa, angle=-PI/2,
                   axis=RIGHT,
                   about_point=pt_topo),
            run_time=1.8
        )
        self.wait(0.5)

        # Face ESQ sobe
        self.play(
            Rotate(face_esq, angle=-PI/2,
                   axis=UP,
                   about_point=pt_esq),
            run_time=1.8
        )
        self.wait(0.5)

        # Face DIR sobe
        self.play(
            Rotate(face_dir, angle=PI/2,
                   axis=UP,
                   about_point=pt_dir),
            run_time=1.8
        )
        self.wait(0.5)

        # ── ETAPA 4: TAMPA fecha o cubo ──────────────────────────────
        # Agora a tampa dobra em torno da aresta superior da face_topo
        # já erguida (pt_topo deslocado de s no eixo z)
        self.play(FadeOut(txt), run_time=0.3)
        txt2 = Text("A face superior fecha o cubo.", color=COR_TAMPA, font_size=26)
        txt2.to_edge(UP)
        self.add_fixed_in_frame_mobjects(txt2)
        self.play(Write(txt2), run_time=0.8)

        # Tampa: calcular eixo e sentido corretos a partir dos vértices reais
        corners = face_tampa.get_vertices()
        # Ordenar por z — os dois de MAIOR z são a aresta de conexão com o topo
        sorted_v = sorted(corners, key=lambda v: v[2], reverse=True)
        p1, p2 = sorted_v[0], sorted_v[1]
        pt_tampa = (p1 + p2) / 2
        eixo_tampa = (p2 - p1) / np.linalg.norm(p2 - p1)

        self.play(
            Rotate(face_tampa, angle=-PI/2,
                   axis=eixo_tampa,
                   about_point=pt_tampa),
            run_time=2.2
        )
        self.wait(1.0)

        # ── ETAPA 5: rotação mostrando cubo completo ─────────────────
        self.play(FadeOut(txt2), run_time=0.3)
        txt3 = Text("Cubo completo!", color=YELLOW, font_size=30, weight=BOLD)
        txt3.to_edge(UP)
        self.add_fixed_in_frame_mobjects(txt3)
        self.play(Write(txt3), run_time=0.8)

        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(4.0)
        self.stop_ambient_camera_rotation()

        # ── ETAPA 6: mini planificação no canto ──────────────────────
        self.play(FadeOut(txt3), run_time=0.4)
        mini = self._mini_planificacao(0.30)
        mini.to_corner(DR, buff=0.5)
        mini.shift(LEFT * 1.2)
        leg = Text("Planificação original", color=WHITE, font_size=17)
        leg.next_to(mini, UP, buff=0.12)
        self.add_fixed_in_frame_mobjects(mini, leg)
        self.play(FadeIn(mini), Write(leg), run_time=1.0)

        txt4 = Text("Cada cor corresponde a uma face do cubo.",
                    color=WHITE, font_size=24)
        txt4.to_edge(UP)
        self.add_fixed_in_frame_mobjects(txt4)
        self.play(Write(txt4), run_time=1.2)
        self.wait(3.5)

    # ── Helpers ─────────────────────────────────────────────────────
    def _face(self, cor):
        return Square(
            side_length=self.S,
            color=cor,
            fill_color=cor,
            fill_opacity=0.72,
            stroke_width=2
        )

    def _mini_planificacao(self, s):
        dados = [
            (COR_BASE,   np.array([ 0,    0,  0])),
            (COR_FRENTE, np.array([ 0,   -s,  0])),
            (COR_ESQ,    np.array([-s,    0,  0])),
            (COR_DIR,    np.array([ s,    0,  0])),
            (COR_TOPO,   np.array([ 0,    s,  0])),
            (COR_TAMPA,  np.array([ 0,   2*s, 0])),
        ]
        grupo = VGroup()
        for cor, pos in dados:
            f = Square(side_length=s, color=cor,
                       fill_color=cor, fill_opacity=0.82, stroke_width=1.2)
            f.move_to(pos)
            grupo.add(f)
        return grupo
