from collections import defaultdict

mensaje="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
print(mensaje + "\n")
orden_frecuencias="eaolsndruitcpmyqbhgfvjñzxkw"

mensaje.upper

def contar_letras(texto):
    frecuencia_letras = defaultdict(int)
    for letra in texto:
        if letra.isalpha():
            frecuencia_letras[letra] += 1

    return dict(frecuencia_letras)

frecuencia = contar_letras(mensaje)

#frecuencia_ordenada = [('o', 3), ('a', 2), ('l', 1), ('h', 1)]
frecuencia_ordenada = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

for letra, cantidad in frecuencia_ordenada:
    print(f"{letra}:{cantidad}", end=", ")
print("\n")

'''#sustituir en orden de frecuencia
i=0
for letra, frecuencia in frecuencia_ordenada:
    mensaje=mensaje.replace(letra,orden_frecuencias[i])
    print(f"{letra}->{orden_frecuencias[i]}", end=", ")
    i +=1
print("\n")'''

#reemplazamos las dos letras más comunes: e y a
mensaje=mensaje.replace(frecuencia_ordenada[0][0],"e")
mensaje=mensaje.replace(frecuencia_ordenada[1][0],"a")


'''#filtramos las palabras que tengan 2 o 3 letras
palabras = mensaje.split()
palabras_cortas = [palabra for palabra in palabras if len(palabra) in [2, 3]]
for palabra in palabras_cortas:
    #primeras_letras = [palabra[0] for palabra in palabras]
    #contador_primeras = Counter(primeras_letras)
    #letra_mas_comun_primera = contador_primeras.most_common(1)
    print(palabra, end=" ")
print("\n")'''
    

print(mensaje + "\n")

while True:
        print("\n" + mensaje + "\n")
        print("Si se ha descifrado el mensaje escribe 'fin'")
        letra1 = input("Introduce la letra que quieras cambiar: ").upper()

        if letra1 == 'FIN':
            print("Mensaje descifrado: ")
            break
        else:
            letra2 = input("Introduce la letra por la cual quieras cambiarla: ").lower()
            mensaje=mensaje.replace(letra1,letra2)





print(mensaje)


