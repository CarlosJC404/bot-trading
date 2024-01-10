import json
import matplotlib.pyplot as plt
import datetime

structure_points = []

def identify_structure(last_trend, points, rupture):
    start = points[0]
    end = points[1]
    trend = None
    point_recoil = None

    if last_trend == None:
        if start["wick"] < end["wick"]:
            trend = "buy"
        if start["wick"] > end["wick"]:
            trend = "sell"
    else:
        if last_trend == "buy":
            trend = last_trend
        elif last_trend == "sell":
            trend = last_trend
        else:
            raise ValueError("La tendencia proporcionada es invalidad.")
        
    for point in points[2:]:
        # if len(structure_points) > 0:
            # print(f"Last structure: {structure_points[-1]}")
        #print(f"Indice: {datetime.datetime.utcfromtimestamp(point['time'])} Point: {point} - Start: {start}")
        if trend == "buy":
            if point[rupture] <= end["wick"] and point[rupture] >= start["wick"]:
                if point_recoil == None:
                    point_recoil = point
                else:
                    if point["wick"] < point_recoil["wick"]:
                        point_recoil = point
            elif point[rupture] > end["wick"]:
                bos = {
                    "type": "bos",
                    "start": { "time": end["time"], "point": end["wick"] },
                    "end": { "time": point["time"], "point": end["wick"] }
                }
                structure_points.append(bos)
                print(f"Retroceso antes de añadir: {point_recoil}")
                start = point_recoil
                end = point
                point_recoil = None
            elif point[rupture] < start["wick"]:
                choch = {
                    "type": "choch",
                    "start": { "time": start["time"], "point": start["wick"] },
                    "end": { "time": point["time"], "point": start["wick"] }
                }
                structure_points.append(choch)
                trend = "sell"
                start = end
                end = point
                point_recoil = None
        elif trend == "sell":
            if point[rupture] >= end["wick"] and point[rupture] <= start["wick"]:
                if point_recoil == None:
                    point_recoil = point
                else:
                    if point["wick"] > point_recoil["wick"]:
                        point_recoil = point
            elif point[rupture] < end["wick"]:
                bos = {
                    "type": "bos",
                    "start": { "time": end["time"], "point": end["wick"] },
                    "end": { "time": point["time"], "point": end["wick"] }
                }
                structure_points.append(bos)
                print(f"Retroceso antes de añadir: {point_recoil}")
                start = point_recoil
                end = point
                point_recoil = None
            elif point[rupture] > start["wick"]:
                choch = {
                    "type": "choch",
                    "start": { "time": start["time"], "point": start["wick"] },
                    "end": { "time": point["time"], "point": start["wick"] }
                }
                structure_points.append(choch)
                trend = "buy"
                start = end
                end = point
                point_recoil = None
            
