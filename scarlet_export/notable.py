from datetime import datetime
from json import loads

def exportNotes(notesList, outputDir):
    """
    Exports the notes from Scarlet Notes to Notable.

    @param notesList: a list of `Note`
    @param outputDir: output directory name
    """
    for note in notesList:
        # color is not available in Notable, so it's not preserved
        # the metadata Notable uses is just YAML front matter
        if note.folder != '':
            outputFolder = outputDir + '/' + note.folder
        else:
            outputFolder = outputDir
        outputFileName = outputFolder + '/' + note.uuid + '.md'
        # make up a string containing all of the tags
        tags = ''
        for tag in note.tags:
            tags += tag + ','
        tags.rstrip(',')
        created = datetime.utcfromtimestamp(note.timestamp)
        modified = datetime.utcfromtimestamp(note.updateTimestamp)
        with open(outputFileName) as output:
            # print YAML front matter first
            output.write('---')
            output.write('created: {0}'.format(created))
            output.write('modified: {0}'.format(modified))
            output.write('tags: [{0}]'.format(tags))
            output.write('---')
            output.write('') # an empty string
            # dump the note text as well, contained in another
            # JSON-formatted string
            output.write(note.content)
    return
