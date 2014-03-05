""" Pin capabilities """
CAP_RESERVED = 0x0
CAP_GPIO     = 0x1
CAP_ADC      = 0x2
CAP_PWM      = 0x4

""" UPER1 board pinout """
pinout = {1 : [CAP_GPIO,             [0]],
          2 : [CAP_GPIO,             [1]],
          3 : [CAP_GPIO | CAP_PWM,   [2,1,2]],
          4 : [CAP_GPIO,             [3]],
          5 : [CAP_GPIO,             [4]],
          6 : [CAP_RESERVED],
          7 : [CAP_RESERVED],
          8 : [CAP_GPIO,             [5]],
          9 : [CAP_GPIO,             [6]],
         10 : [CAP_GPIO | CAP_PWM,   [7,1,0]],
         11 : [CAP_GPIO,             [8]],
         12 : [CAP_GPIO,             [9]],
         13 : [CAP_GPIO,             [10]],
         14 : [CAP_GPIO,             [11]],
         15 : [CAP_GPIO,             [12]],
         16 : [CAP_GPIO,             [13]],
         17 : [CAP_GPIO,             [14]],
         18 : [CAP_GPIO,             [15]],
         19 : [CAP_RESERVED],
         20 : [CAP_RESERVED],
         21 : [CAP_RESERVED],
         22 : [CAP_RESERVED],
         23 : [CAP_GPIO | CAP_ADC,   [33,0]],
         24 : [CAP_GPIO | CAP_ADC,   [32,1]],
         25 : [CAP_GPIO | CAP_ADC,   [31,2]],
         26 : [CAP_GPIO | CAP_ADC,   [30,3]],
         27 : [CAP_GPIO | CAP_PWM,   [29,0,0]],
         28 : [CAP_GPIO | CAP_PWM,   [28,0,1]],
         29 : [CAP_GPIO,             [27]],
         30 : [CAP_GPIO | CAP_ADC,   [26,4]],
         31 : [CAP_GPIO | CAP_ADC,   [25,5]],
         32 : [CAP_GPIO | CAP_ADC,   [24,6]],
         33 : [CAP_GPIO | CAP_ADC,   [23,7]],
         34 : [CAP_GPIO | CAP_PWM,   [22,0,2]],
         35 : [CAP_GPIO,             [21]],
         36 : [CAP_GPIO,             [20]],
         37 : [CAP_GPIO,             [19]],
         38 : [CAP_GPIO,             [18]],
         39 : [CAP_GPIO | CAP_PWM,   [17,1,1]],
         40 : [CAP_GPIO,             [16]]
}