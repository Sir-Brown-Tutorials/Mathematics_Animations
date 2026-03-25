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


class VectorSubtraction(Scene):
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
            r"Given that \\[1em] $\vec{a} = \begin{pmatrix} 2 \\[1em] 6 \end{pmatrix}$ and $\vec{b} = \begin{pmatrix} -8 \\[1em] 3 \end{pmatrix}$, \\[1em]"
            r"find the value of \\[1em] $\frac{1}{2}(\vec{a} - \vec{b})$."
        )
        problem = (
            Tex(r"Subtration of Vectors").to_edge(UP).scale(1.2).set_color(YELLOW_D)
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = VGroup(
            MathTex(
                r"\vec{a} = \begin{pmatrix} 2 \\[1em] 6 \end{pmatrix}",
                r"\qquad",
                r"\vec{b} = \begin{pmatrix} -8 \\[1em] 3 \end{pmatrix}",
            ),
            Tex(r"Find $\frac{1}{2}(\vec{a} - \vec{b})$"),
            MathTex(r"\vec{a} - \vec{b}"),
            MathTex(
                r"\vec{a} - \vec{b} = \begin{pmatrix} 2 \\[1em] 6 \end{pmatrix} - \begin{pmatrix} -8 \\[1em] 3 \end{pmatrix}"
            ),
            MathTex(r"\vec{a} - \vec{b} = \begin{pmatrix} 10 \\[1em] 3 \end{pmatrix}"),
            MathTex(
                r"\frac{1}{2}(\vec{a} - \vec{b}) = \frac{1}{2}\begin{pmatrix} 10 \\[1em] 3 \end{pmatrix}"
            ),
            MathTex(r"\begin{pmatrix} 5 \\[1em] \frac{3}{2} \end{pmatrix}"),
        ).arrange(DOWN, buff=0.5)
        rectangle_box = SurroundingRectangle(
            eq_group[6], buff=0.2, color=PURE_RED, corner_radius=0.2
        )

        cancel_1 = MathTex(
            r"\vec{a} - \vec{b} = \begin{pmatrix} 2 & - & (-8) \\[1em] 6 & - & 3 \end{pmatrix}",
        )
        cancel_1.move_to(eq_group[3])
        cancel_2 = MathTex(
            r"\frac{1}{2}(\vec{a} - \vec{b}) = \begin{pmatrix} 5 \\[1em] \frac{3}{2} \end{pmatrix}"
        )
        cancel_2.move_to(eq_group[5])

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
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[3], cancel_1))
        self.wait(2)
        self.play(TransformFromCopy(cancel_1, eq_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[4], eq_group[5]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[5], cancel_2))
        self.wait(2)
        self.play(TransformFromCopy(cancel_2, eq_group[6]))
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


