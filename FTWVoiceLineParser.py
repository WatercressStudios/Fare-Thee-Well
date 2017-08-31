#Fare Thee Well Voice Parser 1.0.0
print('Please enter the file to be parsed. Include the file path.')
inputFilePath = input()

inputFileName = inputFilePath.rsplit('\\', 1)[1]
filePath = inputFilePath.rsplit('\\', 1)[0]

outputFileName = '\\parsed_' + inputFileName
outputFilePath = filePath + outputFileName

print('Please enter the scene\'s route tag.')
routeTag = input()

print('Please enter the scene number.')
sceneNumber = input()

lineCount = 1

with open(inputFilePath, 'r') as infile, open(outputFilePath, 'w') as outfile:
    for line in infile:
        if 'wan' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Wayfarer (Terrance Drye)\n')
            outfile.write(line)
            lineCount += 1
        elif 'ten' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Bartender (Andrew Boa)\n')
            outfile.write(line)
            lineCount += 1
        elif 'gir' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Emmeline (Hayley Nelson)\n')
            outfile.write(line)
            lineCount += 1
        elif 'emm' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Emmeline (Hayley Nelson)\n')
            outfile.write(line)
            lineCount += 1
        elif 'tru' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Trucker (Sean Wisner)\n')
            outfile.write(line)
            lineCount += 1
        elif 'can' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Candace (Victoria Wong)\n')
            outfile.write(line)
            lineCount += 1
        elif 'ros' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Rosa (Tiana Camacho)\n')
            outfile.write(line)
            lineCount += 1
        elif 'mic' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Michael (Reece Bridger)\n')
            outfile.write(line)
            lineCount += 1
        elif 'yic' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Young Michael (Dani Chambers)\n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
