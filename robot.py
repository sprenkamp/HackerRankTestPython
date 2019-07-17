def robot_bot(string):
    face = 0
    pos = [0, 0]
    string = string.upper()
    dirc = {
        0: [1, 0],
        90: [0, 1],
        180: [-1, 0],
        270: [0, -1],
        360: [1, 0],
        -90: [0, -1],
        -180: [-1, 0],
        -270: [0, 1]
    }
    for _ in range(4):
        for ch in string:
            if ch == "R": face -= 90
            elif ch == "L": face += 90
            if ch == "G":
                pos[0] += dirc[face][0]
                pos[1] += dirc[face][1]
            if abs(face) == 360:
                face = 0
    return True if pos == [0, 0] else False

def solution(commands):
    list_result = []
    for i in commands:
        if(robot_bot(i)):
            list_result.append('YES')
        else:
            list_result.append('NO')
    return list_result

# Driver program 
path = ["GGGGR",'RGL']

print(solution(path))