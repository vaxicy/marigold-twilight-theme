<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/marigold-twilight-theme/main/assets/icon.png" alt="Marigold Twilight Theme logo" width="128">
</p>

<h1 align="center">Marigold Twilight Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.marigold-twilight-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-80426E?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-F2A67B?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-FFD38B?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/marigold-twilight-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

Plum dusk and marigold light. The light variant is warm paper with an amber title bar and plum ink; the dark one is a purple night lit by marigold and amber accents.

梅紫的黄昏与万寿菊的光。浅色版是暖纸配琥珀标题栏与梅紫墨字，深色版是紫夜，靠万寿菊与琥珀提亮。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Marigold Twilight Theme Light](https://raw.githubusercontent.com/vaxicy/marigold-twilight-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Marigold Twilight Theme Dark](https://raw.githubusercontent.com/vaxicy/marigold-twilight-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FFFBF6` warm paper | `#3A2048` purple night |
| Foreground | `#3E2438` plum ink | `#F6E8DC` warm cream |
| Muted text / placeholders | `#A08A8C` | `#B09A9C` |
| Side bar | `#FFF6EC` | `#331C42` |
| Panel / terminal | `#FFF9F2` | `#361E46` |
| Title bar | `#FFD38B` with `#4A2A3E` text | `#2C1738` with `#E6D2C4` text |
| Tab bar / inactive tab | `#F7EADF` | `#361E46` |
| Active tab / indicator | `#331D2E` text, `#F2A67B` top border | `#FFF3E8` text, `#F2A67B` top border |
| Activity bar | `#FBEBCF` with `#8A4A62` icons | `#291435` with `#F2A67B` icons |
| Status bar | `#522D60` with `#FFF3E4` text | `#80426E` with `#FFEEDF` text |
| Selection | `#F9DCC4` | `#5A2E62` |
| Current line | `#FFF7EC` | `#43224F` |
| Borders | `#F0DFD0` | `#57305F` |
| Indent guides | `#F2E0D0` | `#472457` |
| Button | `#80426E` with white text (hover `#6B3659`) | `#F2A67B` with `#3A2048` text (hover `#FFD38B`) |
| Badge | `#522D60` with white text | `#FFD38B` with `#3A2048` text |
| Cursor | `#80426E` | `#F2A67B` |
| Links | `#80426E` | `#F2A67B` |
| Errors / warnings | `#A8455F` / `#A66A2E` | `#F0A0A8` / `#FFC98A` |
| Git added / modified / deleted | `#5B7A5E` / `#A66A2E` / `#A8455F` | `#B8D8C8` / `#FFC98A` / `#F0A0A8` |

Night `#522D60`, plum `#80426E`, marigold `#F2A67B` and amber `#FFD38B` carry both variants, so a file still reads as "marigold twilight" after switching.

夜紫 `#522D60`、梅紫 `#80426E`、万寿菊 `#F2A67B` 与琥珀 `#FFD38B` 贯穿明暗两版，切换后整个文件还是同一场黄昏。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#A08A8C` | `#A38A94` |
| Keywords / storage | `#80426E` | `#F2A67B` |
| Strings | `#A65A2E` | `#FFD38B` |
| Functions / methods | `#8A4A62` | `#E8A0B4` |
| Types / classes | `#5A4A7A` | `#B8A8E0` |
| Numbers / constants | `#B0713A` | `#FFC98A` |
| Variables | `#3E2438` | `#F6E8DC` |
| Parameters | `#63434F` | `#D6C0B8` |
| Properties | `#8A4A62` | `#E8A0B4` |
| Operators | `#8A7578` | `#C4B0B4` |
| Punctuation | `#A08A8C` | `#A38A94` |
| HTML tags | `#80426E` | `#F2A67B` |
| Attribute names | `#B0713A` | `#FFC98A` |
| Regex | `#A66A2E` | `#E8C48A` |
| Escape characters | `#A65A2E` | `#FFE6B8` |

Semantic highlighting is enabled, so variables, parameters, properties, functions and types follow the same mapping in TypeScript, JavaScript, Go, Rust and Python.

已开启语义高亮，TypeScript、JavaScript、Go、Rust 与 Python 里的变量、参数、属性、函数与类型都会落到同一套配色。

## Install / 安装

1. 打开扩展面板 `Ctrl+Shift+X`。
2. 搜索 **Marigold Twilight Theme** 并安装。
3. 按 `Ctrl+K Ctrl+T`，选择 `Marigold Twilight Theme Light` 或 `Marigold Twilight Theme Dark`。

也可以用命令行安装：

```bash
code --install-extension lilinhuang.marigold-twilight-theme
```

## Build from source / 本地构建

```bash
py -3 scripts/build-theme.py       # regenerate both theme JSON files
py -3 scripts/generate-icon.py     # export assets/icon.png from the selected logo
py -3 scripts/capture-real-screenshots.py   # real VS Code screenshots
```

## License / 许可证

Non-Commercial License — free for personal, educational and non-commercial use. See [LICENSE](https://github.com/vaxicy/marigold-twilight-theme/blob/main/LICENSE).

非商业许可证：个人、教育与非商业用途免费使用，详见 LICENSE。
