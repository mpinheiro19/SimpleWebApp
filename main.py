from conectores.conector_plano import get_all

if __name__=="__main__":
    r = get_all()
    for i,_ in enumerate(r):
        print(r[i].__str__())