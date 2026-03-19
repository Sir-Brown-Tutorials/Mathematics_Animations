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
        self.play(TransformFromCopy(eq_group[7], eq_group[8]))
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
            Text("Solve for", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .to_edge(UP)
        )
        # Subtitle
        subtitle = (
            Tex(r"$k$ \text{in algebraic formula}")
            .scale(1.5)
            .next_to(title, DOWN * 5, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(r"x = \frac{b - k^3}{k^3}", color=WHITE)
            .scale(1.7)
            .next_to(subtitle, DOWN * 5, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
