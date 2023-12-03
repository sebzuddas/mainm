from manim import *

delta = 1e-3  # Small delta for floating-point comparison
dot_color = {"color": BLUE_A}  # Dictionary to hold the color
fade_time = 3.75

# Set the configuration for the scene's aspect ratio
config.frame_width = 9
config.frame_height = 16
config.pixel_height = 1080
config.pixel_width = round(1920 // (16 / 9) * (9 / 16))  # Adjusting to maintain resolution




# Update the dot based on the condition
def update_static_dots(dots, theta):
    theta_mod = theta % (2 * PI)
    for n, static_dot in enumerate(dots):
        if np.isclose(theta_mod, n * (PI / 8), atol=1e-3):
            static_dot.set_opacity(100)  # Change color instead of redrawing
        else:
            static_dot.set_opacity(0)  # Reset color


# Function to create static dots
def create_static_dots(plane):
    dots = VGroup()
    for n in range(0, 17):
        point = plane.n2p(np.exp(complex(0, n * (PI / 8))))
        dot = Dot(point, stroke_width=4, color=RED, fill_opacity=0)
        dots.add(dot)
        dot.fade_time = 0

        
    return dots

class EulersIdentity(Scene):
    def construct(self):
        test = 1
        test = 22
        fade_time = 3.75*8

        plane = ComplexPlane(
            x_range=[-1, 1, 1],
            y_range=[-1, 1, 1]
        ).scale(3.5)  # Scale based on height of frame

        theta_tracker = ValueTracker(0) #Tracks the angle

        ##################################################
        self.add(plane)

        # Add arrows to the end of the axes lines
        plane.add(plane.get_horizontal_line(plane.c2p(plane.x_range[1], 0)).add_tip())
        plane.add(plane.get_vertical_line(plane.c2p(0, plane.y_range[1])).add_tip())

        # Add 'Re' and 'Im' labels to the axes
        plane.add(MathTex("\Re").next_to(plane.get_x_axis().get_end(), DOWN))
        plane.add(MathTex("\Im").next_to(plane.get_y_axis().get_end(), DR))

        # Create a DecimalNumber object to display the value of theta
        theta_value = DecimalNumber(
            theta_tracker.get_value(),
            num_decimal_places=2,  # Number of decimal places to display
            include_sign=False,    # Whether to include the + sign for positive numbers
            unit=" rad",           # The unit to display after the number
        )

        theta_value.add_updater(lambda v: v.set_value(theta_tracker.get_value() % (2 * PI)))

        euler_formula_text = MathTex(r"e^{i \theta} \ | \ \theta = {}")
        euler_formula = VGroup(euler_formula_text, theta_value)
        theta_value.next_to(euler_formula_text, RIGHT)
        euler_formula.to_edge(DOWN)
        
        complex_point = always_redraw(
            lambda: Dot(
                plane.n2p(np.exp(complex(0, theta_tracker.get_value()))),
                color=BLUE,
                stroke_width=2
            )
        )

        # # Update this updater to pass the static dots as well
        # complex_point.add_updater(update_complex_point)

        line_to_origin = always_redraw(
            lambda: Line(
                start=plane.c2p(0, 0),  # Origin point
                end=complex_point.get_center(),  # End at the complex point
                color=WHITE,  # Color of the line
                stroke_width=0.5,  # Thickness of the line
            )
        )

        # tracer = TracedPath(complex_point.get_center, stroke_width=4, stroke_color=RED_B)

        self.add(complex_point)
        self.add(line_to_origin)
        
        # Add it to the scene
        self.add(theta_value)
        self.add(euler_formula)

        # THIS NEEDS FIXING
        def update_static_dot(dot, dt, n, spinning_dot_theta, fade_out_time=fade_time):
            # The angle difference at which the dot starts to fade out

            spinning_dot_theta_value = spinning_dot_theta.get_value() % (2 * PI)

            start_fade_angle_diff = 0

            # The angle at which the dot is fully lit
            lit_angle_diff = PI / 16
            
            static_dot_theta = n * (PI / 8)  # where n is an integer from 0 to 7


            angle_diff = min(
                abs(static_dot_theta - spinning_dot_theta_value),
                2 * PI - abs(static_dot_theta - spinning_dot_theta_value)
            )
                        
            # If the spinning dot is approaching the static dot
            if angle_diff <= start_fade_angle_diff:
                # Calculate how close the spinning dot is to the static dot
                # where 0 means it's directly at the static dot's position
                # and 1 means it's just starting to fade in or out
                proximity = angle_diff / lit_angle_diff
                proximity = min(max(proximity, 0), 1)  # Clamp the value between 0 and 1

                # Interpolate opacity based on the proximity, where 0 means full opacity
                opacity = 1 - proximity
                dot.set_opacity(opacity)
                dot.fade_time = fade_out_time  # Reset fade time when dot turns red

            # Handle fading out the dot once the spinning dot has passed
            if dot.fade_time > 0:
                dot.fade_time -= dt  # Decrease fade time based on the time passed
                new_opacity = dot.fade_time / fade_out_time  # Calculate new opacity
                dot.set_opacity(max(new_opacity, 0))  # Ensure opacity isn't less than 0
            else:
                dot.set_opacity(0)  # If fade time is up, make dot fully transparent

        static_dots = create_static_dots(plane)
        self.add(static_dots)

        for n, dot in enumerate(static_dots):
            dot.add_updater(lambda d, dt, n=n: update_static_dot(d, dt, n, theta_tracker))
        
        self.play(
            theta_tracker.animate.increment_value(4 * 2 * PI),  # Four full rotations
            run_time=240,  # Assuming you want each rotation to be 60 seconds
            rate_func=linear
        )


         # Remember to remove the static dots' updaters at the end of the animation
        for dot in static_dots:
            dot.remove_updater(lambda d, dt, n=n: update_static_dot(d, dt, n, theta_tracker))
        

