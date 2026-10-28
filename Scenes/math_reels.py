from typing import override

from manim import *

config.frame_rate = 30
config.pixel_width = 1080
config.frame_width = 9
config.pixel_height = 1920
config.frame_height = 16
config.disable_caching = True


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# FIRST MATH REEL PROJECT
# --------------------------------------------------------------------------------------------------------------------------------------------------------
class FirstMathReel(Scene):
    @override
    def construct(self):

        # -----------------------------------------------------------------
        # Create a custom Latex template that includes the cancel package
        # -----------------------------------------------------------------
        my_template = TexTemplate()
        my_template.add_to_preamble(r"\usepackage{xcolor}")
        my_template.add_to_preamble(r"\usepackage{cancel}")
        my_template.add_to_preamble(r"\renewcommand{\CancelColor}{\color{red}}")

        # -----------------------------------------------------------------
        # Load and position logo image
        # -----------------------------------------------------------------
        logo = ImageMobject("../Images/sir_brown_logo_trans.png")
        logo_corner = logo.scale(0.15)
        logo_corner.to_corner(DR, buff=-0.1)
        self.add(logo_corner)

        # -----------------------------------------------------------------
        # Problem Statement
        # -----------------------------------------------------------------
        problem = Tex(
            r"Simplify $\frac{3b}{y+b} + \frac{2b}{y-b} - \frac{6b^2}{b^2 - y^2}$",
        )
        problem[-1].scale(1.5)
        title = Tex(
            r"Simplify $\frac{3b}{y+b} + \frac{2b}{y-b} - \frac{6b^2}{b^2 - y^2}$",
        )
        underline = Underline(title)
        title_group = VGroup(title, underline).to_edge(UP).scale(1.25).set_color(YELLOW)

        # -----------------------------------------------------------------
        # Equation group
        # -----------------------------------------------------------------
        eq_group = VGroup(
            MathTex(
                r"\frac{3b}{y+b} ",
                r" \;+ \frac{2b}{y-b}\;",
                r"- \frac{6b^2}{b^2 - y^2}",
            ),
            MathTex(r"\frac{3b}{y+b} + \frac{2b}{y-b} + \frac{6b^2}{(y+b)(y-b)}"),
            MathTex(r"\frac{3by - 3b^2 + 2by + 2b^2 + 6b^2}{(y+b)(y-b)}"),
            MathTex(r"\frac{5by + 5b^2}{(y+b)(y-b)}"),
            MathTex(r"\frac{5b(y+b)}{(y+b)(y-b)}"),
            MathTex(r"\frac{5b}{y-b}"),
        ).arrange(DOWN, buff=0.75)

        # -----------------------------------------------------------------
        # Adding Braces and their labels
        # -----------------------------------------------------------------
        eq_1 = MathTex(
            r"-\frac{6b^2}{b^2-y^2} = - \frac{6b^2}{-(y-b)(y+b)} = +\frac{6b^2}{(y-b)(y+b)}"
        ).scale(0.75)
        eq_1.move_to(eq_group[1])

        eq_2 = MathTex(r"\frac{3b(y-b) + 2b(y+b) + 6b^2}{(y+b)(y-b)}")
        eq_2.move_to(eq_group[2])

        eq_3 = MathTex(
            r"\frac{5b\cancel{(y+b)}}{\cancel{(y+b)}(y-b)}",
            tex_template=my_template,
        )
        eq_3.move_to(eq_group[4])

        # eq_4 = MathTex(r"\sqrt{y^2} = \pm \sqrt{\frac{am}{b - m}}")
        # eq_4.move_to(eq_group[6])
        #
        rectangle_box_1 = SurroundingRectangle(
            eq_group[5], buff=0.2, color=PURE_RED, corner_radius=0.2
        )
        # rectangle_box_2 = SurroundingRectangle(
        #     eq_group[0][-1], buff=0.1, color=PURE_YELLOW
        # )
        #
        # arrow_1 = CurvedArrow(
        #     eq_group[1][0].get_top(),
        #     eq_group[1][2].get_top(),
        #     angle=-TAU / 4,
        #     color=PURE_GREEN,
        # )
        # arrow_2 = CurvedArrow(
        #     eq_group[1][0].get_top(),
        #     eq_group[1][4].get_top(),
        #     angle=-TAU / 4,
        #     color=PURE_BLUE,
        # )
        # -----------------------------------------------------------------
        # Animations
        # -----------------------------------------------------------------
        self.play(Write(problem), run_time=2)
        self.wait(2)
        self.play(FadeTransform(problem, title_group))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Circumscribe(eq_group[0][-1], shape=Rectangle))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[0][-1], eq_1))
        self.wait(2)
        self.play(ReplacementTransform(eq_1, eq_group[1]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[1], eq_2))
        self.wait(2)
        self.play(ReplacementTransform(eq_2, eq_group[2]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[3], eq_group[4]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[4], eq_3))
        self.wait(2)
        self.play(TransformFromCopy(eq_3, eq_group[5]))
        self.wait(2)
        self.play(Create(rectangle_box_1))
        self.wait(2)

        # -----------------------------------------------------------------
        # Outro
        # -----------------------------------------------------------------
        final_text = Tex("Thank you for watching!", color=YELLOW)
        self.play(
            Write(final_text),
            ShrinkToCenter(
                VGroup(
                    title_group,
                    eq_group,
                    # eq_1,
                    # eq_2,
                    eq_3,
                    # eq_4,
                    rectangle_box_1,
                    # rectangle_box_2,
                    # arrow_1,
                    # arrow_2,
                )
            ),
        )
        self.wait()
        self.play(logo_corner.animate.move_to(ORIGIN).scale(3), FadeOut(final_text))
        self.wait()
        self.play(ShrinkToCenter(logo_corner))


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Thumbnail
# --------------------------------------------------------------------------------------------------------------------------------------------------------
class Thumbnail(Scene):
    @override
    def construct(self):
        # Add background image
        background = ImageMobject("../Images/chalk_board.jpg")
        background.set_z_index(-1)
        background.scale_to_fit_height(config.frame_height)
        background.scale_to_fit_width(config.frame_width)
        self.add(background)

        # Title text
        title = (
            Text("Simplify", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .shift(UP * 3)
        )
        # Subtitle
        subtitle = (
            Tex(r"\text{the following}").scale(1.5).next_to(title, DOWN, buff=0.3)
        )

        # Formula
        formula = (
            MathTex(
                r"\frac{3b}{y+b} + \frac{2b}{y-b} - \frac{6b^2}{b^2 - y^2}", color=WHITE
            )
            .scale(1.5)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
