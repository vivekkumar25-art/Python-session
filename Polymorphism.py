class Pen:
    def write(self):
        print("Pen is writing with ink.")


class Pencil:
    def write(self):
        print("Pencil is writing with graphite.")


class Marker:
    def write(self):
        print("Marker is writing with bold ink.")


stationery = [
    Pen(),
    Pencil(),
    Marker()
]

for item in stationery:
    item.write()