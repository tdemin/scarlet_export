from argparse import ArgumentParser
from json import load, JSONDecodeError
from pathlib import Path

from scarlet_export.note import Note
from scarlet_export.notable import exportNotes as exportToNotable

def main():
    """
    Program entry point.
    """
    parser = ArgumentParser(
        prog='scarlet_export',
        description='Scarlet Notes data export program'
    )
    parser.add_argument(
        '-t', dest='program',
        type=str,
        help='the file format the data will be exported to [notable]',
        required=False,
        default='notable'
    )
    parser.add_argument(
        '-o', dest='outputDirName',
        type=str,
        help='output directory (where the data will be saved to)',
        required=True
    )
    parser.add_argument(
        dest='inputFileName',
        type=str,
        help='input file (the .txt file from Scarlet Notes)'
    )
    args = parser.parse_args()
    # check if the input file exists
    inputPath = Path(args.inputFileName)
    if not inputPath.is_file():
        print('File {0} does not exist. Exiting.'.format(
            args.inputFileName
        ))
        exit(1)
    # create the output dir if it doesn't exist yet
    outputPath = Path(args.outputDirName)
    try:
        if not outputPath.exists() and not outputPath.is_file():
            outputPath.mkdir()
    except IOError:
        print('Cannot create directory {0}. Exiting.'.format(
            args.outputDirName
        ))
        exit(1)
    # read and parse the file as JSON
    with open(args.inputFileName, encoding='utf-8') as inputFile:
        try:
            data = load(inputFile)
        except JSONDecodeError:
            print('Could not parse the input file.')
            exit(1)
    # do parsing
    notes = []
    tags = {}
    for tag in data['tags']:
        tags[tag['uuid']] = tag['title']
    folders = {}
    # folders are only available in Scarlet v6 and later
    if 'folders' in data:
        for folder in data['folders']:
            folders[folder['uuid']] = folder['title']
    for note in data['notes']:
        parsedNote = Note(note, tags, folders)
        notes.append(parsedNote)
    # currently the script only supports a single program to export the
    # data to
    if args.program == 'notable':
        exportToNotable(notes, args.outputDirName)
    else:
        print('The program {0} is currently not supported.'.format(
            args.program
        ))
        print('Exiting.')
        exit(1)
