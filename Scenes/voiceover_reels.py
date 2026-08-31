"""
Factorise Completely: 2x^2y - 11xy + 5y
-----------------------------------------
Manim CE scene with manim-voiceover RecorderService, so narration
is recorded live in your own voice as each animation plays.

Run with (draft quality, for checking pacing while you record):
    manim -pql factorise_2x2y_11xy_5y.py FactoriseCompletely

Final render (high quality):
    manim -pqh factorise_2x2y_11xy_5y.py FactoriseCompletely

Note: the first time you run this, RecorderService will prompt you
in the terminal to record each voiceover line. Re-running the scene
reuses cached audio unless you delete it from the voiceover cache
(the .mp3/.json files it creates alongside your project), so re-record
a line by deleting its cached files and running again.
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

# from manim_voiceover.services.recorder import RecorderService


config.frame_rate = 30
config.pixel_width = 1080
config.frame_width = 9
config.pixel_height = 1920
config.frame_height = 16
config.disable_caching = True


class FactoriseCompletely(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(device_index=7, rate=48000))
        # self.set_speech_service(GTTSService(lang="en", transcription_model="base"))

        title = Text("Factorise Completely", font_size=40, color=BLUE).to_edge(UP)

        # -----------------------------------------------------------
        # Step 0: Show the problem
        # -----------------------------------------------------------
        expr = MathTex("2x^2y", "-", "11xy", "+", "5y").scale(1.2)

        with self.voiceover(
            text="Let's factorise completely: 2 x squared y, minus 11 x y, plus 5 y."
        ) as tracker:
            self.play(Write(title), run_time=1)
            self.play(Write(expr), run_time=max(tracker.duration - 1, 1))
        self.wait(0.5)

        # -----------------------------------------------------------
        # Step 1: Take out the common factor y
        # -----------------------------------------------------------
        step1_label = Text(
            "Step 1: Take out the common factor y", font_size=28, color=YELLOW
        ).next_to(expr, DOWN, buff=1)

        with self.voiceover(
            text="Notice that y appears in every term, so we factor it out first."
        ) as tracker:
            self.play(FadeIn(step1_label), run_time=tracker.duration)

        factored_y = MathTex("y", "(", "2x^2", "-", "11x", "+", "5", ")").scale(1.2)

        with self.voiceover(
            text="Taking y out gives us y, times, 2 x squared minus 11 x plus 5."
        ) as tracker:
            self.play(Transform(expr, factored_y), run_time=tracker.duration)
        self.play(FadeOut(step1_label))
        self.wait(0.5)

        self.play(expr.animate.to_edge(UP).shift(DOWN * 1.2))

        # -----------------------------------------------------------
        # Step 2: Split the middle term of the quadratic
        # -----------------------------------------------------------
        step2_label = Text(
            "Step 2: Split the middle term of 2x² - 11x + 5",
            font_size=28,
            color=YELLOW,
        ).next_to(expr, DOWN, buff=0.8)

        with self.voiceover(
            text="Now we factorise the quadratic part, 2 x squared minus 11 x plus 5, "
            "using the split middle term method."
        ) as tracker:
            self.play(FadeIn(step2_label), run_time=tracker.duration)

        explanation = Text(
            "Find two numbers that multiply to 2 x 5 = 10\n"
            "and add up to -11  →  they are -10 and -1",
            font_size=26,
        ).next_to(step2_label, DOWN, buff=0.5)

        with self.voiceover(
            text="We need two numbers whose product is 2 times 5, which is 10, and "
            "whose sum is negative 11. Those numbers are negative 10 and negative 1."
        ) as tracker:
            self.play(Write(explanation), run_time=tracker.duration)
        self.wait(1)

        # working line for the quadratic (kept separate from expr up top)
        work = MathTex("2x^2", "-", "10x", "-", "x", "+", "5").scale(1.1)
        work.next_to(explanation, DOWN, buff=0.6)

        with self.voiceover(
            text="So we rewrite negative 11 x as negative 10 x minus x."
        ) as tracker:
            self.play(Write(work), run_time=tracker.duration)
        self.wait(1)

        self.play(FadeOut(step2_label), FadeOut(explanation))
        self.play(work.animate.move_to(ORIGIN))

        # -----------------------------------------------------------
        # Step 3: Group in pairs and factor each group
        # -----------------------------------------------------------
        step3_label = Text(
            "Step 3: Group in pairs and factor each group",
            font_size=28,
            color=YELLOW,
        ).next_to(work, DOWN, buff=0.8)

        grouped = (
            MathTex("(", "2x^2", "-", "10x", ")", "-", "(", "x", "-", "5", ")")
            .scale(1.1)
            .move_to(work)
        )

        with self.voiceover(
            text="Group the first two terms and the last two terms, being careful "
            "with the minus sign in front of the second group."
        ) as tracker:
            self.play(FadeIn(step3_label), run_time=1)
            self.play(Transform(work, grouped), run_time=max(tracker.duration - 1, 1))
        self.wait(0.5)

        factored_groups = (
            MathTex("2x", "(", "x", "-", "5", ")", "-", "1", "(", "x", "-", "5", ")")
            .scale(1.1)
            .move_to(work)
        )

        with self.voiceover(
            text="From the first group we can take out 2 x, and from the second "
            "group we take out 1."
        ) as tracker:
            self.play(Transform(work, factored_groups), run_time=tracker.duration)
        self.wait(1)
        self.play(FadeOut(step3_label))

        # -----------------------------------------------------------
        # Step 4: Factor out the common bracket, then restore y
        # -----------------------------------------------------------
        quad_factored = MathTex(
            "(", "2x", "-", "1", ")", "(", "x", "-", "5", ")"
        ).scale(1.2)

        with self.voiceover(
            text="Both groups share the common factor, x minus 5, so we factor "
            "that bracket out."
        ) as tracker:
            self.play(Transform(work, quad_factored), run_time=tracker.duration)
        self.wait(1)

        full_answer = MathTex(
            "y", "(", "2x", "-", "1", ")", "(", "x", "-", "5", ")"
        ).scale(1.3)

        with self.voiceover(
            text="Remember the y we factored out right at the start. Bringing it "
            "back gives our fully factorised expression."
        ) as tracker:
            self.play(FadeOut(expr), run_time=0.5)
            self.play(
                Transform(work, full_answer), run_time=max(tracker.duration - 0.5, 1)
            )
        self.play(work.animate.move_to(ORIGIN))
        self.wait(0.5)

        # -----------------------------------------------------------
        # Final answer, boxed
        # -----------------------------------------------------------
        box = SurroundingRectangle(work, color=GREEN, buff=0.3)
        answer_label = Text("Final Answer", font_size=28, color=GREEN).next_to(box, UP)

        with self.voiceover(
            text="So, 2 x squared y minus 11 x y plus 5 y factorises completely to "
            "y, times, 2 x minus 1, times, x minus 5."
        ) as tracker:
            self.play(Create(box), Write(answer_label), run_time=tracker.duration)
        self.wait(2)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# FIRST VOICEOVER REELS PROJECT
# --------------------------------------------------------------------------------------------------------------------------------------------------------
class FirstProject(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(RecorderService(device_index=7, rate=48000))
        self.set_speech_service(GTTSService(lang="en", transcription_model="base"))

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
            r"Solve the equation $2x^2 = x + 7$, \\",
            r"giving your answer to two decimal places",
        )
        title = Tex(r"Solve $2x^2 = x = 7$")
        underline = Underline(title)
        title_group = VGroup(title, underline).to_edge(UP).scale(1.5).set_color(YELLOW)

        # -----------------------------------------------------------------
        # Equation group
        # -----------------------------------------------------------------
        eq_group = VGroup(
            MathTex(r"2x^2 = x + 7"),
            MathTex(r"ax^2 + bx + c = 0"),
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
            Tex(r"$a = 2$,", r"$b = -1$,", r"$c = -7$"),
            MathTex(r"x = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(2)(-7)}}{2(2)}"),
            MathTex(r"x = \frac{1 \pm \sqrt{57}}{4}"),
            MathTex(r"x = \frac{1 + 7.5498}{4} \approx 2.13745"),
            Text(r"or", font_size=40, color=RED),
            MathTex(r"x = \frac{1 - 7.5498}{4} \approx -1.63745"),
            Tex(r"$x = 2.14$", r" \qquad or \qquad", r"$x = -1.64$"),
        ).arrange(DOWN, buff=0.5)

        # -----------------------------------------------------------------

        # -----------------------------------------------------------------
        rectangle_box_1 = SurroundingRectangle(
            eq_group[9][0], buff=0.2, color=PURE_RED, corner_radius=0.2
        )
        rectangle_box_2 = SurroundingRectangle(
            eq_group[9][-1], buff=0.2, color=PURE_RED, corner_radius=0.2
        )
        # -----------------------------------------------------------------

        # -----------------------------------------------------------------
        sub_eq_1 = MathTex(r"2x^2 - x -7 = 0")
        sub_eq_1.move_to(eq_group[1])

        sub_eq_2 = MathTex(r"x = \frac{1 \pm \sqrt{1 + 56}}{4}")
        sub_eq_2.move_to(eq_group[4])

        # -----------------------------------------------------------------

        # -----------------------------------------------------------------
        text = "We are given an equation 2x squared equals x plus 7, we are required to solve for x and give our answer to two decimal places."
        with self.voiceover(text=text) as tracker:
            self.play(Write(problem), run_time=2)
        self.wait()
        self.play(FadeTransform(problem, title_group))
        self.wait()
        self.play(Write(eq_group[0]))

        text = "The first step is to write the equation in a standard form of ax to the power 2 plus bx plus c is equal to zero"

        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[1]), run_time=2)
        self.wait()

        text = (
            "The equation will transform to 2x squared minus x minus 7 is equal to zero"
        )
        with self.voiceover(text=text) as tracker:
            self.play(
                ReplacementTransform(eq_group[1], sub_eq_1), run_time=tracker.duration
            )
        self.wait()

        text = "We will use the quadratic formula"
        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[2]), run_time=tracker.duration)
        self.wait()

        text = "From the equation, a = 2"
        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[3][0]), run_time=tracker.duration)
        self.wait()

        text = "b = -1"
        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[3][1]), run_time=tracker.duration)
        self.wait()

        text = "c = -7"
        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[3][-1]), run_time=tracker.duration)
        self.wait()

        text = "We substitute the values of a, b, and c into the quadratic formula"
        with self.voiceover(text=text):
            self.play(Write(eq_group[4]), run_time=2)
            self.play(ReplacementTransform(eq_group[4], sub_eq_2), run_time=1)
        self.wait()

        text = f"The equation simplifies to {MathTex(r'x = \frac{1 \pm \sqrt{57}}{4}')}"
        with self.voiceover(text=text) as tracker:
            self.play(
                TransformFromCopy(sub_eq_2, eq_group[5]), run_time=tracker.duration
            )
        self.wait()

        text = "Since the squareroot of 57 is equivalent to 7.5498, we get x is equal to 1 plus 7.5498 over 4 which is approximately 2.17745"
        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[6]))
        self.wait()

        text = "or x equals 1 minus 7.5498 over 4 which is approximately -1.63745"
        with self.voiceover(text=text) as tracker:
            self.play(
                FadeIn(eq_group[7]), Write(eq_group[8]), run_time=tracker.duration
            )
        self.wait()

        text = "Therefore, our final answer to two decimal places are x = 2.14 or x = -1.64"
        with self.voiceover(text=text) as tracker:
            self.play(Write(eq_group[9], run_time=2))
            self.play(Create(rectangle_box_1), run_time=1)
            self.play(Create(rectangle_box_2), run_time=1)
        self.wait()

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
                    problem,
                    rectangle_box_1,
                    rectangle_box_2,
                    sub_eq_1,
                    sub_eq_2,
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


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Thumbnail
# --------------------------------------------------------------------------------------------------------------------------------------------------------
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
            Text("Solve", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .shift(UP * 3)
        )
        # Subtitle
        subtitle = (
            Tex(r"\text{for} \textbf{x}").scale(1.5).next_to(title, DOWN, buff=0.75)
        )

        # Formula
        formula = (
            MathTex(
                r"2^{2x} + 32 = 3(2^{x + 2})",
                color=WHITE,
            )
            .scale(1.5)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
