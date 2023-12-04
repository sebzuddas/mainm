from manim import *
import random
import functions

class ZScoreVisualization(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=(-1, 6),
            y_range=(0, 12),
            axis_config={"color": WHITE},
        )

        # BAU and Model Outputs
        b = [random.randint(0, 10) for _ in range(5)]
        y = [random.randint(0, 10) for _ in range(5)]

        # Create dots for b and y
        dots_b = [Dot(axes.c2p(i, val), color=RED) for i, val in enumerate(b, start=1)]
        dots_y = [Dot(axes.c2p(i, val), color=BLUE) for i, val in enumerate(y, start=1)]

        # Create vertical lines between b and y (deviations)
        lines = [Line(start=dots_b[i].get_center(), end=dots_y[i].get_center(), color=GREEN) for i in range(len(b))]

        # Create text labels for b, y and d
        labels_b = [Text(f"b{i+1}", font_size=24).next_to(dot, RIGHT) for i, dot in enumerate(dots_b)]
        labels_y = [Text(f"y{i+1}", font_size=24).next_to(dot, LEFT) for i, dot in enumerate(dots_y)]
        labels_d = [Text(f"d{i+1}", font_size=24).next_to(line, RIGHT) for i, line in enumerate(lines)]
        



        # Add plots and lines to the scene
        self.play(Create(axes))
        self.play(*[Create(dot) for dot in dots_b + dots_y])
        self.wait(1)
        self.play(*[Write(label) for label in labels_b + labels_y + labels_d])
        self.wait(1)
        self.play(*[Create(line) for line in lines])
        self.wait(1)


