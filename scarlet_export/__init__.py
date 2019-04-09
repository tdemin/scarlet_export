from argparse import ArgumentParser
from pathlib import Path
import json

from note import Note
from notable import exportNotes as exportToNotable

if __name__ == '__main__':
    parser = ArgumentParser('Scarlet Notes data export program')
    parser.add_argument(
        '-t', dest='program',
        type='str',
        help='the file format the data will be exported to [notable]',
        optional=True
    )
    parser.add_argument(
        '-o', dest='outputDirName',
        type='str',
        help='output directory (where the data will be saved to)',
        optional=False,
    )
    parser.add_argument(
        'inputFile', dest='inputFileName',
        type='str',
        help='input file (the .txt file from Scarlet Notes)',
        optional=False
    )
    args = parser.parse_args()
    # check if the input file exists
    inputPath = Path(args['inputFileName'])
    if not inputPath.is_file():
        print('File {0} does not exist. Exiting.'.format(
            args['inputFileName']
        ))
        exit(1)
    # create the output dir if it doesn't exist yet
    outputPath = Path(args['outputDirName'])
    if not outputPath.exists() and not outputPath.is_file():
        outputPath.mkdir()
    else:
        print('Cannot create directory {0}. Exiting.'.format(
            args['outputDirName']
        ))
        exit(1)
    # read and parse the file as JSON
    with open(args['inputFileName']) as inputFile:
        try:
            data = json.load(inputFile)
        except json.JSONDecodeError:
            print('Could not parse the input file.')
            exit(1)
    # do parsing
    notes = []
    for note in data['notes']:
        parsedNote = Note(note)
        notes.append(parsedNote)
    # currently the script only supports a single program to export the
    # data to
    if args['program'] == 'notable':
        exportToNotable(notes, args['outputDirName'])
    else:
        print('The program {0} is currently not supported.'.format(
            args['program']
        ))
        print('Exiting.')
        exit(1)
