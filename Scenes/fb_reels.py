from manim import *

config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
config.disable_caching = True
# config.background_color = GRAY_E


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
        problem = Tex(r"Solve for $k$ in $x = \frac{b - k^3}{k^3}$")
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = VGroup(
            MathTex(r"k^3 \times x = \frac{b - k^3}{k^3} \times k^3"),
            MathTex(r"k^3x = b - k^3"),
            MathTex(r"k^3x + k^3 = b - k^3 + k^3"),
            MathTex(r"k^3x + k^3 = b"),
            MathTex(r"k^3(x + 1) = b"),
            MathTex(r"\frac{k^3(x + 1)}{(x + 1)} = \frac{b}{x + 1}"),
            MathTex(r"k^3 = \frac{b}{x + 1}"),
            MathTex(r"\sqrt[3]{k^3} = \sqrt[3]{\frac{b}{x + 1}}"),
            MathTex(r"k = \sqrt[3]{\frac{b}{x + 1}}"),
        ).arrange(DOWN, buff=0.5)
        rectangle_box = SurroundingRectangle(
            eq_group[8], buff=0.2, color=PURE_RED, corner_radius=0.2
        )
        cancel_1 = MathTex(
            r"k^3 \times x = \frac{b - k^3}{\cancel{k^3}} \times \cancel{k^3}",
            tex_template=my_template,
        )
        cancel_1.move_to(eq_group[0])
        cancel_2 = MathTex(
            r"\frac{k^3\cancel{(x + 1)}}{\cancel{(x + 1)}} = \frac{b}{x + 1}",
            tex_template=my_template,
        )
        cancel_2.move_to(eq_group[5])
        cancel_3 = MathTex(
            r"\sqrt[{\cancel{3}}]{k^{\cancel{3}}} = \sqrt[3]{\frac{b}{x + 1}}",
            tex_template=my_template,
        )
        cancel_3.move_to(eq_group[7])

        self.play(Write(problem_group[0]))
        self.wait(2)
        self.play(problem_group.animate.to_edge(UP).scale(1.5).set_color(YELLOW))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[0], cancel_1))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[0], eq_group[1]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[1], eq_group[2]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[3], eq_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[4], eq_group[5]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[5], cancel_2))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[5], eq_group[6]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[6], eq_group[7]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[7], cancel_3))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[7], eq_group[8:]))
        self.wait(2)
        self.play(Create(rectangle_box))
        self.wait(2)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW)
        self.play(
            Write(final_text),
            ShrinkToCenter(
                VGroup(
                    problem_group, eq_group, rectangle_box, cancel_1, cancel_2, cancel_3
                )
            ),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.shift(DOWN * 4).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))


class QuadraticEquation(Scene):
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
        problem = Tex(r"Solve the equation $3x^2 + 6x - 2 = 0$")
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = VGroup(
            Tex(r"Use the quadratic formula"),
            Tex(r"$a = 3$, $b = 6$ and $c = -2$"),
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
            MathTex(r"x = \frac{-6 \pm \sqrt{b^2 - 4(3)(-2)}}{2(3)}"),
            MathTex(r"x = \frac{-6 \pm \sqrt{36 + 24}}{6}"),
            MathTex(r"x = \frac{-6 \pm \sqrt{60}}{6}"),
            MathTex(r"x = \frac{-6 \pm 7.746}{6}"),
            Tex(r"$x = \frac{-6 + 7.746}{6}$ or $\frac{-6 - 7.746}{6}$"),
            Tex(r"$x \approx 0.291$", r"\quad or \quad", r"$x \approx -2.29$"),
        ).arrange(DOWN, buff=0.5)
        box_1 = SurroundingRectangle(
            eq_group[8][0], color=PURE_BLUE, corner_radius=0.2, buff=0.2
        )
        box_2 = SurroundingRectangle(
            eq_group[8][2], color=PURE_GREEN, corner_radius=0.2, buff=0.2
        )

        self.play(Write(problem_group[0]))
        self.wait(2)
        self.play(problem_group.animate.to_edge(UP).set_color(YELLOW))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Write(eq_group[1]))
        self.wait(2)
        self.play(Write(eq_group[2]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[3], eq_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[4], eq_group[5]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[5], eq_group[6]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[6], eq_group[7]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[7], eq_group[8]))
        self.wait(2)
        self.play(Create(box_1), Create(box_2))
        self.wait(7)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW)
        self.play(
            Write(final_text),
            ShrinkToCenter(VGroup(problem_group, eq_group, box_1, box_2)),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.shift(DOWN * 4).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))