# points_test = [
#     {'time': 1698733800, 'wick': 0.58229, 'body': 0.58241}, 
#     {'time': 1698745500, 'wick': 0.58476, 'body': 0.58456}, 
#     {'time': 1698746400, 'wick': 0.58386, 'body': 0.58417}, 
#     {'time': 1698750000, 'wick': 0.58570, 'body': 0.58548}, 
#     {'time': 1698753600, 'wick': 0.58452, 'body': 0.58487}, 
#     {'time': 1698757200, 'wick': 0.58528, 'body': 0.58521}, 
#     {'time': 1698760800, 'wick': 0.58455, 'body': 0.58481}, 
#     {'time': 1698761700, 'wick': 0.58524, 'body': 0.58492}, 
#     {'time': 1698768000, 'wick': 0.58131, 'body': 0.58206}, 
#     {'time': 1698768900, 'wick': 0.58268, 'body': 0.58248}, 
#     {'time': 1698772500, 'wick': 0.58033, 'body': 0.58063}, 
#     {'time': 1698782400, 'wick': 0.58201, 'body': 0.58188}, 
#     {'time': 1698783300, 'wick': 0.58155, 'body': 0.58164}, 
#     {'time': 1698786000, 'wick': 0.58254, 'body': 0.58251}, 
#     {'time': 1698787800, 'wick': 0.58215, 'body': 0.58253}, 
#     {'time': 1698788700, 'wick': 0.58262, 'body': 0.58258}, 
#     {'time': 1698793200, 'wick': 0.58114, 'body': 0.58232}, 
#     {'time': 1698795000, 'wick': 0.58270, 'body': 0.58270}, 
#     {'time': 1698796800, 'wick': 0.57940, 'body': 0.58017}, 
#     {'time': 1698799500, 'wick': 0.58121, 'body': 0.58097}, 
#     {'time': 1698803100, 'wick': 0.58041, 'body': 0.58087}, 
#     {'time': 1698804000, 'wick': 0.58114, 'body': 0.58080}, 
#     {'time': 1698808500, 'wick': 0.57923, 'body': 0.57956}, 
#     {'time': 1698809400, 'wick': 0.58019, 'body': 0.58012}, 
#     {'time': 1698810300, 'wick': 0.57890, 'body': 0.57908}, 
#     {'time': 1698816600, 'wick': 0.58090, 'body': 0.58081}, 
#     {'time': 1698819300, 'wick': 0.58023, 'body': 0.58023}, 
#     {'time': 1698820200, 'wick': 0.58088, 'body': 0.58072}, 
#     {'time': 1698822000, 'wick': 0.58033, 'body': 0.58062}, 
#     {'time': 1698823800, 'wick': 0.58084, 'body': 0.58078}, 
#     {'time': 1698824700, 'wick': 0.58060, 'body': 0.58068}, 
#     {'time': 1698829200, 'wick': 0.58224, 'body': 0.58220}, 
#     {'time': 1698831900, 'wick': 0.58113, 'body': 0.58136}, 
#     {'time': 1698836400, 'wick': 0.58245, 'body': 0.58222}, 
#     {'time': 1698839100, 'wick': 0.58134, 'body': 0.58150}, 
#     {'time': 1698843600, 'wick': 0.58255, 'body': 0.58240}, 
#     {'time': 1698844500, 'wick': 0.58185, 'body': 0.58194}, 
#     {'time': 1698849900, 'wick': 0.58391, 'body': 0.58350}, 
#     {'time': 1698852600, 'wick': 0.58148, 'body': 0.58207}, 
#     {'time': 1698857100, 'wick': 0.58583, 'body': 0.58566},
#     {'time': 1698865200, 'wick': 0.58209, 'body': 0.58229}, 
#     {'time': 1698874200, 'wick': 0.58577, 'body': 0.58530}, 
#     {'time': 1698879600, 'wick': 0.58375, 'body': 0.58395}, 
#     {'time': 1698880500, 'wick': 0.58491, 'body': 0.58480}, 
#     {'time': 1698882300, 'wick': 0.58454, 'body': 0.58467}, 
#     {'time': 1698894000, 'wick': 0.58940, 'body': 0.58940}, 
#     {'time': 1698895800, 'wick': 0.58872, 'body': 0.58892}, 
#     {'time': 1698899400, 'wick': 0.58962, 'body': 0.58955}
# ]
# points_test = [
#     {"time": 1, "wick": 1, "body": 2}, 
#     {"time": 2, "wick": 10, "body": 8.5}, 
#     {"time": 3, "wick": 5, "body": 5}, 
#     {"time": 4, "wick": 12, "body": 11}, 
#     {"time": 5, "wick": 6, "body": 6.5}, 
#     {"time": 6, "wick": 8, "body": 8.5}, 
#     {"time": 7, "wick": 3, "body": 3},
#     {"time": 8, "wick": 4.5, "body": 4.3},
#     {"time": 9, "wick": 1, "body": 1},
#     {"time": 10, "wick": 5, "body": 5},

# ]
points_test = json.load(open("./data/points.json", "r"))
# print(points_test[0]["point"])

# print("Hola")

identify_structure(last_trend=None, points=points_test, rupture="body")
# print(structure_points)
x = []
y = []
z = []
for i in range(len(points_test)):
    x.append(points_test[i]["time"])
    y.append(points_test[i]["wick"])
    z.append(points_test[i]["body"])


# x = [datetime.datetime.fromtimestamp(ts) for ts in x]

plt.plot(x, y)
plt.plot(x, z)
for line in structure_points:
    color = ""
    if line["type"] == "bos":
        color = "green"
    else:
        color = "red"
    plt.plot([line["start"]["time"], line["end"]["time"]], [line["start"]["point"], line["end"]["point"]], color=color)

plt.show()