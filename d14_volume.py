"""
=======================================================================
ANIMAÇÃO EDUCACIONAL – MANIM COMMUNITY EDITION
=======================================================================
Título    : Descritor D14 – Resolver Problemas Envolvendo Noções de Volume
Nível     : Ensino Fundamental – 9º Ano
Contexto  : SAEB (Sistema de Avaliação da Educação Básica)
Uso       : Dissertação de Mestrado Profissional em Matemática
Fundamento: Phillips, Norris e Macnab (2010) – princípios de visualização
            matemática eficaz para aprendizagem
=======================================================================

CENAS (renderizar individualmente ou em sequência):
  1. Abertura              – Apresentação do descritor D14
  2. CenaConceito          – O que é volume? Intuição geométrica
  3. CenaFormula           – Fórmula V = c × l × h e sua derivação visual
  4. CenaUnidades          – Conversão entre unidades de volume
  5. CenaProblema1         – Problema: caixa d'água paralelepípedo
  6. CenaProblema2         – Problema: cubinhos dentro de embalagem
  7. Encerramento          – Síntese e mapa conceitual

RENDERIZAÇÃO:
  # Teste rápido (480p)
  manim -pql d14_volume_mestrado.py Abertura

  # Alta qualidade para dissertação (1080p)
  manim -pqh d14_volume_mestrado.py Abertura

  # Renderizar todas as cenas em sequência (PowerShell):
  foreach ($c in @("Abertura","CenaConceito","CenaFormula","CenaUnidades",
    "CenaProblema1","CenaProblema2","Encerramento")) {
      manim -pqh d14_volume_mestrado.py $c }
=======================================================================
"""

from manim import *

# =======================================================================
# PALETA SEMÂNTICA GLOBAL (uso consistente em todas as cenas)
# =======================================================================
# COR_TITULO    YELLOW   → títulos e cabeçalhos
# COR_SOLIDO    BLUE_D   → faces dos sólidos geométricos
# COR_ARESTA    WHITE    → arestas e contornos
# COR_FORMULA   GREEN_B  → fórmulas e resultados finais
# COR_DESTAQUE  ORANGE   → medidas, valores numéricos e alertas


def make_parallelpiped(cx, cy, cz, ox=0, oy=0,
                       face_color=BLUE_D, edge_color=WHITE,
                       face_opacity=0.55):
    """
    Constrói um paralelepípedo 2-D com projeção isométrica simplificada.
    Parâmetros:
        cx, cy, cz : dimensões (comprimento, altura, profundidade isométrica)
        ox, oy     : deslocamento de origem no plano
        face_color : cor das faces principais
        edge_color : cor das arestas
        face_opacity: opacidade das faces
    Retorna VGroup com face_frontal, face_topo, face_lateral.
    """
    # Vértices da face frontal
    A = np.array([ox - cx/2, oy - cy/2, 0])
    B = np.array([ox + cx/2, oy - cy/2, 0])
    C = np.array([ox + cx/2, oy + cy/2, 0])
    D = np.array([ox - cx/2, oy + cy/2, 0])
    # Offset isométrico (simula profundidade)
    iso = np.array([cz * 0.55, cz * 0.55, 0])

    face_frontal = Polygon(
        A, B, C, D,
        fill_color=face_color,
        fill_opacity=face_opacity,
        stroke_color=edge_color,
        stroke_width=2.2
    )
    face_topo = Polygon(
        D, C, C + iso, D + iso,
        fill_color=interpolate_color(face_color, WHITE, 0.3),
        fill_opacity=face_opacity - 0.05,
        stroke_color=edge_color,
        stroke_width=2.2
    )
    face_lateral = Polygon(
        B, B + iso, C + iso, C,
        fill_color=interpolate_color(face_color, BLACK, 0.25),
        fill_opacity=face_opacity + 0.05,
        stroke_color=edge_color,
        stroke_width=2.2
    )
    return VGroup(face_frontal, face_topo, face_lateral), (A, B, C, D, iso)


