import turtle, random
import BeginnerProjects, FunctionFocusedProjects
import IntermediateProjects, RecursiveProjects
import SpecialTurtles



# BeginnerProjects.DrawShape.draw_now()
# BeginnerProjects.DrawSeparatedShapes.draw_now()
# BeginnerProjects.DrawOverlappingShapes()
# BeginnerProjects.DrawWhirlpool.draw_now()
# BeginnerProjects.DrawPieChart.draw_now()
# BeginnerProjects.DrawTarget.draw_now()
# BeginnerProjects.DrawCaptainShield.draw_now()
# BeginnerProjects.RacerTurtles.race_now()
# BeginnerProjects.PolygonFromUser.draw_now()
# BeginnerProjects.DrawChessBoard.draw_now()

# SpecialTurtles.Demos.conga_turtle_demo()
# SpecialTurtles.Demos.rainbow_turtle_demo()
# rainbow_pen = SpecialTurtles.CongaTurtle(6)
# for i in range(6):
#     rainbow_pen.forward(220)
#     rainbow_pen.left(60)

# FunctionFocusedProjects.DrawGraph().draw_now()
# FunctionFocusedProjects.DrawGarden().draw_now()
# FunctionFocusedProjects.DrawNightSky().draw_now()
# FunctionFocusedProjects.SpiralArt().draw_now()

# spiro_drawer = IntermediateProjects.DrawTrueSpirograph()
# spiro_drawer.print_more_info()
# spiro_drawer.R = 6
# spiro_drawer.r = 1
# spiro_drawer.draw_now()

snowflake_drawer = RecursiveProjects.KochSnowflakeDrawer()
for i in range(4):
    snowflake_drawer.draw_snowflake(i, 300)



turtle.exitonclick()
