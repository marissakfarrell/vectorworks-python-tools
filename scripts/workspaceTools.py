import vs # type: ignore

def GetPalettePath(paletteName):
    totalPalettes = vs.ws2GetToolsCnt("")
    curPalette = 0
    outName = ""
    while curPalette < totalPalettes:
        pName = vs.ws2GetToolAt("", curPalette)
        result, outDisplayName, outShortcutKey, outShortcutKeyModifier, outResourceID = vs.ws2GetToolInfo(pName)
        if (outDisplayName == paletteName):
            outName = pName;
            break;
        curPalette = curPalette + 1
    
    return outName
    
def GetToolsetPath(paletteName, tsName):
    outName = ""
    palletteUName = GetPalettePath(paletteName)
    if (palletteUName != ""):
        totalToolSets = vs.ws2GetToolsCnt(palletteUName)
        curToolSet = 0
        tsUName = ""
        while curToolSet < totalToolSets:
            tsUName = vs.ws2GetToolAt(palletteUName, curToolSet)
            result, outDisplayName, outShortcutKey, outShortcutKeyModifier, outResourceID = vs.ws2GetToolInfo(palletteUName + "/" + tsUName)
            if (outDisplayName == tsName):
                outName = palletteUName + "/" + tsUName;
                break;
            curToolSet = curToolSet + 1
    return outName