class Quadratic_1(Scene):
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
            r"Factorise completely \\[1em] $10 + 8m - 24m^2$"
        ).scale(1.35)
        problem = (
            Tex(r"Factorise $10 + 8m - 24m^2$")
            .to_edge(UP)
            .scale(1.35)
            .set_color(YELLOW_D)
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = (
            VGroup(
                MathTex(r"10 + 8m - 24m^2"),
                MathTex(r"\Downarrow"),
                MathTex(r"-24m^2 + 8m + 10"),
                MathTex(r"-2", r"(", r"12m^2 - 4m - 5", r")"),
                MathTex(r"12m^2 - 4m - 5"),
                MathTex(r"12m^2 - 10m", r"+ 6m - 5"),
                MathTex(r"(12m^2 - 10m)", r"+(6m - 5)"),
                MathTex(r"2m", r"(6m - 5)", r"+1", r"(6m- 5)"),
                MathTex(r"(2m + 1)", r"(6m - 5)"),
                MathTex(r"-2", r"(2m + 1)", r"(6m - 5)"),
            )
            .arrange(DOWN, buff=0.6)
            .scale(1.2)
        )
        rectangle_box = SurroundingRectangle(
            eq_group[9], buff=0.2, color=PURE_RED, corner_radius=0.2
        )
        box_1 = SurroundingRectangle(eq_group[3][0])

        # cancel_1 = MathTex(
        #    r"\frac{20}{4} = \frac{\cancel{4}k}{\cancel{4}}",
        #   tex_template=my_template,
        # )
        # cancel_1.move_to(eq_group[10])
        # cancel_2 = MathTex(
        #    r"\frac{1}{2}(\vec{a} - \vec{b}) = \begin{pmatrix} 5 \\[1em] \frac{3}{2} \end{pmatrix}"
        # )
        # cancel_2.move_to(eq_group[5])

        self.play(Write(problem_statement))
        self.wait(2)
        self.play(Transform(problem_statement, problem_group))
        self.wait(2)
        self.play(Write(eq_group[0]))
        self.wait(2)
        self.play(Create(eq_group[1]))
        self.wait(2)
        self.play(Write(eq_group[2]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[2], eq_group[3]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[3][2], eq_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[4], eq_group[5]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[5][0], eq_group[6][0]))
        self.wait()
        self.play(TransformFromCopy(eq_group[5][-1], eq_group[6][1]))
        self.wait()
        self.play(TransformFromCopy(eq_group[6][0], eq_group[7][:2]))
        self.wait()
        self.play(TransformFromCopy(eq_group[6][1], eq_group[7][-2:]))
        self.wait()
        self.play(
            TransformFromCopy(VGroup(eq_group[7][0], eq_group[7][2]), eq_group[8][0])
        )
        self.wait()
        self.play(
            TransformFromCopy(VGroup(eq_group[7][1], eq_group[7][3]), eq_group[8][1])
        )
        self.wait()
        self.play(Create(box_1))
        self.wait()
        self.play(TransformFromCopy(eq_group[3][0], eq_group[9][0]), FadeOut(box_1))
        self.wait()
        self.play(TransformFromCopy(eq_group[8][0], eq_group[9][1]))
        self.wait()
        self.play(TransformFromCopy(eq_group[8][-1], eq_group[9][2]))
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
                    # cancel_1,
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


class Polynomial(Scene):
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
            r"When a Polynomial $x^3 + 5x^2 - 4x + k$ \\[0.5em] is divided by $(x - 2)$, \\[0.5em] the remainder is $5k$. \\[0.5em] Calculate the value of $k$"
        )
        problem = (
            Tex(r"Remainder Theorem of Polynomials")
            .to_edge(UP)
            .scale(1)
            .set_color(YELLOW_D)
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)
        eq_group = VGroup(
            Tex(
                r"When a Polynomial $f(x)$ is divided \\ by $(x - a)$, the remainder is $f(a)$"
            ),
            MathTex(r"f(x) = x^3 + 5x^2 - 4x + k"),
            MathTex(r"\Downarrow"),
            MathTex(r"(x - 2) \quad \Longrightarrow \quad x = 2 "),
            MathTex(r"f(2) = 2^3 + 5(2)^2 - 4(2) + k"),
            MathTex(r"f(2) = 8 + 20 - 8 + k"),
            MathTex(r"f(2) = 20 + k = 5k"),
            MathTex(r"20 + k = 5k"),
            MathTex(r"20 + k - k = 5k - k"),
            MathTex(r"20 = 4k"),
            MathTex(r"\frac{20}{4} = \frac{4k}{4}"),
            MathTex(r"k = 5"),
        ).arrange(DOWN, buff=0.5)
        rectangle_box = SurroundingRectangle(
            eq_group[11], buff=0.2, color=PURE_RED, corner_radius=0.2
        )

        cancel_1 = MathTex(
            r"\frac{20}{4} = \frac{\cancel{4}k}{\cancel{4}}",
            tex_template=my_template,
        )
        cancel_1.move_to(eq_group[10])
        # cancel_2 = MathTex(
        #    r"\frac{1}{2}(\vec{a} - \vec{b}) = \begin{pmatrix} 5 \\[1em] \frac{3}{2} \end{pmatrix}"
        # )
        # cancel_2.move_to(eq_group[5])

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
        self.play(Write(eq_group[3]))
        self.wait(2)
        self.play(Write(eq_group[4]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[4], eq_group[5]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[5], eq_group[6]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[6], eq_group[7]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[7], eq_group[8]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[8], eq_group[9]))
        self.wait(2)
        self.play(TransformFromCopy(eq_group[9], eq_group[10]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group[10], cancel_1))
        self.wait(2)
        self.play(TransformFromCopy(cancel_1, eq_group[11]))
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


