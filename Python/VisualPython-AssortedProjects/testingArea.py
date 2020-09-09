import turtle, random, time
import BeginnerProjects, FunctionFocusedProjects
import IntermediateProjects, RecursiveProjects, IteratorProjects
import SpecialTurtles

########################################################################################################
# Uncomment a chunk of code, and hit run to see it in action.
# Certain chunks are one-liners, others are larger so you can experiment.
########################################################################################################

# # Any one of these will run in isolation:
# BeginnerProjects.DrawShape.draw_now()
# BeginnerProjects.DrawThreeShapes.draw_now()
# BeginnerProjects.DrawOverlappingShapes.draw_now()
# BeginnerProjects.StickHouseChallenge.draw_now(size=200)
# BeginnerProjects.PolygonFromUser.draw_now()
# BeginnerProjects.NestedShapes.draw_now(shapes=7, sides=4)
# BeginnerProjects.DrawSquareSpiral.draw_now()
# BeginnerProjects.DrawSquareSpiral.draw_doubled_version()
# BeginnerProjects.FlagPole.draw_now(image_address="flag.gif", flag_x=-22, flag_y=120)
    # Flag needs to be told its center XY coords. Default turtle can't change/read image sizes.
# BeginnerProjects.StampArt.draw_now()
# BeginnerProjects.StampedSpiral.draw_now()
# BeginnerProjects.AgeGroupTurtle.draw_now()
# BeginnerProjects.Slinky.draw_now()
# BeginnerProjects.Star.draw_now(size=200, edges=5, bgcolor="midnight blue", turtle_color="gold")
# BeginnerProjects.Minion.draw_now() # The minion is a long project, but isn't very complicated if you break it up.
# BeginnerProjects.ClockFace.draw_now(size=250, hours=2, minutes=30)
# BeginnerProjects.DrawGrassTuft.draw_now()
# BeginnerProjects.Bubbles.draw_now()
# BeginnerProjects.DrawGradientBackground.draw_now()
# BeginnerProjects.ColourPalette.draw_now(pixels_between_stamps=3)
# BeginnerProjects.TwoValueBarGraph.draw_now(value1=0.3, value2=0.7, scaling_factor=100)
# BeginnerProjects.DrawBarGraph.draw_now(data = [20, 51, 105, 156, 201, 275, 180, -75, -150, 10])
BeginnerProjects.SolarSystem.draw_now()
# BeginnerProjects.Spear.draw_now()  # Similar structure to the GradientBackground project - but with a start and end
# BeginnerProjects.DrawMedicCross.draw_now()
# BeginnerProjects.Wormhole.draw_now()
# BeginnerProjects.SnailShell.draw_now()
# BeginnerProjects.SnailShell.draw_now(colors=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
# BeginnerProjects.BrickWall.draw_now()
# BeginnerProjects.DrawPencilLead.draw_now()
# BeginnerProjects.DrawCircleOfCircles.draw_now(debug_mode=False, circles=12)
# BeginnerProjects.TruthTable.draw_now()
# BeginnerProjects.Dice.draw_now(number=3)
# BeginnerProjects.DrawWhirlpool.draw_now()
# BeginnerProjects.Jellyfish.draw_now()
# BeginnerProjects.DrawPieChart.draw_now(data=[10, 17, 50, 52, 30])
# BeginnerProjects.RightAngleCalculator.draw_now(a=None, b=300, c=500)
# BeginnerProjects.LineGraph.draw_now(data=[[-374, -396], [-230, -211], [-16, -21], [158, 165], [269, 286], [398, 405]])
# BeginnerProjects.DrawTarget.draw_now()
# BeginnerProjects.DrawCaptainShield.draw_now()
# BeginnerProjects.RandomWalking.draw_now(max_steps=500)
# BeginnerProjects.RacerTurtles.race_now()
# BeginnerProjects.ParallelShapeFilling.draw_now()
# BeginnerProjects.DrawChessBoard.draw_now(height=7, width=7)

# FunctionFocusedProjects.DrawGraph().draw_now()
# FunctionFocusedProjects.DrawGarden().draw_now()
# FunctionFocusedProjects.DrawNightSky().draw_now()
# FunctionFocusedProjects.SpiralArt().draw_now()
# FunctionFocusedProjects.ParallelTurtleFlock(edges=6, angle=360/6, size=200, turtle_count=25).draw_now()

########################################################################################################
# Examples after this point are often not one-liners.
# Be a bit careful with how much you uncomment.
########################################################################################################

# SpecialTurtles.Demos.conga_turtle_demo()
# SpecialTurtles.Demos.rainbow_turtle_demo()
# rainbow_pen = SpecialTurtles.rainbow_turtle_demo()
# for i in range(6):
#     rainbow_pen.forward(220)
#     rainbow_pen.left(60)

# drawer = IntermediateProjects.SevenSegmentDrawer()
# for num in range(10):
#     drawer.draw_now(num)
#     time.sleep(1)

# spiro_drawer = IntermediateProjects.DrawTrueSpirograph()
# spiro_drawer.print_more_info()
# spiro_drawer.R = 6
# spiro_drawer.r = 2
# spiro_drawer.draw_now()

# IntermediateProjects.PandemicTurtleSimulator(turtle_count=60).draw_now()
# IntermediateProjects.MazeMaker(width=20, height=40).draw_now()


# RecursiveProjects.KochSnowflakeDrawer().draw_snowflake(2, 50)
# snowflake_drawer = RecursiveProjects.KochSnowflakeDrawer()
# for i in range(4):
#    snowflake_drawer.draw_snowflake(i, 300)

# RecursiveProjects.GenericShapeFractal().draw(size=1600, complexity=2, edges=7)

################
# Iterator projects. Recreating things like Range and Zip. Also useful if you implement __iter__()
# These are placeholders for now, and will be refined with a matching course.
################
# for i in IteratorProjects.RangeRemake.Range(7, 0, -0.5):
#     print(i)
# IteratorProjects.ZipTwoCollections.demo()
# IteratorProjects.PermutationGenerator.demo()
# IteratorProjects.RandomColorGenerator.demo()

turtle.exitonclick()
