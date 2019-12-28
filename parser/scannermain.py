
import scannerclass as sc
import scannerfunc as sf

file_name = 'test.txt'
scanner = sf.scanner(file_name)

if scanner.fp != None:
    print('       记号类别              字符串     常数值  函数指针\n')
    print('——————————————————————')
    while(1):
        token = scanner.GetToken()  #输出一个记号
        if token.type == sc.Token_Type.ERRTOKEN:     ##优化空格
            #记号的类别不是错误或者空格，就打印出他的内容
            continue
        elif token.type != sc.Token_Type.ERRTOKEN:  #NONTOKEN       ## 文件结束符直接跳下一行读取数据放在语法分析器里面完成之前的bug
            print("{:20s},{:>12s},{:12f},{}".format(token.type, token.lexeme,token.value,token.funcptr))
        else:
            break
    scanner.CloseScanner()
else:
    print('Open Error!')