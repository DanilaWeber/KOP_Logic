
def input_expression(outText):
    out = []
    for i in outText:
        if input(i+'(enter t/f)') == 't':
            out.append(True)
        else:
            out.append(False)
    return out

x,y,z,u,v,w = input_expression(['я поеду автобусом','автобус опоздает','я пропущу свидание','я начну огорчаться','мне следует ехать домой','я получу работу'])

print(x&y>=z, x&u>=(not v), (not w)>=u&v, x&y<=w)

