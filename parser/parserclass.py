import scannerclass as sc


class ExprNode(object):     ## 语法树节点类
    def __init__(self,item):        ## item 表示符号类型Token_Type
        self.item = item #表示对应的元素
        if self.item == sc.Token_Type.PLUS or self.item == sc.Token_Type.MINUS or \
                self.item == sc.Token_Type.MUL or self.item == sc.Token_Type.DIV or \
                self.item == sc.Token_Type.POWER:
            # 运算符 - 两个孩子
            self.left=None
            self.right=None
        elif self.item == sc.Token_Type.FUNC:
            self.FuncPtr = None
            self.center = None      ## 一个孩子
        self.value = None       ## 传入的所有类型都有value
    def __str__(self):      ## 叶子节点
        return str(self.item)  #print 一个 Node 类时会打印 __str__ 的返回值

    def GetExprValue(self):
        if self.item == sc.Token_Type.PLUS:
            self.value = self.right.value + self.left.value
        elif self.item == sc.Token_Type.MINUS:
            self.value = self.left.value - self.right.value
        elif self.item == sc.Token_Type.MUL:
            self.value = self.left.value * self.right.value
        elif self.item == sc.Token_Type.DIV:
            self.value = self.left.value / self.right.value
        elif self.item == sc.Token_Type.POWER:
            self.value = self.left.value ** self.right.value
        elif self.item == sc.Token_Type.FUNC:
            self.value = self.FuncPtr(self.center.value)
        return self.value
