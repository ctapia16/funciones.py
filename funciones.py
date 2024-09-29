import streamlit as st

# Título de la aplicación
st.title("Function Web Page")
st.image("data:image/jpeg;base64,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")
st.subheader("Realizamos esta página para que los usuarion puedan entrar a realizar operaciones ya establecidas mediante funciones  ")
st.write("*Puede cambiar su seleccion en la caja de opciones que se encuentra en la esquina superior derecha*")
st.title("Ejercicios Con Funciones")

# Sidebar para navegación entre ejercicios
opcion = st.sidebar.selectbox(
    "Selecciona el ejercicio",
    [
        "Saludo simple",
        "Suma de dos números",
        "Área de un triángulo",
        "Calculadora de descuento",
        "Suma de una lista",
        "Valores predeterminados",
        "Números pares e impares",
        "Multiplicación con *args",
        "Información personal",
        "Calculadora flexible"
    ]
)
st.write(f"### {opcion}")
st.image("https://www.google.com/imgres?q=imagen%20de%20saludo&imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1303509809%2Fes%2Fvector%2Ficono-de-gesto-de-mano-agitando-vector-de-gesto-de-mano-ondulante-aislado-sobre-fondo-blanco.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DCFXYpppm7uHSEtjayl98DG5Oi9L9GmTKOIpOujfOaf8%3D&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fes%2Ffotos%2Fsaludo-manos&docid=BFQxY4jf5k5apM&tbnid=6KnsD8XOCCTITM&vet=12ahUKEwi3_azGgemIAxWnLEQIHUCVILMQM3oECBgQAA..i&w=612&h=612&hcb=2&ved=2ahUKEwi3_azGgemIAxWnLEQIHUCVILMQM3oECBgQAA")

# Muestra la opción seleccionada

# Funciones correspondientes a cada ejercicio
def saludar(nombre):
    return f"Hola , {nombre}"

def sumar(a, b):
    return a + b

def calc_area_triangulo(base, altura):
    return (base * altura) / 2

def precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio * ((100 - descuento) / 100)
    precio_final = precio_descuento * ((100 + impuesto) / 100)
    return precio_final

def sumar_lista(lista):
    return sum(lista)

def producto(nombre, cantidad=1, precio=10):
    return cantidad * precio


def numeros_pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    if not args:
        return 1
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def informacion_personal(**kwargs):
    info = "\n".join(f"{clave}: {valor}" for clave, valor in kwargs.items())
    return info

def calculadora_flexible(a, b, operacion="suma"):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicación":
        return a * b
    elif operacion == "división":
        return a / b if b != 0 else "Error: División por cero"
    else:
        return "Operación no válida"
#Ejecucion de seleccion por el usuario 
if opcion == "Saludo simple":
    nombre = st.text_input("Ingresa tu nombre:", "")
    if nombre:
        st.write(saludar(nombre))
elif opcion == "Suma de dos números":
    a = st.number_input("Ingresa el primer número:", value=0)
    b = st.number_input("Ingresa el segundo número:", value=0)
    if st.button("Sumar"):
        st.write(f"La suma es: {sumar(a, b)}")
elif opcion == "Área de un triángulo":
    base = st.number_input("Ingresa la base del triángulo:", value=0.0)
    altura = st.number_input("Ingresa la altura del triángulo:", value=0.0)
    if st.button("Calcular área"):
        st.write(f"El área del triángulo es: {calc_area_triangulo(base, altura)}")
elif opcion == "Calculadora de descuento":
    precio = st.number_input("Precio original:", value=0.0)
    descuento = st.number_input("Porcentaje de descuento:", value=10)
    impuesto = st.number_input("Porcentaje de impuesto:", value=16)
    if st.button("Calcular precio final"):
        st.write(f"El precio final es: {precio_final(precio, descuento, impuesto)}")
elif opcion == "Suma de una lista":
    lista = st.text_input("Ingresa una lista de números separados por comas:", "1,2,3")
    numeros = list(map(int, lista.split(',')))
    st.write(f"La suma de la lista es: {sumar_lista(numeros)}")
elif opcion == "Valores predeterminados":
    nombre_producto = st.text_input("Nombre del producto:", "Producto")
    cantidad = st.number_input("Cantidad:", value=1)
    precio = st.number_input("Precio por unidad:", value=10.0)
    if st.button("Calcular total"):
        st.write(f"El precio total es: {producto(nombre_producto, cantidad, precio)}")
elif opcion == "Números pares e impares":
    lista = st.text_input("Ingresa una lista de números separados por comas:", "1,2,3,4")
    numeros = list(map(int, lista.split(',')))
    pares, impares = numeros_pares_e_impares(numeros)
    st.write(f"Números pares: {pares}")
    st.write(f"Números impares: {impares}")
elif opcion == "Multiplicación con *args":
    numeros = st.text_input("Ingresa números separados por comas:", "1,2,3")
    args = list(map(int, numeros.split(',')))
    st.write(f"El resultado de multiplicar todos los números es: {multiplicar_todos(*args)}")
elif opcion == "Información personal":
    nombre = st.text_input("Nombre:", "")
    edad = st.number_input("Edad:", value=0)
    direccion = st.text_input("Dirección:", "")
    if st.button("Mostrar información"):
        st.text(informacion_personal(nombre=nombre, edad=edad, direccion=direccion))
elif opcion == "Calculadora flexible":
    a = st.number_input("Número 1:", value=0)
    b = st.number_input("Número 2:", value=0)
    operacion = st.selectbox("Operación:", ["suma", "resta", "multiplicación", "división"])
    if st.button("Calcular"):
        st.write(f"El resultado es: {calculadora_flexible(a, b, operacion)}")
