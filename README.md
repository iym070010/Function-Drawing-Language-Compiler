# <编译原理 - 函数绘图语言解释器（1）词法分析器 - python>

### scanner:词法分析器

+ [<编译原理 - 函数绘图语言解释器（1）解释器 - python>](https://www.cnblogs.com/ymjun/p/11773681.html "词法分析器")

+ 设计思路：
	1. 设计记号：词法分析器读取一个序列并根据构词规则把序列转化为记号流

	2. 定义一个字典：把所有符合一个模式的保留字、常量名、参数名、函数名等放进字典。字典是个数组，其元素的类型和记号的类型相同

	3. 设计程序的结构，具体见下面的代码

+ 用Pycharm写了三个.py文件：
	+ scannerclass.py - 构造枚举类 记号类 符号表
	
	+ scannerfunc.py - 构造词法分析器类
	
	+ scannermain.py - 完成I/O流
	
	+ 输入流是序列（存储在.txt文本），输出流是“字典”（一个个识别好的记号对象）
	
	+ 测试文本序列（1）：
	`FOR T FROM 0 TO 2*PI STEP PI/50 DRAW(COS(t),sin(t));`
	
	+ 测试文本序列（2）：
	
```
//------------------This is zhushi!!------------------------
ORIGIN IS (100,300);  						// Sets the offset of the origin
ROT IS 0;									// Set rotation Angle.
SCALE IS (1,1);								// Set the abscissa and ordinate scale.
FOR T FROM 0 TO 200 STEP 1 DRAW (T,0);		// The trajectory of the x-coordinate.
FOR T FROM 0 TO 150 STEP 1 DRAW (0,-T);		// The trajectory of the y-coordinate.
FOR T FROM 0 TO 120 STEP 1 DRAW (T,-T);		// The trajectory of the function f[t]=t.
```


### parser:语法分析器

+ [<编译原理 - 函数绘图语言解释器（2）语法分析器 - python>](https://www.cnblogs.com/ymjun/p/11963230.html "语法分析器")

+ 设计思路：
	1. 设计函数绘图语言的文法，使其适合递归下降分析；
	
	2. 设计语法树的结构，用于存放表达式的语法树；
	
	3. 设计递归下降子程序，分析句子并构造表达式的语法树；
	
	4. 设计测试程序和测试用例，检验分析器是否正确。

+ 消除无二义/无左递归完整的EBNF文法：

![](https://img2018.cnblogs.com/blog/1816059/201911/1816059-20191130170322636-359501919.png)

+ 表达式的语法树：

![](https://img2018.cnblogs.com/blog/1816059/201911/1816059-20191130170330251-1823170695.png)

+ 用Pycharm写了三个.py文件：
	+ parserclass.py - 构造语法树节点类
	
	+ parserfunc.py - 构造语法分析器类
	
	+ parsermain.py - 完成I/O流
	
	+ 输入流是词法分析器得到的记号流，输出流是语法树
	
	+ 测试文本序列（1）
```
FOR T FROM 0 TO 2*PI STEP PI/50 DRAW(COS(T),SIN(T));
```

	+ 测试文本序列 (2)
```
//------------------This is zhushi!!------------------------
ORIGIN IS (100,300);                        // Sets the offset of the origin
ROT IS 0;                                   // Set rotation Angle.
SCALE IS (1,1);                             // Set the abscissa and ordinate scale.
FOR T FROM 0 TO 200 STEP 1 DRAW (T,0);      // The trajectory of the x-coordinate.
FOR T FROM 0 TO 150 STEP 1 DRAW (0,-T);     // The trajectory of the y-coordinate.
FOR T FROM 0 TO 120 STEP 1 DRAW (T,-T);     // The trajectory of the function f[t]=t.
```

### semantic:解释器

+ [<编译原理 - 函数绘图语言解释器（3）解释器 - python>](https://www.cnblogs.com/ymjun/p/12006048.html "解释器")

+ 设计思路：
	+ 将语法分析器并入绘图功能
	
	+ 继承语法分析器覆盖重写
	
+ 用Pycharm写了一个.py文件：
	+ semanticfunc.py - 继承语法分析器并入绘制功能
	
	+ semanticmain.py - 解释器主函数入口 //与语法分析器入门用的同一个入口
	
	+ 输入流是语法分析器得到的语法树，输出流是绘制的图像

	+ 测试文本序列：
	
```
//----------------测试程序1：分别测试------------------------
ORIGIN IS (100,300);                        // Sets the offset of the origin
ROT IS 0;                                   // Set rotation Angle.
SCALE IS (1,1);                             // Set the abscissa and ordinate scale.
FOR T FROM 0 TO 200 STEP 1 DRAW (T,0);      // The trajectory of the x-coordinate.
FOR T FROM 0 TO 150 STEP 1 DRAW (0,-T);     // The trajectory of the y-coordinate.
FOR T FROM 0 TO 120 STEP 1 DRAW (T,-T);     // The trajectory of the function f[t]=t.
FOR T FROM 0 TO 2*PI STEP PI/50 DRAW(COS(T),SIN(T));
//---------测试程序2----------
ORIGIN IS (20, 200);
ROT IS 0;
SCALE IS (40, 40);
FOR T FROM 0 TO 2*PI STEP PI/50 DRAW (T, -SIN(T));
ORIGIN IS (20, 240);
FOR T FROM 0 TO 2*PI STEP PI/50 DRAW (T, -SIN(T));
ORIGIN IS (20, 280);
FOR T FROM 0 TO 2*PI STEP PI/50 DRAW (T, -SIN(T));
//-----------------测试程序3--------------
ORIGIN IS (380, 240);
SCALE IS (80, 80/3);
ROT IS PI/2+0*PI/3 ;
FOR T FROM -PI TO PI STEP PI/50 DRAW (COS(T), SIN(T));
ROT IS PI/2+2*PI/3;
FOR T FROM -PI TO PI STEP PI/50 DRAW (COS(T), SIN(T));
ROT IS PI/2-2*PI/3;
FOR T FROM -PI TO PI STEP PI/50 DRAW (COS(T), SIN(T));
//-------------------测试程序4-------------
ORIGIN IS(580, 240);
SCALE IS (80, 80);
ROT IS 0;
FOR T FROM 0 TO 2*PI STEP PI/50 DRAW(COS(T),SIN(T));
FOR T FROM 0 TO PI*20 STEP PI/50 DRAW((1-1/(10/7))*COS(T)+1/(10/7)*COS(-T*((10/7)-1)),(1-1/(10/7))*SIN(T)+1/(10/7)*SIN(-T*((10/7)-1)));
//-------------------测试程序5------------
//------------ 函数复杂度图形：-----------
ROT IS 0;	-- 不旋转
ORIGIN IS (50, 400);	-- 设置新原点（距系统默认原点的偏移量）
SCALE IS (2,1);	-- 设置比例
FOR T FROM 0 TO 300 STEP 1 DRAW (T,0);	-- 横坐标
FOR T FROM 0 TO 300 STEP 1 DRAW (0,-T);	-- 纵坐标
SCALE IS (2,1);	-- 设置比例
FOR T FROM 0 TO 300 STEP 1 DRAW (T,-T);	-- 函数F(T)=T的轨迹
SCALE IS (2,0.1);	-- 设置比例
FOR T FROM 0 TO 55 STEP 1 DRAW (T,-T*T);	-- 函数F(T)=T*T的轨迹
SCALE IS (10,5);	-- 设置比例
FOR T FROM 0 TO 60 STEP 1 DRAW (T,-SQRT(T));	-- 函数F(T)=SQRT(T)的轨迹
SCALE IS (20,0.1);	-- 设置比例
FOR T FROM 0 TO 8 STEP 0.1 DRAW (T,-EXP(T));	-- 函数F(T)=EXP(T)的轨迹
SCALE IS (2,20);	-- 设置比例
FOR T FROM 0 TO 300 STEP 1 DRAW (T,-LN(T));	-- 函数F(T)=LN(T)的轨迹
```


### My Blog：[Welcome to Hlong Blog!](https://www.cnblogs.com/ymjun/ "黄龙士")