# Chpater1

## 基本宣告
最基本的C程式會是如下  
```c
int main(void){
	return 0;
}
```
或者  

```c
void main(void)
{
}
```

[c code 1] `int`代表這個函式會回傳一個整數行態的值,`main(void)`中的`void`表示這個函式不需要任何參數  
[c code 2] `void`代表這個函式不會傳回任何數值  

C語言本身提供了一些最基本的數值儲存型態
| type           | 數值範圍                                                                                                  | Bits |  

| char           | -128~127                                                                                                  | 1    |  
| unsigned char  | 0~255                                                                                                     | 1    |  
| short          | -32768~32767                                                                                              | 2    |  
| unsigned short | 0~65536                                                                                                   | 2    |  
| int            | -2147483648~2147483647                                                                                    | 4    |  
| unsigned int   | 0~4294967295                                                                                              | 4    |  
| long           | -2147483648~2147483647                                                                                    | 4    |  
| unsigned long  | 0~429496729                                                                                               | 4    |  
| float          | 1.175494351e-38~3.402823466e+38 or -1.175494351e-38~-3.402823466e+38                                      | 4    |  
| double         | 2.2250738585072014e-308~1.7976931348623158e+308 or -2.2250738585072014e-308~-1.7976931348623158e+308      | 8    |  

宣告就是跟電腦要求一塊記憶體空間  

測試代碼: [chapter1-1.c](https://github.com/yuhioh217/Code-Tutorial/tree/master/C%20tutorial/Chapter1/chapter1-1.c)


## 輸出 output (printf)

從電腦發出訊息的功能稱做為`output`, C語言的stdio.h中有提供最簡單的printf輸出函式  

```
#include<stdio.h>

void main(void)
{
	printf("hello world\n");
	//透過printf, hello world將會被打印出來, \n是換行符號
	//在printf中，兩個雙引號中間的東西叫做字串
	//記住在C/C++的程式裡每一行程式的結束都要加入分號 ";"
}
```

測試代碼: [chapter1-2.c](https://github.com/yuhioh217/Code-Tutorial/tree/master/C%20tutorial/Chapter1/chapter1-2.c)

Authors
-
Copyright(c) 2017 KE Jiang<<yuihoh217@gmail.com>>
