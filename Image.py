import cv2
import imageio
class Img:
    def __init__(self, nameWindow,fileName):
        self.file_name = fileName 
        self.nameWindow = nameWindow
        self.current_img=imageio.imread(fileName)
        self.prev_img=""
        self.text=""
        self.shape=""
        self.show_image()
    def show_image(self):
        self.current_img = imageio.imread(self.file_name)
        self.current_img = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2RGB)
        self.current_img=cv2.resize(self.current_img,(600,400))
        cv2.imshow(self.nameWindow,self.current_img)
    def circle(self):
        self.shape = "circle"
        cv2.setMouseCallback(self.nameWindow, self.draw)
        print("c")
    def rectangle(self):
        self.shape = "rectangle"
        cv2.setMouseCallback(self.nameWindow, self.draw)
        print("r")
    def line(self):
        self.shape = "line"
        cv2.setMouseCallback(self.nameWindow, self.draw)
        print("l")
    def draw(self, event, x, y, flags, param):

        self.renderImg()
        global ix,iy,drawing
        drawing=False
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix = x
            iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if self.shape=="line":
                cv2.line(self.current_img, (ix, iy), (x, y), (200,100, 100), 8)
                cv2.imshow(self.nameWindow,self.current_img)
            elif self.shape=="rectangle":
                cv2.rectangle(self.current_img, (ix, iy), (x, y), (100, 0, 100), 5)
                cv2.imshow(self.nameWindow, self.current_img)
            elif self.shape=="circle":
                cv2.circle(self.current_img, ((ix + x) // 2, (iy + y) // 2),int(((((ix - x) ** 2) + ((iy - y) ** 2)) ** 0.5) / 2), (180, 50, 80), 5)
                cv2.imshow(self.nameWindow, self.current_img)
    def ImgBeforeEffects(self):
        self.prev_img=self.current_img
    def black_white(self):
        try:
            self.current_img=cv2.cvtColor(self.current_img, cv2.COLOR_RGB2GRAY)
            self.renderImg()
        except Exception:
            self.current_img=self.prev_img
            self.black_white()

    def just_edges(self):
            self.prev_img = self.current_img
            self.current_img=cv2.Canny(self.current_img, 50,180)
            self.renderImg()
    def blur(self):
        self.current_img=cv2.blur(self.current_img,(20,20))
        self.renderImg()
    def colorful(self):
        try:
            self.prev_img = self.current_img
            self.current_img = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2YCrCb)
            self.renderImg()
        except:
            self.current_img=self.prev_img
            self.renderImg()
            self.colorful()
    def add_text(self,text):
        global t
        t=text
        cv2.setMouseCallback(self.nameWindow,self.draw_text)
    def draw_text(self,event,x,y,flags,params):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(self.current_img, t, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            self.renderImg()
    def cut(self):
        cv2.setMouseCallback(self.nameWindow, self.cutting)
    def cutting(self,event,x,y,flags,params):
        global ix, iy
        if event == cv2.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
        elif event==cv2.EVENT_LBUTTONUP:
            cut_image=self.current_img[iy:y,ix:x]
            cv2.imshow(self.nameWindow,cut_image)
    def renderImg(self):
        cv2.imshow(self.nameWindow, self.current_img)
    def rotate(self):
        self.current_img = cv2.rotate(self.current_img, cv2.ROTATE_90_CLOCKWISE)
        self.renderImg()
    def exit(self):#
        cv2.destroyAllWindows()
    def save(self):
        cv2.imwrite("your_img.jpg",self.current_img)

