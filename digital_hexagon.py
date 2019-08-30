from math import sqrt       
import pygame, sys
pygame.init()

def getting_hexa(scaling_ratio, start_vector):    
    hex_coords = [(0,0), (1,0), (1.5, 3**(1/2)/2), (1, 3**(1/2)), (0,3**(1/2)), (-0.5, 3**(1/2)/2)]
    scaled_coords = []
    for x,y in hex_coords:
        scaled_coords.append([x*scaling_ratio, y*scaling_ratio])
    points = []
    for x,y in scaled_coords:
        points.append([x+start_vector[0], y + start_vector[1]])
    return points


def euclidean_metric(vector):
    squared = [x*x for x in vector]
    return sqrt(sum(squared))

def point_in_hexagon(hexa_points, coords):
    boundary_vectors = []
    connection_vectors = []
    for i in range(len(hexa_points)):
        boundary_vectors.append((hexa_points[(i+1)%len(hexa_points)][0]-hexa_points[i][0],hexa_points[(i+1)%len(hexa_points)][1]-hexa_points[i][1]))
        connection_vectors.append((coords[0]-hexa_points[i][0], coords[1]-hexa_points[i][1]))
    test = True
    angles = []
    for i in range(len(hexa_points)):
        angles.append((boundary_vectors[i][0]*connection_vectors[i][0]+boundary_vectors[i][1]*connection_vectors[i][1])
                      /(euclidean_metric(boundary_vectors[i])*euclidean_metric(connection_vectors[i])))
        if angles[i] <= -0.5:
            test = False
    return test



showed_display = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption('Clickable_Hexagon')
showed_display.fill((255,255,255))

hexagon1 = getting_hexa(50, (50,50))
hexagon2 = getting_hexa(80, (200,200))
hexagons = [hexagon1, hexagon2]


pygame.draw.polygon(showed_display, (100,100,100),hexagon1 )
pygame.draw.aalines(showed_display, (0,0,255), True, hexagon1, 15)
pygame.draw.polygon(showed_display, (100,100,100), hexagon2)
pygame.draw.aalines(showed_display, (0,255,0), True, hexagon2, 15)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                point_in_hexagon_list = []
                for x in hexagons:
                    point_in_hexagon_list.append(point_in_hexagon(x, event.pos))
                for i in range(len(hexagons)):
                    if point_in_hexagon_list[i] == True:
                        pygame.draw.circle(showed_display,((20*i)%256,(20*i+100)%256,(20*i+200)%256), event.pos, 6)
                if True not in point_in_hexagon_list:
                    pygame.draw.circle(showed_display,(255,0,0), event.pos, 5)
            elif event.button == 3:
                print("You pressed the right mouse button")
        #elif event.type == pygame.MOUSEBUTTONUP:
            #print("You released the mouse button")
        pygame.display.update()