"""ABC is a triangle such that AB = 8 cm, angle B = 90⁰ and BC = 6 cm. M is the midpint of BC. Calculate:
(a) angle BAM
(b) angle MAC
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


# Construct a Figure
# ===== Define coordinates of the points
def make_figure():
    A = 2 * DOWN + 3 * LEFT
    B = 2 * DOWN + 2 * RIGHT
    C = 2 * UP + 2 * RIGHT
    M = 2 * RIGHT

    # ===== Define the sides of a triangle
    AB = Line(A, B)
    AC = Line(A, C)
    BC = Line(B, C)
    AM = Line(A, M, stroke_width=2).set_opacity(opacity=0)
    triangle = Polygon(A, B, C, stroke_width=2, color=WHITE)

    # ===== Define the dots and labels
    dot_A, dot_B, dot_C, dot_M = (
        Dot(A, radius=0.025),
        Dot(B, radius=0.025),
        Dot(C, radius=0.025),
        Dot(M, radius=0.05),
    )
    labA = MathTex("A").next_to(dot_A, UL, buff=0.12).scale(0.5)
    labB = MathTex("B").next_to(dot_B, DR, buff=0.12).scale(0.5)
    labC = MathTex("C").next_to(dot_C, UR, buff=0.12).scale(0.5)
    labM = MathTex("M").next_to(dot_M, UL, buff=0.12).scale(0.5)
    dot_label_group = VGroup(dot_A, dot_B, dot_C, dot_M, labA, labB, labC, labM)

    # Length annotations (nice for horizontal/vertical legs)
    braceAB = BraceBetweenPoints(A, B, direction=DOWN, buff=0.025).set_fill(opacity=0)
    textAB = braceAB.get_tex(r"8 cm", buff=0).scale(0.5)
    braceBC = BraceBetweenPoints(B, C, direction=RIGHT).set_fill(opacity=0)
    textBC = braceBC.get_tex(r"6 cm", buff=0).scale(0.5)
    braceBM = BraceBetweenPoints(B, M, direction=RIGHT, buff=0.025).set_fill(opacity=0)
    textBM = braceBM.get_tex(r"3 cm", buff=0).scale(0.5).set_fill(opacity=0)
    brace_group = VGroup(braceAB, braceBC, braceBM, textAB, textBC, textBM)

    # ==== Define Angles
    right_angle = RightAngle(AB, BC, length=0.5, stroke_width=2, quadrant=(-1, 1))
    angle_BAC = Angle(AC, AB, radius=1, stroke_width=2, other_angle=True).set_opacity(0)
    angle_BAM = Angle(AB, AM, radius=0.9, stroke_width=2).set_opacity(0)
    angle_BAM_label = (
        MathTex(r"20.5^\circ")
        .next_to(dot_A, UR, buff=0.75)
        .shift(DOWN * 0.75)
        .scale(0.5)
        .set_opacity(0)
    )
    angle_MAC = Angle(AM, AC, radius=1.1, stroke_width=2).set_opacity(0)
    angle_MAC_label = (
        MathTex(r"16^\circ")
        .next_to(dot_A, UR, buff=0.85)
        .shift(DOWN * 0.4)
        .scale(0.5)
        .set_opacity(0)
    )
    angle_group = VGroup(
        right_angle, angle_BAC, angle_BAM, angle_BAM_label, angle_MAC, angle_MAC_label
    )

    # ===== Figure Group
    figure = VGroup(triangle, dot_label_group, brace_group, angle_group, AM)
    return figure


class TangentTriangle(VoiceoverScene):
    def construct(self):
        # Voiceover Instant
        self.set_speech_service(GTTSService(lang="en", transcription_model="base"))

        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{cancel}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Intro
        title = Tex(r"Using Tangents to Solve Triangles.", color=YELLOW)
        institution = Tex(r"@Kasiwa Academy")
        text = """
            Hello! Welcome to yet another lesson. Here we will be demonstrating how we can solve a problem involving triangles.
            We will use one of the trigonometric ratios called the tangent. Stay with us right here at <bookmark mark="A"/> 
            Kasiwa Academy as-we-continue-helping-each-other-develop-skills-in-Mathematics.
             """
        with self.voiceover(text=text) as tracker:
            self.play(Write(title), run_time=tracker.time_until_bookmark("A", limit=1))
            self.wait()
            self.play(title.animate.shift(UP).scale(1.3).set_color(YELLOW_B))
            self.wait_until_bookmark("A")
            self.play(FadeIn(institution, shift=UP))
        self.wait(2)

        # Problem Statement
        sub_title_1 = Tex(r"Problem Statement:", color=YELLOW).to_edge(DOWN)
        statement_1 = Tex(
            r"$ABC$ is a triangle such that $AB = 8cm$, $\angle B = 90^\circ$ \\"
            r"and $BC = 6cm$. $M$ is the midpoint of BC. Calculate:"
        )
        eq_group_1 = (
            VGroup(Tex(r"(a) $\angle BAM$"), Tex(r"(b) $\angle MAC$"))
            .arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            .next_to(statement_1, DOWN, buff=0.75)
        )
        text_1 = """
                We begin by introducing the problem. We are given a triangle A-B-C in which A-B is equal to 8 cm, angle B is equal to 90
                degrees and line B-C is equal to 6 cm. Point M is located at the middle of line B-C. We are asked to find the size of 
               <bookmark mark="A"/> angle B-A-M and the size of<bookmark mark="B"/> angle M-AC.
                 """
        with self.voiceover(text=text_1) as tracker:
            self.play(Write(sub_title_1))
            self.wait()
            self.play(
                FadeOut(title, institution, shift=UP),
                sub_title_1.animate.to_edge(UP).scale(1.3).set_color(YELLOW_B),
                Write(statement_1),
            )
            self.wait_until_bookmark("A")
            self.play(
                Write(eq_group_1[0]), run_time=tracker.time_until_bookmark("B", limit=1)
            )
            self.wait_until_bookmark("B")
            self.play(Write(eq_group_1[1]))
            self.wait()
        self.wait(2)

        # Draw a sketch of the Triangle
        sub_title_2 = Tex(
            r"Draw a sketch of the triangle $ABC$.", color=YELLOW
        ).to_edge(DOWN)
        figure = make_figure()
        text_2 = """
                Let us draw a sketch of the triangle A-B-C, showing all the given information.
                 """
        with self.voiceover(text=text_2) as tracker:
            self.play(Write(sub_title_2))
            self.wait()
            self.play(
                FadeOut(sub_title_1, statement_1, eq_group_1, shift=UP),
                sub_title_2.animate.to_edge(UP).scale(1.3).set_color(YELLOW_B),
                FadeIn(figure),
            )
        self.wait(2)

        # Solutions
        sub_title_3 = Tex(r"Solutions:", color=YELLOW).to_edge(DOWN)

        ## ====== Solution to question (a)
        question_1 = Tex(r"(a) Calculate $\angle BAM$.").move_to([-4, 2, 0]).scale(1)
        solution_group_1 = (
            VGroup(
                Tex(r"Join $A$ to $M$. Using $\triangle ABM$,"),
                Tex(r"$BM = 3cm$ (midpoint of $BC$)"),
                Tex(r"Since $\tan \theta = \frac{Opposite Side}{Adjacent Side}$"),
                MathTex(r"\Rightarrow \tan BAM = \frac{BM}{AB}"),
                MathTex(r"\Rightarrow \tan BAM = \frac{3}{8} = 0.375"),
                MathTex(r"\Rightarrow \tan^{-1} 0.375 = 20.5^\circ"),
                MathTex(r"\therefore \angle BAM = 20.5^\circ"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.8)
            .to_edge(RIGHT)
            .scale(0.6)
            .shift(DOWN * 0.5)
        )
        question_1_group = VGroup(
            question_1, solution_group_1, figure[2][2], figure[2][-1]
        )

        question_2 = Tex(r"(b) Calculate $\angle MAC$.").move_to([-4, 2, 0]).scale(1)
        solution_group_2 = (
            VGroup(
                Tex(r"Using $\triangle ABC$, we can find $\angle BAC$"),
                MathTex(
                    r"\Rightarrow \tan \angle BAC = \frac{BC}{AB} = \frac{6}{8} = 0.75"
                ),
                MathTex(
                    r"\Rightarrow \tan^{-1} 0.75 =", r" 36.5^\circ"
                ).set_color_by_tex(r"36.5^\circ", PURE_RED),
                Tex(r"$\angle MAC$ is $\between \angle BAC$ and $\angle BAM$"),
                MathTex(r"\Rightarrow \angle MAC = \angle BAC - \angle BAM"),
                MathTex(r"\Rightarrow \angle MAC = 36.5^\circ - 20.5^\circ = 16^\circ"),
                MathTex(r"\therefore \angle MAC = 16^\circ"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.8)
            .to_edge(RIGHT)
            .scale(0.6)
            .shift(DOWN * 0.5)
        )
        question_2_group = VGroup(
            question_2, solution_group_2, figure[2][0], figure[2][1]
        )

        sub_title_4 = Tex(r"Final  Solutions:", color=YELLOW_B).scale(1.3).to_edge(UP)
        solution_group_3 = (
            VGroup(
                MathTex(r"\boxed{\angle MAC = 16^\circ}", color=YELLOW_D),
                MathTex(r"\boxed{\angle BAM = 20.5^\circ}", color=YELLOW_D),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=1.5)
            .to_edge(RIGHT)
            .scale(1)
        )
        text_3 = """
                Let us solve the first qustion where we are asked to calculate the size of angle B-A-M. We are firstly 
                required <bookmark mark="A"/> to join point A to point M. From the newly created triangle A-B-M,
                <bookmark mark="B"/> line B-M is equal to 3 cm. It is half of line B-C as M is the mid-point of B-C. 
                Using the tangent ratio <bookmark mark="C"/> which is simply the ratio of the opposite-side and the adjacent side,
                we get <bookmark mark="D"/> tangent of angle B-A-M as the ratio of line BM and line A-B.
                The <bookmark mark="E"/> tangent of angle B-A-M becomes the ratio of 3 cm and 8 cm which simplifies to 0.375.
                Taking the <bookmark mark="F"/> inverse of the tangent of angle A-B-M we get 20.5 degrees.
                Therefore the size of <bookmark mark="G"/>  angle B-A-M is 20.5 degrees.
                 """
        with self.voiceover(text=text_3) as tracker:
            self.play(Write(sub_title_3))
            self.wait()
            self.play(
                FadeOut(sub_title_2, shift=UP),
                sub_title_3.animate.to_edge(UP).set_color(YELLOW_B).scale(1.3),
                figure.animate.to_edge(LEFT),
                Write(question_1),
            )
            self.wait_until_bookmark("A")
            self.play(
                Write(solution_group_1[0]),
                run_time=tracker.time_until_bookmark("B", limit=1),
            )
            self.wait()
            self.play(figure[-1].animate.set_opacity(1))
            self.play(Indicate(figure[-1]))
            self.wait_until_bookmark("B")
            self.play(
                Write(solution_group_1[1]),
                run_time=tracker.time_until_bookmark("C", limit=1),
            )
            self.wait()
            self.play(
                figure[2][2].animate.set_opacity(1),
                figure[2][-1].animate.set_fill(opacity=1),
            )
            self.play(Indicate(figure[2][2]))
            self.wait_until_bookmark("C")
            self.play(
                Write(solution_group_1[2]),
                run_time=tracker.time_until_bookmark("D", limit=1),
            )
            self.wait_until_bookmark("D")
            self.play(
                Write(solution_group_1[3]),
                run_time=tracker.time_until_bookmark("E", limit=1),
            )
            self.wait()
            self.play(
                figure[2][0].animate.set_fill(opacity=1),
                figure[3][2].animate.set_stroke(opacity=1),
            )
            self.wait_until_bookmark("E")
            self.play(
                TransformFromCopy(solution_group_1[3], solution_group_1[4]),
                run_time=tracker.time_until_bookmark("F", limit=1),
            )
            self.wait()
            self.play(
                Indicate(figure[2][0]), Indicate(figure[3][2]), Indicate(figure[2][2])
            )
            self.wait_until_bookmark("F")
            self.play(
                TransformFromCopy(solution_group_1[4], solution_group_1[5]),
                run_time=tracker.time_until_bookmark("G", limit=1),
            )
            self.wait_until_bookmark("G")
            self.play(
                TransformFromCopy(solution_group_1[5], solution_group_1[6]),
                figure[3][3].animate.set_fill(opacity=1),
            )
            self.wait()
            self.play(Circumscribe(solution_group_1[6]), Indicate(figure[3][3]))
        self.wait(2)
        self.play(ShrinkToCenter(question_1_group))
        text_4 = """
                Let us now solve the second question where we are required to find the size of angle M-A-C. Using 
                the big <bookmark mark="A"/> triangle A-B-C we can find angle B-A-C. We use the same tangent ratio that we used for solving
                the first question. We will get the <bookmark mark="B"/> ratio of line B-C and A-B with sizes 6 cm and 8 cm respectively. 
                This ratio  evaluates to 0.75. Taking the inverse of <bookmark mark="C"/> tangent of angle B-A-C we find the size of angle
                B-A-C to be 36.5 degrees. The angle <bookmark mark="D"/> that we want to find angle M-A-C is between angle B-A-C and angle
                B-A-M. Which means angle M-A-C <bookmark mark="E"/> can be found by subtracting angle B-A-M from angle B-A-C. If we 
                <bookmark mark="F"/> subtract 20.5 degrees for angle B-A-M from 36.5 degrees for angle B-A-C we get 16 degrees. Therefore 
                <bookmark mark="G"/> the size of angle M-A-C is 16 degrees.
                 """
        with self.voiceover(text=text_4) as tracker:
            self.play(Write(question_2))
            self.wait_until_bookmark("A")
            self.play(
                Write(solution_group_2[0]),
                Indicate(figure[0]),
                run_time=tracker.time_until_bookmark("B", limit=1),
            )
            self.wait()
            self.play(
                figure[3][1].animate.set_stroke(opacity=1),
                figure[2][1].animate.set_fill(opacity=1),
            )
            self.wait_until_bookmark("B")
            self.play(
                Write(solution_group_2[1]),
                run_time=tracker.time_until_bookmark("C", limit=1),
            )
            self.wait_until_bookmark("C")
            self.play(
                TransformFromCopy(solution_group_2[1], solution_group_2[2]),
                figure[3][1].animate.set_color(PURE_RED),
                run_time=tracker.time_until_bookmark("D", limit=1),
            )
            self.wait_until_bookmark("D")
            self.play(
                Write(solution_group_2[3]),
                figure[3][-2].animate.set_stroke(opacity=1),
                run_time=tracker.time_until_bookmark("E", limit=1),
            )
            self.wait_until_bookmark("E")
            self.play(
                Write(solution_group_2[4]),
                run_time=tracker.time_until_bookmark("F", limit=1),
            )
            self.wait_until_bookmark("F")
            self.play(
                TransformFromCopy(solution_group_2[4], solution_group_2[5]),
                run_time=tracker.time_until_bookmark("G", limit=1),
            )
            self.wait_until_bookmark("G")
            self.play(
                TransformFromCopy(solution_group_2[5], solution_group_2[6]),
                figure[3][-1].animate.set_opacity(1),
                FadeOut(figure[3][1]),
            )
            self.wait()
            self.play(Circumscribe(solution_group_2[6]), Indicate(figure[3][-1]))
        self.wait(2)
        self.play(ShrinkToCenter(question_2_group))
        text_5 = """
                We have successfully found solutions to our questions. We have  managed to calculate the size of <bookmark mark="A"/>
                angle M-A-C as 16 degrees and the size of <bookmark mark="B"/> angle B-A-M as-20.5-degrees.
                 """
        with self.voiceover(text=text_5) as tracker:
            self.play(
                FadeTransform(sub_title_3, sub_title_4),
                GrowFromEdge(solution_group_3, RIGHT),
            )
            self.wait_until_bookmark("A")
            self.play(
                Indicate(solution_group_3[0], color=PURE_BLUE),
                Indicate(figure[3][-1], color=PURE_BLUE),
                run_time=tracker.time_until_bookmark("B", limit=2),
            )
            self.wait_until_bookmark("B")
            self.play(
                Indicate(solution_group_3[1], color=PURE_RED),
                Indicate(figure[3][-3], color=PURE_RED),
                run_time=2,
            )
        self.wait(2)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        final_solution_group = VGroup(sub_title_4, figure, solution_group_3)
        text_6 = """
                Thank you for watching, see you in our next video.
                 """
        with self.voiceover(text=text_6) as tracker:
            self.play(Write(final_text), ShrinkToCenter(final_solution_group))
            self.wait()
            self.play(
                logo_corner.animate.move_to(ORIGIN).scale(3),
                final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
            )
            self.wait()
        self.play(FadeOut(final_text, logo_corner))
        self.wait()


# Thumbnail for CubicGraph
class Thumbnail(Scene):
    def construct(self):
        # Add background image
        background = ImageMobject("../Images/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        # Title text
        title = (
            Text("Using Tangents", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )

        subtitle = (
            Text("to Solve Triangles", font="Roboto", weight=BOLD, color=WHITE)
            .scale(1.5)
            .next_to(title, DOWN, buff=0.3)
        )

        # Formula
        # formula = MathTex(r"x = \frac{b - k^3}{k^3}", color=WHITE).scale(1.7).next_to(subtitle, DOWN, buff=1)

        # Add everything
        figure = make_figure()
        figure = figure.shift(DOWN).scale(0.85)
        line_AM = figure[-1].set_opacity(1)
        angle_BAM = figure[3][2].set_opacity(1)
        angle_MAC = figure[3][4].set_opacity(1)
        self.add(title, subtitle, figure, line_AM, angle_BAM, angle_MAC)
