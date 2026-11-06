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
| `tools/contrast.py` | Valida o contraste WCAG do `colors.toml` |

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

## Validar

```bash
python3 tools/contrast.py            # contraste WCAG
omarchy dev theme-preview colors.toml --no-osc   # paleta no terminal, sem aplicar
```

## Instalar para testar

```bash
ln -s "$PWD" ~/.config/omarchy/themes/tron
omarchy theme set Tron
```

Para voltar: `omarchy theme set "Circuit Horizon"` e `rm ~/.config/omarchy/themes/tron`.

## Base e licença

A estrutura segue o tema [Circuit Horizon](https://github.com/jennabrinning/omarchy-circuit-horizon-theme) (MIT). Nenhum arquivo ou wallpaper dele foi copiado. A licença deste projeto ainda precisa ser definida.
