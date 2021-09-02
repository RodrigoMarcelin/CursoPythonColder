def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'

def tac_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'

if __name__ == '__main__':

    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('flahou', inline='error'))
    print(tag_bloco(tac_lista('Item 1', 'Item 2'), classe='info'))