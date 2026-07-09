from manim import *

config.frame_width = 16
config.frame_height = 9
config.frame_rate = 30
config.disable_caching = True


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
            Text("Factorise", font="Roboto", weight=BOLD, color=YELLOW)
            .scale(1.5)
            .shift(UP * 3)
        )
        # Subtitle
        subtitle = Tex(r"\text{completely}").scale(1.5).next_to(title, DOWN, buff=0.75)

        # Formula
        formula = (
            MathTex(
                r"2a^3 - 14a^2 + 24a",
                color=WHITE,
            )
            .scale(1.5)
            .next_to(subtitle, DOWN, buff=1)
        )

        # Add everything
        self.add(title, subtitle, formula)