class DomainRange(Scene):
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
        problem_statement = Tex(
            r"Given that \\[1em] $g(x) = \frac{2\sqrt{x}}{3} + 1$, \\[1em] calculate the domain when \\[0.5em] the range is $6$"
        )
        problem = (
            Tex(r"Calculate Domain given Range")
            .to_edge(UP)
            .scale(1.2)
            .set_color(YELLOW_D)
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = VGroup(
            MathTex(r"g(x) = \frac{2\sqrt{x}}{3} + 1"),
            Tex(r"Range (Output) is $6$"),
            MathTex(r"g(x) = 6"),
            MathTex(r"\Downarrow"),
            MathTex(r"6 = \frac{2\sqrt{x}}{3} + 1"),
            MathTex(r"6 - 1 = \frac{2\sqrt{x}}{3} + 1 - 1"),
            MathTex(r"5 \times 3 = \frac{2\sqrt{x}}{3} \times 3"),
            MathTex(r"\frac{5}{2} = \frac{2\sqrt{x}}{2}"),
            MathTex(r"(\sqrt{x})^2 = \left(\frac{5}{2}\right)^2"),
        ).arrange(DOWN, buff=0.5)
        cancel_1 = MathTex(
            r"5 = \frac{2\sqrt{x}}{3}",
        )
        cancel_1.move_to(eq_group[5])
        cancel_2 = MathTex(
            r"5 = \frac{2\sqrt{x}}{\cancel{3}} \times \cancel{3}",
            tex_template=my_template,
        )
        cancel_2.move_to(eq_group[6])
        cancel_3 = MathTex(r"5 = 2\sqrt{x}")
        cancel_3.move_to(eq_group[6])
        cancel_4 = MathTex(
            r"\frac{5}{2} = \frac{\cancel{2}\sqrt{x}}{\cancel{2}",
            tex_template=my_template,
        )
        cancel_4.move_to(eq_group[7])
        cancel_5 = MathTex(r"\sqrt{x} = \frac{5}{2}")
        cancel_5.move_to(eq_group[7])
        cancel_6 = MathTex(r"x = \frac{225}{4}")
        cancel_6.move_to(eq_group[8])
        cancel_7 = MathTex(r"x = 56.25")
        cancel_7.move_to(eq_group[8])
        rectangle_box = SurroundingRectangle(
            cancel_7, buff=0.2, color=PURE_RED, corner_radius=0.2
        )

        self.play(Write(problem_statement))
        self.wait(2)
        self.play(Transform(problem_statement, problem_group))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Write(eq_group[1]))
        self.wait(2)
        self.play(Write(eq_group[2]))
        self.wait(2)
        self.play(Create(eq_group[3]))
        self.wait(2)
        self.play(Write(eq_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[4], eq_group[5]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[5], cancel_1))
        self.wait(2)
        self.play(TransformFromCopy(cancel_1, eq_group[6]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[6], cancel_2))
        self.wait(2)
        self.play(ReplacementTransform(cancel_2, cancel_3))
        self.wait(2)
        self.play(TransformFromCopy(cancel_3, eq_group[7]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[7], cancel_4))
        self.wait(2)
        self.play(ReplacementTransform(cancel_4, cancel_5))
        self.wait(2)
        self.play(TransformFromCopy(cancel_5, eq_group[8]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[8], cancel_6))
        self.wait(2)
        self.play(ReplacementTransform(cancel_6, cancel_7))
        self.wait(2)
        self.play(Create(rectangle_box))
        self.wait(7)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW)
        self.play(
            Write(final_text),
            ShrinkToCenter(
                VGroup(
                    problem_statement,
                    eq_group,
                    rectangle_box,
                    cancel_1,
                    cancel_2,
                    cancel_3,
                    cancel_4,
                    cancel_5,
                    cancel_6,
                    cancel_7,
                )
            ),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.shift(DOWN * 4).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))


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
            Text("Calculate", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .shift(UP * 3)
        )
        # Subtitle
        subtitle = (
            Tex(r"\text{Domain given Range}").scale(1.5).next_to(title, DOWN, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(r"g(x) = \frac{2\sqrt{x}}{3} + 1", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
