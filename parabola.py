import turtle as turt
x = 0
x_multi = 8 #ajuda na representação de x na parabola
y_multi = 6#ajuda na representação de y na parabola
x_positions = []
y_positions = []

repeation = 12

#essa é a terceira função, ela define as linhas
def draw_lines():
    turt.clear()#limpeza dos pontos
    print(str(x_positions))
    print(str(y_positions))
    turt.up()
    print('im drawing lines dude, chill tf down ')
    turt.goto(0,-100)#volta ao lugar do inicio, SEMPRE seja igual ao do grafico
    #esse for loop é para colocar o ponto em antigas cordenadas, essa passagem faz com que a
    #linha siga ela, assim montando um grafico
    for i in range(len(x_positions)):
        
        print('this is your index bitch' + str(i))
        print('dont forget to shove the length of your list deep in you ass ' +
              str(len(x_positions)))

        
        #esse goto coloca as cordenadas do ponto em suas antigas posições, assim a parabola
        #é retraçada e assim monta uma parabola em uma linha continua, não em pontos
        turt.goto(x_positions[i], y_positions[i]-100)
        print(str(x_positions[i]))
        print(str(y_positions[i]))
        
        turt.down()
        



def draw_graph(x,y, end, i):
    
    turt.getscreen()
    #esses multis estão aqui para ajudar a representação no grafico
    x_turte = x*x_multi
    y_turte = y*y_multi
    turt.goto(0, -100)
    print(str(x) + ',' + str(y) + ' originals')
    #print(str(offsetx) + ',' + str(offsety) + ' offsets')
    print(str(x_turte) + ',' + str(y_turte) + ' turtes')
    
    
    
    
    #isso te leva até o ponto exato
    turt.left(90)
    turt.forward(y_turte)
    turt.right(90)
    turt.forward(x_turte)
    
    
    cords = str(x) + ', ' + str(y)
    
    #isso arquiva as cordenadas em uma lista e marca o ponto 
    if end == False: 
        print('im end')
        turt.down()
        turt.dot()
        turt.up()
        x_positions.append(x_turte)
        y_positions.append(y_turte)

    #ja esse else, ele começa o desenho da linhas, por isso que
    #usamos um True e False na função do grafico
    else:
        print('im end evil brother, i am...STARTTTTTTTTTTTTTTTT')
        draw_lines()
        
        
def math_time():
    
    turt.speed(10)#isso define a velocidade do grafico
    #essas proximas 4 linhas define que a janela turtle vai
    #aparecer acima de qualquer outra janela, seja o shell, seja
    #qualquer outra
    wn = turt.Screen()
    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    
    for i in range(repeation):
        i += 1
        #esse for loop esta aqui para representar varios pontos x
        turt.up()
        x = i
        #para mudar o tamanho, mude o termo do meio
        #para mudar a quantidade de pontos, mude os primeiros termos
        #mas não se esqueçade mudar a variavel repeation e o i do x
        y = x**2*-1 + 12*x + 18


        #isso é para decidir quanto a linha sera desenhada, esse -1 esta aqui pois se não
        #o codigo quebra, talvez seja devido que o index começa no 0, e o repeation e o index
        #não se encontram devido a aquele unico digito de diferença

        #eu tentei consertar mudando algumas coisas, não garanto que esteja perfeito, esse codigo
        #é sustentado por cuspe e fita, a qualquer momento isso se quebra
        if i == repeation:
            draw_graph(x,y, True, i)
        else: 
            draw_graph(x,y, False, i)


#define qual grafico sera representado
choice = ' '
while choice == ' ':
    print('escolhas:' + '\nparabola' + '\nnão tenho' + '\ncala a boca mlk EU JA DISSE QUE ACABOU')
    
    choice = input(str('what formula you want to visualize? '))
    
    if choice == 'parabola':
        math_time()
    

        
