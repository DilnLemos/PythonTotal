PERFUMERIA = 0
FARMACOS = 0
COSMETICOS   = 0

def decorador(turnero):

    def aux(ticket):
        print("Sú número de ticket es:")
        gen = turnero(ticket)
        

        return gen

    return aux

@decorador
def turnero(area):
    
    ticket = ""
    
    if area == 1:
        global PERFUMERIA
        PERFUMERIA += 1
        ticket = f"P{PERFUMERIA}"
        yield ticket

    elif area == 2:
        global FARMACOS
        FARMACOS += 1
        ticket = f"F{FARMACOS}"
        yield ticket

    elif area == 3:
        global COSMETICOS
        COSMETICOS += 1
        ticket = f"C{COSMETICOS}"
        yield ticket
