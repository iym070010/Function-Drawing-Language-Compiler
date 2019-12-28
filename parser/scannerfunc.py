import scannerclass as sc
import os


class scanner():

    ##——————初始化词法分析器
    def __init__(self,file_name):   #输入要输入字符流的文件名
        self.LineNo = 0 #记录字符所在行的行号
        self.TokenBuffer = '' #待识别记号缓存区
        self.file_name=r'C:\Users\62473\Desktop\\'+file_name     #此处根据个人情况做调整
        if os.path.exists(self.file_name):
            self.fp = open(self.file_name, "r",encoding='UTF-8')     #文件指针
        else:
            self.fp = None

    ##——————关闭词法分析器
    def CloseScanner(self):
        if self.fp!=None:
            self.fp.close()

    ##——————从输入流中读入一个字符
    def GetChar(self):
        Char = self.fp.read(1)
        return Char

    ##——————输入流回退一个字符
    def BackChar(self,Char):        ## 非二进制打开方式不能直接seek目前位置回溯，所以用tell()-1方式从头跳转前一位置
        if Char != '':
            self.fp.seek(self.fp.tell()-1)

    ##——————加入字符到TokenBuffer待识别字符串中
    def AddCharToString(self,Char):
        self.TokenBuffer+=Char

    ##——————清空TokenBuffer字符串
    def EmptyString(self):
        self.TokenBuffer=''

    ##——————识别的字符串查表
    def JudgeKeyToken(self):
        Token=sc.Alphabet.get(self.TokenBuffer,sc.Tokens(sc.Token_Type.ERRTOKEN,self.TokenBuffer,0.0,None))
        return Token


    ##——————获取记号
    # 此函数由DFA转化而来(有必要的话可以写个模拟dfa函数)此函数输出一个记号。每调用该函数一次，仅仅获得一个记号。
    # 因此，要获得源程序的所有记号，就要重复调用这个函数。上面声明的函数都被此函数调用过
    # 因为没有自定义变量，所以只需要查表不需要构造其他东西
    # 输出一个记号，没有输入
    def GetToken(self):

        Char = ''   ##字符流
        type = ''   ##指向返回输出的Tokens对象
        self.EmptyString()  #清空缓冲区
        while(1):
            Char = self.GetChar()
            if Char == ' ':
                type = sc.Tokens(sc.Token_Type.NONTOKEN,Char,0.0,None)
                return type
            if Char == '\n':
                self.LineNo=self.LineNo+1
            if ~Char.isspace():
                break
        self.AddCharToString(Char) ##若不是空格、TAB、回车、文件结束符等，则先加入到记号的字符缓冲区中
        if Char.isalpha():## 判断是否是英文
            while(1):
                Char = self.GetChar()
                if Char.isalnum():
                    self.AddCharToString(Char)
                else:
                    break
            self.BackChar(Char)
            type = self.JudgeKeyToken()
            type.lexeme = self.TokenBuffer
            return type

        elif Char.isdigit():
            while(1):
                Char = self.GetChar()
                if Char.isdigit():
                    self.AddCharToString(Char)
                else:
                    break
            if Char == '.':
                self.AddCharToString(Char)
                while(1):
                    Char = self.GetChar()
                    if Char.isdigit():
                        self.AddCharToString(Char)
                    else:
                        break
            self.BackChar(Char)
            type = sc.Tokens(sc.Token_Type.CONST_ID,self.TokenBuffer,float(self.TokenBuffer),None)
            return type

        else:
            if Char == ';':
                type = sc.Tokens(sc.Token_Type.SEMICO,Char,0.0,None)
            elif Char == '(':
                type = sc.Tokens(sc.Token_Type.L_BRACKET,Char,0.0,None)
            elif Char == ')':
                type = sc.Tokens(sc.Token_Type.R_BRACKET, Char, 0.0, None)
            elif Char == ',':
                type = sc.Tokens(sc.Token_Type.COMMA, Char, 0.0, None)
            elif Char == '+':
                type = sc.Tokens(sc.Token_Type.PLUS, Char, 0.0, None)
            elif Char == '-':   ##可能是行分割或减号
                Char = self.GetChar()
                if Char == '-':
                    while Char != '\n' and Char != '':
                        Char = self.GetChar()
                    self.BackChar(Char)
                    return self.GetToken()
                else:
                    self.BackChar(Char)
                    type = sc.Tokens(sc.Token_Type.MINUS, '-', 0.0, None)
            elif Char == '/':   ##可能是注释分割或除号
                Char = self.GetChar()
                if Char == '/':
                    self.fp.readline()
                    return self.GetToken()  ## 读到注释直接跳到下一行
                else:
                    self.BackChar(Char)
                    type = sc.Tokens(sc.Token_Type.DIV, '/', 0.0, None)
            elif Char == '*':
                Char = self.GetChar()
                if (Char == '*'):
                        type = sc.Tokens(sc.Token_Type.POWER, '**', 0.0, None)
                else:
                    self.BackChar(Char)
                    type = sc.Tokens(sc.Token_Type.MUL, '*', 0.0, None)
            else:
                type = sc.Tokens(sc.Token_Type.ERRTOKEN, Char, 0.0, None)
        return type
