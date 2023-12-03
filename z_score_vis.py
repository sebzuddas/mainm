from manim import *

class ZScoreVisualization(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=(-3, 3),
            y_range=(0, 0.5),
            axis_config={"color": BLUE},
        )

        square = Square()
        square.rotate(PI/4)

        # Create a Gaussian curve
        gauss_curve = axes.plot(lambda x: 1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * x**2), color=WHITE)

        # Create a z-score marker
        z_marker = Line(3*LEFT, 3*LEFT, color=RED)

        # Add text labels
        mean_label = Text("Mean", color=BLUE).next_to(axes.x_axis, DOWN)
        z_label = Text("Z-Score", color=RED).next_to(z_marker, UP)

        # Add everything to the scene
        self.play(Create(axes), Create(gauss_curve))
        self.play(Transform(square, gauss_curve))
        self.play(Create(z_marker), Write(mean_label), Write(z_label))
        self.wait(2)

