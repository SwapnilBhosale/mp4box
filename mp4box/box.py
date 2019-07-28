class Box:
    def __init__(self, size: int, box_type: str, uuid):
        self.size = size
        self.type = box_type
        self.uuid = uuid

class FullBox(Box):
    def __init__(self, size: int, box_type: str, uuid, v: int, f: int):
        super().__init__(size, box_type, uuid)
        #Boxes with an unrecognized version shall be ignored and skipped. 
        self.version = v
        self.flags = f

class FileTypeBox(Box):
    def __init__(self, size: int, major_brand: int, minor_version: int, compatible_brands: [int]):
        super().__init__(size, 'ftyp')
        self.major_brand = major_brand
        self.minor_brand = minor_version
        self.compatible_brands = compatible_brands

class MovieTypeBox(Box):
    def __init__(self, size: int):
        super().__init__(size, 'moov')

class MovieHeaderBox(FullBox):
    def __init__(v: int, f: int):
        super().__init__(size, 'mvhd', 0, v, f)
        self.creation_time = 0
        self.modification_time = 0
        self.timescale = 0
        self.duration = 0
        self.rate = 0x00010000
        self.volume = 0x0100
        self.reserved = 0
        self.matrix = [0x00010000,0,0,0,0x00010000,0,0,0,0x40000000]
        self.predefined = []
        self.next_track_id = 0
