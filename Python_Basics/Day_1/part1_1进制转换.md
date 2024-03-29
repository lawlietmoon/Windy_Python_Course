### 1.1 计算机硬件基本认知
```python
cpu:   中央处理器.   相当于人的大脑.运算中心,控制中心.
内存:  临时存储数据.  优点:读取速度快。 缺点:容量小,造价高,断电即消失.
硬盘:  长期存储数据.  优点:容量大,造价相对低,断电不消失。 缺点:读取速度慢.
操作系统:统一管理计算机软硬件资源的程序
```
![1557729534117](D:\python8\day1\assets\1557729534117.png)python



### 1.2计算机文件大小单位

```python
b = bit  位(比特)
B = Byte 字节

1Byte = 8 bit   #一个字节等于8位  可以简写成 1B = 8b
1KB = 1024B
1MB = 1024KB
1GB = 1024MB
1TB = 1024GB
1PB = 1024TB
1EB = 1024PB
```
### 1.3进制转换

```python
二进制:由2个数字组成,有0 和 1  			   例:  0b101 
八进制:由8个数字组成,有0,1,2,3,4,5,6,7        例:  0o127 
十进制:有10个数字组成,有0,1,2,3,4,5,6,7,8,9   例:  250
十六进制:有16个数字组成,有0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f(字母大小写都可以,分别代表10,11,12,13,14,15) 例:0xff  0Xff  0XFF	        
```
#### 1.3.1 二进制 转化成 十进制
```python
#例:	0b10100101  
运算:1* 2^0 + 0* 2^1 + 1* 2^2 + 0* 2^3 + 0* 2^4 + 1* 2^5 + 0* 2^6 + 1* 2^7= 
1 + 0 + 4 + 0 + 0 + 32 + 0 + 128 = 165
```
#### 1.3.2 八进制 转化成 十进制
```python
#例:	0o127
运算:7*8^0 + 2*8^1 + 1*8^2 = 7+16+64 = 87
```
#### 1.3.3 十六进制 转化成 十进制
```python
#例:	0xff
运算:15*16^0 + 15*16^1 = 255
```

####  *小练习: 转化成对应进制

```python
723 => 2 
654 => 2
723 => 8  
654 => 8
723 => 16 
654 => 16
```
#### 1.3.4 十进制 转化成 二进制

```python
426 => 0b110101010  
运算过程:   用426除以2,得出的结果再去不停地除以2,
			直到除完最后的结果小于2停止,
			在把每个阶段求得的余数从下到上依次拼接完毕即可
```
#### 1.3.5 十进制 转化成 八进制		
```python
426 => 0o652
运算过程:   用426除以8,得出的结果再去不停地除以8,
			直到除完最后的结果小于8停止,
			在把每个阶段求得的余数从下到上依次拼接完毕即可
```
#### 1.3.6 十进制 转化成 十六进制	
```python
运算过程:   用426除以16,得出的结果再去不停地除以16,
			直到除完最后的结果小于16停止,
			在把每个阶段求得的余数从下到上依次拼接完毕即可
```
####  *小练习: 转化成对应进制
```python
723 => 2 
654 => 2
723 => 8  
654 => 8
723 => 16 
654 => 16
```
####  1.3.7  二进制与八进制转换
```
二进制与八进制对应关系:
八进制  二进制
0		000
1		001
2		010
3		011
4		100
5		101
6		110
7		111
```
```
例:1010100101
八进制:从右向左 3位一隔开 不够三位用0补位 变成:
001 010 100 101
0o   1    2   4   5
```
####  1.3.8  二进制与十六进制转换
```
十六进制  二进制
0		  0000
1		  0001
2		  0010
3		  0011
4		  0100
5		  0101
6		  0110
7		  0111
8		  1000
9		  1001
a		  1010
b		  1011
c		  1100
d		  1101
e		  1110
f		  1111
```
```
例:1010100101
十六进制:从右向左 4位一隔开 不够四位用0补位 变成:
0010 1010 0101 
0x2a5
```
#### 1.3.9 八进制 与 十六进制的转换
```python
先转换成二进制 再去对应转换 
比如:0x2a5 转换成 1010100101 再转8进制 0o1245
```
#### *小练习: 转化成对应进制
```
0x1DD => 8 
0x29a => 8
0o573 => 16
0o336 => 16
```
### 1.4原码,反码,补码
```
# 1.原码 或 补码 都是用来表达二进制数据  
    原码: 用来转换对应进制 
    反码: 二进制码0变1,1变0叫做反码,反码用于原码补码之间的转换.(首位符号位不变)
    补码: 用来做数据的存储和运算. 补码的提出用于表达一个数的正负（实现减法）    

    计算机的所有数据在底层都是以二进制的[补码]形式存储
    实际上人们看到的数字是[原码]转化来的
    [原码] 和 [补码] 可以通过计算互相转化

# 2.整体顺序：
补码 -> 原码 -> 最后人们看到的数
***进制转换的时候需要先把内存存储的补码拿出来变成原码在进行转换输出***

# 3.运算规律：
原码：正数高位补0  负数高位补1  
    数字1   00000000 1  正数高位第一位补0
    数字-1  10000000 1  负数高位第一位补1

计算机默认只会做加法,实现减法用负号： 5+(-3) => 5-3
乘法除法:是通过左移和右移 << >> 来实现

# 4.原码 与 反码之间的转换
(原码 反码 补码之间的转换 , 符号位不要动)
正数: 原码 = 反码 = 补码
负数: 原码 = 补码取反加1   给补码求原码
负数: 补码 = 原码取反加1   给原码求补码
```
#### *小练习：原码 与 反码的转换
```
#给原码求补码
    -6 的补码是多少? 
    6  的补码是多少?
    10 的补码是多少?
   -10 的补码是多少?
     9 的补码是多少?
    -9 的补码是多少?
#给补码求原码
	1 ... 111  00011 (高位都是1) 
	1 ... 111  01100 (高位都是1) 
# 9+(-5) 用二进制相加运算一下
```
