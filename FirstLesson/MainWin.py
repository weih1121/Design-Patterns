class Point:
    __pos_x
    __pos_y

    def __init__(self, x, y):
        self.__pos_x = x
        self.__pox_y = y

class Line:
    __Point_start
    __Point_end

    def __init__(self, Point1, Point2):
        self.__Point_start = Point1
        self.__Point_end   = Point2

class Rect:
    __Point_left_top
    __Width
    __Height

    def __init__(self, Point, width, height):
        self.__Point_left_top = Point
        self.__Width          = width
        self.__Height         = height

class Form:                                     #Form是一个抽象基类
    pass; 

class MainForm(Form):
    __Point1
    __Point2
    __LineList
    __RectList
    def __init__(self):
        super.__init__()
        pass
    
    def OnMouseDown(self, e):
        #追踪鼠标动作
        self.__Point1.x = e.x
        self.__Point1.y = e.y
        if (e.action() == drawLine)
            self.__LineList.append(self.Point1)
        elif (e.action() == drawRect):
            self.__RectList.append(self.Point1)
        else:
            pass
        #...
        pass

    def OnMouseUp(self, e):
        self.__Point2.x = e.x
        self.__Point2.y = e.y
        self.OnPaint()   #更新窗口操作


    def OnPaint(self, e):
        if (e.action() == drawLine)
            self.drawLine(self.__Point1, self.__Point2)
        elif (e.action() == drawRect):
            width = abs(self.__Point1.x - self.__Point2.x)
            height = abs(self.__Point1.y - self.__Point2.y)
            self.drawRect(self.__Point1, width, height)
        else:
            pass
        pass

    def drawLine(self, Point_start, Point_end):
        pass

    def drawRect(self, Point_left_top, width, height):
        pass



