// OLED library version < 2.0.0
// Created by http://oleddisplay.squix.ch/ Consider a donation
// In case of problems make sure that you are using the font file with the correct version!
const char SansSerif_bold_14[] PROGMEM = {
	0x10, // Width: 16
	0x11, // Height: 17
	0x20, // First Char: 32
	0xE0, // Numbers of Chars: 224

	// Char Widths:
	0x05, // 32: 5
	0x06, // 33: 6
	0x07, // 34: 7
	0x0C, // 35: 12
	0x0A, // 36: 10
	0x0E, // 37: 14
	0x0D, // 38: 13
	0x04, // 39: 4
	0x06, // 40: 6
	0x06, // 41: 6
	0x07, // 42: 7
	0x0C, // 43: 12
	0x05, // 44: 5
	0x06, // 45: 6
	0x05, // 46: 5
	0x05, // 47: 5
	0x0A, // 48: 10
	0x0A, // 49: 10
	0x0A, // 50: 10
	0x0A, // 51: 10
	0x0A, // 52: 10
	0x0A, // 53: 10
	0x0A, // 54: 10
	0x0A, // 55: 10
	0x0A, // 56: 10
	0x0A, // 57: 10
	0x06, // 58: 6
	0x06, // 59: 6
	0x0C, // 60: 12
	0x0C, // 61: 12
	0x0C, // 62: 12
	0x08, // 63: 8
	0x0E, // 64: 14
	0x0B, // 65: 11
	0x0A, // 66: 10
	0x0B, // 67: 11
	0x0B, // 68: 11
	0x09, // 69: 9
	0x09, // 70: 9
	0x0C, // 71: 12
	0x0B, // 72: 11
	0x04, // 73: 4
	0x04, // 74: 4
	0x0B, // 75: 11
	0x09, // 76: 9
	0x0D, // 77: 13
	0x0B, // 78: 11
	0x0C, // 79: 12
	0x0A, // 80: 10
	0x0C, // 81: 12
	0x0A, // 82: 10
	0x0A, // 83: 10
	0x0A, // 84: 10
	0x0B, // 85: 11
	0x0B, // 86: 11
	0x0F, // 87: 15
	0x0A, // 88: 10
	0x0A, // 89: 10
	0x0B, // 90: 11
	0x06, // 91: 6
	0x05, // 92: 5
	0x06, // 93: 6
	0x0C, // 94: 12
	0x07, // 95: 7
	0x07, // 96: 7
	0x09, // 97: 9
	0x0A, // 98: 10
	0x09, // 99: 9
	0x0A, // 100: 10
	0x0A, // 101: 10
	0x06, // 102: 6
	0x0A, // 103: 10
	0x0A, // 104: 10
	0x04, // 105: 4
	0x04, // 106: 4
	0x09, // 107: 9
	0x04, // 108: 4
	0x0E, // 109: 14
	0x0A, // 110: 10
	0x0A, // 111: 10
	0x0A, // 112: 10
	0x0A, // 113: 10
	0x07, // 114: 7
	0x09, // 115: 9
	0x06, // 116: 6
	0x0A, // 117: 10
	0x09, // 118: 9
	0x0E, // 119: 14
	0x09, // 120: 9
	0x09, // 121: 9
	0x09, // 122: 9
	0x0A, // 123: 10
	0x05, // 124: 5
	0x0A, // 125: 10
	0x0C, // 126: 12
	0x08, // 127: 8
	0x08, // 128: 8
	0x08, // 129: 8
	0x08, // 130: 8
	0x08, // 131: 8
	0x08, // 132: 8
	0x08, // 133: 8
	0x08, // 134: 8
	0x08, // 135: 8
	0x08, // 136: 8
	0x08, // 137: 8
	0x08, // 138: 8
	0x08, // 139: 8
	0x08, // 140: 8
	0x08, // 141: 8
	0x08, // 142: 8
	0x08, // 143: 8
	0x08, // 144: 8
	0x08, // 145: 8
	0x08, // 146: 8
	0x08, // 147: 8
	0x08, // 148: 8
	0x08, // 149: 8
	0x08, // 150: 8
	0x08, // 151: 8
	0x08, // 152: 8
	0x08, // 153: 8
	0x08, // 154: 8
	0x08, // 155: 8
	0x08, // 156: 8
	0x08, // 157: 8
	0x08, // 158: 8
	0x08, // 159: 8
	0x05, // 160: 5
	0x06, // 161: 6
	0x0A, // 162: 10
	0x0A, // 163: 10
	0x09, // 164: 9
	0x0A, // 165: 10
	0x05, // 166: 5
	0x07, // 167: 7
	0x07, // 168: 7
	0x0E, // 169: 14
	0x08, // 170: 8
	0x09, // 171: 9
	0x0C, // 172: 12
	0x06, // 173: 6
	0x0E, // 174: 14
	0x07, // 175: 7
	0x07, // 176: 7
	0x0C, // 177: 12
	0x06, // 178: 6
	0x06, // 179: 6
	0x07, // 180: 7
	0x0A, // 181: 10
	0x09, // 182: 9
	0x05, // 183: 5
	0x07, // 184: 7
	0x06, // 185: 6
	0x08, // 186: 8
	0x09, // 187: 9
	0x0F, // 188: 15
	0x0F, // 189: 15
	0x0F, // 190: 15
	0x08, // 191: 8
	0x0B, // 192: 11
	0x0B, // 193: 11
	0x0B, // 194: 11
	0x0B, // 195: 11
	0x0B, // 196: 11
	0x0B, // 197: 11
	0x0F, // 198: 15
	0x0B, // 199: 11
	0x09, // 200: 9
	0x09, // 201: 9
	0x09, // 202: 9
	0x09, // 203: 9
	0x04, // 204: 4
	0x04, // 205: 4
	0x04, // 206: 4
	0x04, // 207: 4
	0x0B, // 208: 11
	0x0B, // 209: 11
	0x0C, // 210: 12
	0x0C, // 211: 12
	0x0C, // 212: 12
	0x0C, // 213: 12
	0x0C, // 214: 12
	0x0C, // 215: 12
	0x0C, // 216: 12
	0x0B, // 217: 11
	0x0B, // 218: 11
	0x0B, // 219: 11
	0x0B, // 220: 11
	0x0A, // 221: 10
	0x0A, // 222: 10
	0x0A, // 223: 10
	0x09, // 224: 9
	0x09, // 225: 9
	0x09, // 226: 9
	0x09, // 227: 9
	0x09, // 228: 9
	0x09, // 229: 9
	0x10, // 230: 16
	0x09, // 231: 9
	0x0A, // 232: 10
	0x0A, // 233: 10
	0x0A, // 234: 10
	0x0A, // 235: 10
	0x04, // 236: 4
	0x04, // 237: 4
	0x04, // 238: 4
	0x04, // 239: 4
	0x0A, // 240: 10
	0x0A, // 241: 10
	0x0A, // 242: 10
	0x0A, // 243: 10
	0x0A, // 244: 10
	0x0A, // 245: 10
	0x0A, // 246: 10
	0x0C, // 247: 12
	0x0A, // 248: 10
	0x0A, // 249: 10
	0x0A, // 250: 10
	0x0A, // 251: 10
	0x0A, // 252: 10
	0x09, // 253: 9
	0x0A, // 254: 10
	0x09, // 255: 9

	// Font Data:
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 32
	0x00,0x00,0x30,0x0C,0xC3,0x30,0x0C,0x03,0x30,0x0C,0x00,0x00,0x00, // 33
	0x00,0x00,0xC0,0x66,0xB3,0xD9,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 34
	0x00,0x00,0x00,0x00,0x00,0x32,0x30,0x01,0x13,0xFC,0x07,0x19,0x98,0xE0,0x3F,0xC8,0x80,0x0C,0x4C,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 35
	0x00,0x00,0x00,0x02,0x08,0x78,0xB0,0xC2,0x02,0x0F,0xF8,0x80,0x07,0x1A,0x69,0xF8,0x80,0x00,0x02,0x00,0x00,0x00, // 36
	0x00,0x00,0x00,0x00,0x00,0x70,0x30,0x36,0x86,0xCD,0x61,0x3B,0xD8,0x76,0xDC,0x36,0xB8,0x0D,0x67,0xC3,0xD8,0x18,0x1C,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 37
	0x00,0x00,0x00,0x00,0x00,0x78,0x80,0x11,0x30,0x00,0x0E,0x60,0x63,0xC6,0xCC,0xB0,0x18,0x1C,0xC6,0x83,0xCF,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 38
	0x00,0x60,0x66,0x06,0x00,0x00,0x00,0x00,0x00, // 39
	0x00,0xC0,0x31,0x8C,0x61,0x18,0x86,0x61,0x30,0x0C,0x07,0x00,0x00, // 40
	0x00,0xE0,0x30,0x0C,0x86,0x61,0x18,0x86,0x31,0x8C,0x03,0x00,0x00, // 41
	0x00,0x00,0x00,0x91,0xF4,0x71,0x7C,0x49,0x04,0x00,0x00,0x00,0x00,0x00,0x00, // 42
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x60,0x00,0x06,0xFC,0xC3,0x3F,0x60,0x00,0x06,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 43
	0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x63,0x44,0x00,0x00, // 44
	0x00,0x00,0x00,0x00,0x00,0x00,0x9E,0x07,0x00,0x00,0x00,0x00,0x00, // 45
	0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x63,0x00,0x00,0x00, // 46
	0x00,0x00,0x8C,0x11,0x63,0x84,0x18,0x23,0xC6,0x00,0x00, // 47
	0x00,0x00,0x00,0x00,0x1E,0xCC,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 48
	0x00,0x00,0x00,0x00,0x0E,0x34,0xC0,0x00,0x03,0x0C,0x30,0xC0,0x00,0x03,0x0C,0xFC,0x00,0x00,0x00,0x00,0x00,0x00, // 49
	0x00,0x00,0x00,0x00,0x1F,0xE2,0x00,0x03,0x0C,0x38,0x70,0xE0,0xC0,0x81,0x03,0xFE,0x00,0x00,0x00,0x00,0x00,0x00, // 50
	0x00,0x00,0x00,0x00,0x3F,0x82,0x01,0x06,0x18,0x3E,0xC0,0x01,0x06,0x98,0x70,0x7C,0x00,0x00,0x00,0x00,0x00,0x00, // 51
	0x00,0x00,0x00,0x00,0x38,0xD0,0x20,0xC3,0x8C,0x31,0xC2,0xF8,0x07,0x0C,0x30,0xC0,0x00,0x00,0x00,0x00,0x00,0x00, // 52
	0x00,0x00,0x00,0x80,0x3F,0x06,0x18,0xE0,0x87,0x30,0x80,0x01,0x06,0x98,0x30,0x7C,0x00,0x00,0x00,0x00,0x00,0x00, // 53
	0x00,0x00,0x00,0x00,0x1E,0x8C,0x18,0xE0,0x87,0x33,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 54
	0x00,0x00,0x00,0x80,0x7F,0x80,0x01,0x03,0x0C,0x38,0x60,0xC0,0x01,0x03,0x0E,0x18,0x00,0x00,0x00,0x00,0x00,0x00, // 55
	0x00,0x00,0x00,0x00,0x3F,0x86,0x19,0x66,0x18,0x1E,0xCE,0x19,0x66,0x98,0x73,0xFC,0x00,0x00,0x00,0x00,0x00,0x00, // 56
	0x00,0x00,0x00,0x00,0x1E,0xCC,0x18,0x66,0x98,0x61,0xCC,0xE1,0x07,0x18,0x31,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 57
	0x00,0x00,0x00,0x80,0x61,0x18,0x00,0x60,0x18,0x06,0x00,0x00,0x00, // 58
	0x00,0x00,0x00,0x80,0x61,0x18,0x00,0x60,0x18,0x86,0x10,0x00,0x00, // 59
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0xC0,0x83,0x0F,0x1E,0xE0,0x01,0xF8,0x00,0x3C,0x00,0x02,0x00,0x00,0x00,0x00,0x00,0x00, // 60
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0x3F,0xFE,0x03,0x00,0x00,0xE0,0x3F,0xFE,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 61
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x20,0x00,0x1E,0x80,0x0F,0xC0,0x03,0x3C,0xF8,0xE0,0x01,0x02,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 62
	0x00,0x00,0x00,0x3C,0x62,0x60,0x70,0x38,0x1C,0x0C,0x00,0x0C,0x0C,0x00,0x00,0x00,0x00,0x00, // 63
	0x00,0x00,0x00,0x00,0x00,0x80,0x0F,0x18,0x04,0x01,0x42,0x3E,0xC9,0x4C,0x32,0x93,0xCC,0x24,0xB3,0x90,0x1F,0x04,0x00,0x86,0x01,0x3E,0x00,0x00,0x00,0x00, // 64
	0x00,0x00,0x00,0x00,0xE0,0x00,0x07,0x6C,0x60,0x83,0x31,0x8C,0xE1,0x8F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 65
	0x00,0x00,0x00,0x80,0x3F,0x86,0x19,0x66,0x98,0x3F,0x86,0x19,0x66,0x98,0x61,0xFE,0x00,0x00,0x00,0x00,0x00,0x00, // 66
	0x00,0x00,0x00,0x00,0xE0,0xC7,0x21,0x06,0x18,0xC0,0x00,0x06,0x30,0x00,0x03,0x38,0x04,0x3F,0x00,0x00,0x00,0x00,0x00,0x00, // 67
	0x00,0x00,0x00,0x00,0xFC,0x60,0x1C,0xC3,0x18,0xCC,0x60,0x06,0x33,0x98,0x61,0x8C,0xE3,0x07,0x00,0x00,0x00,0x00,0x00,0x00, // 68
	0x00,0x00,0x00,0xF0,0x67,0xC0,0x80,0x01,0x7F,0x06,0x0C,0x18,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 69
	0x00,0x00,0x00,0xF0,0x67,0xC0,0x80,0x01,0x7F,0x06,0x0C,0x18,0x30,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 70
	0x00,0x00,0x00,0x00,0x00,0x3F,0x1C,0xC2,0x00,0x06,0x60,0x78,0x06,0x66,0x60,0x0C,0xC6,0x61,0xF0,0x07,0x00,0x00,0x00,0x00,0x00,0x00, // 71
	0x00,0x00,0x00,0x00,0x0C,0x66,0x30,0x83,0x19,0xCC,0x7F,0x06,0x33,0x98,0xC1,0x0C,0x66,0x30,0x00,0x00,0x00,0x00,0x00,0x00, // 72
	0x00,0x60,0x66,0x66,0x66,0x66,0x06,0x00,0x00, // 73
	0x00,0x60,0x66,0x66,0x66,0x66,0x66,0x36,0x00, // 74
	0x00,0x00,0x00,0x00,0x0C,0x63,0x0C,0x33,0xD8,0xC0,0x03,0x36,0x30,0x83,0x31,0x0C,0x63,0x30,0x00,0x00,0x00,0x00,0x00,0x00, // 75
	0x00,0x00,0x00,0x30,0x60,0xC0,0x80,0x01,0x03,0x06,0x0C,0x18,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 76
	0x00,0x00,0x00,0x00,0x00,0x07,0xE7,0xF1,0x3C,0x9E,0x6D,0xB3,0x6D,0xE6,0xCC,0x9C,0x19,0x31,0x03,0x66,0xC0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 77
	0x00,0x00,0x00,0x00,0x1C,0xE6,0x30,0x8F,0x59,0xCC,0x66,0x66,0x33,0x9B,0xF1,0x0C,0x67,0x38,0x00,0x00,0x00,0x00,0x00,0x00, // 78
	0x00,0x00,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0C,0xC3,0x30,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 79
	0x00,0x00,0x00,0x80,0x1F,0xC6,0x19,0x66,0x98,0x61,0xC6,0xF9,0x61,0x80,0x01,0x06,0x00,0x00,0x00,0x00,0x00,0x00, // 80
	0x00,0x00,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0E,0xC3,0x30,0xF0,0x00,0x18,0x00,0x03,0x00,0x00,0x00, // 81
	0x00,0x00,0x00,0x80,0x3F,0x86,0x19,0x66,0x98,0x71,0xFE,0x18,0x63,0x98,0x61,0x06,0x03,0x00,0x00,0x00,0x00,0x00, // 82
	0x00,0x00,0x00,0x00,0x3F,0x86,0x18,0xE0,0x01,0x3F,0xF0,0x01,0x06,0x98,0x60,0xFE,0x00,0x00,0x00,0x00,0x00,0x00, // 83
	0x00,0x00,0x00,0x80,0x7F,0x30,0xC0,0x00,0x03,0x0C,0x30,0xC0,0x00,0x03,0x0C,0x30,0x00,0x00,0x00,0x00,0x00,0x00, // 84
	0x00,0x00,0x00,0x00,0x0C,0x66,0x30,0x83,0x19,0xCC,0x60,0x06,0x33,0x98,0xC1,0x18,0x83,0x0F,0x00,0x00,0x00,0x00,0x00,0x00, // 85
	0x00,0x00,0x00,0x00,0x06,0x6C,0x30,0x83,0x19,0x8C,0x31,0x8C,0xC1,0x06,0x36,0xB0,0x01,0x07,0x00,0x00,0x00,0x00,0x00,0x00, // 86
	0x00,0x00,0x00,0x00,0x00,0xC0,0x38,0x66,0x1C,0x33,0x8E,0x31,0x65,0xD8,0x36,0x6C,0x1B,0x16,0x0D,0x8E,0x03,0xC7,0x81,0xE3,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 87
	0x00,0x00,0x00,0xC0,0xE1,0x86,0x31,0xC3,0x0C,0x1E,0x78,0x30,0xC3,0x8C,0x61,0x87,0x03,0x00,0x00,0x00,0x00,0x00, // 88
	0x00,0x00,0x00,0xC0,0xE1,0x86,0x31,0xC3,0x0C,0x1E,0x30,0xC0,0x00,0x03,0x0C,0x30,0x00,0x00,0x00,0x00,0x00,0x00, // 89
	0x00,0x00,0x00,0x00,0xFC,0x07,0x30,0xC0,0x00,0x03,0x0C,0x30,0xC0,0x00,0x03,0x0C,0xE0,0x3F,0x00,0x00,0x00,0x00,0x00,0x00, // 90
	0x00,0xE0,0x19,0x86,0x61,0x18,0x86,0x61,0x18,0x86,0x07,0x00,0x00, // 91
	0x00,0x80,0x31,0x84,0x31,0x84,0x30,0x86,0x30,0x06,0x00, // 92
	0x00,0xE0,0x61,0x18,0x86,0x61,0x18,0x86,0x61,0x98,0x07,0x00,0x00, // 93
	0x00,0x00,0x00,0x00,0x00,0x07,0xF8,0xC0,0x1D,0x06,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 94
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFE,0x00, // 95
	0x00,0x03,0x03,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 96
	0x00,0x00,0x00,0x00,0x00,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 97
	0x00,0x00,0x60,0x80,0x01,0x06,0xD8,0xE1,0x8C,0x61,0x86,0x19,0x66,0x98,0x33,0x76,0x00,0x00,0x00,0x00,0x00,0x00, // 98
	0x00,0x00,0x00,0x00,0x00,0x00,0x0F,0x23,0x03,0x06,0x0C,0x18,0x60,0x84,0x07,0x00,0x00,0x00,0x00,0x00, // 99
	0x00,0x00,0x00,0x18,0x60,0x80,0xE1,0xC6,0x9C,0x61,0x86,0x19,0x66,0x18,0x73,0xB8,0x01,0x00,0x00,0x00,0x00,0x00, // 100
	0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0xC1,0x8C,0x61,0xFE,0x19,0x60,0x00,0x43,0xF8,0x00,0x00,0x00,0x00,0x00,0x00, // 101
	0x00,0x80,0x33,0x8C,0xCF,0x30,0x0C,0xC3,0x30,0x0C,0x00,0x00,0x00, // 102
	0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0xC6,0x9C,0x61,0x86,0x19,0x66,0x18,0x73,0xB8,0x01,0x46,0x0C,0x1E,0x00,0x00, // 103
	0x00,0x00,0x60,0x80,0x01,0x06,0xD8,0xE3,0x98,0x61,0x86,0x19,0x66,0x98,0x61,0x86,0x01,0x00,0x00,0x00,0x00,0x00, // 104
	0x00,0x66,0x60,0x66,0x66,0x66,0x06,0x00,0x00, // 105
	0x00,0x66,0x60,0x66,0x66,0x66,0x66,0x36,0x00, // 106
	0x00,0x00,0x18,0x30,0x60,0xC0,0x98,0x19,0x1B,0x1E,0x6C,0x98,0x31,0x66,0x18,0x00,0x00,0x00,0x00,0x00, // 107
	0x00,0x66,0x66,0x66,0x66,0x66,0x06,0x00,0x00, // 108
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0xDD,0xE3,0x9C,0x19,0x63,0xC6,0x98,0x31,0x66,0x8C,0x19,0x63,0xC6,0x18,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 109
	0x00,0x00,0x00,0x00,0x00,0x00,0xD8,0xE3,0x98,0x61,0x86,0x19,0x66,0x98,0x61,0x86,0x01,0x00,0x00,0x00,0x00,0x00, // 110
	0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0xC1,0x8C,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 111
	0x00,0x00,0x00,0x00,0x00,0x00,0xD8,0xE1,0x8C,0x61,0x86,0x19,0x66,0x98,0x33,0x76,0x18,0x60,0x80,0x01,0x00,0x00, // 112
	0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0xC6,0x9C,0x61,0x86,0x19,0x66,0x18,0x73,0xB8,0x01,0x06,0x18,0x60,0x00,0x00, // 113
	0x00,0x00,0x00,0x00,0xB0,0x3B,0x0C,0x06,0x83,0xC1,0x60,0x00,0x00,0x00,0x00, // 114
	0x00,0x00,0x00,0x00,0x00,0x80,0x8F,0x21,0x03,0x7E,0xF8,0x01,0x13,0xC6,0x07,0x00,0x00,0x00,0x00,0x00, // 115
	0x00,0x00,0x18,0xC6,0x67,0x18,0x86,0x61,0x18,0x1C,0x00,0x00,0x00, // 116
	0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x98,0x71,0xBC,0x01,0x00,0x00,0x00,0x00,0x00, // 117
	0x00,0x00,0x00,0x00,0x00,0x60,0xB0,0x31,0x63,0xC6,0xD8,0xB0,0xC1,0x81,0x03,0x00,0x00,0x00,0x00,0x00, // 118
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x31,0x66,0x8C,0x31,0x33,0xEC,0x0D,0x7B,0x83,0x52,0xE0,0x1C,0x38,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 119
	0x00,0x00,0x00,0x00,0x00,0xE0,0xB8,0x31,0x36,0x38,0x70,0xB0,0x31,0x76,0x1C,0x00,0x00,0x00,0x00,0x00, // 120
	0x00,0x00,0x00,0x00,0x00,0x60,0xB0,0x31,0x63,0xC6,0xD8,0xB0,0x41,0x83,0x03,0x06,0x0E,0x0F,0x00,0x00, // 121
	0x00,0x00,0x00,0x00,0x00,0xC0,0x1F,0x30,0x30,0x30,0x30,0x30,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 122
	0x00,0x00,0x00,0x0E,0x0C,0x30,0xC0,0x00,0x03,0x0C,0x1C,0xC0,0x00,0x03,0x0C,0x30,0xC0,0x00,0x0E,0x00,0x00,0x00, // 123
	0x00,0x30,0xC6,0x18,0x63,0x8C,0x31,0xC6,0x18,0x63,0x00, // 124
	0x00,0x00,0xC0,0x01,0x0C,0x30,0xC0,0x00,0x03,0x0C,0xE0,0xC0,0x00,0x03,0x0C,0x30,0xC0,0xC0,0x01,0x00,0x00,0x00, // 125
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xC0,0x23,0xFE,0x23,0x1E,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 126
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 127
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 128
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 129
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 130
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 131
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 132
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 133
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 134
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 135
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 136
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 137
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 138
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 139
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 140
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 141
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 142
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 143
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 144
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 145
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 146
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 147
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 148
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 149
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 150
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 151
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 152
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 153
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 154
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 155
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 156
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 157
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 158
	0x00,0x00,0x00,0xFE,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0x82,0xFE,0x00,0x00,0x00, // 159
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 160
	0x00,0x00,0x00,0x00,0xC3,0x00,0x0C,0xC3,0x30,0x0C,0xC3,0x00,0x00, // 161
	0x00,0x00,0x00,0x00,0x04,0x10,0xE0,0xC0,0x85,0x05,0x16,0x58,0x60,0x01,0x17,0x38,0x40,0x00,0x01,0x00,0x00,0x00, // 162
	0x00,0x00,0x00,0x00,0x1E,0x8C,0x30,0xC0,0x80,0x1F,0x0C,0x30,0xC0,0x00,0x03,0xFF,0x00,0x00,0x00,0x00,0x00,0x00, // 163
	0x00,0x00,0x00,0x00,0x00,0x40,0x10,0x7F,0x66,0x84,0x08,0x31,0xE3,0x27,0x00,0x00,0x00,0x00,0x00,0x00, // 164
	0x00,0x00,0x00,0x80,0x73,0xCC,0xE0,0xE1,0x1F,0x0C,0xFE,0xC1,0x00,0x03,0x0C,0x30,0x00,0x00,0x00,0x00,0x00,0x00, // 165
	0x00,0x00,0xC6,0x18,0x63,0x00,0x30,0xC6,0x18,0x03,0x00, // 166
	0x00,0x00,0x00,0xCF,0x64,0xE0,0xDC,0x46,0x37,0x0E,0x4C,0xE6,0x01,0x00,0x00, // 167
	0x00,0x80,0xCD,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 168
	0x00,0x00,0x00,0x00,0x00,0x80,0x07,0x18,0x06,0x7A,0x41,0x93,0x50,0x20,0x14,0x08,0x0D,0x82,0x5E,0x60,0x18,0xE0,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 169
	0x00,0x00,0x00,0x3E,0x60,0x7C,0x66,0x66,0x7C,0x00,0x7E,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 170
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x12,0x36,0x36,0x6C,0xB0,0x41,0x02,0x00,0x00,0x00,0x00,0x00,0x00, // 171
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0x3F,0xFE,0x03,0x30,0x00,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 172
	0x00,0x00,0x00,0x00,0x00,0x00,0x9E,0x07,0x00,0x00,0x00,0x00,0x00, // 173
	0x00,0x00,0x00,0x00,0x00,0x80,0x07,0x18,0x06,0x7A,0x41,0x92,0x90,0x27,0xA4,0x09,0x49,0x82,0x52,0x60,0x18,0xE0,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 174
	0x00,0x00,0x80,0x07,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 175
	0x00,0x00,0x80,0x23,0x12,0x89,0x38,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 176
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x60,0xE0,0x7F,0xFE,0x07,0x06,0x60,0xE0,0x7F,0xFE,0x07,0x00,0x00,0x00,0x00,0x00,0x00, // 177
	0x00,0x00,0x78,0x32,0x8C,0x31,0x3E,0x00,0x00,0x00,0x00,0x00,0x00, // 178
	0x00,0x00,0xF8,0x30,0x07,0xCB,0x1E,0x00,0x00,0x00,0x00,0x00,0x00, // 179
	0x00,0x30,0x0C,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 180
	0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x98,0x61,0xFE,0x1B,0x60,0x80,0x01,0x00,0x00, // 181
	0x00,0x00,0x00,0xE0,0xE3,0xC5,0x8B,0x17,0x2F,0x5C,0xA0,0x40,0x81,0x02,0x05,0x0A,0x00,0x00,0x00,0x00, // 182
	0x00,0x00,0x00,0x00,0x30,0xC6,0x00,0x00,0x00,0x00,0x00, // 183
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x40,0x38,0x00, // 184
	0x00,0x00,0x3C,0x0C,0xC3,0x30,0x1E,0x00,0x00,0x00,0x00,0x00,0x00, // 185
	0x00,0x00,0x00,0x3C,0x66,0x66,0x66,0x66,0x3C,0x00,0x7E,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 186
	0x00,0x00,0x00,0x00,0x00,0x00,0x80,0x04,0x1B,0x6C,0xD8,0xD8,0x90,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 187
	0x00,0x00,0x00,0x00,0x00,0xE0,0xE1,0xC0,0x30,0x60,0x1C,0x30,0x06,0x98,0x01,0xDE,0x1C,0x30,0x0E,0x9C,0x06,0xE6,0x87,0x83,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 188
	0x00,0x00,0x00,0x00,0x00,0xE0,0xE1,0xC0,0x30,0x60,0x1C,0x30,0x06,0x98,0x01,0xDE,0x1E,0x30,0x19,0x1C,0x0C,0x06,0x83,0xC3,0x00,0xF0,0x01,0x00,0x00,0x00,0x00,0x00, // 189
	0x00,0x00,0x00,0x00,0x00,0xC0,0xE7,0x00,0x33,0xE0,0x1C,0xC0,0x06,0xE4,0x01,0xDE,0x1C,0x30,0x0E,0x9C,0x06,0xE6,0x87,0x83,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 190
	0x00,0x00,0x00,0x00,0x00,0x30,0x30,0x00,0x30,0x30,0x18,0x0C,0x06,0x06,0x46,0x3C,0x00,0x00, // 191
	0x30,0x00,0x00,0x00,0xE0,0x00,0x07,0x6C,0x60,0x83,0x31,0x8C,0xE1,0x8F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 192
	0x30,0x00,0x00,0x00,0xE0,0x00,0x07,0x6C,0x60,0x83,0x31,0x8C,0xE1,0x8F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 193
	0xD8,0x00,0x00,0x00,0xE0,0x00,0x07,0x6C,0x60,0x83,0x31,0x8C,0xE1,0x8F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 194
	0xE8,0x00,0x00,0x00,0xE0,0x00,0x07,0x6C,0x60,0x83,0x31,0x8C,0xE1,0x8F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 195
	0xD8,0x00,0x00,0x00,0xE0,0x00,0x07,0x6C,0x60,0x83,0x31,0x8C,0xE1,0x8F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 196
	0x70,0x40,0x04,0x22,0xE0,0x80,0x0D,0x6C,0x30,0x86,0x31,0x8C,0xF1,0x9F,0xC1,0x0C,0x36,0x60,0x00,0x00,0x00,0x00,0x00,0x00, // 197
	0x00,0x00,0x00,0x00,0x00,0x00,0xFE,0x07,0x1B,0xC0,0x0C,0x60,0x06,0x18,0x7F,0x8C,0x01,0xFE,0x80,0x61,0xC0,0x30,0x30,0xF8,0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 198
	0x00,0x00,0x00,0x00,0xE0,0xC7,0x21,0x06,0x18,0xC0,0x00,0x06,0x30,0x00,0x03,0x38,0x04,0x3F,0x40,0x00,0x02,0x1C,0x00,0x00, // 199
	0x18,0x00,0x00,0xF0,0x67,0xC0,0x80,0x01,0x7F,0x06,0x0C,0x18,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 200
	0x18,0x00,0x00,0xF0,0x67,0xC0,0x80,0x01,0x7F,0x06,0x0C,0x18,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 201
	0x6C,0x00,0x00,0xF0,0x67,0xC0,0x80,0x01,0x7F,0x06,0x0C,0x18,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 202
	0x6C,0x00,0x00,0xF0,0x67,0xC0,0x80,0x01,0x7F,0x06,0x0C,0x18,0x30,0xE0,0x0F,0x00,0x00,0x00,0x00,0x00, // 203
	0x06,0x60,0x66,0x66,0x66,0x66,0x06,0x00,0x00, // 204
	0x06,0x60,0x66,0x66,0x66,0x66,0x06,0x00,0x00, // 205
	0x09,0x60,0x66,0x66,0x66,0x66,0x06,0x00,0x00, // 206
	0x09,0x60,0x66,0x66,0x66,0x66,0x06,0x00,0x00, // 207
	0x00,0x00,0x00,0x00,0xFC,0x60,0x1C,0xC3,0x18,0xEC,0x63,0x06,0x33,0x98,0x61,0x8C,0xE3,0x07,0x00,0x00,0x00,0x00,0x00,0x00, // 208
	0xE8,0x00,0x00,0x00,0x1C,0xE6,0x30,0x8F,0x59,0xCC,0x66,0x66,0x33,0x9B,0xF1,0x0C,0x67,0x38,0x00,0x00,0x00,0x00,0x00,0x00, // 209
	0x30,0x00,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0C,0xC3,0x30,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 210
	0x30,0x00,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0C,0xC3,0x30,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 211
	0xD8,0x00,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0C,0xC3,0x30,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 212
	0xD0,0x00,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0C,0xC3,0x30,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 213
	0x98,0x01,0x00,0x00,0x00,0x0F,0x0C,0xC3,0x30,0x06,0x66,0x60,0x06,0x66,0x60,0x0C,0xC3,0x30,0xF0,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 214
	0x00,0x00,0x00,0x00,0x00,0x00,0x08,0xC1,0x39,0xF8,0x01,0x0F,0xF0,0x80,0x1F,0x9C,0x83,0x10,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 215
	0x00,0x00,0x00,0x00,0x00,0x4F,0x0C,0xC3,0x30,0x86,0x66,0x64,0x26,0x66,0x61,0x0C,0xC3,0x30,0xF2,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 216
	0x30,0x00,0x00,0x00,0x0C,0x66,0x30,0x83,0x19,0xCC,0x60,0x06,0x33,0x98,0xC1,0x18,0x83,0x0F,0x00,0x00,0x00,0x00,0x00,0x00, // 217
	0x30,0x00,0x00,0x00,0x0C,0x66,0x30,0x83,0x19,0xCC,0x60,0x06,0x33,0x98,0xC1,0x18,0x83,0x0F,0x00,0x00,0x00,0x00,0x00,0x00, // 218
	0xD8,0x00,0x00,0x00,0x0C,0x66,0x30,0x83,0x19,0xCC,0x60,0x06,0x33,0x98,0xC1,0x18,0x83,0x0F,0x00,0x00,0x00,0x00,0x00,0x00, // 219
	0xD8,0x00,0x00,0x00,0x0C,0x66,0x30,0x83,0x19,0xCC,0x60,0x06,0x33,0x98,0xC1,0x18,0x83,0x0F,0x00,0x00,0x00,0x00,0x00,0x00, // 220
	0x30,0x00,0x00,0xC0,0xE1,0x86,0x31,0xC3,0x0C,0x1E,0x30,0xC0,0x00,0x03,0x0C,0x30,0x00,0x00,0x00,0x00,0x00,0x00, // 221
	0x00,0x00,0x00,0x80,0x01,0x7E,0x18,0x67,0x98,0x61,0x86,0x19,0xE7,0x87,0x01,0x06,0x00,0x00,0x00,0x00,0x00,0x00, // 222
	0x00,0x00,0xC0,0x87,0x31,0xC6,0x98,0x61,0x83,0x0D,0xF6,0x98,0x67,0x98,0x61,0xF6,0x00,0x00,0x00,0x00,0x00,0x00, // 223
	0x00,0x18,0x60,0x80,0x01,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 224
	0x00,0x80,0x81,0x81,0x01,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 225
	0x00,0x70,0xA0,0x60,0x03,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 226
	0x00,0xB0,0x60,0x41,0x03,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 227
	0x00,0x00,0xB0,0x61,0x03,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 228
	0x30,0x90,0x20,0x81,0x01,0x00,0x0F,0x31,0x60,0xFC,0x8C,0x19,0x33,0xC7,0x0D,0x00,0x00,0x00,0x00,0x00, // 229
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x78,0x1E,0x84,0x33,0x80,0x61,0xFC,0x7F,0x86,0x01,0x86,0x01,0xC6,0x43,0x7C,0x3F,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 230
	0x00,0x00,0x00,0x00,0x00,0x00,0x0F,0x23,0x03,0x06,0x0C,0x18,0x60,0x84,0x07,0x04,0x08,0x1C,0x00,0x00, // 231
	0x00,0x30,0x80,0x01,0x0C,0x00,0xE0,0xC1,0x8C,0x61,0xFE,0x19,0x60,0x00,0x43,0xF8,0x00,0x00,0x00,0x00,0x00,0x00, // 232
	0x00,0x00,0x03,0x06,0x0C,0x00,0xE0,0xC1,0x8C,0x61,0xFE,0x19,0x60,0x00,0x43,0xF8,0x00,0x00,0x00,0x00,0x00,0x00, // 233
	0x00,0xE0,0x80,0x02,0x1B,0x00,0xE0,0xC1,0x8C,0x61,0xFE,0x19,0x60,0x00,0x43,0xF8,0x00,0x00,0x00,0x00,0x00,0x00, // 234
	0x00,0x00,0xC0,0x06,0x1B,0x00,0xE0,0xC1,0x8C,0x61,0xFE,0x19,0x60,0x00,0x43,0xF8,0x00,0x00,0x00,0x00,0x00,0x00, // 235
	0x30,0xC6,0x60,0x66,0x66,0x66,0x06,0x00,0x00, // 236
	0x00,0xC8,0x60,0x66,0x66,0x66,0x06,0x00,0x00, // 237
	0x60,0x9F,0x60,0x66,0x66,0x66,0x06,0x00,0x00, // 238
	0x00,0x99,0x60,0x66,0x66,0x66,0x06,0x00,0x00, // 239
	0x00,0x00,0x80,0x09,0x1C,0x7C,0x80,0x83,0x8F,0x63,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 240
	0x00,0x40,0x82,0x0A,0x12,0x00,0xD8,0xE3,0x98,0x61,0x86,0x19,0x66,0x98,0x61,0x86,0x01,0x00,0x00,0x00,0x00,0x00, // 241
	0x00,0x30,0x80,0x01,0x0C,0x00,0xE0,0xC1,0x8C,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 242
	0x00,0x00,0x03,0x06,0x0C,0x00,0xE0,0xC1,0x8C,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 243
	0x00,0xC0,0x80,0x07,0x12,0x00,0xE0,0xC1,0x8C,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 244
	0x00,0x60,0x42,0x09,0x19,0x00,0xE0,0xC1,0x8C,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 245
	0x00,0x00,0xC0,0x0C,0x33,0x00,0xE0,0xC1,0x8C,0x61,0x86,0x19,0x66,0x18,0x33,0x78,0x00,0x00,0x00,0x00,0x00,0x00, // 246
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x06,0x60,0x00,0x00,0xFC,0xC3,0x3F,0x00,0x00,0x06,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00, // 247
	0x00,0x00,0x00,0x00,0x00,0x00,0xE0,0xC5,0x8C,0x79,0xA6,0x59,0xE6,0x19,0x33,0x7A,0x00,0x00,0x00,0x00,0x00,0x00, // 248
	0x00,0x60,0x00,0x03,0x18,0x00,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x98,0x71,0xBC,0x01,0x00,0x00,0x00,0x00,0x00, // 249
	0x00,0x00,0x06,0x0C,0x18,0x00,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x98,0x71,0xBC,0x01,0x00,0x00,0x00,0x00,0x00, // 250
	0x00,0xC0,0x80,0x07,0x12,0x00,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x98,0x71,0xBC,0x01,0x00,0x00,0x00,0x00,0x00, // 251
	0x00,0x00,0xC0,0x0C,0x33,0x00,0x18,0x66,0x98,0x61,0x86,0x19,0x66,0x98,0x71,0xBC,0x01,0x00,0x00,0x00,0x00,0x00, // 252
	0x00,0x80,0x81,0x81,0x01,0x60,0xB0,0x31,0x63,0xC6,0xD8,0xB0,0x41,0x83,0x03,0x06,0x0E,0x0F,0x00,0x00, // 253
	0x00,0x00,0x60,0x80,0x01,0x06,0xD8,0xE1,0x8C,0x61,0x86,0x19,0x66,0x98,0x33,0x76,0x18,0x60,0x80,0x01,0x00,0x00, // 254
	0x00,0x00,0xB0,0x61,0x03,0x60,0xB0,0x31,0x63,0xC6,0xD8,0xB0,0x41,0x83,0x03,0x06,0x0E,0x0F,0x00,0x00 // 255
};
