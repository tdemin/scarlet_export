from time import gmtime, strftime
from json import loads
from pathlib import Path

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
        createdTime = gmtime(note.timestamp / 1000)
        modifiedTime = gmtime(note.updateTimestamp / 1000)
        created = strftime(
            '%Y-%m-%dT%H:%M:%SZ',
            createdTime
        )
        modified = strftime(
            '%Y-%m-%dT%H:%M:%SZ',
            modifiedTime
        )
        # check if the folder exists
        outputPath = Path(outputFolder)
        if not outputPath.is_dir():
            outputPath.mkdir()
        with open(outputFileName, encoding='utf-8', mode='w') as output:
            # print YAML front matter first
            output.write('---\n')
            output.write('created: {0}\n'.format(created))
            output.write('modified: {0}\n'.format(modified))
            output.write('tags: [{0}]\n'.format(tags))
            output.write('---\n')
            output.write('\n') # an empty string
            # dump the note text as well, contained in another
            # JSON-formatted string
            output.write(note.content)
    return
