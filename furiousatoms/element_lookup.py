import csv
from io import StringIO


elems_csv = """\
number,symbol,name,mass,valency
1,H,hydrogen,1.0079,1
2,He,helium,4.0026,0
3,Li,lithium,6.941,1
4,Be,beryllium,9.0122,2
5,B,boron,10.811,3
6,C,carbon,12.0107,4
7,N,nitrogen,14.0067,-3
8,O,oxygen,15.9994,-2
9,F,fluorine,18.9984,-1
10,Ne,neon,20.1797,0
11,Na,sodium,22.9897,1
12,Mg,magnesium,24.305,2
13,Al,aluminium,26.9815,3
14,Si,silicon,28.0855,4
15,P,phosphorus,30.9738,5
16,S,sulfur,32.065,6
17,Cl,chlorine,35.453,-1
18,Ar,argon,39.948,0
19,K,potassium,39.0983,1
20,Ca,calcium,40.078,2
21,Sc,scandium,44.9559,3
22,Ti,titanium,47.867,4
23,V,vanadium,50.9415,5
24,Cr,chromium,51.9961,3
25,Mn,manganese,54.938,2
26,Fe,iron,55.845,2
27,Co,cobalt,58.9332,3
28,Ni,nickel,58.6934,2
29,Cu,copper,63.546,2
30,Zn,zinc,65.39,2
31,Ga,gallium,69.723,3
32,Ge,germanium,72.64,-4
33,As,arsenic,74.9216,-3
34,Se,selenium,78.96,-2
35,Br,bromine,79.904,-1
36,Kr,krypton,83.8,2
37,Rb,rubidium,85.4678,1
38,Sr,strontium,87.62,2
39,Y,yttrium,88.9059,3
40,Zr,zirconium,91.224,4
41,Nb,niobium,92.9064,5
42,Mo,molybdenum,95.94,4
43,Tc,technetium,98,4
44,Ru,ruthenium,101.07,3
45,Rh,rhodium,102.9055,3
46,Pd,palladium,106.42,2
47,Ag,silver,107.8682,1
48,Cd,cadmium,112.411,2
49,In,indium,114.818,3
50,Sn,tin,118.71,-4
51,Sb,antimony,121.76,0
52,Te,tellurium,127.6,-3
53,I,iodine,126.9045,-2
54,Xe,xenon,131.293,2
55,Cs,caesium,132.9055,1
56,Ba,barium,137.327,2
57,La,lanthanum,138.9055,3
58,Ce,cerium,140.116,3
59,Pr,praseodymium,140.9077,3
60,Nd,neodymium,144.24,3
61,Pm,promethium,145,3
62,Sm,samarium,150.36,3
63,Eu,europium,151.964,3
64,Gd,gadolinium,157.25,3
65,Tb,terbium,158.9253,3
66,Dy,dysprosium,162.5,3
67,Ho,holmium,164.9303,3
68,Er,erbium,167.259,3
69,Tm,thulium,168.9342,3
70,Yb,ytterbium,173.04,3
71,Lu,lutetium,174.967,3
72,Hf,hafnium,178.49,4
73,Ta,tantalum,180.9479,5
74,W,tungsten,183.84,4
75,Re,rhenium,186.207,4
76,Os,osmium,190.23,4
77,Ir,iridium,192.217,3
78,Pt,platinum,195.078,2
79,Au,gold,196.9665,3
80,Hg,mercury,200.59,1
81,Tl,thallium,204.3833,1
82,Pb,lead,207.2,2
83,Bi,bismuth,208.9804,3
84,Po,polonium,209,-2
85,At,astatine,210,-1
86,Rn,radon,222,0
87,Fr,francium,223,1
88,Ra,radium,226,2
89,Ac,actinium,227,3
90,Th,thorium,232.0381,4
91,Pa,protactinium,231.0359,5
92,U,uranium,238.0289,6
93,Np,Neptunium,237.064,5
94,Pu, Plutonium,244.064,3
95,Am,Americium,243.061,3
96,Cm,Curium,247.070,3
97,Bk,Berkelium,247.070,3
98,Cf,Californium,251.080,3
99,Es,Einsteinium,254,3
100,Fm,Fermium,257.0953,3
101,Md,Mendelevium,258.1,3
102,No,Nobelium,259.101,2
103,Lr,Lawrencium,262,3
104,Rf,Rutherfordium,261,4
105,Db,Dubnium,262,5
106,Sg,Seaborgium,266,6
107,Bh,Bohrium,264,7
108,Hs,Hassium,269,8
109,Mt,Meitnerium,278,0
110,Ds,Darmstadtium,281,0
111,Rg,Roentgenium,280,0
112,Cn,Copernicium,285,2
113,Nh,Nihonium,286,0
114,Fl,Fleronium,289,0
115,Mc,Moscovium,289,0
116,Lv,Livermorium,293,0
117,Ts,Tennessine,294,0
118,Og,Oganesson,294,0
"""




