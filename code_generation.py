import frhd
new_track = frhd.Track.Track()

with open('track_coords.txt', 'r') as f:
    coords: list = f.readlines()
    for coord in coords:
        # Simple inserts
        if coord[0] == "s" or coord[0] == "p":
            type, x1, y1, x2, y2 = coord.split(" ")
            new_track.insLine(type, int(x1), int(y1), int(x2), int(y2))
        elif coord[0] == "b":
            _, x, y, rot = coord.split(" ")
            new_track.insBoost(int(x), int(y), int(rot))
        elif coord[0] == "k":
            _, x, y = coord.split(" ")
            new_track.insBomb(int(x), int(y))
        elif coord[0] == "g":
            _, x, y, rot = coord.split(" ")
            new_track.insGrav(int(x), int(y), int(rot))
        elif coord[0] == "c":
            _, x, y = coord.split(" ")
            new_track.insCheck(int(x), int(y))
        elif coord[0] == "t":
            _, x, y = coord.split(" ")
            new_track.insStar(int(x), int(y))
        elif coord[0] == "m":
            _, x, y = coord.split(" ")
            new_track.insSlo(int(x), int(y))

        # More complicated inserts
        elif coord[0] == "T":
            options = {
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            }
            letters = coord.split(">")
            del letters[0]

        else:
            print(f"There was an error while generating `{coord.strip()}`")


print(new_track.genCode())
