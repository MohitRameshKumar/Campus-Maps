classrooms = [#B Building Done
            'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
              #C Building Done
              'C1', 'C2', 'C3','C4', 'C5', 'C6',
              #D Building Done
              'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D10', 'D11', 'D12',
              #E Building Done
              'E1', 'E2', 'E3', 'E4',
              #G Building Done
              'G1', 'G2', 'G3', 'G4', 'G5',
              #H Building Done
              'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10','H11',
              #I Building Done
              'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
              #J Building
              'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8',
              #L Building Done
              'L1', 'L2', 'L3', 'L4', 'L5', 'L6',
              #M Building
              'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8', 'M9', 'M10',
              #Q first floor Done
              'Q101', 'Q102', 'Q103', 'Q104', 'Q105', 'Q106', 'Q107', 'Q108', 'Q109', 'Q110', 'Q111', 'Q112',
              #Q second floor Done
              'Q201', 'Q202', 'Q203', 'Q204', 'Q205', 'Q206', 'Q207', 'Q208', 'Q209', 'Q210', 'Q211', 'Q212',
              #Portables Done
              'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9',
              #R first floor Done
              'R101', 'R102', 'R103', 'R107', 'R120', 'R121', 'R123', 'R124',
              #R second floor Done
              'R201', 'R205', 'R202', 'R206', 'R203', 'R207', 'R215', 'R210', 'R216', 'R213', 'R211', 'R217', 'R212',
              #Other
              'Library', 'MPR', 'Track', 'Band', 'Orchestra', 'Large Gym', 'Small Gym', 'Pool', 'Theatre', 'Boys Locker Room', 'Girls Locker Room', 'Weight Room', 'Tennis Courts', 'Front Parking Lot', 'Back Parking Lot', 'Main Office', 'Large Gym Corner', 'Cafe', 'Cafeteria',
              #Stairs Done
              'RStair1', 'RStair2', 'RStair3', 'QStair1', 'QStair2', 'QStair3', 'RBackCorner'
              ]