class Matrix_1(Scene):
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
            r"Given that \\[1em] $A = \begin{bmatrix} 3 & 15 \\ 9 & 12 \end{bmatrix}$ and $B = \begin{bmatrix} 1 & 3 \\ 4 & -2 \end{bmatrix}$,",
            r"\\[1em] find \\[0.5em] $\frac{1}{3}A - B^2$",
        )
        problem = (
            Tex(r"Matrix Calculations").to_edge(UP).scale(1.2).set_color(PURE_YELLOW)
        )
        underline = Underline(problem)
        problem_group = VGroup(problem, underline)

        eq_group_1 = (
            VGroup(
                Tex(
                    r"$A = \begin{bmatrix} 3 & 15 \\ 9 & 12 \end{bmatrix}$, \qquad"
                    r"$B = \begin{bmatrix} 1 & 3 \\ 4 & -2 \end{bmatrix}$"
                ),
                Tex(r"find $\frac{1}{3}A - B^2$"),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(problem_group, DOWN * 2)
        )

        eq_group_2 = (
            VGroup(
                Tex(r"1. Compute $\mathbf{\frac{1}{3}A}$").set_color(YELLOW_B),
                MathTex(
                    r"\frac{1}{3}A = ",
                    r"\frac{1}{3}\begin{bmatrix} 3 & 15 \\[1em] 9 & 12 \end{bmatrix}",
                ),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(eq_group_1, DOWN * 3)
        )

        eq_group_3 = (
            VGroup(
                Tex(r"2. Compute $\mathbf{B^2}$").set_color(YELLOW_B),
                MathTex(r"B^2 = B \times B"),
            )
            .arrange(DOWN, buff=1)
            .next_to(eq_group_2, DOWN * 3)
        )

        eq_group_4 = (
            VGroup(
                Tex(r"1. Compute $\mathbf{\frac{1}{3}A - B^2}$").set_color(YELLOW_B),
                MathTex(
                    r"\frac{1}{3}A",
                    r" - ",
                    r"B^2",
                    r" = ",
                    r"\begin{bmatrix} 1 & 6 \\[1em] 3 & 4 \end{bmatrix}",
                    r" - ",
                    r"\begin{bmatrix} 13 & -3 \\[1em] -4 & 16 \end{bmatrix}",
                ),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(eq_group_3, DOWN * 4)
        )
        sub_1 = MathTex(
            r"\frac{1}{3}A = \begin{bmatrix} \frac{1}{3}(3) & \frac{1}{3}(15) \\[1em] \frac{1}{3}(9) & \frac{1}{3}(12) \end{bmatrix}",
        )
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
        sub_1.move_to(eq_group_2[1])
        sub_2 = MathTex(
            r"\frac{1}{3}A",
            r" = ",
            r"\begin{bmatrix} 1 & 6 \\[1em] 3 & 4 \end{bmatrix}",
        )
        sub_2.move_to(eq_group_2[1])
        box_1 = SurroundingRectangle(sub_2[0])
        box_2 = SurroundingRectangle(sub_2[-1])
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
        sub_3 = MathTex(
            r"B^2 = \begin{bmatrix} 1 & 3 \\[1em] 4 & -2 \end{bmatrix} \times \begin{bmatrix} 1 & 3 \\[1em] 4 & -2 \end{bmatrix}"
        )
        sub_3.move_to(eq_group_3[1])
        sub_4 = MathTex(
            r"B^2 = \begin{bmatrix} 1(1)+3(4) & 1(3)+3(-2) \\[1em] 4(1)+(-2)(4) & 4(3)+(-2)(-2) \end{bmatrix}",
        )
        sub_4.move_to(eq_group_3[1])
        sub_5 = MathTex(
            r"B^2 = \begin{bmatrix}1+12 & 3-6 \\[1em] 4-8 & 12+4 \end{bmatrix}"
        )
        sub_5.move_to(eq_group_3[1])
        sub_6 = MathTex(
            r"B^2", r" = ", r"\begin{bmatrix} 13 & -3 \\[1em] -4 & 16 \end{bmatrix}"
        )
        sub_6.move_to(eq_group_3[1])
        box_3 = SurroundingRectangle(sub_6[0])
        box_4 = SurroundingRectangle(sub_6[-1])
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
        sub_7 = MathTex(
            r"\frac{1}{3}A - B^2 = \begin{bmatrix} 1-3 & 5-(-3) \\[1em] 3-(-4) & 4-16 \end{bmatrix}"
        )
        sub_7.move_to(eq_group_4[1])
        sub_8 = MathTex(
            r"\frac{1}{3}A",
            r" - ",
            r"B^2",
            r" = ",
            r"\begin{bmatrix} -12 & 8 \\[1em] 7 & -12 \end{bmatrix}",
        )
        sub_8.move_to(eq_group_4[1])
        rectangle_box = SurroundingRectangle(
            sub_8[-1], buff=0.2, color=PURE_RED, corner_radius=0.2
        )

        self.play(Write(problem_statement))
        self.wait(2)
        self.play(Transform(problem_statement, problem_group))
        self.wait(2)
        self.play(Write(eq_group_1[0]))
        self.wait(2)
        self.play(Write(eq_group_1[1]))
        self.wait(2)

        self.play(Write(eq_group_2[0]))
        self.wait(2)
        self.play(Write(eq_group_2[1]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group_2[1], sub_1))
        self.wait(2)
        self.play(ReplacementTransform(sub_1, sub_2))
        self.wait(2)

        self.play(Write(eq_group_3[0]))
        self.wait(2)
        self.play(Write(eq_group_3[1]))
        self.wait(2)
        self.play(ReplacementTransform(eq_group_3[1], sub_3))
        self.wait(2)
        self.play(ReplacementTransform(sub_3, sub_4))
        self.wait(2)
        self.play(ReplacementTransform(sub_4, sub_5))
        self.wait(2)
        self.play(ReplacementTransform(sub_5, sub_6))
        self.wait(2)

        self.play(Write(eq_group_4[0]))
        self.wait(2)
        self.play(Create(box_1))
        self.wait()
        self.play(TransformFromCopy(sub_2[0], eq_group_4[1][0]), FadeOut(box_1))
        self.wait()
        self.play(Create(box_3))
        self.wait()
        self.play(
            TransformFromCopy(sub_6[0], eq_group_4[1][2]),
            FadeOut(box_3),
            FadeIn(VGroup(eq_group_4[1][1], eq_group_4[1][3])),
        )
        self.wait()
        self.play(Create(box_2))
        self.wait()
        self.play(TransformFromCopy(sub_2[-1], eq_group_4[1][-3]), FadeOut(box_2))
        self.wait()
        self.play(Create(box_4))
        self.wait()
        self.play(
            TransformFromCopy(sub_6[-1], eq_group_4[1][-1]),
            FadeOut(box_4),
            FadeIn(eq_group_4[1][-2]),
        )
        self.wait(2)
        self.play(ReplacementTransform(eq_group_4[1], sub_7))
        self.wait(2)
        self.play(ReplacementTransform(sub_7, sub_8))
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
                    eq_group_1,
                    eq_group_2[0],
                    eq_group_3[0],
                    eq_group_4[0],
                    rectangle_box,
                    sub_8,
                    sub_2,
                    sub_6,
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
            Text("Calculating", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .shift(UP * 3)
        )
        # Subtitle
        subtitle = Tex(r"\text{Matrices}").scale(1.5).next_to(title, DOWN, buff=0.3)

        # Formula
        formula = (
            Tex(
                r",\text{Find} \frac{1}{3}A - B^2",
                color=WHITE,
            )
            .scale(1.5)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