def lookup_element_by_mass(mass: float):
    elems = [row for row in csv.DictReader(StringIO(elems_csv))]
    #Search for element with mass that's up to 0.1 different from input.
    #If it can't find one, try again with 1.0. 
    for tolerance in (0.1, 1.0):
        for row in elems:
            m = float(row['mass'])
            if abs(mass - m) < tolerance:
                return row
    raise ValueError("No element exists with mass", mass)




class ColorLookup():
    def __init__(self) -> None:
        #Colors CSV credit to https://sciencenotes.org/molecule-atom-colors-cpk-colors/
        colors_csv = """
        1	H	255,255,255
        1	D, H-2	255,255,192
        1	T, H-3	255,255,160
        2	He	217,255,255
        3	Li	204,128,255
        4	Be	194,255,0
        5	B	255,181,181
        6	C	144,144,144
        6	C-13	80,80,80
        6	C-14	64,64,64
        7	N	48,80,248
        7	N-15	16,80,80
        8	O	255,13,13
        9	F	144,224,80
        10	Ne	179,227,245
        11	Na	171,92,242
        12	Mg	138,255,0
        13	Al	191,166,166
        14	Si	240,200,160
        15	P	255,128,0
        16	S	255,255,48
        17	Cl	31,240,31
        18	Ar	128,209,227
        19	K	143,64,212
        20	Ca	61,255,0
        21	Sc	230,230,230
        22	Ti	191,194,199
        23	V	166,166,171
        24	Cr	138,153,199
        25	Mn	156,122,199
        26	Fe	224,102,51
        27	Co	240,144,160
        28	Ni	80,208,80
        29	Cu	200,128,51
        30	Zn	125,128,176
        31	Ga	194,143,143
        32	Ge	102,143,143
        33	As	189,128,227
        34	Se	255,161,0
        35	Br	166,41,41
        36	Kr	92,184,209
        37	Rb	112,46,176
        38	Sr	0,255,0
        39	Y	148,255,255
        40	Zr	148,224,224
        41	Nb	115,194,201
        42	Mo	84,181,181
        43	Tc	59,158,158
        44	Ru	36,143,143
        45	Rh	10,125,140
        46	Pd	0,105,133
        47	Ag	192,192,192
        48	Cd	255,217,143
        49	In	166,117,115
        50	Sn	102,128,128
        51	Sb	158,99,181
        52	Te	212,122,0
        53	I	148,0,148
        54	Xe	66,158,176
        55	Cs	87,23,143
        56	Ba	0,201,0
        57	La	112,212,255
        58	Ce	255,255,199
        59	Pr	217,255,199
        60	Nd	199,255,199
        61	Pm	163,255,199
        62	Sm	143,255,199
        63	Eu	97,255,199
        64	Gd	69,255,199
        65	Tb	48,255,199
        66	Dy	31,255,199
        67	Ho	0,255,156
        68	Er	0,230,117
        69	Tm	0,212,82
        70	Yb	0,191,56
        71	Lu	0,171,36
        72	Hf	77,194,255
        73	Ta	77,166,255
        74	W	33,148,214
        75	Re	38,125,171
        76	Os	38,102,150
        77	Ir	23,84,135
        78	Pt	208,208,224
        79	Au	255,209,35
        80	Hg	184,184,208
        81	Tl	166,84,77
        82	Pb	87,89,97
        83	Bi	158,79,181
        84	Po	171,92,0
        85	At	117,79,69
        86	Rn	66,130,150
        87	Fr	66,0,102
        88	Ra	0,125,0
        89	Ac	112,171,250
        90	Th	0,186,255
        91	Pa	0,161,255
        92	U	0,143,255
        93	Np	0,128,255
        94	Pu	0,107,255
        95	Am	84,92,242
        96	Cm	120,92,227
        97	Bk	138,79,227
        98	Cf	161,54,212
        99	Es	179,31,212
        100	Fm	179,31,186
        101	Md	179,13,166
        102	No	189,13,135
        103	Lr	199,0,102
        104	Rf	204,0,89
        105	Db	209,0,79
        106	Sg	217,0,69
        107	Bh	224,0,56
        108	Hs	230,0,46
        109	Mt	235,0,38
        110	Ds	unassigned
        111	Rg	unassigned
        112	Cn	unassigned
        113	Nh	unassigned
        114	Fl	unassigned
        115	Mc	unassigned
        116	Lv	unassigned
        117	Ts	unassigned
        118	Og	unassigned
        """
        self.table = [row for row in csv.DictReader(StringIO(colors_csv), delimiter='\t',fieldnames=['number','symbol','color'])]
        colors_csv = None

    def get_element_color(self, symbol: str) -> list:
        for row in self.table:
            if symbol == row['symbol']:
                if row['color'] == "unassigned":
                    return None
                color = row['color'].split(",")
                return [int(color[0]), int(color[1]), int(color[2]), OPACITY]
        return None

COLOR_LOOKUP = ColorLookup()
OPACITY = 1