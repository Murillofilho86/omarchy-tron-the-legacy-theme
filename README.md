# TRON // Digital Frontier

Tema escuro para Omarchy 4.5, inspirado em TRON: Legacy. Ciano elétrico só onde há informação importante; o resto é preto e azul-marinho.

**Status:** paleta e overrides do shell prontos. Wallpapers ainda não existem, então `omarchy theme set` avisa que o tema não tem fundo.

## Arquivos

| Arquivo | Função |
| --- | --- |
| `colors.toml` | Paleta central. O Omarchy gera terminal, btop, neovim, navegador etc. a partir dela |
| `shell.bar.toml` | Barra: Void quase opaco, Orange para módulos em alerta |
| `shell.controls.toml` | Botões e campos: borda Circuit em repouso, Electric só em foco e seleção |
| `shell.lock.toml` | Tela de bloqueio: Circuit em repouso, Electric ao digitar, Red em erro |
| `icons.theme` | Ícones `Yaru-blue` |
| `keyboard.rgb` | Teclado RGB em Electric (`00e5ff`) |

Cada `shell.*.toml` substitui a seção inteira do `shell.toml` gerado, por isso todos listam todas as chaves.

## Do design system para o `colors.toml`

| Chave do Omarchy | Token | Valor |
| --- | --- | --- |
| `background`, `darker_background` | Void | `#03070D` |
| `dark_background` | Deep | `#07111D` |
| `lighter_background` | Grid | `#0B1928` |
| `accent`, `bright_cyan` | Electric | `#00E5FF` |
| `cyan` | Cyan | `#00A9D6` |
| `selection`, `selection_background` | Deep Blue | `#164B78` |
| `foreground`, `selection_foreground` | White | `#F0F8FF` |
| `light_foreground` | Silver | `#C5D9E8` |
| `muted` | Muted | `#819AAF` |
| `dark_foreground` | Disabled | `#526B82` |
| `orange` | Orange | `#FF8A3D` |
| `red` | Red | `#FF5263` |
| `green` | Green | `#43E6A2` |
| `yellow` | Amber | `#FFD166` |

Circuit (`#087CA7`) não é uma chave de cor. Aparece nas bordas de repouso dos controles e da tela de bloqueio.

### Cores fora do design system

O Omarchy exige estas cores e a paleta aprovada não as define. Foram derivadas e validadas a 5:1 ou mais sobre Void:

- `blue` `#4F9CF9` e `bright_blue` `#8DBCFF`. Circuit tem 4,28:1 sobre Void e Deep Blue tem 2,22:1, então não servem como texto.
- `magenta` `#D06BFF` e `bright_magenta` `#DD99FF`.
- `brown` `#C27A4A`.
- `bright_red` `#FF8A96`, `bright_yellow` `#FFE08F`, `bright_green` `#7DF0BE`.
- `bright_foreground` `#FFFFFF`, necessário porque White já é o `foreground` e o Omarchy pede um branco mais claro para cursor e ANSI 15.

## Contraste (WCAG 2.x)

Razões calculadas com a fórmula de luminância relativa do WCAG. O mínimo para texto é 4,5:1.

| Texto | Sobre Void | Sobre Deep | Sobre Grid |
| --- | --- | --- | --- |
| `foreground` (White) | 18,82 | 17,68 | 16,53 |
| `light_foreground` (Silver) | 13,91 | 13,07 | 12,22 |
| `muted` | 6,90 | 6,48 | 6,06 |
| `accent` (Electric) | 13,13 | 12,33 | 11,53 |
| Pior cor ANSI (`red` sobre Void, `brown` sobre Grid) | 6,38 | não medido | 5,22 |
| `dark_foreground` (Disabled) | 3,64 | 3,42 | 3,20 |

- White sobre a seleção Deep Blue: 8,47. Electric sobre a seleção: 5,91.
- Disabled fica abaixo de 4,5 de propósito, porque é texto desativado.
- A borda de janela inativa (Deep Blue sobre Void) tem 2,22, abaixo dos 3:1 recomendados para elementos de interface. É discreta de propósito.

Para ver a paleta no terminal sem aplicar o tema:

```bash
omarchy dev theme-preview colors.toml --no-osc
```

## Instalar para testar

```bash
ln -s "$PWD" ~/.config/omarchy/themes/tron
omarchy theme set Tron
```

Para voltar: `omarchy theme set "Circuit Horizon"` e `rm ~/.config/omarchy/themes/tron`.

## Base e licença

A estrutura segue o tema [Circuit Horizon](https://github.com/jennabrinning/omarchy-circuit-horizon-theme) (MIT). Nenhum arquivo ou wallpaper dele foi copiado.

Licenciado sob a [MIT](LICENSE). TRON é um tema da comunidade, sem afiliação com o Omarchy, TRON ou a Disney.
