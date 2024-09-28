#A densidade de pixels (PPI - Pixels por polegada) de um monitor depende da resolução e do tamanho da tela.
#A resolução full HD é de 1920X1080 pixels e por exemplo o tamanho da tela do monitor é de 32 polegadas. Assim sendo, a PPI é calculada conforme a equação abaixo. Elabore um fluxograma e posteriormente desenvolva um programa em python para calcular o valor da PPI.
#PPI = LARGURA AO QUADRADO + ALTURA AO QUADRADO DIVIDO PELO TAMANHO DA TELA.

resolucao = (1920, 1080)
tamanho_tela = 32 
largura = resolucao[0]
altura = resolucao[1]
ppi = (largura**2 + altura**2)**0.5 / tamanho_tela
print(f'A densidade de pixels (PPI) é: {ppi:.2f}')