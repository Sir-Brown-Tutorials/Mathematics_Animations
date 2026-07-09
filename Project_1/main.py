from manim import *

config.frame_width = 16
config.frame_height = 9
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

        self.play(Write(problem_group[0]))
        self.wait(2)
        self.play(problem_group.animate.to_edge(UP).scale(1.5).set_color(YELLOW))
        self.wait(5)

        # Outro
        final_text = Tex("Thank you for watching!", color=YELLOW)
        self.play(
            Write(final_text),
            ShrinkToCenter(VGroup(problem_group)),
        )
        self.wait()
        self.play(
            logo_corner.animate.move_to(ORIGIN).scale(3),
            final_text.animate.shift(DOWN * 4).set_color(WHITE).scale(1.3),
        )
        self.wait()
        self.play(FadeOut(final_text, logo_corner))
