from datetime import datetime
from json import loads

def exportNotes(inputJson, outputDir):
    """
    Exports the notes from Scarlet Notes to Notable.

    @param inputJson: an object generated with `json.load()`
    @param outputDir: output directory name
    """
    for note in inputJson['notes']:
        # color is not available in Notable, so it's not preserved
        # the metadata Notable uses is just YAML front matter
        if note['folder'] != '':
            outputFolder = outputDir + '/' + note['folder']
        else:
            outputFolder = outputDir
        outputFileName = outputFolder + '/' + note['uuid'] + '.md'
        tags = '[{0}]'.format(note['tags'])
        timestamp = int(note['timestamp'])
        updateTimestamp = int(note['updateTimestamp'])
        created = datetime.utcfromtimestamp(timestamp)
        modified = datetime.utcfromtimestamp(updateTimestamp)
        with open(outputFileName) as output:
            # print YAML front matter first, then dump the note content
            output.write('---')
            output.write('created: {0}'.format(created))
            output.write('modified: {0}'.format(modified))
            output.write('tags: {0}'.format(tags))
            output.write('---')
            output.write('') # an empty string
            # dump the note text as well, contained in another
            # JSON-formatted string
            noteText = loads(note['description'])['note']['text']
            output.write(noteText)
    return
