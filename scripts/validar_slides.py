#!/usr/bin/env python3
"""Valida a estrutura de slides de um HTML de aula (index.html / mobile.html)."""

import re
import sys


def linha_de(html, pos):
    return html.count('\n', 0, pos) + 1


def encontrar_slides(html):
    """Retorna lista de (linha, classes) para cada elemento com classe 'slide'."""
    slides = []
    for m in re.finditer(r'<(\w+)\s+[^>]*class="([^"]*)"[^>]*>', html):
        classes = m.group(2).split()
        if 'slide' in classes:
            slides.append((linha_de(html, m.start()), classes))
    return slides


def checar_slides_sem_layout(slides):
    problemas = []
    for linha, classes in slides:
        if not any(c.startswith('layout-') for c in classes):
            problemas.append(
                f"linha {linha}: elemento .slide sem classe de layout (classes: \"{' '.join(classes)}\")"
            )
    return problemas


def checar_display_global(html):
    """Rejeita regras CSS cujo seletor é exatamente '.slide.active' (sem
    classe de layout) e que definem 'display'. '.slide { display: none }'
    sozinho é o estado base esperado e não é problema."""
    problemas = []
    for style_m in re.finditer(r'<style>(.*?)</style>', html, re.DOTALL):
        css = style_m.group(1)
        offset = style_m.start(1)
        css_sem_comentarios = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
        for regra_m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css_sem_comentarios):
            seletor_bruto = regra_m.group(1)
            corpo = regra_m.group(2)
            if 'display' not in corpo:
                continue
            for seletor in seletor_bruto.split(','):
                seletor = seletor.strip()
                if not re.fullmatch(r'(\.[\w-]+)+', seletor):
                    continue
                classes = set(re.findall(r'\.([\w-]+)', seletor))
                if classes == {'slide', 'active'}:
                    linha = linha_de(html, offset + regra_m.start(1))
                    problemas.append(
                        f"linha {linha}: regra global \"{seletor}\" define display "
                        f"(\"{corpo.strip()}\") — display deve vir da classe de layout"
                    )
    return problemas


def checar_classes_layout_existem(html):
    """Toda classe layout-* usada no HTML precisa ter uma regra no CSS."""
    problemas = []
    usadas = {}
    for m in re.finditer(r'class="([^"]*)"', html):
        for c in m.group(1).split():
            if c.startswith('layout-') and c not in usadas:
                usadas[c] = linha_de(html, m.start())

    css_total = ''
    for style_m in re.finditer(r'<style>(.*?)</style>', html, re.DOTALL):
        css_total += style_m.group(1)
    definidas = set(re.findall(r'\.((?:layout-)[\w-]+)', css_total))

    for classe, linha in sorted(usadas.items(), key=lambda kv: kv[1]):
        if classe not in definidas:
            problemas.append(
                f"linha {linha}: classe de layout \".{classe}\" usada no HTML mas não definida no CSS"
            )
    return problemas


def checar_object_fit_cover(html):
    problemas = []
    for m in re.finditer(r'object-fit\s*:\s*cover', html):
        problemas.append(f"linha {linha_de(html, m.start())}: object-fit: cover encontrado (usar contain)")
    return problemas


def validar(caminho):
    with open(caminho, encoding='utf-8-sig') as f:
        html = f.read()

    problemas = []
    problemas += checar_slides_sem_layout(encontrar_slides(html))
    problemas += checar_display_global(html)
    problemas += checar_classes_layout_existem(html)
    problemas += checar_object_fit_cover(html)
    return problemas


def main():
    if len(sys.argv) != 2:
        print("uso: python validar_slides.py <caminho-do-html>")
        sys.exit(1)

    problemas = validar(sys.argv[1])

    if not problemas:
        print("OK")
        sys.exit(0)

    for p in sorted(problemas, key=lambda p: int(re.search(r'\d+', p).group())):
        print(p)
    sys.exit(1)


if __name__ == '__main__':
    main()
