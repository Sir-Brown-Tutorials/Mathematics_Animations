from manim import *
from manim.utils.color.X11 import BROWN

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.disable_caching = True


class Reel(Scene):
    def construct(self):
        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{xcolor}")
        my_template.add_to_preamble(r"\usepackage{cancel}")
        my_template.add_to_preamble(r"\renewcommand{\CancelColor}{\color{red}}")

        # Load and position logo image
        logo = ImageMobject("../Images/sir_brown_logo_trans.png")
        logo_corner = logo.scale(0.2)
        logo_corner.to_corner(DR, buff=-0.1)
        self.add(logo_corner)

        # Problem Statement
        problem = Tex(
            r"Solve for $p$ and $q$ in $\frac{32^4 \times 625^3}{8^6 \times 25^4} = 2^p5^q$"
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = (
            VGroup(
                MathTex(r"\frac{32^4 \times 625^3}{8^6 \times 25^4} = 2^p5^q"),
                MathTex(r"\frac{2^{20} \times 5^{12}}{2^{18} \times 5^8} = 2^p5^q"),
                MathTex(r"2", r"^2", r"\times 5", r"^4", r"= 2", r"^p", r"5", r"^q"),
                Tex(r"$p=2$", r" and ", r"$q=4$"),
            )
            .arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            .shift(RIGHT * 3)
        )
        eq_group[2][1].set_color(PURE_BLUE)
        eq_group[2][5].set_color(PURE_BLUE)
        eq_group[2][3].set_color(PURE_GREEN)
        eq_group[2][7].set_color(PURE_GREEN)
        eq_group[3][0].set_color(PURE_BLUE)
        eq_group[3][2].set_color(PURE_GREEN)

        box_1 = SurroundingRectangle(eq_group[3][0], color=PURE_BLUE, buff=0.1)
        box_2 = SurroundingRectangle(eq_group[3][2], color=PURE_GREEN, buff=0.1)
        annot_1 = (
            Tex(
                r"Write each element as a \\"
                r"power of $2$ and $5$."
            )
            .next_to(eq_group[0], LEFT * 3)
            .set_color(RED)
            .scale(0.85)
        )
        annot_2 = (
            Tex(
                r"Simplify the Left-Hand-Side\\"
                r"of the equation."
            )
            .next_to(eq_group[1], LEFT * 3)
            .set_color(RED)
            .scale(0.85)
        )
        annot_3 = (
            Tex(r"Equate the elements")
            .next_to(eq_group[2], LEFT * 3)
            .set_color(RED)
            .scale(0.85)
        )
        annot_group = VGroup(annot_1, annot_2, annot_3)
        self.play(Write(problem_group[0]))
        self.wait(2)
        self.play(problem_group.animate.to_edge(UP).scale(1.1).set_color(YELLOW_B))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Write(annot_group[0]))
        self.wait()
        self.play(TransformFromCopy(eq_group[0], eq_group[1]))
        self.wait(2)
        self.play(Write(annot_group[1]))
        self.wait()
        self.play(TransformFromCopy(eq_group[1], eq_group[2]))
        self.wait(2)
        self.play(Write(annot_group[2]))
        self.wait()
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(
            Indicate(eq_group[3][0], color=PURE_BLUE),
            Indicate(eq_group[3][2], color=PURE_GREEN),
            FadeIn(box_1, box_2),
        )
        self.wait(3)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
            Write(final_text),
            ShrinkToCenter(VGroup(problem_group, eq_group, annot_group, box_1, box_2)),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        # self.wait()