# =======================================================================
# CENA 1 – ABERTURA
# Objetivo pedagógico: situar o aluno no contexto avaliativo e temático
# =======================================================================
class Abertura(Scene):
    """
    Conceito : Contextualização do Descritor D14 – SAEB
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Apresentar o tema, o contexto avaliativo e a estrutura
               da animação ao aluno.
    """

    def construct(self):
        # --- Faixa superior de identificação institucional ---
        faixa = Rectangle(
            width=14, height=1.1,
            fill_color=BLUE_E, fill_opacity=1,
            stroke_width=0
        ).to_edge(UP, buff=0)

        inst = Text(
            "SAEB  ·  Matemática  ·  9º Ano  ·  Ensino Fundamental",
            color=WHITE, font_size=22
        ).move_to(faixa.get_center())

        self.add(faixa, inst)

        # --- Título central ---
        titulo_d14 = Text(
            "Descritor D14",
            color=YELLOW, font_size=52, weight=BOLD
        ).move_to(UP * 2.0)  # subido de 1.2 → 2.0

        subtitulo = Text(
            "Resolver problemas envolvendo\nnoções de volume",
            color=WHITE, font_size=32, line_spacing=1.3
        ).next_to(titulo_d14, DOWN, buff=0.45)

        self.play(Write(titulo_d14), run_time=1.8)
        self.wait(0.4)
        self.play(FadeIn(subtitulo, shift=UP * 0.2), run_time=1.4)
        self.wait(1.2)

        # --- Linha separadora ---
        linha = Line(LEFT * 5, RIGHT * 5, color=YELLOW, stroke_width=1.5)
        linha.next_to(subtitulo, DOWN, buff=0.5)
        self.play(Create(linha), run_time=1.0)

        # --- Índice de cenas ---
        topicos = VGroup(
            Text("1. O que é Volume?",                color=WHITE, font_size=24),
            Text("2. Fórmula do Paralelepípedo",      color=WHITE, font_size=24),
            Text("3. Unidades de Medida de Volume",   color=WHITE, font_size=24),
            Text("4. Problema: Caixa d'água",         color=WHITE, font_size=24),
            Text("5. Problema: Cubos na embalagem",   color=WHITE, font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        topicos.next_to(linha, DOWN, buff=0.15)  # reduzido de 0.35 → 0.15
        topicos.shift(LEFT * 0.3)

        # Marcadores coloridos à esquerda de cada tópico
        dots_group = VGroup()
        for i, t in enumerate(topicos):
            dot = Dot(color=ORANGE, radius=0.07).next_to(t, LEFT, buff=0.18)
            dots_group.add(dot)
            self.play(FadeIn(dot), Write(t), run_time=0.6)

        self.wait(2.5)
        self.play(FadeOut(VGroup(titulo_d14, subtitulo, linha, topicos, dots_group)), run_time=1.2)


# =======================================================================
# CENA 2 – CONCEITO DE VOLUME
# Objetivo pedagógico: construir intuição sobre volume como
#                      "quantidade de espaço ocupado por um sólido"
# =======================================================================
class CenaConceito(Scene):
    """
    Conceito : O que é volume?
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Construir a intuição de volume por meio da
               visualização do preenchimento de um sólido
               com unidades cúbicas.
    """

    def construct(self):
        # --- Cabeçalho fixo ---
        cab = Text("O que é Volume?", color=YELLOW, font_size=36, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.5, RIGHT * 5.5, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- ETAPA 1: definição textual ---
        definicao = Text(
            "Volume é a medida do espaço\nocupado por um sólido geométrico.",
            color=WHITE, font_size=28, line_spacing=1.35
        ).next_to(linha_cab, DOWN, buff=0.45)

        self.play(FadeIn(definicao, shift=UP * 0.15), run_time=1.4)
        self.wait(1.8)
        self.play(FadeOut(definicao), run_time=0.8)

        # --- ETAPA 2: cubo unitário ---
        label_unit = Text(
            "Unidade de volume: o cubo unitário (1 × 1 × 1)",
            color=WHITE, font_size=26
        ).next_to(linha_cab, DOWN, buff=0.45)
        self.play(FadeIn(label_unit), run_time=1.0)
        self.wait(0.5)

        # Cubo unitário pequeno à esquerda
        cubo_unit, _ = make_parallelpiped(
            0.55, 0.55, 0.22,
            ox=-3.8, oy=-0.5,
            face_color=ORANGE,
            face_opacity=0.8
        )
        self.play(DrawBorderThenFill(cubo_unit[0]), run_time=0.8)
        self.play(DrawBorderThenFill(cubo_unit[1]), run_time=0.6)
        self.play(DrawBorderThenFill(cubo_unit[2]), run_time=0.6)
        rot_label = MathTex("1 \\times 1 \\times 1 = 1\\,u^3",
                            color=ORANGE, font_size=28)
        rot_label.next_to(cubo_unit, RIGHT, buff=0.35)
        self.play(Write(rot_label), run_time=1.0)
        self.wait(1.2)

        # --- ETAPA 3: empilhar 4 cubos para mostrar volume crescente ---
        empilha_label = Text(
            "Empilhando cubos unitários → o volume aumenta",
            color=WHITE, font_size=24
        ).next_to(label_unit, DOWN, buff=0.35)
        self.play(Write(empilha_label), run_time=1.0)
        self.wait(0.5)

        # Cria 4 cubos posicionados em linha
        cubos = VGroup()
        for i in range(4):
            c, _ = make_parallelpiped(
                0.5, 0.5, 0.20,
                ox=0.3 + i * 0.75, oy=-0.8,
                face_color=BLUE_D,
                face_opacity=0.7
            )
            cubos.add(c)
            self.play(DrawBorderThenFill(c[0]),
                      DrawBorderThenFill(c[1]),
                      DrawBorderThenFill(c[2]), run_time=0.5)

        contagem = MathTex("V = 4\\,u^3", color=GREEN_B, font_size=34)
        contagem.next_to(cubos, DOWN, buff=0.35)
        self.play(Write(contagem), run_time=1.0)
        self.wait(1.5)

        # --- Limpa tela ---
        self.play(
            FadeOut(VGroup(label_unit, empilha_label,
                           cubo_unit, rot_label, cubos, contagem)),
            run_time=1.0
        )

        # --- ETAPA 4: ideia central ---
        ideia = Text(
            "Volume = quantidade de cubos unitários\nque preenchem o sólido sem folgas.",
            color=GREEN_B, font_size=28, line_spacing=1.35
        ).next_to(linha_cab, DOWN, buff=0.5)
        caixa_ideia = SurroundingRectangle(ideia, color=GREEN_B, buff=0.25, corner_radius=0.12)
        self.play(FadeIn(ideia), Create(caixa_ideia), run_time=1.4)
        self.wait(2.5)
        self.play(FadeOut(VGroup(ideia, caixa_ideia, cab, linha_cab)), run_time=1.0)


# =======================================================================
# CENA 3 – FÓRMULA DO PARALELEPÍPEDO
# Objetivo pedagógico: derivar visualmente V = c × l × h a partir
#                      da área da base multiplicada pela altura
# =======================================================================
class CenaFormula(Scene):
    """
    Conceito : Fórmula do volume do paralelepípedo retangular
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Demonstrar que V = comprimento × largura × altura
               é uma generalização do preenchimento por camadas.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Fórmula do Volume do Paralelepípedo",
                   color=YELLOW, font_size=32, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.8, RIGHT * 5.8, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- ETAPA 1: área da base ---
        passo1 = Text("Passo 1 — Área da base (retângulo)",
                      color=WHITE, font_size=26)
        passo1.next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(passo1), run_time=1.0)
        self.wait(0.5)

        base = Rectangle(
            width=3.2, height=1.8,
            fill_color=BLUE_D, fill_opacity=0.5,
            stroke_color=WHITE, stroke_width=2
        ).move_to(DOWN * 0.8 + LEFT * 2.5)

        label_c = MathTex("c", color=ORANGE, font_size=30)
        label_c.next_to(base, DOWN, buff=0.18)
        label_l = MathTex("l", color=ORANGE, font_size=30)
        label_l.next_to(base, LEFT, buff=0.18)

        formula_base = MathTex(
            r"A_{\text{base}} = c \times l",
            color=GREEN_B, font_size=34
        ).move_to(DOWN * 0.8 + RIGHT * 2.0)

        self.play(DrawBorderThenFill(base), run_time=1.2)
        self.play(Write(label_c), Write(label_l), run_time=0.8)
        self.play(Write(formula_base), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(VGroup(passo1, base, label_c, label_l, formula_base)),
                  run_time=0.8)

        # --- ETAPA 2: empilhar camadas até altura h ---
        passo2 = Text("Passo 2 — Empilhar camadas até a altura h",
                      color=WHITE, font_size=26)
        passo2.next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(passo2), run_time=1.0)
        self.wait(0.5)

        solido, (A, B, C, D, iso) = make_parallelpiped(
            2.8, 1.6, 0.7,
            ox=-1.8, oy=-0.8,
            face_color=BLUE_D,
            face_opacity=0.55
        )
        self.play(DrawBorderThenFill(solido[0]), run_time=1.0)
        self.play(
            DrawBorderThenFill(solido[1]),
            DrawBorderThenFill(solido[2]),
            run_time=1.0
        )
        self.wait(0.5)

        # Labels posicionados sobre as arestas corretas da projeção isométrica
        # c (comprimento) → aresta inferior da face frontal (horizontal, abaixo de A-B)
        mid_AB = (A + B) / 2
        med_c = MathTex("c", color=ORANGE, font_size=32)
        med_c.move_to(mid_AB + DOWN * 0.35)

        # h (altura) → aresta esquerda da face frontal (vertical, à esquerda de A-D)
        mid_AD = (A + D) / 2
        med_h = MathTex("h", color=ORANGE, font_size=32)
        med_h.move_to(mid_AD + LEFT * 0.35)

        # l (largura/profundidade) → aresta inferior da face lateral diagonal (B → B+iso)
        mid_B_Biso = (B + (B + iso)) / 2
        med_l = MathTex("l", color=ORANGE, font_size=32)
        med_l.move_to(mid_B_Biso + DOWN * 0.32 + RIGHT * 0.15)

        self.play(Write(med_c), Write(med_h), Write(med_l), run_time=0.8)
        self.wait(0.8)

        # --- ETAPA 3: fórmula completa ---
        formula_completa = MathTex(
            r"V = c \times l \times h",
            color=GREEN_B, font_size=42
        ).move_to(RIGHT * 3.5 + DOWN * 0.8)

        self.play(Write(formula_completa), run_time=1.4)

        box_f = SurroundingRectangle(formula_completa, color=GREEN_B,
                                      buff=0.22, corner_radius=0.1)
        self.play(Create(box_f), run_time=0.8)
        self.wait(1.5)

        # --- ETAPA 4: leitura da fórmula ---
        self.play(
            FadeOut(VGroup(passo2, solido, med_c, med_h, med_l, box_f)),
            run_time=0.8
        )
        formula_completa.generate_target()
        formula_completa.target.move_to(UP * 0.5)
        self.play(MoveToTarget(formula_completa), run_time=0.8)

        leitura = VGroup(
            Text("c  =  comprimento   (base)", color=ORANGE, font_size=26),
            Text("l   =  largura", color=ORANGE, font_size=26),
            Text("h  =  altura", color=ORANGE, font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        leitura.next_to(formula_completa, DOWN, buff=0.45)

        for linha in leitura:
            self.play(FadeIn(linha, shift=RIGHT * 0.2), run_time=0.7)

        self.wait(2.5)
        self.play(FadeOut(VGroup(cab, linha_cab, formula_completa, leitura)),
                  run_time=1.0)
# =======================================================================
# CENA 4 – UNIDADES DE VOLUME
# Objetivo pedagógico: apresentar as unidades mais utilizadas e
#                      a relação 1 dm³ = 1 L = 1 000 cm³
# =======================================================================
class CenaUnidades(Scene):
    """
    Conceito : Unidades de medida de volume e conversão
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Compreender as unidades m³, dm³, cm³, mm³ e L,
               e as relações de conversão entre elas.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Unidades de Medida de Volume",
                   color=YELLOW, font_size=34, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.5, RIGHT * 5.5, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- ETAPA 1: tabela de unidades ---
        dados = [
            ("Unidade",            "Símbolo",  "Relação"),
            ("Metro cúbico",       r"m^3",     r"= 1\,000\,dm^3"),
            ("Decímetro cúbico",   r"dm^3",    r"= 1\,000\,cm^3 = 1\,L"),
            ("Centímetro cúbico",  r"cm^3",    r"= 1\,000\,mm^3"),
            ("Litro",              r"L",       r"= 1\,dm^3 = 1\,000\,mL"),
        ]

        cabecalho = VGroup(
            Text("Unidade",   color=YELLOW, font_size=24, weight=BOLD),
            Text("Símbolo",   color=YELLOW, font_size=24, weight=BOLD),
            Text("Relação",   color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(RIGHT, buff=1.5)
        cabecalho.next_to(linha_cab, DOWN, buff=0.4)

        linha_sep = Line(
            cabecalho.get_left() + LEFT * 0.3,
            cabecalho.get_right() + RIGHT * 0.3,
            color=YELLOW, stroke_width=0.8
        ).next_to(cabecalho, DOWN, buff=0.15)

        self.play(FadeIn(cabecalho), Create(linha_sep), run_time=1.0)

        linhas_tabela = VGroup()
        for i, (nome, simb, rel) in enumerate(dados[1:]):
            cor_linha = WHITE if i % 2 == 0 else BLUE_B
            linha_row = VGroup(
                Text(nome, color=cor_linha, font_size=22),
                MathTex(simb, color=ORANGE, font_size=24),
                MathTex(rel,  color=GREEN_B, font_size=22),
            )
            # Alinha com os cabeçalhos
            linha_row[0].move_to(cabecalho[0].get_center() + DOWN * (0.55 * (i+1)))
            linha_row[1].move_to(cabecalho[1].get_center() + DOWN * (0.55 * (i+1)))
            linha_row[2].move_to(cabecalho[2].get_center() + DOWN * (0.55 * (i+1)))
            linhas_tabela.add(linha_row)
            self.play(FadeIn(linha_row, shift=RIGHT * 0.1), run_time=0.7)

        self.wait(1.8)

        # --- ETAPA 2: destaque 1 dm³ = 1 L ---
        destaque = Text(
            "Relação importante:  1 dm³  =  1 litro  =  1 000 cm³",
            color=ORANGE, font_size=26
        )
        box_dest = SurroundingRectangle(destaque, color=ORANGE,
                                         buff=0.2, corner_radius=0.1)
        grupo_dest = VGroup(destaque, box_dest)
        grupo_dest.next_to(linhas_tabela, DOWN, buff=0.5)

        self.play(FadeIn(destaque), Create(box_dest), run_time=1.2)
        self.wait(2.0)

        # --- ETAPA 3: conversão passo a passo ---
        self.play(
            FadeOut(VGroup(cabecalho, linha_sep, linhas_tabela, grupo_dest)),
            run_time=0.8
        )

        conv_titulo = Text("Exemplo de conversão:",
                           color=WHITE, font_size=26)
        conv_titulo.next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(conv_titulo), run_time=0.8)

        conv1 = MathTex(r"2{,}5\,m^3 = ?\,dm^3",
                        color=WHITE, font_size=34)
        conv2 = MathTex(r"2{,}5 \times 1\,000 = 2\,500\,dm^3",
                        color=WHITE, font_size=34)
        conv3 = MathTex(r"2\,500\,dm^3 = 2\,500\,\text{litros}",
                        color=GREEN_B, font_size=34)

        grupo_conv = VGroup(conv1, conv2, conv3).arrange(DOWN, buff=0.45)
        grupo_conv.next_to(conv_titulo, DOWN, buff=0.45)

        self.play(Write(conv1), run_time=1.2)
        self.wait(0.8)
        self.play(TransformMatchingShapes(conv1.copy(), conv2), run_time=1.4)
        self.wait(0.8)
        self.play(Write(conv3), run_time=1.2)
        box_conv3 = SurroundingRectangle(conv3, color=GREEN_B, buff=0.15,
                                          corner_radius=0.08)
        self.play(Create(box_conv3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(cab, linha_cab, conv_titulo,
                           grupo_conv, box_conv3)),
            run_time=1.0
        )


# =======================================================================
# CENA 5 – PROBLEMA 1: CAIXA D'ÁGUA
# Objetivo pedagógico: aplicar V = c × l × h em contexto real;
#                      identificar dados, fórmula e resolução
# =======================================================================
class CenaProblema1(Scene):
    """
    Conceito : Aplicação da fórmula em problema contextualizado
    Nível    : 9º Ano – Ensino Fundamental
    Problema : Caixa d'água paralelepípedo
               Medidas: 2 m × 3 m × 1,5 m — calcular o volume em m³
    Resposta : B) 7,5 m³
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Problema 1 — Caixa d'água",
                   color=YELLOW, font_size=34, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.5, RIGHT * 5.5, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- ETAPA 1: enunciado ---
        enunc = VGroup(
            Text("Uma caixa d'água em forma de paralelepípedo",
                 color=WHITE, font_size=25),
            Text("retangular possui as seguintes medidas:",
                 color=WHITE, font_size=25),
            MathTex(
                r"c = 2\,\text{m} \quad l = 3\,\text{m} \quad h = 1{,}5\,\text{m}",
                color=ORANGE, font_size=30
            ),
            Text("Qual é a capacidade máxima em m³?",
                 color=WHITE, font_size=25),
        ).arrange(DOWN, buff=0.28)
        enunc.next_to(linha_cab, DOWN, buff=0.4)

        for item in enunc:
            self.play(FadeIn(item, shift=UP * 0.1), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(enunc), run_time=0.8)

        # --- ETAPA 2: representação do sólido (lado esquerdo) ---
        etapa2_label = Text("Representação do sólido:",
                             color=WHITE, font_size=24)
        etapa2_label.next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(etapa2_label), run_time=0.8)

        solido, (A, B, C, D, iso) = make_parallelpiped(
            2.8, 1.2, 0.6,
            ox=-2.8, oy=-0.9,
            face_color=BLUE_D,
            face_opacity=0.58
        )
        self.play(DrawBorderThenFill(solido[0]), run_time=1.0)
        self.play(DrawBorderThenFill(solido[1]),
                  DrawBorderThenFill(solido[2]), run_time=0.9)
        self.wait(0.4)

        # Cotas posicionadas sobre as arestas corretas da projeção isométrica
        # c = 2 m → aresta inferior da face frontal (horizontal, abaixo de A-B)
        mid_AB_p1 = (A + B) / 2
        cota_c = MathTex(r"2\,\text{m}", color=ORANGE, font_size=24)
        cota_c.move_to(mid_AB_p1 + DOWN * 0.32)

        # h = 1,5 m → aresta esquerda da face frontal (vertical, à esquerda de A-D)
        mid_AD_p1 = (A + D) / 2
        cota_h = MathTex(r"1{,}5\,\text{m}", color=ORANGE, font_size=24)
        cota_h.move_to(mid_AD_p1 + LEFT * 0.42)

        # l = 3 m → aresta inferior da face lateral diagonal (B → B+iso)
        mid_B_Biso_p1 = (B + (B + iso)) / 2
        cota_l = MathTex(r"3\,\text{m}", color=ORANGE, font_size=24)
        cota_l.move_to(mid_B_Biso_p1 + DOWN * 0.30 + RIGHT * 0.15)

        self.play(Write(cota_c), Write(cota_h), Write(cota_l), run_time=1.0)
        self.wait(1.0)

        # --- ETAPA 3: resolução passo a passo (lado direito) ---
        passo_tit = Text("Resolução:", color=WHITE, font_size=26)
        passo_tit.move_to(RIGHT * 2.2 + UP * 0.8)

        f1 = MathTex(r"V = c \times l \times h",
                     color=GREEN_B, font_size=30)
        f2 = MathTex(r"V = 2 \times 3 \times 1{,}5",
                     color=WHITE, font_size=30)
        f3 = MathTex(r"V = 6 \times 1{,}5",
                     color=WHITE, font_size=30)
        f4 = MathTex(r"V = 7{,}5\,\text{m}^3",
                     color=GREEN_B, font_size=38)

        passos = VGroup(passo_tit, f1, f2, f3, f4).arrange(DOWN, buff=0.32)
        passos.move_to(RIGHT * 2.6 + DOWN * 0.3)

        self.play(FadeIn(passo_tit), run_time=0.8)
        self.play(Write(f1), run_time=1.2)
        self.wait(0.6)
        self.play(Write(f2), run_time=1.0)
        self.wait(0.6)
        self.play(Write(f3), run_time=1.0)
        self.wait(0.6)
        self.play(Write(f4), run_time=1.2)

        box_f4 = SurroundingRectangle(f4, color=GREEN_B, buff=0.18,
                                       corner_radius=0.1)
        self.play(Create(box_f4), run_time=0.7)
        self.wait(1.0)

        # --- ETAPA 4: gabarito ---
        gabarito = Text(r"Resposta: V = 7,5 m³",
                        color=YELLOW, font_size=26)
        gabarito.to_edge(DOWN, buff=0.45)
        self.play(Write(gabarito), run_time=1.0)
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(etapa2_label, solido, cota_c, cota_h, cota_l,
                           passos, box_f4, gabarito, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 6 – PROBLEMA 2: CUBOS NA EMBALAGEM
# Objetivo pedagógico: calcular quantas unidades cúbicas cabem
#                      em um paralelepípedo — raciocínio combinatório
# =======================================================================
class CenaProblema2(Scene):
    """
    Conceito : Quantidade de cubos em uma embalagem
    Nível    : 9º Ano – Ensino Fundamental
    Problema : Caixa 40 cm × 60 cm × 20 cm
               Cubinhos de 10 cm de lado
               Quantos cabem sem ultrapassar a altura?
    Resposta : D) 48
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Problema 2 — Cubos na embalagem",
                   color=YELLOW, font_size=34, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.5, RIGHT * 5.5, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- ETAPA 1: enunciado ---
        enunc = VGroup(
            Text("Fabiana colocará cubos de 10 cm de lado",
                 color=WHITE, font_size=25),
            Text("dentro de uma embalagem paralelepipédica:",
                 color=WHITE, font_size=25),
            MathTex(
                r"40\,\text{cm} \times 60\,\text{cm} \times 20\,\text{cm}",
                color=ORANGE, font_size=30
            ),
            Text("Quantos cubos cabem sem ultrapassar a altura?",
                 color=WHITE, font_size=25),
        ).arrange(DOWN, buff=0.28)
        enunc.next_to(linha_cab, DOWN, buff=0.4)

        for item in enunc:
            self.play(FadeIn(item, shift=UP * 0.1), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(enunc), run_time=0.8)

        # --- ETAPA 2: sólido da embalagem ---
        etapa2_label = Text("Embalagem (visão isométrica):",
                             color=WHITE, font_size=24)
        etapa2_label.next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(etapa2_label), run_time=0.8)

        caixa, (A2, B2, C2, D2, iso2) = make_parallelpiped(
            3.0, 0.9, 0.75,
            ox=-2.6, oy=-1.0,
            face_color=BLUE_D,
            face_opacity=0.50
        )
        self.play(DrawBorderThenFill(caixa[0]), run_time=1.0)
        self.play(DrawBorderThenFill(caixa[1]),
                  DrawBorderThenFill(caixa[2]), run_time=0.9)

        # 40 cm = comprimento (cx) → aresta inferior da face frontal (A2-B2)
        mid_AB2 = (A2 + B2) / 2
        m40 = MathTex(r"40\,\text{cm}", color=ORANGE, font_size=22)
        m40.move_to(mid_AB2 + DOWN * 0.30)

        # 60 cm = profundidade (cz) → aresta inferior da face lateral (B2 → B2+iso2)
        mid_B2_Biso2 = (B2 + (B2 + iso2)) / 2
        m60 = MathTex(r"60\,\text{cm}", color=ORANGE, font_size=22)
        m60.move_to(mid_B2_Biso2 + DOWN * 0.28 + RIGHT * 0.15)

        # 20 cm = altura (cy) → aresta esquerda da face frontal (A2-D2)
        mid_AD2 = (A2 + D2) / 2
        m20 = MathTex(r"20\,\text{cm}", color=ORANGE, font_size=22)
        m20.move_to(mid_AD2 + LEFT * 0.42)

        self.play(Write(m40), Write(m60), Write(m20), run_time=1.0)
        self.wait(1.0)

        # --- ETAPA 3: estratégia de divisão ---
        self.play(
            FadeOut(VGroup(etapa2_label, caixa, m40, m60, m20)),
            run_time=0.8
        )

        strat_tit = Text("Estratégia: dividir cada dimensão pelo lado do cubo",
                          color=WHITE, font_size=24)
        strat_tit.next_to(linha_cab, DOWN, buff=0.4)
        self.play(FadeIn(strat_tit), run_time=0.9)
        self.wait(0.4)

        # Divisão das dimensões
        d1 = MathTex(
            r"\text{Comprimento: } \frac{40}{10} = 4 \text{ cubos}",
            color=WHITE, font_size=28
        )
        d2 = MathTex(
            r"\text{Largura: } \frac{60}{10} = 6 \text{ cubos}",
            color=WHITE, font_size=28
        )
        d3 = MathTex(
            r"\text{Altura: } \frac{20}{10} = 2 \text{ camadas}",
            color=WHITE, font_size=28
        )

        divisoes = VGroup(d1, d2, d3).arrange(DOWN, buff=0.4)
        divisoes.next_to(strat_tit, DOWN, buff=0.45)

        self.play(Write(d1), run_time=1.0)
        self.wait(0.5)
        self.play(Write(d2), run_time=1.0)
        self.wait(0.5)
        self.play(Write(d3), run_time=1.0)
        self.wait(1.0)

        # --- ETAPA 4: total de cubos ---
        total_label = Text("Total de cubos (embalagem completa):",
                            color=WHITE, font_size=24)
        total_formula = MathTex(
            r"4 \times 6 \times 2 = 48 \text{ cubos}",
            color=WHITE, font_size=32
        )
        total_grupo = VGroup(total_label, total_formula).arrange(DOWN, buff=0.25)
        total_grupo.next_to(divisoes, DOWN, buff=0.45)

        self.play(FadeIn(total_label), run_time=0.8)
        self.play(Write(total_formula), run_time=1.2)
        self.wait(0.8)

        # --- ETAPA 5: leitura atenta do enunciado! ---
        self.play(
            FadeOut(VGroup(strat_tit, divisoes, total_grupo)),
            run_time=0.8
        )

        alerta = Text(
            '⚠  Atenção: "sem ultrapassar a altura"',
            color=ORANGE, font_size=26
        )
        alerta.next_to(linha_cab, DOWN, buff=0.45)

        explicacao = Text(
            "O cubo tem 10 cm de lado e a caixa tem 20 cm de altura.\n"
            "Como 20 ÷ 10 = 2, cabem exatamente 2 camadas completas\n"
            "sem ultrapassar a altura — nenhum cubo fica de fora.",
            color=WHITE, font_size=23, line_spacing=1.35
        ).next_to(alerta, DOWN, buff=0.4)

        self.play(FadeIn(alerta), run_time=1.0)
        self.play(FadeIn(explicacao), run_time=1.2)
        self.wait(1.5)

        # --- ETAPA 6: resolução correta ---
        self.play(FadeOut(VGroup(alerta, explicacao)), run_time=0.8)
        self.wait(0.3)

        passo_tit = Text("Resolução correta:", color=WHITE, font_size=26)
        passo_tit.next_to(linha_cab, DOWN, buff=0.45)

        r1 = MathTex(
            r"\text{Base: } 4 \times 6 = 24 \text{ cubos por camada}",
            color=WHITE, font_size=30
        )
        r2 = MathTex(
            r"\text{Camadas: } 20 \div 10 = 2 \text{ camadas}",
            color=WHITE, font_size=30
        )
        r3 = MathTex(
            r"\text{Total} = 24 \times 2 = 48 \text{ cubos}",
            color=GREEN_B, font_size=36
        )

        resolucao = VGroup(passo_tit, r1, r2, r3).arrange(DOWN, buff=0.38)
        resolucao.next_to(linha_cab, DOWN, buff=0.35)

        self.play(FadeIn(passo_tit), run_time=0.8)
        self.play(Write(r1), run_time=1.1)
        self.wait(0.6)
        self.play(Write(r2), run_time=1.1)
        self.wait(0.6)
        self.play(Write(r3), run_time=1.2)

        box_r3 = SurroundingRectangle(r3, color=GREEN_B, buff=0.18,
                                       corner_radius=0.1)
        self.play(Create(box_r3), run_time=0.7)

        gabarito = Text("Resposta: 48 cubos",
                        color=YELLOW, font_size=26)
        gabarito.to_edge(DOWN, buff=0.45)
        self.play(Write(gabarito), run_time=1.0)
        self.wait(2.5)

        self.play(
            FadeOut(VGroup(resolucao, box_r3, gabarito, cab, linha_cab)),
            run_time=1.2
        )


# =======================================================================
# CENA 7 – ENCERRAMENTO
# Objetivo pedagógico: consolidar o mapa conceitual do D14,
#                      apresentar a fórmula central e as estratégias
# =======================================================================
class Encerramento(Scene):
    """
    Conceito : Síntese do Descritor D14
    Nível    : 9º Ano – Ensino Fundamental
    Objetivo : Consolidar os conceitos de volume, fórmula e estratégias
               de resolução de problemas trabalhados na animação.
    """

    def construct(self):
        # --- Cabeçalho ---
        cab = Text("Síntese — Descritor D14",
                   color=YELLOW, font_size=36, weight=BOLD)
        cab.to_edge(UP, buff=0.4)
        linha_cab = Line(LEFT * 5.5, RIGHT * 5.5, color=YELLOW, stroke_width=1)
        linha_cab.next_to(cab, DOWN, buff=0.18)
        self.play(Write(cab), Create(linha_cab), run_time=1.2)
        self.wait(0.5)

        # --- Fórmula central em destaque ---
        formula_central = MathTex(
            r"V_{\text{paralelepípedo}} = c \times l \times h",
            color=GREEN_B, font_size=42
        )
        formula_central.next_to(linha_cab, DOWN, buff=0.5)
        box_fc = SurroundingRectangle(formula_central, color=GREEN_B,
                                       buff=0.22, corner_radius=0.12)
        self.play(Write(formula_central), Create(box_fc), run_time=1.4)
        self.wait(1.0)

        # --- Mapa: estratégias de resolução ---
        mapa_tit = Text("Estratégias para resolver problemas de volume:",
                         color=WHITE, font_size=24)
        mapa_tit.next_to(box_fc, DOWN, buff=0.45)
        self.play(FadeIn(mapa_tit), run_time=0.9)

        estrategias = VGroup(
            Text("1. Identificar o sólido e suas dimensões",
                 color=WHITE, font_size=22),
            Text("2. Verificar se as unidades são as mesmas",
                 color=ORANGE, font_size=22),
            Text("3. Aplicar a fórmula V = c × l × h",
                 color=GREEN_B, font_size=22),
            Text("4. Ler o enunciado com atenção ao que é pedido",
                 color=ORANGE, font_size=22),
            Text("5. Conferir a unidade da resposta (cm³, m³, L…)",
                 color=WHITE, font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        estrategias.next_to(mapa_tit, DOWN, buff=0.3)

        dots_encerramento = VGroup()
        for i, linha in enumerate(estrategias):
            dot = Dot(
                color=GREEN_B if i % 2 == 0 else ORANGE,
                radius=0.07
            ).next_to(linha, LEFT, buff=0.15)
            dots_encerramento.add(dot)
            self.play(FadeIn(dot), FadeIn(linha, shift=RIGHT * 0.1), run_time=0.65)

        self.wait(1.5)

        # --- Fade final limpo ---
        self.play(
            FadeOut(VGroup(cab, linha_cab, formula_central, box_fc,
                           mapa_tit, estrategias, dots_encerramento)),
            run_time=1.5
        )



# =======================================================================
# LOGO – Identidade visual da Prof.ª Emilly Mayre
# =======================================================================
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