distances = {
    ('B1', 'B2'): 25,
    ('B2', 'B3'): 25,
    ('B3', 'B4'): 35,
    ('B4', 'B5'): 25,
    ('B5', 'B6'): 25,
    ('B6', 'B7'): 25,
    ('B7', 'B8'): 25,
    ('B8', 'C6'): 130, #approximate
    ('B4', 'C4'): 130, #approximate
    ('C1', 'C2'): 25,
    ('C2', 'C3'): 25,
    ('C3', 'C4'): 35,
    ('C4', 'C5'): 53, #approximate
    ('C5', 'C6'): 33,
    ('C6', 'D1'): 75,
    ('C4', 'D3'): 75,
    ('C2', 'D12'): 50,
    ('D1', 'D2'): 50,
    ('D2', 'D3'): 50,
    ('D3', 'D4'): 100,
    ('D4', 'D5'): 50,
    ('D5', 'D6'): 50,
    ('D1', 'D6'): 100,
    ('D7', 'D8'): 50,
    ('D3', 'D8'): 30,
    ('D7', 'D4'): 30,
    ('D8', 'D12'): 60, #approximate
    ('D11', 'D12'): 75,
    ('D7', 'D10'): 100,
    ('D4', 'E2'): 10,
    ('E2', 'E3'): 66.6,
    ('D5', 'E1'): 10,
    ('D6', 'Cafeteria'): 75,
    ('Cafeteria', 'MPR'): 100,
    ('E1', 'E4'): 66.6,
    ('E1', 'E2'): 30, #approximate
    ('E3', 'E4'): 10,
    ('G1', 'G2'): 33,
    ('G1', 'G5'): 73, 
    ('G2', 'G3'): 106,
    ('G3', 'G4'): 33,
    ('MPR', 'G2'): 75,
    ('MPR', 'R101'): 100, #approximate
    ('R101', 'R102'): 58,
    ('R102', 'R103'): 33,
    ('R103', 'R120'): 33,
    ('R120', 'R121'): 33,
    ('R121', 'R123'): 33,
    ('R123', 'R124'): 20,
    ('R124', 'RBackCorner'): 175,
    ('H9', 'RBackCorner'): 225,
    ('R101', 'RStair1'): 50,
    ('R102', 'RStair2'): 10,
    ('R120', 'RStair3'): 10,
    ('RStair1', 'R201'): 50,
    ('RStair2', 'R203'): 60,
    ('RStair3', 'R211'): 60,
    ('R211', 'R212'): 20,
    ('R201', 'R202'): 66,
    ('R202', 'R203'): 30,
    ('R203', 'R211'): 66,
    ('RBackCorner', 'I6'): 150,
    ('I6', 'I7'): 50,
    ('I7', 'I8'): 25,
    ('I8', 'I9'): 25,
    ('I9', 'I10'): 75,
    ('I10', 'I1'): 50,
    ('I1', 'I2'): 50,
    ('I2', 'I3'): 25,
    ('I3', 'I4'): 25,
    ('I4', 'I5'): 25,
    ('I5', 'I6'): 75,
    ('H10', 'I5'): 75,
    ('I5', 'H12'): 25,
    ('I10', 'L4'): 75,
    ('L4', 'L5'): 50,
    ('L5', 'L6'): 50,
    ('L6', 'L1'): 80,
    ('L1', 'L2'): 50,
    ('L2', 'L3'): 50,
    ('L3', 'L4'): 80,
    ('L1', 'Choir'): 25,
    ('Orchestra', 'Band'): 110,
    ('Band', 'Large Gym'): 100,
    ('Large Gym', 'Large Gym Corner'): 200,
    ('Large Gym Corner', 'P1'): 150,
    ('Large Gym Corner', 'Track'): 200,
    ('Band', 'Large Gym Corner'): 166,
    ('P1', 'P2'): 25,
    ('P2', 'P3'): 25,
    ('P3', 'P4'): 25,
    ('P4', 'P5'): 25,
    ('P5', 'P6'): 25,
    ('P6', 'P7'): 25,
    ('P7', 'P8'): 25,
    ('P8', 'P9'): 25,
    ('P9', 'QStair1'): 125,
    ('QStair1', 'Front Parking Lot'): 66,
    ('P9', 'Front Parking Lot'): 75,
    ('Q111', 'Q112'): 10,
    ('Q111', 'Q109'): 25,
    ('Q109', 'Q110'): 10,
    ('Q110', 'Q112'): 25,
    ('Q109', 'Q107'): 25,
    ('Q107', 'Q108'): 10,
    ('Q108', 'Q110'): 25,
    ('Q108', 'Q106'): 100,
    ('Q105', 'Q106'): 10,
    ('Q105', 'Q103'): 25,
    ('Q103', 'Q104'): 10,
    ('Q104', 'Q106'): 25,
    ('Q103', 'Q101'): 25,
    ('Q101', 'Q102'): 10,
    ('Q102', 'Q104'): 25,
    ('QStair1', 'Q212'): 93,
    ('Q211', 'Q212'): 10,
    ('Q211', 'Q209'): 25,
    ('Q209', 'Q210'): 10,
    ('Q210', 'Q212'): 25,
    ('Q209', 'Q207'): 25,
    ('Q207', 'Q208'): 10,
    ('Q208', 'Q210'): 25,
    ('Q208', 'Q206'): 100,
    ('Q205', 'Q206'): 10,
    ('Q205', 'Q203'): 25,
    ('Q203', 'Q204'): 10,
    ('Q204', 'Q206'): 25,
    ('Q203', 'Q201'): 25,
    ('Q201', 'Q202'): 10,
    ('Q202', 'Q204'): 25,
    ('QStair3', 'Q202'): 93,
    ('QStair2', 'Q106'): 20,
    ('QStair2', 'Q108'): 20,
    ('QStair2', 'Q206'): 100,
    ('QStair2', 'Q208'): 100,
    ('Q102', 'QStair3'): 20,
    ('Pool', 'Front Parking Lot'): 200,
    ('Pool', 'QStairs3'): 180,
    ('Small Gym', 'QStairs3'): 100,
    ('Pool', 'Small Gym'): 100,
    ('Girls Locker Room', 'Cafe'): 50,
    ('Small Gym', 'Weight Room'): 100,
    ('Cafe', 'Weight Room'): 25,
    ('RStair1', 'H3'): 100,
    ('H3', 'H4'): 10,
    ('H4', 'H8'): 33,
    ('H8', 'H7'): 10,
    ('H7', 'H3'): 33,
    ('H8', 'H9'): 33,
    ('H9', 'H10'): 10,
    ('H7', 'H10'): 33,
    ('H10', 'H11'): 70,
    ('H11','H12'): 66,
    ('H12', 'H5'): 50,
    ('H12', 'H6'): 40,
    ('H5', 'H6'): 40,
    ('H1', 'H2'): 60,
    ('H2', 'H3'): 50,
    ('H1', 'Library'): 150,
    ('H2', 'RStair1'): 125,
    ('H2', 'C6'): 200,
    ('Boys Locker Room', 'Large Gym'): 50,
    ('Boys Locker Room', 'Cafe'): 150,
    ('Girls Locker Room', 'Small Gym'): 50,
    ('Cafe', 'Library'): 250,
    ('Library', 'B8'): 200,
    ('Large Gym Corner', 'Tennis Courts'): 125,
    ('Track', 'Tennis Courts'): 125,
    ('G1', 'Back Parking Lot'): 25,
    ('R103', 'Back Parking Lot'): 50,
    ('Main Office', 'B4'): 125,
    ('Main Office', 'Library'): 250,
    ('Cafeteria', 'MPR'): 75,
    ('D6', 'Cafeteria'): 75,
    ('L1', 'M6'): 66, #approximate
    ('L1', 'M7'): 66, #approximate
    ('M6', 'M7'): 66, #approximate
    ('M7', 'M8'): 33,
    ('M8', 'M9'): 43,
    ('M8', 'Orchestra'): 33,
    ('M8', 'Band'): 75,
    ('M9', 'Band'): 50,
    ('M9', 'Large Gym'): 100,
    ('M9', 'M1'): 158,
    ('M3', 'M6'): 158,
    ('M3', 'M2'): 25,
    ('M1', 'M2'): 25,
    ('M1', 'Cafe'): 100,
    ('M9', 'Cafe'): 200,
    ('J8', 'J7'): 33,
    ('J7', 'J6'): 33,
    ('J6', 'J5'): 33,
    ('J5', 'J4'): 66,
    ('J4', 'J3'): 33,
    ('J3', 'J2'): 33,
    ('J1', 'J2'): 33,
    ('J4', 'M6'): 50,
    ('L2', 'J4'): 50,
    ('J8', 'Library'): 75,
    ('I1', 'J1'): 33,
    ('J8', 'M3'): 125,
    ('J8', 'Cafe'): 150,

    }

start = input('Start:').strip()
end = input('End:').strip()

#DONT CHANGE
def minimum(distances, unexplored):
    return min(unexplored, key=lambda k: distances[k])

def dijkstra(airports, lines, start, end):
    distances = {airport: float('inf') for airport in airports}
    distances[start] = 0
    previous = {airport: None for airport in airports}
    unexplored = set(airports)

    while unexplored:
        current = minimum(distances, unexplored)
        if current == end:
            break
        unexplored.remove(current)

        for (src, dst), time in lines.items():
            if src == current and dst in unexplored:
                alt = distances[current] + time
                if alt < distances[dst]:
                    distances[dst] = alt
                    previous[dst] = current
            elif dst == current and src in unexplored:
                alt = distances[current] + time
                if alt < distances[src]:
                    distances[src] = alt
                    previous[src] = current

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    return distances[end], path

time, path = dijkstra(classrooms, distances, start, end)
print(f"Minimum distance: {time}")
print(f"Path: {' -> '.join(path)}")

