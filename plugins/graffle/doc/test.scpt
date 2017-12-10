on convertGraffleFile(graffleFile, outputFile, canvasname)
   tell application "OmniGraffle"
        set area type of current export settings to all graphics
        open graffleFile
        tell canvas canvasname to save in file outputFile
        close front document
    end tell
end convertGraffleFile

convertGraffleFile("Users:jshrall:tools:pm_tools:plugins:graffle:doc:assets:sample.graffle", "Users:jshrall:tools:pm_tools:plugins:graffle:doc:auto:sample.graffle_Canvas_1_02e41.svg", "Canvas 1")
