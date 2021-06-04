

def newPointResolution(X, resolution):
    ratio = resolution[1] / 768
    center = [resolution[0] / 2, resolution[1] / 2]

    newX = int((X[0] - 512) * ratio + center[0])
    newY = int((X[1] - 384) * ratio + center[1])

    return newX, newY

def MakeAOI(params):

    # def newPointResolution(n,center,ratio):
    #     return int((n-center) * ratio + center)


    resolution = params['screenSize']
    faceLocations = []
    for i in range(4):
        for j in range(4):
            x1 = 136 + 192 * j
            y1 = 8 + 192 * i
            x2 = 311 + 192 * j
            y2 = 184 + 192 * i

            x1New, y1New = newPointResolution([x1, y1], resolution)
            x2New, y2New = newPointResolution([x2, y2], resolution)

            faceLocations.append([x1New, y1New, x2New, y2New])

    params['faceLocations'] = faceLocations

