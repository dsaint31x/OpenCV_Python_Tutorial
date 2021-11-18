import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import IM6



'''
vi3.py에서 실행을 시켜주시면 됩니다.
1. src 폴더 설정 : set_directory - open_src_file
2. label 폴더 설정 : set_directory - open_label_file (만일 label이 없으면 선택 안하면 됩니다)
3. save_path 설정 : Save_path - open_save_file or 직접 입력

세팅해주시고 '실행/Tk종료' 버튼 클릭하면 됩니다.


'''
class A:    
    def __init__(self):
        self.window = Tk()
        self.window.geometry('800x700')
        self.window.title("DIP")
        aa=Label(self.window,text='[주의] <CLAHE와 global_HE>와, <bright와 dark>는 중복 선택 불가!', bg='#ff0', fg='#f00').grid(row=0, column=1)

        menubar = Menu(self.window)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Set_Directory",menu=filemenu)
        filemenu.add_cascade(label="Open_src_file", command=self.src_directory)
        filemenu.add_cascade(label="Open_label_file", command=self.label_directory)
        filemenu.add_separator()
        filemenu2 = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Save_path", menu=filemenu2)
        filemenu2.add_cascade(label="Open_save_file", command=self.save_directory)


        self.window.config(menu=menubar)

        self.check_ch=IntVar()
        self.check_ch1=IntVar()
        self.check_ch2=IntVar()
        self.check_ch3=IntVar()
        self.cl_ck=0
        self.gl_ck=0
        self.br_ck=0
        self.br2_ck=0
        self.window.label_name = None
        self.window.save_name = None

        self.ch3 = Checkbutton(self.window, text="bright", variable=self.check_ch2)
        self.ch3.grid(row=1, column=1)
        self.ch4 = Checkbutton(self.window, text="dark", variable=self.check_ch3)
        self.ch4.grid(row=2, column=1)
        self.ch = Checkbutton(self.window, text="CLAHE", variable=self.check_ch)
        self.ch.grid(row=3, column=1)
        self.ch2 = Checkbutton(self.window, text="global_HE", variable=self.check_ch1)
        self.ch2.grid(row=4, column=1)
        
        
        cl_bm_but = Button(self.window, text="미리보기",command=self.gui)
        cl_bm_but.grid(row=5, column=1)

        #a1_txt = tkinter.IntVar(self.window, value="1")
        #d1_txt = tkinter.StringVar(self.window, value="reflect")
        a = Label(self.window, text=' ').grid(row=7, column=0)

        
        a1=Label(self.window, text='convert_numbers ').grid(row=8, column=0, padx=10)
        self.a2=Entry(self.window,textvariable=IntVar(value=1))
        self.a2.grid(row=8, column=1, sticky='w')
        

        b1=Label(self.window, text='crop_numbers ').grid(row=9, column=0, padx=10)
        self.b2=Entry(self.window,textvariable=IntVar(value=1))
        self.b2.grid(row=9, column=1, sticky='w')
        
        c1=Label(self.window, text='brightness_value ').grid(row=10, column=0, padx=10)
        self.c2=Entry(self.window,textvariable=IntVar())
        self.c2.grid(row=10, column=1, sticky='w')
        c3=Label(self.window, text='brightness 옵션 : -255 ~ 255').grid(row=10, column=2)
        
        d1=Label(self.window, text='fill_mode ').grid(row=11, column=0, padx=10)
        self.d2=Entry(self.window, textvariable=StringVar(value="reflect"))
        self.d2.grid(row=11, column=1, sticky='w')
        d3=Label(self.window, text='(fill_mode 옵션 : reflect, nearest, constant, wrap)').grid(row=11,column=2, sticky='w')
        d4=Label(self.window, text= 'constant_cval ').grid(row=12,column=0)
        self.d5=Entry(self.window, textvariable=IntVar())
        self.d5.grid(row=12, column=1, sticky='w')
        d6=Label(self.window, text='fill_mode가 constant일 경우에만 설정해주세요').grid(row=12, column=2, sticky='w')
        
        self.check_e1=BooleanVar()
        self.e1 = Checkbutton(self.window, text="global_HE ", variable=self.check_e1)
        self.e1.grid(row=13, column=0, sticky='w')


        def check_box():
            if self.check_f1.get()==True:
                f2.grid(row=15, column=0, sticky='w')
                self.f3.grid(row=15, column=1, sticky='w') 
                f4.grid(row=16, column=0, sticky='w')
                self.f5.grid(row=16, column=1, sticky='w')
                
            elif self.check_f1.get() == False:
                f2.grid_forget()
                self.f3.grid_forget()
                f4.grid_forget()
                self.f5.grid_forget()


            if self.check_h1.get()==True:
                h2.grid(row=19, column=0)
                self.h3.grid(row=19, column=1, sticky='w')
                h4.grid(row=19, column=2)
            elif self.check_h1.get() == False:
                h2.grid_forget()
                self.h3.grid_forget()
                h4.grid_forget()

            if self.check_i1.get() == True:
                i2.grid(row=21, column=0)
                self.i3.grid(row=21, column=1, sticky='w')
                i4.grid(row=21, column=2)
            elif self.check_i1.get() == False:
                i2.grid_forget()
                self.i3.grid_forget()
                i4.grid_forget()
            
            if self.check_j1.get()==True:
                j2.grid(row=23, column=0, sticky='w')
                self.j3.grid(row=23, column=1, sticky='w')
                self.jj1.grid(row=22, column=1, sticky='w')
            elif self.check_j1.get()==False:
                j2.grid_forget()
                self.j3.grid_forget()
                self.jj1.grid_forget()

            if self.check_m1.get()==True:
                m2.grid(row=27, column=0, sticky='w')
                self.m3.grid(row=27, column=1, sticky='w')
                m4.grid(row=27, column=2)
            elif self.check_m1.get()==False:
                m2.grid_forget()
                self.m3.grid_forget()
                m4.grid_forget()
        
        self.check_f1=BooleanVar()
        self.f1 = Checkbutton(self.window, text="clahe ", variable=self.check_f1, command = check_box)
        self.f1.grid(row=14, column=0, sticky='w')
        f2 = Label(self.window, text="       ㄴcontrast_limit ")
        self.f3 = Entry(self.window, textvariable=IntVar(value=40))
        f4 = Label(self.window, text="       ㄴgrid_size ")
        self.f5 = Entry(self.window, textvariable=StringVar(value="8,8"))
        
        g1=Label(self.window, text='color ').grid(row=17, column=0, padx=10, sticky='w')
        self.g2=Entry(self.window, textvariable=IntVar())
        self.g2.grid(row=17, column=1, sticky='w')
        g3=Label(self.window,wraplength =260, text='(color 옵션 :  0(COLOR_UNCHANGED) : 그대로 / 1(COLOR_GRAY) : grayscale / 2(COLOR_BGR) : BGR [default=0])').grid(row=17,column=2, sticky='w')
        

        
        self.check_h1=BooleanVar()
        h1=Checkbutton(self.window, text='width_shift_range ', variable=self.check_h1, command=check_box)
        h1.grid(row=18, column=0)
        h2 = Label(self.window, text="   ㄴwidth_shift")
        self.h3 = Entry(self.window, textvariable=DoubleVar())
        h4 = Label(self.window, text="width_shift 옵션 : 0 ~ 1")

        
        self.check_i1=BooleanVar()
        i1=Checkbutton(self.window, text='height_shift_range ', variable=self.check_i1, command=check_box)
        i1.grid(row=20, column=0)
        i2 = Label(self.window, text="   ㄴheight_shift")
        self.i3 = Entry(self.window, textvariable=DoubleVar())
        i4 = Label(self.window, text="height_shift 옵션 : 0 ~ 1")
        

        
        self.check_j1=BooleanVar()
        j1=Checkbutton(self.window, text='degree ', variable=self.check_j1, command = check_box)
        j1.grid(sticky='w',row=22, column=0)
        self.jj1 = Entry(self.window, textvariable=IntVar())
        j2=Label(self.window, text="       ㄴcenter_range")
        self.j3=Entry(self.window, textvariable=DoubleVar())
        
        self.check_k1=BooleanVar()
        k1=Checkbutton(self.window, text='vertical_flip ', variable=self.check_k1)
        k1.grid(row=24, column=0, sticky='w')

        self.check_l1=BooleanVar()
        l1=Checkbutton(self.window, text='horizontal_flip ', variable=self.check_l1)
        l1.grid(row=25, column=0, sticky='w')

        
        self.check_m1=BooleanVar()
        m1=Checkbutton(self.window, text='crop_size ', variable=self.check_m1, command=check_box)
        m1.grid(row=26, column=0, sticky='w')
        m2=Label(self.window, text = "       ㄴ ( y , x )")
        self.m3=Entry(self.window, textvariable = StringVar(value="0,0"))
        m4=Label(self.window, text=" y = 열 길이, x = 행 길이")

        n1 = Label(self.window, text="save_path")
        n1.grid(row=29, column=0, sticky='w', padx=10)
        self.n2 = Entry(self.window, width=50, textvariable=StringVar())
        self.n2.grid(row=29, column=1, sticky='w')


        

        self.finish_but = Button(self.window, text="실행/Tk종료", command=self.fin)
        self.finish_but.grid(row=100, column=1)

        self.window.mainloop()

    def src_directory(self):    # src 파일 path
        self.window.src_name =  filedialog.askdirectory() + "/"
    def label_directory(self):  # label 파일 path
        self.window.label_name =  filedialog.askdirectory() + "/"
    def save_directory(self):
        self.window.save_name = filedialog.askdirectory()
        print(self.window.save_name)
        self.n2.insert(0, self.window.save_name)

    # 버튼으로 tkinter 종료
    def fin(self):
        run = IM6.CCC()
        
        cv = None
        cl = None
        gr2 = None
        ws = None
        hs = None
        cr = None
        cs2 = None
        dd = None
        if self.d2.get() == 'constant':
            cv=int(self.d5.get())
        if self.check_f1.get():
            cl = int(self.f3.get())
            gr = self.f5.get()
            gr1 = gr.split(',')
            gr2 = (int(gr1[0]), int(gr1[1]))

        if self.check_h1.get():
            ws = float(self.h3.get())
        if self.check_i1.get():
            hs = float(self.i3.get())
        if self.check_j1.get():
            dd = int(self.jj1.get())
            cr = float(self.j3.get())
        if self.check_m1.get():
            cs = self.m3.get()
            cs1 = cs.split(',')
            cs2 = (int(cs1[0]), int(cs1[1]))

        run.BBB(
            a1=int(self.a2.get()), 
            a2=int(self.b2.get()), 
            a3=int(self.c2.get()), 
            a4=self.d2.get(), 
            a5=cv, 
            a6=self.check_e1.get(), 
            a7=self.check_f1.get(),
            a8=cl, 
            a9=gr2,
            a10 = int(self.g2.get()),
            a11 = ws,
            a12 = hs,
            a13 = dd,
            a14 = cr,
            a15 = self.check_k1.get(),
            a16 = self.check_l1.get(),
            a17 = cs2,
            a18 = self.n2.get(),
            a19 = self.window.src_name,
            a20 = self.window.label_name

            )
        #____________________________________________----------------------------------------------------
        
        
        
        self.window.destroy()


    def onChange(self,pos):
        self.cl_ck=1
    def onChange2(self,pos):
        self.br_ck=1
    def onChange3(self,pos):
        self.br2_ck=1
        
    
    def gui(self):

        if (self.check_ch.get()==1 and self.check_ch1.get()==1) or (self.check_ch2.get()==1 and self.check_ch3.get()==1) :    # clahe와 global_HE 같이 체크 / 밝기 중복 체크
            messagebox.showerror("경고!", "bright와 dark / CLAHE와 global_HE 중 하나만 선택해주세요")
                    
        else:

            img_list = os.listdir(self.window.src_name)  
            #src폴더 내에 n번째 이미지 불러오기
            self.set_img_n = cv2.imread(self.window.src_name + img_list[0])                  

            cv2.namedWindow('imgView', cv2.WINDOW_NORMAL)

            cv2.imshow('imgView',self.set_img_n)

            if self.check_ch2.get() == 1: #bright 체크된 상태
                cv2.createTrackbar("bright", "imgView", 0, 255, self.onChange2)
                
            if self.check_ch3.get() == 1:   #dark 체크된 상태
                cv2.createTrackbar("dark", "imgView", 0,255, self.onChange3)

            if self.check_ch1.get() ==1:  #global_he 체크된 상태
                self.gl_ck=1

            if self.check_ch.get() == 1:  #clahe 체크된 상태
                cv2.createTrackbar("CLAHE", "imgView", 0, 100, self.onChange)

            while True:
                sample_image = cv2.cvtColor(self.set_img_n, cv2.COLOR_BGR2YUV)
                
                if cv2.waitKey()&0xff ==27:
                    cv2.destroyAllWindows()
                    break
                else:
                    # CLAHE setting
                    if self.cl_ck==1:
                        clip = cv2.getTrackbarPos("CLAHE", "imgView")
                        clip_0 = sample_image.copy()
                        if clip == 0:
                            sample_image[:,:,0] = clip_0[:,:,0]
                        else:
                            clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(8,8))
                    
                            sample_image[:,:,0] = clahe.apply(sample_image[:,:,0])

                    # global_HE setting
                    if self.gl_ck==1:
                        sample_image[:,:,0] = cv2.equalizeHist(sample_image[:,:,0])
                    
                    # brightness setting
                    if self.br_ck==1:
                        br = cv2.getTrackbarPos("bright", "imgView")
                        sample_image[:,:,0] = cv2.add(sample_image[:,:,0], br)

                    if self.br2_ck==1:
                        br2 = cv2.getTrackbarPos("dark", "imgView")
                        sample_image[:,:,0] = cv2.subtract(sample_image[:,:,0],br2)

                    sample_image = cv2.cvtColor(sample_image, cv2.COLOR_YUV2BGR)
                    cv2.imshow('imgView', sample_image)


A()