class ExpandExpression(Scene):
    def construct(self):
        # Create a custom Latex template that includes the cancel package
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{xcolor}")
        my_template.add_to_preamble(r"\usepackage{cancel}")
        my_template.add_to_preamble(r"\renewcommand{\CancelColor}{\color{red}}")

        # Load and position logo image
        logo = ImageMobject("../Images/logo.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.2)
        self.add(logo_corner)

        # Problem Statement
        problem = (
            Tex(r"Expand and Simplify $(4x - 3)(4x + 3)$")
            .to_edge(UP)
            .scale(1.2)
            .set_color(YELLOW_B)
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        problem_statement = Tex(
            r"Expand and Simplify $\mathbf{(4x-3)(4x+3)}$ \\ using the multiplication grid."
        )
        eq_1 = MathTex(r"(4x - 3)", r"(4x + 3)").next_to(problem_group, DOWN, buff=0.2)
        eq_1[0].set_color(BLUE)
        eq_1[1].set_color(RED)
        table_1 = MathTable(
            [[r"4x \times 4x", r"4x \times -3"], [r"3 \times 4x", r"3 \times -3"]],
            include_outer_lines=True,
        )
        table_2 = MathTable(
            [[r"16x^2", r"-12x"], [r"12x", r"-9"]],
            include_outer_lines=True,
        )
        table_1.get_entries((1, 1)).set_opacity(0)
        table_1.get_entries((1, 2)).set_opacity(0)
        table_1.get_entries((2, 1)).set_opacity(0)
        table_1.get_entries((2, 2)).set_opacity(0)

        labels_1 = Group(
            MathTex(r"4x")
            .next_to(table_1.get_cell((1, 1)), UP, buff=0.25)
            .set_color(BLUE),
            MathTex(r"-3")
            .next_to(table_1.get_cell((1, 2)), UP, buff=0.25)
            .set_color(BLUE),
            MathTex(r"4x")
            .next_to(table_1.get_cell((1, 1)), LEFT, buff=0.25)
            .set_color(BROWN),
            MathTex(r"3")
            .next_to(table_1.get_cell((2, 1)), LEFT, buff=0.25)
            .set_color(BROWN),
        )
        eq_group = (
            VGroup(
                MathTex(r"16x^2", r" - 12x", r" + 12x", r" - 9"),
                MathTex(r"16x^2 - 9"),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(table_1, DOWN, buff=0.5)
        )
        box = SurroundingRectangle(
            eq_group[1], buff=0.25, color=PURE_GREEN, corner_radius=0.1
        )

        self.play(Write(problem_statement))
        self.wait()
        self.play(Transform(problem_statement, problem_group))
        self.wait()
        self.play(Write(eq_1))
        self.wait()
        self.play(FadeIn(table_1))
        self.wait()
        self.play(TransformFromCopy(eq_1[0], labels_1[:2]))
        self.wait()
        self.play(TransformFromCopy(eq_1[1], labels_1[-2:]))
        self.wait()

        self.play(table_1.get_entries((1, 1)).animate.set_opacity(1))
        self.wait()
        self.play(Transform(table_1.get_entries((1, 1)), table_2.get_entries((1, 1))))
        self.wait()
        self.play(TransformFromCopy(table_1.get_entries((1, 1)), eq_group[0][0]))
        self.wait()

        self.play(table_1.get_entries((1, 2)).animate.set_opacity(1))
        self.wait()
        self.play(Transform(table_1.get_entries((1, 2)), table_2.get_entries((1, 2))))
        self.wait()
        self.play(TransformFromCopy(table_1.get_entries((1, 2)), eq_group[0][1]))
        self.wait()

        self.play(table_1.get_entries((2, 1)).animate.set_opacity(1))
        self.wait()
        self.play(Transform(table_1.get_entries((2, 1)), table_2.get_entries((2, 1))))
        self.wait()
        self.play(TransformFromCopy(table_1.get_entries((2, 1)), eq_group[0][2]))
        self.wait()

        self.play(table_1.get_entries((2, 2)).animate.set_opacity(1))
        self.wait()
        self.play(Transform(table_1.get_entries((2, 2)), table_2.get_entries((2, 2))))
        self.wait()
        self.play(TransformFromCopy(table_1.get_entries((2, 2)), eq_group[0][3]))
        self.wait()

        self.play(TransformFromCopy(eq_group[0], eq_group[1]))
        self.wait()
        self.play(Indicate(eq_group[1]), FadeIn(box))
        self.wait(3)
        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW_B)
        self.play(
            ShrinkToCenter(
                Group(problem_statement, table_1, labels_1, eq_group, box, eq_1)
            ),
            Write(final_text),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.to_edge(DOWN).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
        # self.wait()


# Thumbnail
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
            Text("Expand and Simplify", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )
        # Subtitle
        subtitle = (
            Text("Using multiplication Grid", font="Roboto", weight=BOLD, color=WHITE)
            .scale(1.5)
            .next_to(title, DOWN, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(r"(4x - 3)(4x + 3)", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
