# from sage.all import var, solve
# # Replace v1, v2, v3, v4 with your actual values
# v = 4196604293528562019178729176959696479940189487937638820300425092623669070870963842968690664766177268414970591786532318240478088400508536
# v2 = 11553755018372917030893247277947844502733193007054515695939193023629350385471097895533448484666684220755712537476486600303519342608532236
# v3 = 14943875659428467087081841480998474044007665197104764079769879270204055794811591927815227928936527971132575961879124968229204795457570030
# v4 = 6336816260107995932250378492551290960420748628
# # Import SageMath symbols and solve function


# # Define the variables
# cnd1, cnd2, cnd3 = var('cnd1 cnd2 cnd3')

# # Define the known constants v1, v2, v3, and v4
# # Define the equations
# eq1 = cnd1**3 + cnd3**2 + cnd2 - v
# eq2 = cnd2**3 + cnd1**2 + cnd3 - v2
# eq3 = cnd3**3 + cnd2**2 + cnd1 - v3
# eq4 = cnd1 + cnd2 + cnd3 - v4

# # Solve the system of equations
# solutions = solve([eq1, eq2, eq3, eq4], cnd1, cnd2, cnd3, solution_dict=True)
# with open('./solutions.txt','w') as f:
#     f.write(solutions);
# # Display solutions
# print(solutions)
