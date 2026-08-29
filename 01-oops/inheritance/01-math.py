class Math:
    PI = 3.14
    @staticmethod
    def getCircleArea(radius):
        area = Math.PI * radius * radius
        return area
math = Math()
print(math.getCircleArea(5))