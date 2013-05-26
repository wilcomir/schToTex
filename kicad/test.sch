EESchema Schematic File Version 2  date 26/05/2013 21:43:32
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:test-cache
EELAYER 27 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "26 may 2013"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L R R1
U 1 1 51A1FE4F
P 4600 3600
F 0 "R1" V 4680 3600 40  0000 C CNN
F 1 "2k2" V 4607 3601 40  0000 C CNN
F 2 "~" V 4530 3600 30  0000 C CNN
F 3 "~" H 4600 3600 30  0000 C CNN
	1    4600 3600
	0    -1   -1   0   
$EndComp
$Comp
L C C1
U 1 1 51A1FE5E
P 5300 3600
F 0 "C1" H 5300 3700 40  0000 L CNN
F 1 "100nF" H 5306 3515 40  0000 L CNN
F 2 "~" H 5338 3450 30  0000 C CNN
F 3 "~" H 5300 3600 60  0000 C CNN
	1    5300 3600
	0    -1   -1   0   
$EndComp
$Comp
L INDUCTOR_SMALL L1
U 1 1 51A1FE7F
P 6000 3600
F 0 "L1" H 6000 3700 50  0000 C CNN
F 1 "2uH" H 6000 3550 50  0000 C CNN
F 2 "~" H 6000 3600 60  0000 C CNN
F 3 "~" H 6000 3600 60  0000 C CNN
	1    6000 3600
	1    0    0    -1  
$EndComp
$Comp
L BATTERY BT1
U 1 1 51A1FF15
P 4250 4000
F 0 "BT1" H 4250 4200 50  0000 C CNN
F 1 "12V" H 4250 3810 50  0000 C CNN
F 2 "~" H 4250 4000 60  0000 C CNN
F 3 "~" H 4250 4000 60  0000 C CNN
	1    4250 4000
	0    1    1    0   
$EndComp
Wire Wire Line
	4250 3600 4350 3600
Wire Wire Line
	4250 4400 5150 4400
Wire Wire Line
	5150 4400 6350 4400
Wire Wire Line
	6350 4400 6350 3600
Wire Wire Line
	6350 3600 6250 3600
Wire Wire Line
	5750 3600 5500 3600
Wire Wire Line
	5100 3600 4850 3600
Connection ~ 5150 4400
Wire Wire Line
	4250 4400 4250 4300
Wire Wire Line
	4250 3700 4250 3600
$EndSCHEMATC
