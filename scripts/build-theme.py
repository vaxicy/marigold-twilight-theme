# -*- coding: utf-8 -*-
"""Build the Marigold Twilight Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "marigold-twilight-theme"
SLUG = "marigold-twilight"
DISPLAY = "Marigold Twilight Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/marigold-twilight-theme"

UI = {
    "foreground": ("#3E2438", "#F6E8DC"),
    "editor.foreground": ("#3E2438", "#F6E8DC"),
    "terminal.foreground": ("#3E2438", "#F6E8DC"),
    "input.foreground": ("#331D2E", "#FDF3E8"),
    "dropdown.foreground": ("#331D2E", "#FDF3E8"),
    "quickInput.foreground": ("#331D2E", "#FDF3E8"),
    "editorWidget.foreground": ("#331D2E", "#FDF3E8"),
    "editorHoverWidget.foreground": ("#331D2E", "#FDF3E8"),
    "editorSuggestWidget.foreground": ("#331D2E", "#FDF3E8"),
    "notifications.foreground": ("#331D2E", "#FDF3E8"),
    "descriptionForeground": ("#A08A8C", "#B09A9C"),
    "input.placeholderForeground": ("#A08A8C", "#B09A9C"),
    "focusBorder": ("#8A4A62", "#F2A67B"),
    "inputOption.activeBorder": ("#70405A", "#FFD38B"),
    "input.border": ("#F0DFD0", "#57305F"),
    "dropdown.border": ("#F0DFD0", "#57305F"),
    "editor.background": ("#FFFBF6", "#3A2048"),
    "tab.activeBackground": ("#FFFBF6", "#3A2048"),
    "titleBar.activeBackground": ("#FFD38B", "#2C1738"),
    "titleBar.activeForeground": ("#4A2A3E", "#E6D2C4"),
    "titleBar.inactiveBackground": ("#FFE2AE", "#331C42"),
    "titleBar.inactiveForeground": ("#7A5A62", "#A38A94"),
    "activityBar.background": ("#FBEBCF", "#291435"),
    "activityBar.foreground": ("#8A4A62", "#F2A67B"),
    "activityBar.activeBorder": ("#80426E", "#F2A67B"),
    "activityBar.inactiveForeground": ("#B59A8C", "#8E7488"),
    "sideBar.background": ("#FFF6EC", "#331C42"),
    "sideBar.foreground": ("#4A2F3C", "#E2CFC2"),
    "sideBarSectionHeader.background": ("#F9E8D4", "#3B1F4B"),
    "sideBarSectionHeader.foreground": ("#553749", "#EDD9CA"),
    "panel.background": ("#FFF9F2", "#361E46"),
    "terminal.background": ("#FFF9F2", "#361E46"),
    "panel.border": ("#F0DFD0", "#57305F"),
    "editorGroup.border": ("#F0DFD0", "#57305F"),
    "tab.border": ("#F0DFD0", "#57305F"),
    "sideBar.border": ("#F0DFD0", "#57305F"),
    "titleBar.border": ("#F0DFD0", "#57305F"),
    "statusBar.background": ("#522D60", "#80426E"),
    "statusBar.noFolderBackground": ("#522D60", "#80426E"),
    "statusBar.foreground": ("#FFF3E4", "#FFEEDF"),
    "statusBar.noFolderForeground": ("#FFF3E4", "#FFEEDF"),
    "statusBarItem.hoverBackground": ("#62376F", "#8F4E7C"),
    "statusBar.debuggingBackground": ("#A65A2E", "#A66A38"),
    "statusBar.debuggingForeground": ("#FFF8F0", "#FBF0E2"),
    "editorGroupHeader.tabsBackground": ("#F7EADF", "#361E46"),
    "tab.inactiveBackground": ("#F7EADF", "#361E46"),
    "tab.activeForeground": ("#331D2E", "#FFF3E8"),
    "tab.activeBorderTop": ("#F2A67B", "#F2A67B"),
    "tab.inactiveForeground": ("#A08A8C", "#B79AA8"),
    "tab.hoverBackground": ("#FBEEDF", "#3B1F4B"),
    "tab.activeModifiedBorder": ("#A65A2E", "#FFC98A"),
    "tab.inactiveModifiedBorder": ("#A65A2E", "#FFC98A"),
    "list.hoverBackground": ("#FFF3E4", "#3B1F4B"),
    "list.activeSelectionBackground": ("#F9DCC4", "#5A2E62"),
    "editorSuggestWidget.selectedBackground": ("#F9DCC4", "#5A2E62"),
    "list.activeSelectionForeground": ("#3E2438", "#FFF3E8"),
    "list.inactiveSelectionForeground": ("#3E2438", "#FFF3E8"),
    "editorSuggestWidget.selectedForeground": ("#3E2438", "#FFF3E8"),
    "list.inactiveSelectionBackground": ("#FBE9D8", "#4B2556"),
    "list.highlightForeground": ("#8A4A62", "#F2A67B"),
    "list.focusHighlightForeground": ("#8A4A62", "#F2A67B"),
    "tree.indentGuidesStroke": ("#EFDCCA", "#57305F"),
    "editorLineNumber.foreground": ("#BFAA9E", "#8E7488"),
    "editorLineNumber.activeForeground": ("#8A4A62", "#F2A67B"),
    "editor.lineHighlightBackground": ("#FFF7EC", "#43224F"),
    "editor.lineHighlightBorder": ("#FBEDDD", "#4B2556"),
    "editorCursor.foreground": ("#80426E", "#F2A67B"),
    "selection.background": ("#F9DCC4", "#5A2E62"),
    "editor.selectionBackground": ("#F9DCC4", "#5A2E62"),
    "terminal.selectionBackground": ("#F9DCC4", "#5A2E62"),
    "editor.inactiveSelectionBackground": ("#FBE9D8", "#4B2556"),
    "editor.wordHighlightBackground": ("#F9DCC480", "#7A4A7A80"),
    "editor.wordHighlightStrongBackground": ("#F9DCC480", "#7A4A7A80"),
    "editor.selectionHighlightBackground": ("#F9DCC466", "#7A4A7A66"),
    "editor.findMatchHighlightBackground": ("#FFE6B8", "#6B3A62"),
    "editor.findMatchBackground": ("#FFD38B", "#7A4A6E"),
    "editor.findMatchBorder": ("#A65A2E", "#FFD38B"),
    "editorBracketMatch.background": ("#FBE3CC", "#4B2556"),
    "editorBracketMatch.border": ("#80426E", "#F2A67B"),
    "editorIndentGuide.background1": ("#F2E0D0", "#472457"),
    "editorIndentGuide.activeBackground1": ("#C9A898", "#8E7488"),
    "editorWhitespace.foreground": ("#EFDCCA", "#57305F"),
    "editorRuler.foreground": ("#F8EBDE", "#43224F"),
    "textLink.foreground": ("#80426E", "#F2A67B"),
    "textLink.activeForeground": ("#6B3659", "#FFD38B"),
    "editorLink.activeForeground": ("#6B3659", "#FFD38B"),
    "quickInput.background": ("#FFFDF8", "#3B1F4B"),
    "editorHoverWidget.background": ("#FFFDF8", "#3B1F4B"),
    "notifications.background": ("#FFFDF8", "#3B1F4B"),
    "input.background": ("#FFFFFF", "#331C42"),
    "dropdown.background": ("#FFFFFF", "#331C42"),
    "editorWidget.background": ("#FFFDF8", "#3B1F4B"),
    "editorSuggestWidget.background": ("#FFFDF8", "#3B1F4B"),
    "editorWidget.border": ("#F0DFD0", "#603868"),
    "editorHoverWidget.border": ("#F0DFD0", "#603868"),
    "editorSuggestWidget.border": ("#F0DFD0", "#603868"),
    "notifications.border": ("#F0DFD0", "#603868"),
    "button.background": ("#80426E", "#F2A67B"),
    "button.foreground": ("#FFFFFF", "#3A2048"),
    "button.hoverBackground": ("#6B3659", "#FFD38B"),
    "button.secondaryBackground": ("#F9E8D4", "#4B2556"),
    "button.secondaryForeground": ("#4A2F3C", "#EDD9CA"),
    "button.secondaryHoverBackground": ("#F2DCC4", "#5A2E62"),
    "badge.background": ("#522D60", "#FFD38B"),
    "activityBarBadge.background": ("#522D60", "#FFD38B"),
    "badge.foreground": ("#FFFFFF", "#3A2048"),
    "activityBarBadge.foreground": ("#FFFFFF", "#3A2048"),
    "scrollbarSlider.background": ("#BFAA9E66", "#B09A9C88"),
    "scrollbarSlider.hoverBackground": ("#A8938899", "#C0AAAC99"),
    "scrollbarSlider.activeBackground": ("#92806F99", "#F2A67B99"),
    "errorForeground": ("#A8455F", "#F0A0A8"),
    "editorError.foreground": ("#A8455F", "#F0A0A8"),
    "problemsErrorIcon.foreground": ("#A8455F", "#F0A0A8"),
    "gitDecoration.deletedResourceForeground": ("#A8455F", "#F0A0A8"),
    "editorGutter.deletedBackground": ("#A8455F", "#F0A0A8"),
    "editorWarning.foreground": ("#A66A2E", "#FFC98A"),
    "problemsWarningIcon.foreground": ("#A66A2E", "#FFC98A"),
    "editorInfo.foreground": ("#5A4A7A", "#B8A8E0"),
    "problemsInfoIcon.foreground": ("#5A4A7A", "#B8A8E0"),
    "gitDecoration.addedResourceForeground": ("#5B7A5E", "#B8D8C8"),
    "gitDecoration.untrackedResourceForeground": ("#5B7A5E", "#B8D8C8"),
    "editorGutter.addedBackground": ("#5B7A5E", "#B8D8C8"),
    "gitDecoration.modifiedResourceForeground": ("#A66A2E", "#FFC98A"),
    "editorGutter.modifiedBackground": ("#A66A2E", "#FFC98A"),
    "diffEditor.insertedTextBackground": ("#DCEBDCAA", "#4B255666"),
    "diffEditor.removedTextBackground": ("#F5D9D2AA", "#6B3A6266"),
    "diffEditor.insertedLineBackground": ("#DCEBDC66", "#4B255644"),
    "diffEditor.removedLineBackground": ("#F5D9D266", "#6B3A6244"),
    "terminal.ansiBlack": ("#3E2438", "#3B1F4B"),
    "terminal.ansiRed": ("#A8455F", "#F0A0A8"),
    "terminal.ansiGreen": ("#5B7A5E", "#B8D8C8"),
    "terminal.ansiYellow": ("#A66A2E", "#FFC98A"),
    "terminal.ansiBlue": ("#5A4A7A", "#B8A8E0"),
    "terminal.ansiMagenta": ("#80426E", "#F2A67B"),
    "terminal.ansiCyan": ("#4F7A80", "#A8D4DC"),
    "terminal.ansiWhite": ("#A08A8C", "#E2CFC2"),
    "terminal.ansiBrightBlack": ("#7A5A62", "#8E7488"),
    "terminal.ansiBrightRed": ("#BC5A72", "#F7B8C0"),
    "terminal.ansiBrightGreen": ("#6E8E70", "#CBE4D8"),
    "terminal.ansiBrightYellow": ("#B88038", "#FFE0B0"),
    "terminal.ansiBrightBlue": ("#6E60B0", "#CCD4F7"),
    "terminal.ansiBrightMagenta": ("#9A5288", "#FFC0A0"),
    "terminal.ansiBrightCyan": ("#5E8E94", "#C0E4EA"),
    "terminal.ansiBrightWhite": ("#331D2E", "#FDF3E8"),
}

TOKENS = [
    ("comment", ("#A08A8C", "#A38A94"), "italic"),
    (("keyword", "storage"), ("#80426E", "#F2A67B"), None),
    ("string", ("#A65A2E", "#FFD38B"), None),
    (("entity.name.function", "support.function"), ("#8A4A62", "#E8A0B4"), None),
    (("entity.name.type", "support.type", "support.class"), ("#5A4A7A", "#B8A8E0"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#B0713A", "#FFC98A"), None),
    ("variable", ("#3E2438", "#F6E8DC"), None),
    ("variable.parameter", ("#63434F", "#D6C0B8"), None),
    (("variable.other.property", "support.variable.property"), ("#8A4A62", "#E8A0B4"), None),
    ("keyword.operator", ("#8A7578", "#C4B0B4"), None),
    ("punctuation", ("#A08A8C", "#A38A94"), None),
    ("entity.name.tag", ("#80426E", "#F2A67B"), None),
    ("entity.other.attribute-name", ("#B0713A", "#FFC98A"), None),
    ("string.regexp", ("#A66A2E", "#E8C48A"), None),
    ("constant.character.escape", ("#A65A2E", "#FFE6B8"), None),
    ("markup.heading", ("#331D2E", "#FDF3E8"), "bold"),
    ("markup.bold", ("#331D2E", "#FDF3E8"), "bold"),
    ("markup.italic", ("#331D2E", "#FDF3E8"), "italic"),
    ("invalid", ("#A8455F", "#F0A0A8"), None),
]

SEMANTIC = {
    "variable": "#3E2438|#F6E8DC",
    "parameter": "#63434F|#D6C0B8",
    "property": "#8A4A62|#E8A0B4",
    "function": "#8A4A62|#E8A0B4",
    "method": "#8A4A62|#E8A0B4",
    "type": "#5A4A7A|#B8A8E0",
    "class": "#5A4A7A|#B8A8E0",
    "interface": "#5A4A7A|#B8A8E0",
    "variable.readonly": "#B0713A|#FFC98A",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "Deep plum dusk with marigold light: warm paper in the light variant, a purple night with amber glow in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "marigold", "twilight"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#3A2048", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
