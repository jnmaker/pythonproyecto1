import os
from time import sleep

"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE : JUAN MARCO NORIEGA ZAPATA
"""

dic_empresas = {
    '20321608040':{
        'razon_social':'BLOQUE14 S.R.L.',
        'direccion' : 'CALLE DOS DE MAYO 777 - SAN PEDRO DE LLOC'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        
        while True:
            ruc = input("Ingrese RUC: ")
            if not (ruc.isdigit() and len(ruc) == 11):
                print("❌ RUC inválido. Ingrese correctamente los 11 números.")
            elif ruc in dic_empresas:
                print("❌ Ese RUC ya está registrado.")
            else:
                break


        razon_social = input("Ingrese Razón Social: ")
        direccion = input("Ingrese dirección: ")
        dic_nueva_empresa = {
            "razon_social": razon_social,
            "direccion": direccion
        }
        dic_empresas[ruc] = dic_nueva_empresa
        print("✅ Empresa registrada exitosamente.")
        
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        
        for ruc,info in dic_empresas.items():
            print(f"RUC: {ruc}")
            print(f"Razon Social: {info['razon_social']}")
            print(f"Dirección: {info['direccion']}")
            print("*" * ANCHO)
        
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  EMPRESA")
        print("=" * ANCHO)

        ruc = input("Ingrese RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]['razon_social']}")
            nueva_razon_social = input(f"NUEVA RAZÓN SOCIAL ({dic_empresas[ruc]['razon_social']}): ")
            nueva_direccion = input(f"NUEVA DIRECCIÓN ({dic_empresas[ruc]['direccion']}): ")

            if nueva_razon_social:
                dic_empresas[ruc]["razon_social"] = nueva_razon_social
            if nueva_direccion:
                dic_empresas[ruc]["direccion"] = nueva_direccion
            print("✅ EMPRESA ACTUALIZADA EXITOSAMENTE")
        else:
            print("❌ No se encontró la empresa para el RUC ingresado")
        
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
    
        ruc = input("Ingrese RUC de la empresa a eliminar: ")

        if ruc in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc]['razon_social']}")
            while True:
                confirmacion = input("¿Está seguro que desea eliminarla? (S/N): ").upper()
                if confirmacion in ("S", "N"):
                    break
                print("Ingrese solo S o N")

            if confirmacion == "S":
                del dic_empresas[ruc]
                print("✅ EMPRESA ELIMINADA EXITOSAMENTE")
            else:
                print("❎ OPERACIÓN CANCELADA")
        else:
            print("❌ No se encontró la empresa para el RUC ingresado")

        
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(3)
        os.system("cls")
        break
        
    else:
        print("❌ OPCION NO VALIDA ...")
    
    input("Presione ENTER para continuar...")