# 原码和补码转换练习
二进制的最高位 ： 0代表正数  1代表负数

5：  
原码： 00000000 ... 101
反码： 00000000 ... 101
补码： 00000000 ... 101

-3：
原码： 10000000 ... 011
反码： 11111111 ... 100
补码： 11111111 ... 101

5
00000000 ... 101
11111111 ... 101
00000000 ... 010

求补码：
00000000 ... 010  => 2  5+(-3) = 2

-5
原码：10000 ... 101
反码：11111 ... 010
补码: 11111 ... 011

+3
原码：00000 ... 011
反码：00000 ... 011
补码：00000 ... 011

-5 + 3
11111 ... 011
00000 ... 011

求补码：
11111 ... 110

给补码求原码： 互为取反加1
补码：11111 ... 110
反码：10000 ... 001
原码：10000 ... 010

-5 + 3
10000 ... 010 =>-2


9
原码：00000 ...  1001
反码：00000 ...  1001
补码：00000 ...  1001


-5 （求反码 符号位不动的）
原码：1 000 ... 101
反码：1 111 ... 010
补码：1 111 ... 011

9+（-5）
0 000 ...  1001
1 111 ...  1011
0 000 ...  0100

0 000 ...  0100 => 4
