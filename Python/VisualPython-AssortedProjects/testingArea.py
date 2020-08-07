import turtle, random, time
import BeginnerProjects, FunctionFocusedProjects
import IntermediateProjects, RecursiveProjects
import SpecialTurtles

########################################################################################################
# Uncomment a chunk of code, and hit run to see it in action.
# Certain chunks are one-liners, others are larger so you can experiment.
########################################################################################################

# # Any one of these will run in isolation:
# BeginnerProjects.DrawShape.draw_now()
# BeginnerProjects.DrawThreeShapes.draw_now()
# BeginnerProjects.DrawOverlappingShapes.draw_now()
# BeginnerProjects.PolygonFromUser.draw_now()
# BeginnerProjects.DrawGrassTuft.draw_now()
# BeginnerProjects.DrawGradientBackground.draw_now()
# BeginnerProjects.SnailShell.draw_now()
# BeginnerProjects.Minion.draw_now()
# BeginnerProjects.DrawWhirlpool.draw_now()
# BeginnerProjects.DrawPieChart.draw_now()
# BeginnerProjects.DrawTarget.draw_now()
# BeginnerProjects.DrawCaptainShield.draw_now()
# BeginnerProjects.RacerTurtles.race_now()
# BeginnerProjects.DrawChessBoard.draw_now()

# FunctionFocusedProjects.DrawGraph().draw_now()
# FunctionFocusedProjects.DrawGarden().draw_now()
# FunctionFocusedProjects.DrawNightSky().draw_now()
# FunctionFocusedProjects.SpiralArt().draw_now()


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

drawer = IntermediateProjects.SevenSegmentDrawer()
for num in range(10):
    drawer.draw_now(num)
    time.sleep(1)

# spiro_drawer = IntermediateProjects.DrawTrueSpirograph()
# spiro_drawer.print_more_info()
# spiro_drawer.R = 6
# spiro_drawer.r = 2
# spiro_drawer.draw_now()

# RecursiveProjects.KochSnowflakeDrawer().draw_snowflake(2, 50)
# snowflake_drawer = RecursiveProjects.KochSnowflakeDrawer()
# for i in range(4):
#    snowflake_drawer.draw_snowflake(i, 300)

turtle.exitonclick()












































