import unittest
from tempfile import TemporaryFile
from mp4box.box_parser import BoxParser

class TestBoxParser(unittest.TestCase):
    def test_ftyp(self):
        b = 0
        with  TemporaryFile() as f:
            f.write(b"\x00\x00\x00\x18\x66\x74\x79\x70\x69\x73\x6f\x36\x00\x00\x00\x01\x69\x73\x6f\x36\x64\x61\x73\x68")
            f.seek(0)
            bp = BoxParser(f)
            bp.parse()
            boxes = bp.get_boxes()
            self.assertEqual(len(boxes.keys()), 1)

    def test_second_box_size(self):
        b = 0
        with  TemporaryFile() as f:
            f.write(b"\x00\x00\x00\x18\x66\x74\x79\x70\x69\x73\x6f\x6d\x00\x00\x00\x01\x69\x73\x6f\x6d\x61\x76\x63\x31")
            f.seek(0)
            bp = BoxParser(f)
            bp.parse()
            boxes = bp.get_boxes()
            self.assertIsNot(boxes['ftyp'], None) 

    def test_free(self):
         with  TemporaryFile() as f:

            f.write((b"\x00\x00\x00\x45\x66\x72\x65\x65\x49\x73\x6f\x4d\x65\x64\x69\x61\x20\x46\x69\x6c\x65\x20"
                     b"\x50\x72\x6f\x64\x75\x63\x65\x64\x20\x77\x69\x74\x68\x20\x47\x50\x41\x43\x20\x30\x2e\x38\x2e"
                     b"\x30\x2d\x72\x65\x76\x39\x2d\x67\x36\x65\x34\x61\x66\x30\x35\x62\x2d\x6d\x61\x73\x74\x65\x72"
                     b"\x00\x00\x00\x02\xd6"))
            f.seek(0)
            bp = BoxParser(f)
            bp.parse()
            boxes = bp.get_boxes()
            self.assertIsNot(boxes['free'], None) 

if __name__ == "__main__":
    unittest.main()

