from turtle import *
# color('red', 'yellow')
# begin_fill()
while True:
    forward(200)
    left(170)
    print("pos", pos(), abs(pos()))
    if abs(pos()[0]) < 1 and abs(pos()[1]) < 1:
        break
# end_fill()
done()