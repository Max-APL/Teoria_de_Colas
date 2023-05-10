from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from MM1 import *
from MMS import *
from MM1K import *

class Principal(Tk):
	def __init__(self, master=None, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.master = master

		self.principal()


	def principal(self):
		print("Funciona")
		self.notebook = ttk.Notebook(self)
		style = ttk.Style()
		settings = {"TNotebook.Tab": {"configure": {"padding": [10, 1],
                                                    "background": "#13B72F",
                                                    "border":0
                                                   },
                                      "map": {"background": [("selected", "green"), 
                                                             ("active", "green")],
                                              "foreground": [("selected", "#ffffff"),
                                                             ("active", "#ffffff")]

                                             }
                                      }
                   }
		try:
			style.theme_create("mi_estilo", parent="alt", settings=settings)
			style.theme_use("mi_estilo")
		except:
			style.theme_use("mi_estilo")
		self.notebook.pack(fill=BOTH,expand=True)
		
		self.pestana1 = Frame(self.notebook, bg="white")
		self.notebook.add(self.pestana1,text="Modelo M/M/1")
		self.pestana2 = Frame(self.notebook,bg="white")
		self.notebook.add(self.pestana2,text="Modelo M/M/S")
		self.pestana3 = Frame(self.notebook,bg="white")
		self.notebook.add(self.pestana3,text="Modelo M/M/1/K")

		
		self.widgets()
		
   
	def widgets(self):
		
        # LLama a wigets de pentaña1
		self.widgetsPestana1()

        # LLama a wigets de pentaña2
		self.widgetsPestana2()

        # LLama a wigets de pentaña3
		self.widgetsPestana3()

	def widgetsPestana1(self):

		# Variables
		self.lamnda1 = DoubleVar()
		self.niuw1 = DoubleVar()
		self.n1 = IntVar()
		self.p1 = DoubleVar()
		self.p01 = DoubleVar()
		self.pn1 = DoubleVar()
		self.ls1 = DoubleVar()
		self.lq1 = DoubleVar()
		self.ws1 = DoubleVar()
		self.wq1 = DoubleVar()
		


		self.lb_mm1 = Label(self.pestana1, text="Modelo M/M/1", fg="black", font=("Arial Black",20), bg="white")
		self.lb_mm1.place(x=50, y=30)

		self.lb_mm1_parrafo = Text(self.pestana1)
		text='''El modelo MM1 (M/M/1) en un banco sirve 
para analizar y predecir el comportamiento 
de la cola de clientes, estimar el tiempo 
medio de espera, calcular el número 
medio de clientes en la cola y evaluar 
la utilización del personal. 

Estos análisis permiten optimizar la 
gestión de colas, mejorar la eficiencia 
operativa y la asignación de recursos, 
lo que a su vez ayuda amejorar la 
satisfacción del cliente y la toma 
de decisiones en el entorno bancario.
		'''
		self.lb_mm1_parrafo.insert("10.0",text)
		self.lb_mm1_parrafo.config(spacing1=2, font=("Arial",12), fg="black",bg="white",borderwidth=2, highlightthickness=3)
		self.lb_mm1_parrafo.place(x=50, y=90,width=310 ,height=230)


		self.lb_lamda0 = Label(self.pestana1, text="Tasa media de llegada:", fg="black", font=("Arial",11), bg="white")
		self.lb_lamda0.place(x=50, y=330)
		self.lb_lamda = Label(self.pestana1, text="λ = ", fg="black", font=("Arial",12), bg="white")
		self.lb_lamda.place(x=70, y=355)
		self.lb_lamda1 = Label(self.pestana1, text="clientes/hora", fg="black", font=("Arial",12), bg="white")
		self.lb_lamda1.place(x=200, y=355)

		self.et_lamda = Entry(self.pestana1, textvariable=self.lamnda1, font=("Arial",12))
		self.et_lamda.place(x=150, y=355,width=40)

		self.lb_nuew0 = Label(self.pestana1, text="Tasa media de servicio:", fg="black", font=("Arial",11), bg="white")
		self.lb_nuew0.place(x=50, y=390)
		self.lb_nuew = Label(self.pestana1, text="μ = ", fg="black", font=("Arial",12), bg="white")
		self.lb_nuew.place(x=70, y=415)
		self.lb_nuew1 = Label(self.pestana1, text="clientes/hora", fg="black", font=("Arial",12), bg="white")
		self.lb_nuew1.place(x=200, y=415)

		self.et_nuew = Entry(self.pestana1, textvariable= self.niuw1, font=("Arial",12))
		self.et_nuew.place(x=150, y=415,width=40)

		self.lb_n0 = Label(self.pestana1, text="Numero de clientes en el sistema:", fg="black", font=("Arial",11), bg="white")
		self.lb_n0.place(x=50, y=450)
		self.lb_n = Label(self.pestana1, text="n = ", fg="black", font=("Arial",12), bg="white")
		self.lb_n.place(x=70, y=475)
		self.lb_n1 = Label(self.pestana1, text="clientes", fg="black", font=("Arial",12), bg="white")
		self.lb_n1.place(x=200, y=475)

		self.et_n = Entry(self.pestana1, textvariable= self.n1, font=("Arial",12))
		self.et_n.place(x=150, y=475,width=40)

		
		# Cargar la imagen con PIL
		imagen_pil1 = Image.open("assets//images//bmsc-logo.png")

		# Convertir la imagen a un objeto PhotoImage de Tkinter
		self.imagen_tk1 = ImageTk.PhotoImage(imagen_pil1)

		# Crear un widget Label y mostrar la imagen
		self.etiqueta = Label(self.pestana1, image=self.imagen_tk1)
		self.etiqueta.place(x=650,y=30)

		# Formulas 

		self.lb_form0 = Label(self.pestana1, text="Factor de\n Utilidad:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form0.place(x=400, y=150,width=250)
		self.et_form0 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.p1, state="readonly")
		self.et_form0.place(x=700, y=156,height=25)
		
		self.lb_form1 = Label(self.pestana1, text="Probabilidad de que el sistema\n este vacio:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form1.place(x=400, y=200,width=250)
		self.et_form1 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.p01, state="readonly")
		self.et_form1.place(x=700, y=206,height=25)
		
		self.lb_form2 = Label(self.pestana1, text="Probabilidad de que el sistema\n tenga n clientes:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form2.place(x=400, y=250,width=250)
		self.et_form2 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.pn1, state="readonly")
		self.et_form2.place(x=700, y=256,height=25)
		
		self.lb_form3 = Label(self.pestana1, text="Numero de clientes\n en el sistema:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form3.place(x=400, y=300,width=250)
		self.et_form3 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.ls1, state="readonly")
		self.et_form3.place(x=700, y=306,height=25)

		self.lb_form4 = Label(self.pestana1, text="Numero de clientes\n en la cola:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form4.place(x=400, y=350,width=250)
		self.et_form4 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.lq1, state="readonly")
		self.et_form4.place(x=700, y=356,height=25)

		self.lb_form5 = Label(self.pestana1, text="Tiempo promedio de espera\n en el sistema:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form5.place(x=400, y=400,width=250)
		self.et_form5 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.ws1, state="readonly")
		self.et_form5.place(x=700, y=406,height=25)

		self.lb_form6 = Label(self.pestana1, text="Tiempo promedio de espera\n en la cola:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form6.place(x=400, y=450,width=250)
		self.et_form6 = Entry(self.pestana1,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.wq1, state="readonly")
		self.et_form6.place(x=700, y=456,height=25)

		
		self.lb_form0 = Label(self.pestana1, text="", fg="black", bg="white", font=("Arial",12))
		self.lb_form0.place(x=777, y=156)
		
		self.lb_form1 = Label(self.pestana1, text="%", fg="black", bg="white", font=("Arial",12))
		self.lb_form1.place(x=777, y=206)
		
		self.lb_form2 = Label(self.pestana1, text="%", fg="black", bg="white", font=("Arial",12))
		self.lb_form2.place(x=777, y=256)
		
		self.lb_form3 = Label(self.pestana1, text="clientes", fg="black", bg="white", font=("Arial",12))
		self.lb_form3.place(x=777, y=306)
		
		self.lb_form4 = Label(self.pestana1, text="clientes", fg="black", bg="white", font=("Arial",12))
		self.lb_form4.place(x=777, y=356)

		self.lb_form5 = Label(self.pestana1, text="horas", fg="black", bg="white", font=("Arial",12))
		self.lb_form5.place(x=777, y=406)

		self.lb_form6 = Label(self.pestana1, text="horas", fg="black", bg="white", font=("Arial",12))
		self.lb_form6.place(x=777, y=456)

		def calcularMM1():
			modeloMM1 = MM1(self.lamnda1.get(), self.niuw1.get())
			self.p1.set(round(modeloMM1.p(),3))
			self.p01.set(round(modeloMM1.p0(),3))
			self.pn1.set(round(modeloMM1.Pn(self.n1.get())))
			self.ls1.set(round(modeloMM1.Ls(),3))
			self.lq1.set(round(modeloMM1.Lq(),3))
			self.ws1.set(round(modeloMM1.Ws(),3))
			self.wq1.set(round(modeloMM1.Wq(),3))

		def limpiar():
			# Variables
			self.lamnda1.set(0.0)
			self.niuw1.set(0.0)
			self.n1.set(0)
			self.p1.set(0.0)
			self.p01.set(0.0)
			self.pn1.set(0.0)
			self.ls1.set(0.0)
			self.lq1.set(0.0)
			self.ws1.set(0.0)
			self.wq1.set(0.0)

		def mostrar (formula):
			if (formula == 0):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P M/M/1")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Factor de Utilidad ",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_0.png")
				imagen_formula = imagen_formula.resize((100,90))
				self.imagen_formula10 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula10)
				etiqueta.place(x=40, y=50)



			elif (formula == 1):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P(0) M/M/1")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Probabilidad de Sistema vacio",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_1.png")
				imagen_formula = imagen_formula.resize((170,100))
				self.imagen_formula11 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula11)
				etiqueta.place(x=40, y=50)
			elif (formula == 2):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P(n) M/M/1")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Probabilidad de Sistema con n clientes",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_2.png")
				imagen_formula = imagen_formula.resize((230,100))
				self.imagen_formula12 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula12)
				etiqueta.place(x=40, y=50)
			elif (formula == 3):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Ls M/M/1")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Clientes en el sistema",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_3.png")
				imagen_formula = imagen_formula.resize((200,90))
				self.imagen_formula13 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula13)
				etiqueta.place(x=40, y=50)
			elif (formula == 4):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Lq M/M/1")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Clientes en la cola",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_4.png")
				imagen_formula = imagen_formula.resize((200,90))
				self.imagen_formula14 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula14)
				etiqueta.place(x=40, y=50)
			elif (formula == 5):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Ws M/M/1" )
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tiempo en el sistema",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_5.png")
				imagen_formula = imagen_formula.resize((200,90))
				self.imagen_formula15 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula15)
				etiqueta.place(x=40, y=50)
			elif (formula == 6):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Wq M/M/1")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tiempo en la cola",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1_6.png")
				imagen_formula = imagen_formula.resize((210,90))
				self.imagen_formula16 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula16)
				etiqueta.place(x=40, y=50)


		self.btn_calc = Button(self.pestana1, text="Calcular", font=("Arial",14), command= calcularMM1)
		self.btn_calc.place(x=100,y=520)

		self.btn_clear = Button(self.pestana1, text="Limpiar", font=("Arial",14), command= limpiar)
		self.btn_clear.place(x=200,y=520)


		imagen_help = Image.open("assets//images//help.png")

		# Convertir la imagen a un objeto PhotoImage de Tkinter
		imagen_help = imagen_help.resize((25,25))
		self.imagen_help = ImageTk.PhotoImage(imagen_help)

		self.btn_form01 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(0))
		self.btn_form01.place(x=870,y=156,width=25,height=25)
		
		self.btn_form11 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(1))
		self.btn_form11.place(x=870,y=206,width=25,height=25)

		self.btn_form21 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(2))
		self.btn_form21.place(x=870,y=256,width=25,height=25)

		self.btn_form31 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(3))
		self.btn_form31.place(x=870,y=306,width=25,height=25)

		self.btn_form41 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(4))
		self.btn_form41.place(x=870,y=356,width=25,height=25)
		
		self.btn_form51 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(5))
		self.btn_form51.place(x=870,y=406,width=25,height=25)

		self.btn_form61 = Button(self.pestana1, image=self.imagen_help, bd=0, highlightthickness=0, command= lambda:mostrar(6))
		self.btn_form61.place(x=870,y=456,width=25,height=25)

		
		
		pass

	def widgetsPestana2(self):
		# Variables
		self.lamnda2 = DoubleVar()
		self.niuw2 = DoubleVar()
		self.n2 = IntVar()
		self.s2 = IntVar()
		self.p2 = DoubleVar()
		self.p02 = DoubleVar()
		self.pn2 = DoubleVar()
		self.ls2 = DoubleVar()
		self.lq2 = DoubleVar()
		self.ws2 = DoubleVar()
		self.wq2 = DoubleVar()
		


		self.lb_mms = Label(self.pestana2, text="Modelo M/M/S", fg="black", font=("Arial Black",20), bg="white")
		self.lb_mms.place(x=50, y=30)

		self.lb_mms_parrafo = Text(self.pestana2)
		text='''El modelo MMS (M/M/S) en un banco sirve 
para analizar y predecir el comportamiento 
de la cola de clientes en sistemas con 
múltiples servidores. El modelo MMS 
permite estudiar cómo el número de 
servidores afecta las métricas de 
desempeño, como el tiempo medio de 
espera y la utilización del personal. 

Esto resulta especialmente útil en 
bancos con múltiples ventanillas de 
atención al cliente, donde el análisis 
MMS puede ayudar a determinar la 
cantidad óptima de servidores para 
satisfacer la demanda de manera 
eficiente, minimizar los tiempos de 
espera y maximizar la utilización de 
los recursos disponibles.'''
		self.lb_mms_parrafo.insert("10.0",text)
		self.lb_mms_parrafo.config(spacing1=2, font=("Arial",12), fg="black",bg="white",borderwidth=2, highlightthickness=3)
		self.lb_mms_parrafo.place(x=50, y=90,width=310 ,height=190)


		self.lb_lamda0 = Label(self.pestana2, text="Tasa media de llegada:", fg="black", font=("Arial",11), bg="white")
		self.lb_lamda0.place(x=50, y=290)
		self.lb_lamda = Label(self.pestana2, text="λ = ", fg="black", font=("Arial",12), bg="white")
		self.lb_lamda.place(x=70, y=315)
		self.lb_lamda1 = Label(self.pestana2, text="clientes/hora", fg="black", font=("Arial",12), bg="white")
		self.lb_lamda1.place(x=200, y=315)

		self.et_lamda = Entry(self.pestana2, textvariable=self.lamnda2, font=("Arial",12))
		self.et_lamda.place(x=150, y=315,width=40)

		self.lb_nuew0 = Label(self.pestana2, text="Tasa media de servicio:", fg="black", font=("Arial",11), bg="white")
		self.lb_nuew0.place(x=50, y=350)
		self.lb_nuew = Label(self.pestana2, text="μ = ", fg="black", font=("Arial",12), bg="white")
		self.lb_nuew.place(x=70, y=375)
		self.lb_nuew1 = Label(self.pestana2, text="clientes/hora", fg="black", font=("Arial",12), bg="white")
		self.lb_nuew1.place(x=200, y=375)

		self.et_nuew = Entry(self.pestana2, textvariable= self.niuw2, font=("Arial",12))
		self.et_nuew.place(x=150, y=375,width=40)

		self.lb_n0 = Label(self.pestana2, text="Numero de clientes en el sistema:", fg="black", font=("Arial",11), bg="white")
		self.lb_n0.place(x=50, y=410)
		self.lb_n = Label(self.pestana2, text="n = ", fg="black", font=("Arial",12), bg="white")
		self.lb_n.place(x=70, y=435)
		self.lb_n1 = Label(self.pestana2, text="clientes", fg="black", font=("Arial",12), bg="white")
		self.lb_n1.place(x=200, y=435)

		self.et_n = Entry(self.pestana2, textvariable= self.n2, font=("Arial",12))
		self.et_n.place(x=150, y=435,width=40)

		self.lb_s0 = Label(self.pestana2, text="Numero de servidores en el sistema:", fg="black", font=("Arial",11), bg="white")
		self.lb_s0.place(x=50, y=470)
		self.lb_s = Label(self.pestana2, text="s = ", fg="black", font=("Arial",12), bg="white")
		self.lb_s.place(x=70, y=495)
		self.lb_s1 = Label(self.pestana2, text="servidores", fg="black", font=("Arial",12), bg="white")
		self.lb_s1.place(x=200, y=495)

		self.et_s = Entry(self.pestana2, textvariable= self.s2, font=("Arial",12))
		self.et_s.place(x=150, y=495,width=40)


		
		# Cargar la imagen con PIL
		imagen_pil2 = Image.open("assets//images//bmsc-logo.png")

		# Convertir la imagen a un objeto PhotoImage de Tkinter
		self.imagen_tk2 = ImageTk.PhotoImage(imagen_pil2)

		# Crear un widget Label y mostrar la imagen
		self.etiqueta = Label(self.pestana2, image=self.imagen_tk2)
		self.etiqueta.place(x=650,y=30)

		# Formulas 

		self.lb_form0 = Label(self.pestana2, text="Factor de\n Utilidad:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form0.place(x=400, y=150,width=250)
		self.et_form0 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.p2, state="readonly")
		self.et_form0.place(x=700, y=156,height=25)
		
		self.lb_form1 = Label(self.pestana2, text="Probabilidad de que el sistema\n este vacio:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form1.place(x=400, y=200,width=250)
		self.et_form1 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.p02, state="readonly")
		self.et_form1.place(x=700, y=206,height=25)
		
		self.lb_form2 = Label(self.pestana2, text="Probabilidad de que el sistema\n tenga n clientes:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form2.place(x=400, y=250,width=250)
		self.et_form2 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.pn2, state="readonly")
		self.et_form2.place(x=700, y=256,height=25)
		
		self.lb_form3 = Label(self.pestana2, text="Numero de clientes\n en el sistema:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form3.place(x=400, y=300,width=250)
		self.et_form3 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.ls2, state="readonly")
		self.et_form3.place(x=700, y=306,height=25)

		self.lb_form4 = Label(self.pestana2, text="Numero de clientes\n en la cola:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form4.place(x=400, y=350,width=250)
		self.et_form4 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.lq2, state="readonly")
		self.et_form4.place(x=700, y=356,height=25)

		self.lb_form5 = Label(self.pestana2, text="Tiempo promedio de espera\n en el sistema:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form5.place(x=400, y=400,width=250)
		self.et_form5 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.ws2, state="readonly")
		self.et_form5.place(x=700, y=406,height=25)

		self.lb_form6 = Label(self.pestana2, text="Tiempo promedio de espera\n en la cola:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form6.place(x=400, y=450,width=250)
		self.et_form6 = Entry(self.pestana2,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.wq2, state="readonly")
		self.et_form6.place(x=700, y=456,height=25)

		
		self.lb_form0 = Label(self.pestana2, text="", fg="black", bg="white", font=("Arial",12))
		self.lb_form0.place(x=777, y=156)
		
		self.lb_form1 = Label(self.pestana2, text="%", fg="black", bg="white", font=("Arial",12))
		self.lb_form1.place(x=777, y=206)
		
		self.lb_form2 = Label(self.pestana2, text="%", fg="black", bg="white", font=("Arial",12))
		self.lb_form2.place(x=777, y=256)
		
		self.lb_form3 = Label(self.pestana2, text="clientes", fg="black", bg="white", font=("Arial",12))
		self.lb_form3.place(x=777, y=306)
		
		self.lb_form4 = Label(self.pestana2, text="clientes", fg="black", bg="white", font=("Arial",12))
		self.lb_form4.place(x=777, y=356)

		self.lb_form5 = Label(self.pestana2, text="horas", fg="black", bg="white", font=("Arial",12))
		self.lb_form5.place(x=777, y=406)

		self.lb_form6 = Label(self.pestana2, text="horas", fg="black", bg="white", font=("Arial",12))
		self.lb_form6.place(x=777, y=456)

		def calcularMMS():
			modeloMMS = MMS(self.lamnda2.get(), self.niuw2.get(), self.s2.get())
			self.p2.set(round(modeloMMS.p(),3))
			self.p02.set(round(modeloMMS.p0(),3))
			self.pn2.set(round(modeloMMS.Pn(self.n2.get())))
			self.ls2.set(round(modeloMMS.Ls(),3))
			self.lq2.set(round(modeloMMS.Lq(),3))
			self.ws2.set(round(modeloMMS.Ws(),3))
			self.wq2.set(round(modeloMMS.Wq(),3))

		def limpiar():
			# Variables
			self.lamnda2.set(0.0)
			self.niuw2.set(0.0)
			self.n2.set(0)
			self.s2.set(0)
			self.p2.set(0.0)
			self.p02.set(0.0)
			self.pn2.set(0.0)
			self.ls2.set(0.0)
			self.lq2.set(0.0)
			self.ws2.set(0.0)
			self.wq2.set(0.0)

		def mostrar (formula):
			if (formula == 0):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P M/M/S")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Factor de Utilidad ",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_0.png")
				imagen_formula = imagen_formula.resize((100,90))
				self.imagen_formula20 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula20)
				etiqueta.place(x=40, y=50)



			elif (formula == 1):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P(0) M/M/S")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Probabilidad de Sistema vacio",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_1.png")
				imagen_formula = imagen_formula.resize((250,140))
				self.imagen_formula21 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula21)
				etiqueta.place(x=40, y=50)
			elif (formula == 2):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P(n) M/M/S")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Probabilidad de Sistema con n clientes",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_2.png")
				imagen_formula = imagen_formula.resize((250,140))
				self.imagen_formula22 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula22)
				etiqueta.place(x=40, y=50)
			elif (formula == 3):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Ls M/M/S")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Clientes en el sistema",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_3.png")
				imagen_formula = imagen_formula.resize((235,120))
				self.imagen_formula23 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula23)
				etiqueta.place(x=40, y=50)
			elif (formula == 4):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Lq M/M/S")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Clientes en la cola",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_4.png")
				imagen_formula = imagen_formula.resize((200,90))
				self.imagen_formula24 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula24)
				etiqueta.place(x=40, y=50)
			elif (formula == 5):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Ws M/M/S" )
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tiempo en el sistema",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_5.png")
				imagen_formula = imagen_formula.resize((200,90))
				self.imagen_formula25 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula25)
				etiqueta.place(x=40, y=50)
			elif (formula == 6):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Wq M/M/S")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tiempo en la cola",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MMS_6.png")
				imagen_formula = imagen_formula.resize((210,90))
				self.imagen_formula26 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula26)
				etiqueta.place(x=40, y=50)
		
		self.btn_calc = Button(self.pestana2, text="Calcular", font=("Arial",14), command= calcularMMS)
		self.btn_calc.place(x=85,y=525)

		self.btn_clear = Button(self.pestana2, text="Limpiar", font=("Arial",14), command= limpiar)
		self.btn_clear.place(x=185,y=525)


		imagen_help2 = Image.open("assets//images//help.png")

		# Convertir la imagen a un objeto PhotoImage de Tkinter
		imagen_help2 = imagen_help2.resize((25,25))
		self.imagen_help2 = ImageTk.PhotoImage(imagen_help2)

		self.btn_form02 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(0))
		self.btn_form02.place(x=870,y=156,width=25,height=25)
		
		self.btn_form12 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(1))
		self.btn_form12.place(x=870,y=206,width=25,height=25)

		self.btn_form22 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(2))
		self.btn_form22.place(x=870,y=256,width=25,height=25)

		self.btn_form32 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(3))
		self.btn_form32.place(x=870,y=306,width=25,height=25)

		self.btn_form42 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(4))
		self.btn_form42.place(x=870,y=356,width=25,height=25)
		
		self.btn_form52 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(5))
		self.btn_form52.place(x=870,y=406,width=25,height=25)

		self.btn_form62 = Button(self.pestana2, image=self.imagen_help2, bd=0, highlightthickness=0, command= lambda:mostrar(6))
		self.btn_form62.place(x=870,y=456,width=25,height=25)

		
		
		pass

	def widgetsPestana3(self):
		# Variables
		self.lamnda3 = DoubleVar()
		self.niuw3 = DoubleVar()
		self.n3 = IntVar()
		self.k3 = IntVar()
		self.p3 = DoubleVar()
		self.p03 = DoubleVar()
		self.pn3 = DoubleVar()
		self.ls3 = DoubleVar()
		self.lq3 = DoubleVar()
		self.ws3 = DoubleVar()
		self.wq3 = DoubleVar()
		self.lam_prom3 = DoubleVar()
		


		self.lb_mms = Label(self.pestana3, text="Modelo M/M/1/K", fg="black", font=("Arial Black",20), bg="white")
		self.lb_mms.place(x=50, y=30)

		self.lb_mms_parrafo = Text(self.pestana3)
		text='''El modelo MM1K (M/M/1/K) en un banco 
se aplica para analizar y predecir el
comportamiento de la cola de clientes 
cuando se tiene un solo servidor y una 
capacidad de espera limitada a K clientes
en la cola. 

En un entorno bancario, el modelo MM1K 
puede ayudar a determinar un límite 
adecuado para la capacidad de espera, 
optimizar la asignación de recursos y 
la gestión de la cola, y garantizar 
una experiencia de atención al 
cliente más eficiente y satisfactoria, 
evitando situaciones de congestión o 
rechazo de clientes.'''
		self.lb_mms_parrafo.insert("10.0",text)
		self.lb_mms_parrafo.config(spacing1=2, font=("Arial",12), fg="black",bg="white",borderwidth=2, highlightthickness=3)
		self.lb_mms_parrafo.place(x=50, y=90,width=310 ,height=190)


		self.lb_lamda0 = Label(self.pestana3, text="Tasa media de llegada:", fg="black", font=("Arial",11), bg="white")
		self.lb_lamda0.place(x=50, y=290)
		self.lb_lamda = Label(self.pestana3, text="λ = ", fg="black", font=("Arial",12), bg="white")
		self.lb_lamda.place(x=70, y=315)
		self.lb_lamda1 = Label(self.pestana3, text="clientes/hora", fg="black", font=("Arial",12), bg="white")
		self.lb_lamda1.place(x=200, y=315)

		self.et_lamda = Entry(self.pestana3, textvariable=self.lamnda3, font=("Arial",12))
		self.et_lamda.place(x=150, y=315,width=40)

		self.lb_nuew0 = Label(self.pestana3, text="Tasa media de servicio:", fg="black", font=("Arial",11), bg="white")
		self.lb_nuew0.place(x=50, y=350)
		self.lb_nuew = Label(self.pestana3, text="μ = ", fg="black", font=("Arial",12), bg="white")
		self.lb_nuew.place(x=70, y=375)
		self.lb_nuew1 = Label(self.pestana3, text="clientes/hora", fg="black", font=("Arial",12), bg="white")
		self.lb_nuew1.place(x=200, y=375)

		self.et_nuew = Entry(self.pestana3, textvariable= self.niuw3, font=("Arial",12))
		self.et_nuew.place(x=150, y=375,width=40)

		self.lb_n0 = Label(self.pestana3, text="Numero de clientes en el sistema:", fg="black", font=("Arial",11), bg="white")
		self.lb_n0.place(x=50, y=410)
		self.lb_n = Label(self.pestana3, text="n = ", fg="black", font=("Arial",12), bg="white")
		self.lb_n.place(x=70, y=435)
		self.lb_n1 = Label(self.pestana3, text="clientes", fg="black", font=("Arial",12), bg="white")
		self.lb_n1.place(x=200, y=435)

		self.et_n = Entry(self.pestana3, textvariable= self.n3, font=("Arial",12))
		self.et_n.place(x=150, y=435,width=40)

		self.lb_s0 = Label(self.pestana3, text="Capacidad maxima de clientes en cola:", fg="black", font=("Arial",11), bg="white")
		self.lb_s0.place(x=50, y=470)
		self.lb_s = Label(self.pestana3, text="K = ", fg="black", font=("Arial",12), bg="white")
		self.lb_s.place(x=70, y=495)
		self.lb_s1 = Label(self.pestana3, text="clientes", fg="black", font=("Arial",12), bg="white")
		self.lb_s1.place(x=200, y=495)

		self.et_k = Entry(self.pestana3, textvariable= self.k3, font=("Arial",12))
		self.et_k.place(x=150, y=495,width=40)


		
		# Cargar la imagen con PIL
		imagen_pil3 = Image.open("assets//images//bmsc-logo.png")

		# Convertir la imagen a un objeto PhotoImage de Tkinter
		self.imagen_tk3 = ImageTk.PhotoImage(imagen_pil3)

		# Crear un widget Label y mostrar la imagen
		self.etiqueta = Label(self.pestana3, image=self.imagen_tk3)
		self.etiqueta.place(x=650,y=30)

		# Formulas 

		self.lb_form0 = Label(self.pestana3, text="Factor de\n Utilidad:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form0.place(x=400, y=150,width=250)
		self.et_form0 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.p3)
		self.et_form0.place(x=700, y=156,height=25)
		
		self.lb_form1 = Label(self.pestana3, text="Probabilidad de que el sistema\n este vacio:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form1.place(x=400, y=200,width=250)
		self.et_form1 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.p03, state="readonly")
		self.et_form1.place(x=700, y=206,height=25)
		
		self.lb_form2 = Label(self.pestana3, text="Probabilidad de que el sistema\n tenga n clientes:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form2.place(x=400, y=250,width=250)
		self.et_form2 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.pn3, state="readonly")
		self.et_form2.place(x=700, y=256,height=25)
		
		self.lb_form3 = Label(self.pestana3, text="Numero de clientes\n en el sistema:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form3.place(x=400, y=300,width=250)
		self.et_form3 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.ls3, state="readonly")
		self.et_form3.place(x=700, y=306,height=25)

		self.lb_form4 = Label(self.pestana3, text="Numero de clientes\n en la cola:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form4.place(x=400, y=350,width=250)
		self.et_form4 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.lq3, state="readonly")
		self.et_form4.place(x=700, y=356,height=25)

		self.lb_form5 = Label(self.pestana3, text="Tiempo promedio de espera\n en el sistema:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form5.place(x=400, y=400,width=250)
		self.et_form5 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.ws3, state="readonly")
		self.et_form5.place(x=700, y=406,height=25)

		self.lb_form6 = Label(self.pestana3, text="Tiempo promedio de espera\n en la cola:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form6.place(x=400, y=450,width=250)
		self.et_form6 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.wq3, state="readonly")
		self.et_form6.place(x=700, y=456,height=25)

		self.lb_form7 = Label(self.pestana3, text="Tasa de llegada\npromedio:", fg="black", bg="#3CB371", font=("Arial",12))
		self.lb_form7.place(x=400, y=500,width=250)
		self.et_form7 = Entry(self.pestana3,bd=0, relief="solid",bg="#F5F5F5", font=("Arial",12),width=8, textvariable=self.lam_prom3, state="readonly")
		self.et_form7.place(x=700, y=506,height=25)


		
		self.lb_form0 = Label(self.pestana3, text="", fg="black", bg="white", font=("Arial",12))
		self.lb_form0.place(x=777, y=156)
		
		self.lb_form1 = Label(self.pestana3, text="%", fg="black", bg="white", font=("Arial",12))
		self.lb_form1.place(x=777, y=206)
		
		self.lb_form2 = Label(self.pestana3, text="%", fg="black", bg="white", font=("Arial",12))
		self.lb_form2.place(x=777, y=256)
		
		self.lb_form3 = Label(self.pestana3, text="clientes", fg="black", bg="white", font=("Arial",12))
		self.lb_form3.place(x=777, y=306)
		
		self.lb_form4 = Label(self.pestana3, text="clientes", fg="black", bg="white", font=("Arial",12))
		self.lb_form4.place(x=777, y=356)

		self.lb_form5 = Label(self.pestana3, text="horas", fg="black", bg="white", font=("Arial",12))
		self.lb_form5.place(x=777, y=406)

		self.lb_form6 = Label(self.pestana3, text="horas", fg="black", bg="white", font=("Arial",12))
		self.lb_form6.place(x=777, y=456)

		self.lb_form7 = Label(self.pestana3, text="clientes/hr", fg="black", bg="white", font=("Arial",12))
		self.lb_form7.place(x=777, y=506)

		def calcularMMS():
			modeloMM1K = MM1K(self.lamnda3.get(), self.niuw3.get(), self.k3.get())
			self.p3.set(round(modeloMM1K.p(),3))
			self.p03.set(round(modeloMM1K.p0(),3))
			self.pn3.set(round(modeloMM1K.Pn(self.n3.get())))
			self.ls3.set(round(modeloMM1K.Ls(),3))
			self.lq3.set(round(modeloMM1K.Lq(),3))
			self.ws3.set(round(modeloMM1K.Ws(),3))
			self.wq3.set(round(modeloMM1K.Wq(),3))
			self.lam_prom3.set(round(modeloMM1K.lam_prom(),3))

		def limpiar():
			# Variables
			self.lamnda3.set(0.0)
			self.niuw3.set(0.0)
			self.n3.set(0)
			self.k3.set(0)
			self.p3.set(0.0)
			self.p03.set(0.0)
			self.pn3.set(0.0)
			self.ls3.set(0.0)
			self.lq3.set(0.0)
			self.ws3.set(0.0)
			self.wq3.set(0.0)
			self.lam_prom3.set(0.0)

		def mostrar (formula):
			if (formula == 0):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Factor de Utilidad ",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_0.png")
				imagen_formula = imagen_formula.resize((100,90))
				self.imagen_formula30 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula30)
				etiqueta.place(x=40, y=50)



			elif (formula == 1):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P(0) M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Probabilidad de Sistema vacio",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_1.png")
				imagen_formula = imagen_formula.resize((140,90))
				self.imagen_formula31 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula31)
				etiqueta.place(x=40, y=50)
			elif (formula == 2):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("P(n) M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Probabilidad de Sistema con n clientes",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_2.png")
				imagen_formula = imagen_formula.resize((140,90))
				self.imagen_formula32 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula32)
				etiqueta.place(x=40, y=50)
			elif (formula == 3):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Ls M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Clientes en el sistema",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_3.png")
				imagen_formula = imagen_formula.resize((235,120))
				self.imagen_formula33 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula33)
				etiqueta.place(x=40, y=50)
			elif (formula == 4):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Lq M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Clientes en la cola",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_4.png")
				imagen_formula = imagen_formula.resize((200,90))
				self.imagen_formula34 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula34)
				etiqueta.place(x=40, y=50)
			elif (formula == 5):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Ws M/M/1/K" )
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tiempo en el sistema",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_5.png")
				imagen_formula = imagen_formula.resize((120,90))
				self.imagen_formula35 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula35)
				etiqueta.place(x=40, y=50)
			elif (formula == 6):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Wq M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tiempo en la cola",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_6.png")
				imagen_formula = imagen_formula.resize((100,90))
				self.imagen_formula36 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula36)
				etiqueta.place(x=40, y=50)
			elif (formula == 7):
				ventana_formula = Toplevel(self.pestana3)
				ventana_formula.title("Media Lambda M/M/1/K")
				ventana_formula.geometry("300x200")
				ventana_formula.resizable(0,0)
				Label(ventana_formula,text="Tasa de llegada promedio",font=("Arial Black",10)).place(x=10,y=2)
				Label(ventana_formula,text="Formula:",font=("Arial",10)).place(x=30,y=30)
				imagen_formula = Image.open("assets//images//MM1K_7.png")
				imagen_formula = imagen_formula.resize((210,90))
				self.imagen_formula37 = ImageTk.PhotoImage(imagen_formula)
				etiqueta = Label(ventana_formula, image=self.imagen_formula37)
				etiqueta.place(x=40, y=50)
		
		self.btn_calc = Button(self.pestana3, text="Calcular", font=("Arial",14), command= calcularMMS)
		self.btn_calc.place(x=85,y=525)

		self.btn_clear = Button(self.pestana3, text="Limpiar", font=("Arial",14), command= limpiar)
		self.btn_clear.place(x=185,y=525)


		imagen_help3 = Image.open("assets//images//help.png")

		# Convertir la imagen a un objeto PhotoImage de Tkinter
		imagen_help3 = imagen_help3.resize((25,25))
		self.imagen_help3 = ImageTk.PhotoImage(imagen_help3)

		self.btn_form03 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(0))
		self.btn_form03.place(x=870,y=156,width=25,height=25)
		
		self.btn_form13 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(1))
		self.btn_form13.place(x=870,y=206,width=25,height=25)

		self.btn_form23 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(2))
		self.btn_form23.place(x=870,y=256,width=25,height=25)

		self.btn_form33 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(3))
		self.btn_form33.place(x=870,y=306,width=25,height=25)

		self.btn_form43 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(4))
		self.btn_form43.place(x=870,y=356,width=25,height=25)
		
		self.btn_form53 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(5))
		self.btn_form53.place(x=870,y=406,width=25,height=25)

		self.btn_form63 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(6))
		self.btn_form63.place(x=870,y=456,width=25,height=25)

		self.btn_form73 = Button(self.pestana3, image=self.imagen_help3, bd=0, highlightthickness=0, command= lambda:mostrar(7))
		self.btn_form73.place(x=870,y=506,width=25,height=25)

		
		pass





if __name__ == "__main__":
	app = Principal()
	app.title('Teoria de Colas')
	app.geometry("1000x600")
	app.resizable(0,0)
	#app.minsize(height= 600, width=900)
	#app.geometry('1200x750+180+80')
	#ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='C://Users//Max Pasten//OneDrive - UCB//Escritorio//Max Pasten//Programmacion PYTHON//Proyectos//Gui Tkinter//Menu Despegable//logo.png'))	
	
	app.mainloop()


