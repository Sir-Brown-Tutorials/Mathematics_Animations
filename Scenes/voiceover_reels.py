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
from manim_voiceover.services.recorder import RecorderService

config.frame_rate = 30
config.pixel_height = 1080
config.pixel_width = 1920


class FactoriseCompletely(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService(device_index=7, rate=48000))

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
